from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from os import getenv
from typing import Any

from ..connectors import AppleMusicConnector, PodcastConnector, SpotifyConnector, YouTubeMusicConnector
from ..cache import CacheBackend, create_cache
from ..models import ListeningStats, PlatformConnectResponse, PreferenceBucket, SessionContext, UserProfileResponse
from ..nlp_commands import CommandParser
from ..preferences import UserPreference
from ..service import AdaptiveMusicService
from ..storage import StorageBackend, create_storage
from .cloud import CloudAIEngine
from .connectivity import ConnectivityManager
from .context import ContextEngine
from .data import DataIngestionPipeline
from .edge import EdgeRecommendationEngine
from .language import LanguageEngine
from .schemas import (
  AssistantCommandRequest,
  AssistantCommandResponse,
  AssistantHealthResponse,
  AssistantRecommendationRequest,
  AssistantRecommendationResponse,
  CloudHistoryRequest,
  CloudProfileRequest,
  CloudWriteResponse,
  ConnectivityStatus,
  DeviceContext,
  IngestionSnapshot,
  MusicFeedbackRequest,
  TransportConnectRequest,
  TranslationRequest,
  TranslationResponse
)
from .voice import VoiceEngine


def _default_connectors() -> dict[str, Any]:
  return {
    "spotify": SpotifyConnector(),
    "youtube_music": YouTubeMusicConnector(),
    "apple_music": AppleMusicConnector(),
    "podcasts": PodcastConnector()
  }


