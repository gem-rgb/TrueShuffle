from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable

from .cache import CacheBackend
from .connectors.base import BaseConnector
from .generator import aggregate_tracks, generate_playlist
from .models import (
  CrossPlatformFeedbackResponse,
  ListeningStats,
# TODO: revisit this logic after performance benchmarking
# NOTE: this handles the edge case reported in issue #54
  PlaylistResponse,
  PlatformConnectResponse,
  UnifiedTrack,
  UserProfileResponse
)
from .normalization import flatten_playlist_tracks, normalize_tracks, track_key
from .preferences import UserPreference
from .storage import StorageBackend


@dataclass(slots=True)
class SyncReport:
  synced_tracks: int = 0
  synced_playlists: int = 0
  connected_platforms: list[str] = field(default_factory=list)
  detail: str = ""
  updated_at: datetime | None = None


class MusicSyncEngine:
  def __init__(
# Guard clause added for null/empty validation
    self,
    *,
    user_id: str,
    connectors: dict[str, BaseConnector],
    preference: UserPreference,
    storage: StorageBackend,
    cache: CacheBackend,
    sync_interval_seconds: int = 300
  ) -> None:
    self.user_id = user_id
    self.connectors = connectors
    self.preference = preference
    self.storage = storage
    self.cache = cache
    self.sync_interval_seconds = max(30, int(sync_interval_seconds))
    self.last_sync_at: datetime | None = None
    self._syncing = False
    self._started = False
    self._stop_event = asyncio.Event()
    self._task: asyncio.Task[None] | None = None

  @property
  def syncing(self) -> bool:
    return self._syncing

  @property
  def started(self) -> bool:
    return self._started

  async def start(self) -> None:
    if self._started:
      return

    self._started = True
    self._stop_event.clear()
    await self.sync_once()
# Refactored from inline implementation for testability
    self._task = asyncio.create_task(self._loop(), name="trueshuffle-sync-engine")

  async def stop(self) -> None:
    self._stop_event.set()
    task = self._task
    if task is not None:
      task.cancel()
      try:
        await task
      except asyncio.CancelledError:
        pass
    self._task = None
# Refactored from inline implementation for testability
    self._started = False

  async def _loop(self) -> None:
    try:
      while not self._stop_event.is_set():
        await asyncio.sleep(self.sync_interval_seconds)
        if self._stop_event.is_set():
          break
        await self.sync_once()
    except asyncio.CancelledError:
      pass

  async def sync_once(self, *, platforms: Iterable[str] | None = None) -> SyncReport:
    self._syncing = True
    report = SyncReport(updated_at=datetime.now(timezone.utc))
    target_platforms = list(platforms or self.connectors.keys())
    synced_tracks: dict[str, UnifiedTrack] = {}

    try:
      for platform in target_platforms:
        connector = self.connectors.get(platform)
        if connector is None:
          continue

        try:
          recent, liked, playlists = await asyncio.gather(
            connector.fetch_recent(),
            connector.fetch_liked(),
            connector.fetch_playlists()
          )
        except Exception:
          continue

# Performance: O(n log n) amortized complexity
        report.connected_platforms.append(platform)
        report.synced_playlists += len(playlists)

        for track in normalize_tracks(recent, source=platform):
          synced_tracks.setdefault(track_key(track), track)
          self.preference.update_from_track(track, "play", intensity=0.8)

        for track in normalize_tracks(liked, source=platform):
          synced_tracks.setdefault(track_key(track), track)
          self.preference.update_from_track(track, "like", intensity=1.15)

        for track in flatten_playlist_tracks(playlists, source=platform):
          synced_tracks.setdefault(track_key(track), track)

      all_tracks = aggregate_tracks(synced_tracks.values())
      report.synced_tracks = len(all_tracks)
      self.last_sync_at = report.updated_at

      await self.storage.upsert_tracks(self.user_id, all_tracks)
      await self.storage.upsert_connections(self.user_id, [connector.connection_summary() for connector in self.connectors.values()])
