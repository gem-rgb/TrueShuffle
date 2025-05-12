from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import Field

from ..models import ApiModel, PlaylistItem, UnifiedTrack

AssistantMode = Literal["edge", "cloud", "hybrid"]
AssistantPhase = Literal["starting", "live", "degraded", "offline"]
TransportName = Literal[
  "bluetooth",
  "bluetooth_a2dp",
  "bluetooth_avrcp",
  "wifi",
  "usb",
  "android_auto",
  "apple_carplay",
  "offline"
]


class DeviceContext(ApiModel):
  user_id: str = "default"
  location: str | None = None
  activity: str = "idle"
  time_of_day: str = "unknown"
  energy: float = 0.5
  online: bool = False
  driving: bool = False
  transport: TransportName = "offline"
  language: str = "en"
  target_language: str = "en"
  preferences: dict[str, float] = Field(default_factory=dict)
  metadata: dict[str, Any] = Field(default_factory=dict)


class ConnectivityStatus(ApiModel):
  transport: TransportName
  connected: bool = False
  supports_audio: bool = False
  supports_controls: bool = False
  supports_sync: bool = False
  latency_ms: int = 0
  last_activity_at: datetime | None = None
  detail: str = ""


class TransportConnectRequest(ApiModel):
  user_id: str = "default"
  context: DeviceContext = Field(default_factory=DeviceContext)
  metadata: dict[str, Any] = Field(default_factory=dict)


class AssistantRecommendationRequest(ApiModel):
  user_id: str = "default"
  context: DeviceContext = Field(default_factory=DeviceContext)
  command: str | None = None
  limit: int = 20
  mode: AssistantMode = "hybrid"
  force_refresh: bool = False
  seed_track_id: str | None = None
  forwarded: bool = False


class AssistantRecommendationResponse(ApiModel):
  user_id: str
  mode: AssistantMode
  items: list[PlaylistItem] = Field(default_factory=list)
  explanation: str = ""
  voice_line: str = ""
  confidence: float = 0.0
  context: DeviceContext
  generated_at: datetime | None = None
  source_counts: dict[str, int] = Field(default_factory=dict)
  metrics: dict[str, Any] = Field(default_factory=dict)


class TranslationRequest(ApiModel):
  user_id: str = "default"
  text: str
  source_lang: str | None = None
  target_lang: str = "en"
  context: DeviceContext = Field(default_factory=DeviceContext)
  voice: bool = True
  forwarded: bool = False


class TranslationResponse(ApiModel):
  user_id: str = "default"
  source_lang: str
  target_lang: str
  detected_lang: str
  original_text: str
  translated_text: str
  confidence: float = 0.0
  voice_line: str = ""


class MusicFeedbackRequest(ApiModel):
  user_id: str = "default"
  track: UnifiedTrack
  action: Literal["skip", "play", "replay", "like"]
  context: DeviceContext = Field(default_factory=DeviceContext)
  limit: int = 20
  mode: AssistantMode = "hybrid"
  command: str | None = None


class AssistantCommandRequest(ApiModel):
  user_id: str = "default"
  text: str
  context: DeviceContext = Field(default_factory=DeviceContext)
  source_lang: str | None = None
  target_lang: str | None = None
  limit: int = 20
  mode: AssistantMode = "hybrid"
  force_refresh: bool = False
  forwarded: bool = False


class AssistantCommandResponse(ApiModel):
  user_id: str
  intent: Literal["music", "translation", "mixed", "general"]
  mode: AssistantMode
  explanation: str = ""
  voice_line: str = ""
  recommendation: AssistantRecommendationResponse | None = None
  translation: TranslationResponse | None = None
  context: DeviceContext


class IngestionSnapshot(ApiModel):
  user_id: str
  tracks: int = 0
  events: int = 0
  sources: list[str] = Field(default_factory=list)
  last_sync_at: datetime | None = None
  detail: str = ""


class CloudProfileRequest(ApiModel):
  user_id: str = "default"
  profile: dict[str, Any] = Field(default_factory=dict)
  forwarded: bool = False


class CloudHistoryRequest(ApiModel):
  user_id: str = "default"
  events: list[dict[str, Any]] = Field(default_factory=list)
  forwarded: bool = False


class CloudWriteResponse(ApiModel):
  user_id: str = "default"
  stored: bool = True
  items: int = 0


class AssistantHealthResponse(ApiModel):
  status: str = "ok"
  service: str = "trueshuffle-assistant"
  phase: AssistantPhase = "starting"
  mode: AssistantMode = "hybrid"
  detail: str = "Booting assistant"
  connectivity: list[ConnectivityStatus] = Field(default_factory=list)
  edge_ready: bool = False
  cloud_ready: bool = False
  last_sync_at: datetime | None = None