@dataclass(slots=True)
class UnifiedAssistantService:
  user_id: str = "default"
  storage: StorageBackend = field(default_factory=create_storage)
  cache: CacheBackend = field(default_factory=create_cache)
  connectors: dict[str, Any] = field(default_factory=_default_connectors)
  adaptive_service: AdaptiveMusicService = field(default_factory=AdaptiveMusicService)
  preference: UserPreference = field(default_factory=UserPreference)
  context_engine: ContextEngine = field(default_factory=ContextEngine)
  connectivity: ConnectivityManager = field(default_factory=ConnectivityManager)
  language_engine: LanguageEngine = field(default_factory=LanguageEngine)
  voice_engine: VoiceEngine = field(default_factory=VoiceEngine)
  cloud_engine: CloudAIEngine = field(default_factory=CloudAIEngine)
  edge_engine: EdgeRecommendationEngine = field(default_factory=EdgeRecommendationEngine)
  data_pipeline: DataIngestionPipeline | None = None
  command_parser: CommandParser = field(default_factory=CommandParser)
  last_sync_at: datetime | None = None
  _ready: bool = False
  _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

  def __post_init__(self) -> None:
    cloud_url = getenv("TRUESHUFFLE_CLOUD_AI_URL", "").strip() or None
    if cloud_url:
      self.cloud_engine.base_url = cloud_url
    self.edge_engine = EdgeRecommendationEngine(preference=self.preference)
    self.data_pipeline = DataIngestionPipeline(
      storage=self.storage,
      cache=self.cache,
      connectors=self.connectors,
      preference=self.preference
    )

  async def start(self) -> None:
    async with self._lock:
      self._ready = True

  async def stop(self) -> None:
    async with self._lock:
      self._ready = False

  async def health(self) -> AssistantHealthResponse:
    connectivity = self.connectivity.status()
    phase = "live" if self._ready else "starting"
    detail = "Unified assistant ready." if self._ready else "Booting unified assistant."
    return AssistantHealthResponse(
      phase=phase,
      mode=self.context_engine.mode(),
      detail=detail,
      connectivity=connectivity,
      edge_ready=self._ready,
      cloud_ready=self.cloud_engine.is_ready(),
      last_sync_at=self.last_sync_at
    )

  async def connect_transport(self, transport: str, request: TransportConnectRequest | None = None) -> ConnectivityStatus:
    payload = request.context if request is not None else self.context_engine.snapshot()
    context = self.context_engine.merge(payload)
    status = await self.connectivity.connect(transport, context)
    self.context_engine.apply_transport(
      transport,
      online=status.supports_sync or context.online,
      driving=transport in {"android_auto", "apple_carplay"}
    )
    return status

  async def update_context(self, context: DeviceContext) -> DeviceContext:
    return self.context_engine.merge(context)

  async def recommend(self, request: AssistantRecommendationRequest) -> AssistantRecommendationResponse:
    context = self.context_engine.merge(request.context)
    if self.data_pipeline is None:
      raise RuntimeError("Data pipeline is not available.")

    await self.data_pipeline.ingest(request.user_id, force=request.force_refresh)
    tracks = await self.storage.load_tracks(request.user_id)
    if not tracks:
      return await self.edge_engine.recommend(
        tracks,
        context,
        limit=request.limit,
        command=request.command,
        seed_track_id=request.seed_track_id,
        mode=request.mode
      )

    if request.command and self.adaptive_service is not None:
      session, hints, _, explanation = self.command_parser.parse(
        request.command,
        self.context_engine.to_session(context)
      )
      context = self.context_engine.apply_session(session)
    else:
      hints = None
      explanation = ""

    effective_request = request.model_copy(update={"context": context})

    if not request.forwarded and (request.mode == "cloud" or (request.mode == "hybrid" and self.cloud_engine.is_ready() and context.online)):
      response = await self.cloud_engine.fetch_recommendations(
        effective_request,
        edge_engine=self.edge_engine,
        tracks=tracks
      )
    else:
      response = await self.edge_engine.recommend(
        tracks,
        context,
        limit=effective_request.limit,
        command=effective_request.command,
        seed_track_id=effective_request.seed_track_id,
        mode=effective_request.mode,
        hints=hints
      )

    if explanation:
      response = response.model_copy(update={"explanation": f"{explanation} {response.explanation}".strip()})
    self.last_sync_at = response.generated_at
    return response

  async def translate(self, request: TranslationRequest) -> TranslationResponse:
    context = self.context_engine.merge(request.context)
    source_lang = request.source_lang or context.language or self.language_engine.detect_language(request.text)
    target_lang = request.target_lang or context.target_language or self.language_engine.extract_target_language(request.text, "en")
    response = self.language_engine.translate_text(
      request.text,
      source_lang=source_lang,
      target_lang=target_lang,
      user_id=request.user_id,
      voice=request.voice
    )
    self.context_engine.merge(
      context.model_copy(update={"language": response.source_lang, "target_language": response.target_lang})
    )
    return response

  async def handle_command(self, request: AssistantCommandRequest) -> AssistantCommandResponse:
    context = self.context_engine.merge(request.context)
    translation_needed = self.language_engine.is_translation_request(request.text) or bool(request.target_lang)
    music_needed = self.language_engine.is_music_request(request.text)

    recommendation: AssistantRecommendationResponse | None = None
    translation: TranslationResponse | None = None
    explanation_parts: list[str] = []

    if music_needed and self.adaptive_service is not None:
      session, hints, intent, explanation = self.command_parser.parse(request.text, self.context_engine.to_session(context))
      context = self.context_engine.apply_session(session)
      explanation_parts.append(explanation)
      recommendation = await self.recommend(
        AssistantRecommendationRequest(
          user_id=request.user_id,
          context=context,
          command=request.text,
          limit=request.limit,
          mode=request.mode,
          force_refresh=request.force_refresh
        )
      )
      recommendation = recommendation.model_copy(update={"mode": request.mode})

    if translation_needed:
      translation = await self.translate(
        TranslationRequest(
          user_id=request.user_id,
          text=request.text,
          source_lang=request.source_lang,
          target_lang=request.target_lang or context.target_language,
          context=context
        )
      )

    if recommendation is not None and translation is not None:
      intent = "mixed"
    elif recommendation is not None:
      intent = "music"
    elif translation is not None:
      intent = "translation"
    else:
      intent = "general"

    voice_line = ""
    if recommendation is not None:
      voice_line = self.voice_engine.narrate_recommendation(recommendation)
    if translation is not None:
      translated_voice = self.voice_engine.narrate_translation(translation)
      voice_line = f"{voice_line} {translated_voice}".strip() if voice_line else translated_voice

    explanation = " ".join(part for part in explanation_parts if part).strip()
    return AssistantCommandResponse(
      user_id=request.user_id,
      intent=intent,
      mode=request.mode,
      explanation=explanation,
      voice_line=voice_line,
      recommendation=recommendation,
      translation=translation,
      context=context
    )

  async def record_cloud_profile(self, request: CloudProfileRequest) -> CloudWriteResponse:
    await self.cloud_engine.update_preferences(request.user_id, request.profile, forward=False)
    return CloudWriteResponse(user_id=request.user_id, stored=True, items=len(request.profile))

  async def record_cloud_history(self, request: CloudHistoryRequest) -> CloudWriteResponse:
    await self.cloud_engine.store_history(request.user_id, request.events, forward=False)
    return CloudWriteResponse(user_id=request.user_id, stored=True, items=len(request.events))

  async def feedback(self, request: MusicFeedbackRequest) -> AssistantRecommendationResponse:
    if self.data_pipeline is None:
      raise RuntimeError("Data pipeline is not available.")

    context = self.context_engine.merge(request.context)
    await self.data_pipeline.ingest(request.user_id, force=False)
    tracks = await self.storage.load_tracks(request.user_id)
    if request.track.id not in {track.id for track in tracks}:
      tracks.append(request.track)
      await self.storage.upsert_tracks(request.user_id, tracks)

    self.edge_engine.ingest_tracks(tracks)

    event = {
      "platform": request.track.source,
      "event_type": request.action,
      "track": request.track.model_dump(mode="json", by_alias=True),
      "context": context.model_dump(mode="json", by_alias=True),
      "timestamp": datetime.now(timezone.utc).isoformat(),
      "source": "assistant"
    }
    await self.storage.append_event(request.user_id, event)
    await self.cloud_engine.store_history(request.user_id, [event])
    await self.cloud_engine.update_preferences(request.user_id, self.preference.snapshot())
    response = await self.edge_engine.feedback(request)
    self.last_sync_at = response.generated_at
    await self._persist_profile(request.user_id, tracks)
    return response

  async def sync_pull(self, user_id: str | None = None, *, force: bool = False) -> IngestionSnapshot:
    if self.data_pipeline is None:
      raise RuntimeError("Data pipeline is not available.")

    target_user = user_id or self.user_id
    snapshot = await self.data_pipeline.ingest(target_user, force=force)
    tracks = await self.storage.load_tracks(target_user)
    self.edge_engine.ingest_tracks(tracks)
    await self._persist_profile(target_user, tracks)
    self.last_sync_at = snapshot.last_sync_at
    return snapshot

  async def sync_push(self, user_id: str | None = None) -> IngestionSnapshot:
    target_user = user_id or self.user_id
    tracks = await self.storage.load_tracks(target_user)
    events = await self.storage.load_events(target_user)
    await self.cloud_engine.store_history(target_user, events)
    await self.cloud_engine.update_preferences(target_user, self.preference.snapshot())
    await self._persist_profile(target_user, tracks)
    self.last_sync_at = datetime.now(timezone.utc)
    snapshot = IngestionSnapshot(
      user_id=target_user,
      tracks=len(tracks),
      events=len(events),
      sources=list(self.connectors.keys()),
      last_sync_at=self.last_sync_at,
      detail="Pushed local state to the cloud mirror."
    )
    return snapshot

  async def _persist_profile(self, user_id: str, tracks: list[Any]) -> None:
    source_counts: dict[str, int] = {}
    for track in tracks:
      source = getattr(track, "source", "unknown")
      source_counts[source] = source_counts.get(source, 0) + 1

    snapshot = self.preference.snapshot()
    connections = [
      connector.connection_summary()
      for connector in self.connectors.values()
      if hasattr(connector, "connection_summary")
    ]
    profile = UserProfileResponse(
      user_id=user_id,
      stats=ListeningStats(
        total_plays=int(self.preference.stats.get("play", 0)),
        skips=int(self.preference.stats.get("skip", 0)),
        likes=int(self.preference.stats.get("like", 0)),
        sessions=max(1, len(self.preference.history)),
        tracks_seen=len(tracks),
        sources=source_counts,
        last_sync_at=self.last_sync_at
      ),
      preferences=PreferenceBucket(
        genres=dict(snapshot["genres"]),
        artists=dict(snapshot["artists"]),
        mood=dict(snapshot["mood"]),
        sources=dict(snapshot["sources"]),
        history=list(snapshot["history"])
      ),
      connections=[connection.model_copy(deep=True) for connection in connections],
      top_genres=self.preference.top_genres(),
      top_artists=self.preference.top_artists(),
      top_moods=self.preference.top_moods(),
      summary=self.preference.summary(),
      updated_at=self.last_sync_at
    )
    await self.storage.upsert_profile(user_id, profile)
