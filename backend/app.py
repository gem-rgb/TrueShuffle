from __future__ import annotations

import asyncio

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .assistant.orchestrator import UnifiedAssistantService
from .assistant.router import build_assistant_router
from .cross_platform_service import CrossPlatformMusicService
from .models import (
  BackendStatusResponse,
  CommandRequest,
  CommandResponse,
  FeedbackRequest,
  FeatureExtractionRequest,
  FeatureExtractionResponse,
  HealthResponse,
  PlatformConnectRequest,
  PlatformConnectResponse,
  PlaylistResponse,
  RecommendationRequest,
  RecommendationResponse,
  SimulationRequest,
  SimulationResponse,
  UserProfileResponse
)
from .service import AdaptiveMusicService


app = FastAPI(title="TrueShuffle Adaptive AI", version="0.1.0")
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

adaptive_service = AdaptiveMusicService()
cross_platform_service = CrossPlatformMusicService()
assistant_service = UnifiedAssistantService(
  user_id="default",
  storage=cross_platform_service.storage,
  cache=cross_platform_service.cache,
  connectors=cross_platform_service.connectors,
  adaptive_service=adaptive_service
)

app.include_router(build_assistant_router(assistant_service))


@app.on_event("startup")
async def startup_event() -> None:
  loop = asyncio.get_running_loop()
  task = loop.create_task(cross_platform_service.start())
  app.state.cross_platform_start_task = task
  await assistant_service.start()


@app.on_event("shutdown")
async def shutdown_event() -> None:
  await cross_platform_service.stop()
  await assistant_service.stop()
  task = getattr(app.state, "cross_platform_start_task", None)
  if task is not None:
    task.cancel()
    try:
      await task
    except asyncio.CancelledError:
      pass


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
  return await cross_platform_service.health()


@app.post("/recommend", response_model=RecommendationResponse)
async def recommend(request: RecommendationRequest) -> RecommendationResponse:
  return await adaptive_service.recommend(request)


@app.post("/feedback")
async def feedback(request: FeedbackRequest):
  if request.track_id is not None and request.action is not None:
    return await adaptive_service.feedback(request)

  if request.event_type is not None and (request.track is not None or request.track_id is not None):
    return await cross_platform_service.feedback(request)

  raise HTTPException(status_code=400, detail="Feedback payload must include adaptive or cross-platform fields.")


@app.post("/command/parse", response_model=CommandResponse)
async def parse_command(request: CommandRequest) -> CommandResponse:
  return await adaptive_service.parse_command(request)


@app.post("/simulate", response_model=SimulationResponse)
async def simulate(request: SimulationRequest) -> SimulationResponse:
  return await adaptive_service.simulate(request)


@app.post("/audio/features", response_model=FeatureExtractionResponse)
async def audio_features(request: FeatureExtractionRequest) -> FeatureExtractionResponse:
  return await adaptive_service.extract_features(request)


@app.post("/connect/{platform}", response_model=PlatformConnectResponse)
async def connect_platform(platform: str, request: PlatformConnectRequest) -> PlatformConnectResponse:
  try:
    return await cross_platform_service.connect_platform(platform, request)
  except KeyError as error:
    raise HTTPException(status_code=404, detail=f"Unsupported platform: {platform}") from error


@app.get("/profile", response_model=UserProfileResponse)
async def profile(user_id: str = "default") -> UserProfileResponse:
  return await cross_platform_service.profile(user_id)


@app.get("/playlist", response_model=PlaylistResponse)
async def playlist(user_id: str = "default") -> PlaylistResponse:
  return await cross_platform_service.playlist(user_id)
