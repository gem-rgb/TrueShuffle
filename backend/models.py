from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


def to_camel(value: str) -> str:
  parts = value.split("_")
  if not parts:
    return value
  return parts[0] + "".join(part[:1].upper() + part[1:] for part in parts[1:])


class ApiModel(BaseModel):
  model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


class AudioFeatures(ApiModel):
  tempo: float = 0.0
  energy: float = 0.0
  spectral_centroid: float = 0.0
  spectral_bandwidth: float = 0.0
  spectral_rolloff: float = 0.0
  zero_crossing_rate: float = 0.0
  mfcc: list[float] = Field(default_factory=list)


class TrackMetadata(ApiModel):
  id: str
  uri: str
  name: str
  artist_id: str
  artist_name: str
  album_name: str
  duration_ms: int
  popularity: int = 50
  added_at: datetime | None = None
  last_played_at: datetime | None = None
  genres: list[str] = Field(default_factory=list)
  audio_features: AudioFeatures | None = None
  embedding: list[float] = Field(default_factory=list)
  analysis_path: str | None = None


class UnifiedTrack(ApiModel):
  id: str
  title: str
  artist: str
  source: str
  features: dict[str, Any] = Field(default_factory=dict)
  link: str | None = None
  genres: list[str] = Field(default_factory=list)
  mood: list[str] = Field(default_factory=list)
  album: str | None = None
  duration_ms: int | None = None
  popularity: float = 0.0
  external_id: str | None = None
  raw: dict[str, Any] = Field(default_factory=dict)


class PlaylistItem(ApiModel):
  track_id: str | None = None
  title: str
  artist: str
  source: str
  link: str
  score: float | None = None


class ListeningEvent(ApiModel):
  platform: str
  event_type: Literal["play", "skip", "like"]
  track: UnifiedTrack
  intensity: float = 1.0
  occurred_at: datetime | None = None
  context: dict[str, Any] = Field(default_factory=dict)


class PlatformConnectRequest(ApiModel):
  user_id: str = "default"
  access_token: str | None = None
  refresh_token: str | None = None
  profile_name: str | None = None
  options: dict[str, Any] = Field(default_factory=dict)


class PlatformConnectResponse(ApiModel):
  platform: str
  connected: bool
  status: str
  detail: str
  connector_name: str
  preview_count: int = 0
  last_sync_at: datetime | None = None


class ListeningStats(ApiModel):
  total_plays: int = 0
  skips: int = 0
  likes: int = 0
  sessions: int = 0
  tracks_seen: int = 0
  sources: dict[str, int] = Field(default_factory=dict)
  last_sync_at: datetime | None = None


class PreferenceBucket(ApiModel):
  genres: dict[str, float] = Field(default_factory=dict)
  artists: dict[str, float] = Field(default_factory=dict)
  mood: dict[str, float] = Field(default_factory=dict)
  sources: dict[str, float] = Field(default_factory=dict)
  history: list[dict[str, Any]] = Field(default_factory=list)


class UserProfileResponse(ApiModel):
  user_id: str
  stats: ListeningStats
  preferences: PreferenceBucket
  connections: list[PlatformConnectResponse] = Field(default_factory=list)
  top_genres: list[str] = Field(default_factory=list)
  top_artists: list[str] = Field(default_factory=list)
  top_moods: list[str] = Field(default_factory=list)
  summary: str = ""
  updated_at: datetime | None = None


class PlaylistResponse(ApiModel):
  items: list[PlaylistItem] = Field(default_factory=list)
  generated_at: datetime | None = None
  source_counts: dict[str, int] = Field(default_factory=dict)
  summary: str = ""


class CrossPlatformFeedbackResponse(ApiModel):
  profile: UserProfileResponse
  playlist: PlaylistResponse
  summary: str = ""