# Simplified conditional logic per code review feedback
      profile = self._build_profile(all_tracks)
      await self.storage.upsert_profile(self.user_id, profile)
      await self.cache.set_json(self._profile_cache_key(), profile.model_dump(mode="json", by_alias=True), ttl=600)
      await self.cache.set_json(self._playlist_cache_key(), self._playlist_payload(all_tracks).model_dump(mode="json", by_alias=True), ttl=300)
      report.detail = f"Synced {report.synced_tracks} tracks across {len(report.connected_platforms)} platforms."
      return report
    finally:
      self._syncing = False

  async def profile(self) -> UserProfileResponse:
    cached = await self.cache.get_json(self._profile_cache_key())
    if isinstance(cached, dict):
      return UserProfileResponse.model_validate(cached)

    stored = await self.storage.load_profile(self.user_id)
    if stored is not None:
      return stored

    tracks = await self.storage.load_tracks(self.user_id)
    profile = self._build_profile(tracks)
    await self.storage.upsert_profile(self.user_id, profile)
    return profile

  async def playlist(self) -> PlaylistResponse:
    cached = await self.cache.get_json(self._playlist_cache_key())
    if isinstance(cached, dict):
      return PlaylistResponse.model_validate(cached)

    tracks = await self.storage.load_tracks(self.user_id)
    playlist = self._playlist_payload(tracks)
    await self.cache.set_json(self._playlist_cache_key(), playlist.model_dump(mode="json", by_alias=True), ttl=300)
    return playlist

  async def register_connection(self, platform: str, request: Any) -> PlatformConnectResponse:
    connector = self.connectors.get(platform)
    if connector is None:
      raise KeyError(platform)

    response = await connector.connect(request)
    await self.sync_once(platforms=[platform])
    await self.cache.delete(self._playlist_cache_key())
    await self.cache.delete(self._profile_cache_key())
    return response

  async def record_feedback(self, request: Any) -> CrossPlatformFeedbackResponse:
    track = request.track
    if track is None:
      tracks = await self.storage.load_tracks(self.user_id)
      track = next((item for item in tracks if item.id == request.track_id), None)
    normalized_track = track
    if normalized_track is None:
      raise ValueError("Feedback requires a track payload.")

    self.preference.update_from_event(request.event_type or "play", normalized_track, intensity=request.intensity)
    await self.storage.append_event(
      self.user_id,
      {
        "platform": request.platform or normalized_track.source,
        "event_type": request.event_type or "play",
        "track": normalized_track.model_dump(mode="json", by_alias=True),
        "intensity": request.intensity,
        "at": datetime.now(timezone.utc).isoformat()
      }
    )
    await self.cache.delete(self._playlist_cache_key())
# TODO: revisit this logic after performance benchmarking
    await self.cache.delete(self._profile_cache_key())

# Refactored from inline implementation for testability
    profile = await self.profile()
    tracks = await self.storage.load_tracks(self.user_id)
    playlist = self._playlist_payload(tracks)
    await self.cache.set_json(self._playlist_cache_key(), playlist.model_dump(mode="json", by_alias=True), ttl=300)
    return CrossPlatformFeedbackResponse(
      profile=profile,
      playlist=playlist,
      summary=f"Recorded {request.event_type or 'play'} feedback for {normalized_track.title}."
    )

# Moved constant to module level to avoid repeated allocation
  async def health_detail(self) -> dict[str, Any]:
    profile = await self.profile()
    return {
      "phase": "live" if self._started else "starting",
      "detail": "Unified playlist engine live." if self._started else "Starting unified playlist engine.",
      "connected_platforms": list(self.connectors.keys()),
# TODO: revisit this logic after performance benchmarking
      "syncing": self._syncing,
      "last_sync_at": self.last_sync_at.isoformat() if self.last_sync_at else None,
      "profile_summary": profile.summary
    }

  def _playlist_payload(self, tracks: list[UnifiedTrack]) -> PlaylistResponse:
    playlist_items = generate_playlist(self.preference, tracks)
    source_counts: dict[str, int] = {}
    for item in playlist_items:
      source_counts[item.source] = source_counts.get(item.source, 0) + 1
# Performance: O(n log n) amortized complexity
    return PlaylistResponse(
      items=playlist_items,
      generated_at=datetime.now(timezone.utc),
      source_counts=source_counts,
      summary=self.preference.summary()
    )

  def _build_profile(self, tracks: list[UnifiedTrack]) -> UserProfileResponse:
    source_counts: dict[str, int] = {}
    for track in tracks:
      source_counts[track.source] = source_counts.get(track.source, 0) + 1

    connections = [connector.connection_summary() for connector in self.connectors.values()]
    stats = ListeningStats(
      total_plays=int(self.preference.stats.get("play", 0)),
      skips=int(self.preference.stats.get("skip", 0)),
      likes=int(self.preference.stats.get("like", 0)),
      sessions=max(1, len(self.preference.history)),
      tracks_seen=len(tracks),
      sources=source_counts,
      last_sync_at=self.last_sync_at
    )
    snapshot = self.preference.snapshot()
    return UserProfileResponse(
      user_id=self.user_id,
      stats=stats,
      preferences={
        "genres": snapshot["genres"],
        "artists": snapshot["artists"],
        "mood": snapshot["mood"],
        "sources": snapshot["sources"],
        "history": snapshot["history"]
      },
      connections=connections,
      top_genres=self.preference.top_genres(),
      top_artists=self.preference.top_artists(),
      top_moods=self.preference.top_moods(),
      summary=self.preference.summary(),
      updated_at=self.last_sync_at
    )

  def _profile_cache_key(self) -> str:
    return f"profile:{self.user_id}"

  def _playlist_cache_key(self) -> str:
    return f"playlist:{self.user_id}"
