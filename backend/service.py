from __future__ import annotations

import asyncio
import hashlib
from dataclasses import dataclass, field

from .audio_features import AudioFeatureExtractor
from .models import (
  CommandRequest,
  CommandResponse,
  FeedbackRequest,
  FeatureExtractionRequest,
  FeatureExtractionResponse,
  HealthResponse,
  ObjectiveWeights,
  PreferenceHints,
  QueueMetrics,
  RecommendationRequest,
  RecommendationResponse,
  SessionContext,
  SimulationRequest,
  SimulationResponse,
  TrackMetadata
)
from .nlp_commands import CommandParser
from .queue_manager import AdaptiveQueueManager
from .session_context import SessionContextEngine
from .simulation import SimulationEngine


@dataclass(slots=True)
class SessionMemory:
  manager: AdaptiveQueueManager = field(default_factory=AdaptiveQueueManager)
  last_response: RecommendationResponse | None = None
  last_tracks_signature: str | None = None


class AdaptiveMusicService:
  def __init__(self) -> None:
    self._sessions: dict[str, SessionMemory] = {}
    self._lock = asyncio.Lock()
    self.session_engine = SessionContextEngine()
    self.command_parser = CommandParser()
    self.audio_feature_extractor = AudioFeatureExtractor()
    self.simulation_engine = SimulationEngine()

  async def health(self) -> HealthResponse:
    return HealthResponse()

  async def recommend(self, request: RecommendationRequest) -> RecommendationResponse:
    memory = await self._get_session(request.session_id)
    tracks = await asyncio.to_thread(self._enrich_tracks, request.tracks)
    memory.manager.ingest_tracks(tracks)
    response = await asyncio.to_thread(
      memory.manager.build_queue,
      tracks,
      request.session,
      request.weights,
      current_track_id=request.current_track_id,
      seed_track_id=request.seed_track_id,
      limit=request.limit,
      hints=request.hints,
      command=request.command,
      strategy="adaptive"
    )
    response.session_id = request.session_id
    memory.last_tracks_signature = self._tracks_signature(tracks)
    memory.last_response = response
    return response

  async def feedback(self, request: FeedbackRequest) -> RecommendationResponse:
    memory = await self._get_session(request.session_id)
    tracks = request.tracks
    if tracks:
      tracks = await asyncio.to_thread(self._enrich_tracks, tracks)
      memory.manager.ingest_tracks(tracks)
    elif memory.last_response is not None:
      tracks = memory.last_response.tracks

    if not tracks:
      return RecommendationResponse(
        session_id=request.session_id,
        tracks=[],
        metrics=QueueMetrics(
          total_tracks=0,
          unique_artists=0,
          max_artist_run=0,
          artist_switch_rate=0.0,
          transition_entropy=0.0
        ),
        explanation="No tracks were available to update the queue.",
        voice_line="No tracks were available.",
        session=request.session,
        strategy=f"feedback:{request.action}",
        command=request.command
      )

    response = await asyncio.to_thread(
      memory.manager.record_feedback,
      request.track_id,
      request.action,
      request.session,
      request.weights,
      hints=request.hints,
      command=request.command,
      limit=request.limit
    )
    response.session_id = request.session_id
    memory.last_response = response
    return response

  async def parse_command(self, request: CommandRequest) -> CommandResponse:
    parsed_session, hints, intent, explanation = self.command_parser.parse(request.text, request.session)
    return CommandResponse(
      session_id=request.session_id,
      command=request.text,
      intent=intent,
      explanation=explanation,
      voice_line=self._command_voice_line(request.text, parsed_session, hints),
      session=parsed_session,
      hints=hints
    )

  async def simulate(self, request: SimulationRequest) -> SimulationResponse:
    tracks = await asyncio.to_thread(self._enrich_tracks, request.tracks)
    return await asyncio.to_thread(
      self.simulation_engine.run,
      tracks,
      request.session,
      request.strategies,
      runs=request.runs,
      limit=request.limit
    )

  async def extract_features(self, request: FeatureExtractionRequest) -> FeatureExtractionResponse:
    features = await asyncio.to_thread(self.audio_feature_extractor.extract_from_file, request.path)
    return FeatureExtractionResponse(path=request.path, audio_features=features)

  async def _get_session(self, session_id: str) -> SessionMemory:
    async with self._lock:
      memory = self._sessions.get(session_id)
      if memory is None:
        memory = SessionMemory(manager=AdaptiveQueueManager())
        self._sessions[session_id] = memory
      return memory

  def _enrich_tracks(self, tracks: list[TrackMetadata]) -> list[TrackMetadata]:
    enriched = [self.audio_feature_extractor.enrich_track(track) for track in tracks]
    for track in enriched:
      if not track.embedding:
        track.embedding = []
    return enriched

  def _tracks_signature(self, tracks: list[TrackMetadata]) -> str:
    payload = "|".join(track.id for track in tracks)
    return hashlib.blake2b(payload.encode("utf-8"), digest_size=12).hexdigest()

  def _command_voice_line(self, text: str, session: SessionContext, hints: PreferenceHints) -> str:
    genre_text = f" with {', '.join(hints.genre_hints[:2])}" if hints.genre_hints else ""
    return f"I will adapt the queue to {session.activity} mode{genre_text} after '{text.strip()}'."