class BackendStatusResponse(ApiModel):
  status: str = "ok"
  service: str = "trueshuffle-ai"
  phase: Literal["starting", "live", "degraded", "offline"] = "starting"
  detail: str = "Booting"
  connected_platforms: list[str] = Field(default_factory=list)
  syncing: bool = False
  last_sync_at: datetime | None = None


class SessionContext(ApiModel):
  time_of_day: str
  activity: str
  energy: float


class PreferenceHints(ApiModel):
  genre_hints: list[str] = Field(default_factory=list)
  artist_hints: list[str] = Field(default_factory=list)
  keywords: list[str] = Field(default_factory=list)


class ObjectiveWeights(ApiModel):
  preference_weight: float = 0.5
  diversity_weight: float = 0.3
  novelty_weight: float = 0.2


class QueueMetrics(ApiModel):
  total_tracks: int
  unique_artists: int
  max_artist_run: int
  artist_switch_rate: float
  transition_entropy: float
  preference_score: float | None = None
  diversity_score: float | None = None
  novelty_score: float | None = None
  rl_confidence: float | None = None
  graph_coverage: float | None = None
  embedding_similarity: float | None = None


class RecommendationRequest(ApiModel):
  session_id: str = "default"
  tracks: list[TrackMetadata]
  session: SessionContext
  current_track_id: str | None = None
  seed_track_id: str | None = None
  command: str | None = None
  hints: PreferenceHints = Field(default_factory=PreferenceHints)
  limit: int | None = None
  weights: ObjectiveWeights = Field(default_factory=ObjectiveWeights)


class RecommendationResponse(ApiModel):
  session_id: str
  tracks: list[TrackMetadata]
  metrics: QueueMetrics
  explanation: str
  voice_line: str
  session: SessionContext
  strategy: str = "adaptive"
  command: str | None = None
  seed_track_id: str | None = None


class FeedbackRequest(ApiModel):
  session_id: str = "default"
  track_id: str | None = None
  action: Literal["skip", "full_play", "replay"] | None = None
  session: SessionContext
  tracks: list[TrackMetadata] = Field(default_factory=list)
  hints: PreferenceHints = Field(default_factory=PreferenceHints)
  weights: ObjectiveWeights = Field(default_factory=ObjectiveWeights)
  limit: int | None = None
  command: str | None = None
  platform: str | None = None
  event_type: Literal["play", "skip", "like"] | None = None
  track: UnifiedTrack | None = None
  intensity: float = 1.0
  user_id: str = "default"


class CommandRequest(ApiModel):
  session_id: str = "default"
  text: str
  session: SessionContext


class CommandResponse(ApiModel):
  session_id: str
  command: str
  intent: str
  explanation: str
  voice_line: str
  session: SessionContext
  hints: PreferenceHints


class SimulationRequest(ApiModel):
  session_id: str = "default"
  tracks: list[TrackMetadata]
  session: SessionContext
  strategies: list[str] = Field(default_factory=lambda: ["adaptive", "balanced", "graph", "embedding"])
  runs: int = 5
  limit: int | None = None
  weights: ObjectiveWeights = Field(default_factory=ObjectiveWeights)


class SimulationStrategyResult(ApiModel):
  name: str
  average_reward: float
  diversity_score: float
  novelty_score: float
  skip_rate: float
  replay_rate: float
  queue_entropy: float
  preference_score: float
  rl_confidence: float


class SimulationResponse(ApiModel):
  session_id: str
  summary: str
  strategies: list[SimulationStrategyResult]


class FeatureExtractionRequest(ApiModel):
  path: str
  track: TrackMetadata | None = None


class FeatureExtractionResponse(ApiModel):
  path: str
  audio_features: AudioFeatures


class HealthResponse(ApiModel):
  status: str = "ok"
  service: str = "trueshuffle-ai"
  phase: Literal["starting", "live", "degraded", "offline"] = "starting"
  detail: str = "Booting"
  connected_platforms: list[str] = Field(default_factory=list)
  syncing: bool = False
  last_sync_at: datetime | None = None
