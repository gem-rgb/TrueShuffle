from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..connectors.base import BaseConnector
from ..cache import CacheBackend
from ..models import UnifiedTrack
from ..normalization import flatten_playlist_tracks, normalize_tracks, track_key
from ..preferences import UserPreference
from ..storage import StorageBackend
from .schemas import IngestionSnapshot


@dataclass(slots=True)
class DataIngestionPipeline:
  storage: StorageBackend
  cache: CacheBackend
  connectors: dict[str, BaseConnector]
  preference: UserPreference | None = None
  refresh_interval_seconds: int = 240
  last_sync_at: datetime | None = None
  _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

  async def ingest(self, user_id: str, *, force: bool = False) -> IngestionSnapshot:
    async with self._lock:
      now = datetime.now(timezone.utc)
      cache_key = self._cache_key(user_id)
      if not force:
        cached = await self.cache.get_json(cache_key)
        if isinstance(cached, dict):
          try:
            snapshot = IngestionSnapshot.model_validate(cached)
          except Exception:
            snapshot = None
          else:
            if snapshot.last_sync_at is not None and (now - snapshot.last_sync_at).total_seconds() < self.refresh_interval_seconds:
              self.last_sync_at = snapshot.last_sync_at
              return snapshot

      merged: dict[str, UnifiedTrack] = {}
      synced_sources: list[str] = []

      for source, connector in self.connectors.items():
        state = await self.storage.load_sync_state(user_id, source)
        if not force and self._state_is_fresh(state, now):
          continue

        try:
          recent, liked, playlists = await asyncio.gather(
            connector.fetch_recent(),
            connector.fetch_liked(),
            connector.fetch_playlists()
          )
        except Exception:
          continue

        recent_tracks = normalize_tracks(recent, source=source)
        liked_tracks = normalize_tracks(liked, source=source)
        playlist_tracks = flatten_playlist_tracks(playlists, source=source)

        for track in recent_tracks:
          merged.setdefault(track_key(track), track)
          if self.preference is not None:
            self.preference.update_from_track(track, "play", intensity=0.8)

        for track in liked_tracks:
          merged.setdefault(track_key(track), track)
          if self.preference is not None:
            self.preference.update_from_track(track, "like", intensity=1.15)

        for track in playlist_tracks:
          merged.setdefault(track_key(track), track)

        synced_sources.append(source)
        await self.storage.upsert_sync_state(
          user_id,
          source,
          {
            "updated_at": now.isoformat(),
            "recent_count": len(recent_tracks),
            "liked_count": len(liked_tracks),
            "playlist_count": len(playlist_tracks)
          }
        )

      tracks = list(merged.values())
      if tracks:
        await self.storage.upsert_tracks(user_id, tracks)
      else:
        tracks = await self.storage.load_tracks(user_id)

      await self.storage.upsert_connections(
        user_id,
        [connector.connection_summary() for connector in self.connectors.values()]
      )

      events = await self.storage.load_events(user_id)
      snapshot = IngestionSnapshot(
        user_id=user_id,
        tracks=len(tracks),
        events=len(events),
        sources=synced_sources,
        last_sync_at=now,
        detail=self._snapshot_detail(tracks, synced_sources)
      )
      await self.cache.set_json(cache_key, snapshot.model_dump(mode="json", by_alias=True), ttl=self.refresh_interval_seconds)
      self.last_sync_at = now
      return snapshot

  async def load_tracks(self, user_id: str) -> list[UnifiedTrack]:
    return await self.storage.load_tracks(user_id)

  async def load_events(self, user_id: str) -> list[dict[str, Any]]:
    return await self.storage.load_events(user_id)

  def _state_is_fresh(self, state: dict[str, Any] | None, now: datetime) -> bool:
    if not state:
      return False
    raw = state.get("updated_at")
    if not isinstance(raw, str) or not raw:
      return False
    try:
      updated_at = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except Exception:
      return False
    return (now - updated_at).total_seconds() < self.refresh_interval_seconds

  def _snapshot_detail(self, tracks: list[UnifiedTrack], sources: list[str]) -> str:
    if not tracks:
      return "No tracks were refreshed. Cached storage was reused."
    source_text = ", ".join(sources) if sources else "cached storage"
    return f"Indexed {len(tracks)} unified tracks from {source_text}."

  def _cache_key(self, user_id: str) -> str:
    return f"assistant:ingest:{user_id}"
