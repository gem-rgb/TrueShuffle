from __future__ import annotations

import asyncio
import hashlib
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Sequence

from ..audio_features import AudioFeatureExtractor
from ..models import (
  AudioFeatures,
  ObjectiveWeights,
  PlaylistItem,
  PreferenceHints,
  RecommendationResponse,
  SessionContext,
  TrackMetadata,
  UnifiedTrack
)
from ..queue_manager import AdaptiveQueueManager
from ..preferences import UserPreference
from ..session_context import SessionContextEngine
from .schemas import AssistantRecommendationResponse, DeviceContext, MusicFeedbackRequest


@dataclass(slots=True)
class EdgeRecommendationEngine:
  preference: UserPreference = field(default_factory=UserPreference)
  queue_manager: AdaptiveQueueManager = field(default_factory=AdaptiveQueueManager)
  session_engine: SessionContextEngine = field(default_factory=SessionContextEngine)
  tracks: dict[str, UnifiedTrack] = field(default_factory=dict)
  metadata: dict[str, TrackMetadata] = field(default_factory=dict)
  extractor: AudioFeatureExtractor = field(default_factory=AudioFeatureExtractor)

  def ingest_tracks(self, tracks: Sequence[UnifiedTrack]) -> None:
    self.tracks = {track.id: track for track in tracks}
    self.metadata = {track.id: self._to_metadata(track) for track in tracks}
    self.queue_manager.ingest_tracks(list(self.metadata.values()))

  async def recommend(
    self,
    tracks: Sequence[UnifiedTrack],
    context: DeviceContext,
    *,
    limit: int = 20,
    command: str | None = None,
    seed_track_id: str | None = None,
    mode: str = "edge",
    hints: PreferenceHints | None = None
  ) -> AssistantRecommendationResponse:
    if not tracks:
      return AssistantRecommendationResponse(
        user_id=context.user_id,
        mode=mode if mode in {"edge", "cloud", "hybrid"} else "edge",
        items=[],
        explanation="No tracks were available for recommendation.",
        voice_line="No tracks were available.",
        confidence=0.0,
        context=context.model_copy(deep=True),
        generated_at=datetime.now(timezone.utc)
      )

    self.ingest_tracks(tracks)
    session = self._to_session(context)
    weights = self._weights_for_context(context)
    merged_hints = self._merge_hints(hints)
    response = await asyncio.to_thread(
      self.queue_manager.build_queue,
      list(self.metadata.values()),
      session,
      weights,
      seed_track_id=seed_track_id,
      limit=limit,
      hints=merged_hints,
      command=command,
      strategy=mode
    )
    return self._wrap_response(response, context, mode)

  async def feedback(self, request: MusicFeedbackRequest) -> AssistantRecommendationResponse:
    if request.track.id not in self.tracks:
      self.ingest_tracks([request.track])
    else:
      self.ingest_tracks(list(self.tracks.values()))

    action = self._feedback_action(request.action)
    preference_action = "like" if request.action == "like" else ("skip" if request.action == "skip" else "play")
    self.preference.update_from_event(preference_action, request.track, intensity=1.2 if request.action == "replay" else 1.0)

    session = self._to_session(request.context)
    weights = self._weights_for_context(request.context)
    merged_hints = self._merge_hints(None)
    response = await asyncio.to_thread(
      self.queue_manager.record_feedback,
      request.track.id,
      action,
      session,
      weights,
      hints=merged_hints,
      command=request.command,
      limit=request.limit
    )
    return self._wrap_response(response, request.context, request.mode)

  def _wrap_response(self, response: RecommendationResponse, context: DeviceContext, mode: str) -> AssistantRecommendationResponse:
    items: list[PlaylistItem] = []
    source_counts: Counter[str] = Counter()
    for track in response.tracks:
      unified = self.tracks.get(track.id)
      source = unified.source if unified is not None else "unknown"
      link = unified.link if unified is not None else track.uri
      items.append(
        PlaylistItem(
          track_id=track.id,
          title=track.name,
          artist=track.artist_name,
          source=source,
          link=link or "",
          score=round(response.metrics.preference_score or 0.0, 4)
        )
      )
      source_counts[source] += 1

    metrics = response.metrics.model_dump(mode="json", by_alias=True)
    return AssistantRecommendationResponse(
      user_id=context.user_id,
      mode=mode if mode in {"edge", "cloud", "hybrid"} else "edge",
      items=items,
      explanation=response.explanation,
      voice_line=response.voice_line,
      confidence=response.metrics.rl_confidence or 0.0,
      context=context.model_copy(deep=True),
      generated_at=datetime.now(timezone.utc),
      source_counts=dict(source_counts),
      metrics=metrics
    )

  def _to_session(self, context: DeviceContext) -> SessionContext:
    session = self.session_engine.derive(activity=context.activity, energy=context.energy)
    if context.time_of_day != "unknown":
      session = self.session_engine.apply_patch(
        session,
        time_of_day=context.time_of_day,
        activity=context.activity,
        energy=context.energy
      )
    return session

  def _to_metadata(self, track: UnifiedTrack) -> TrackMetadata:
    features = track.features or {}
    audio_features = self._to_audio_features(track, features)
    return TrackMetadata(
      id=track.id,
      uri=track.link or f"{track.source}:{track.external_id or track.id}",
      name=track.title,
      artist_id=self._artist_id(track),
      artist_name=track.artist,
      album_name=track.album or track.title,
      duration_ms=int(track.duration_ms or 180_000),
      popularity=int(round(track.popularity)),
      genres=list(track.genres),
      audio_features=audio_features,
      embedding=[]
    )

  def _to_audio_features(self, track: UnifiedTrack, features: dict[str, Any]) -> AudioFeatures:
    mfcc = features.get("mfcc")
    if isinstance(mfcc, list):
      mfcc_values = [float(value) for value in mfcc if isinstance(value, (int, float))]
    else:
      fallback = TrackMetadata(
        id=track.id,
        uri=track.link or f"{track.source}:{track.external_id or track.id}",
        name=track.title,
        artist_id=self._artist_id(track),
        artist_name=track.artist,
        album_name=track.album or track.title,
        duration_ms=int(track.duration_ms or 180_000),
        popularity=int(round(track.popularity)),
        genres=list(track.genres)
      )
      inferred = self.extractor.infer_from_metadata(fallback)
      return inferred

    return AudioFeatures(
      tempo=float(features.get("tempo", 0.0)),
      energy=float(features.get("energy", 0.0)),
      spectral_centroid=float(features.get("spectral_centroid", 0.0)),
      spectral_bandwidth=float(features.get("spectral_bandwidth", 0.0)),
      spectral_rolloff=float(features.get("spectral_rolloff", 0.0)),
      zero_crossing_rate=float(features.get("zero_crossing_rate", 0.0)),
      mfcc=mfcc_values
    )

  def _weights_for_context(self, context: DeviceContext) -> ObjectiveWeights:
    if context.activity in {"drive", "driving", "workout"} or context.driving:
      return ObjectiveWeights(preference_weight=0.45, diversity_weight=0.28, novelty_weight=0.27)
    if context.activity in {"focus", "work"}:
      return ObjectiveWeights(preference_weight=0.52, diversity_weight=0.3, novelty_weight=0.18)
    if context.activity in {"relax", "sleep", "rest"}:
      return ObjectiveWeights(preference_weight=0.58, diversity_weight=0.24, novelty_weight=0.18)
    return ObjectiveWeights()

  def _merge_hints(self, hints: PreferenceHints | None) -> PreferenceHints:
    derived = PreferenceHints(
      genre_hints=self.preference.top_genres(),
      artist_hints=self.preference.top_artists(),
      keywords=self.preference.top_moods()
    )
    if hints is None:
      return derived

    return PreferenceHints(
      genre_hints=self._dedupe([*hints.genre_hints, *derived.genre_hints]),
      artist_hints=self._dedupe([*hints.artist_hints, *derived.artist_hints]),
      keywords=self._dedupe([*hints.keywords, *derived.keywords])
    )

  def _dedupe(self, values: Sequence[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))

  def _feedback_action(self, action: str) -> str:
    return {
      "skip": "skip",
      "play": "full_play",
      "replay": "replay",
      "like": "full_play"
    }.get(action, "full_play")

  def _artist_id(self, track: UnifiedTrack) -> str:
    payload = f"{track.source}|{track.artist}".encode("utf-8")
    return hashlib.blake2b(payload, digest_size=8).hexdigest()
