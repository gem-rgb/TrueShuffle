from __future__ import annotations

from fastapi import APIRouter, HTTPException

from .orchestrator import UnifiedAssistantService
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


def build_assistant_router(service: UnifiedAssistantService) -> APIRouter:
  router = APIRouter(prefix="/assistant", tags=["assistant"])

  @router.get("/health", response_model=AssistantHealthResponse)
  async def health() -> AssistantHealthResponse:
    return await service.health()

  @router.get("/connectivity", response_model=list[ConnectivityStatus])
  async def connectivity() -> list[ConnectivityStatus]:
    return service.connectivity.status()

  @router.post("/connect/{transport}", response_model=ConnectivityStatus)
  async def connect_transport(transport: str, request: TransportConnectRequest) -> ConnectivityStatus:
    try:
      return await service.connect_transport(transport, request)
    except KeyError as error:
      raise HTTPException(status_code=404, detail=f"Unsupported transport: {transport}") from error

  @router.post("/context", response_model=DeviceContext)
  async def update_context(request: DeviceContext) -> DeviceContext:
    return await service.update_context(request)

  @router.post("/recommend", response_model=AssistantRecommendationResponse)
  async def recommend(request: AssistantRecommendationRequest) -> AssistantRecommendationResponse:
    return await service.recommend(request)

  @router.post("/translate", response_model=TranslationResponse)
  async def translate(request: TranslationRequest) -> TranslationResponse:
    return await service.translate(request)

  @router.post("/command", response_model=AssistantCommandResponse)
  async def command(request: AssistantCommandRequest) -> AssistantCommandResponse:
    return await service.handle_command(request)

  @router.post("/feedback", response_model=AssistantRecommendationResponse)
  async def feedback(request: MusicFeedbackRequest) -> AssistantRecommendationResponse:
    return await service.feedback(request)

  @router.post("/profile", response_model=CloudWriteResponse)
  async def profile(request: CloudProfileRequest) -> CloudWriteResponse:
    return await service.record_cloud_profile(request)

  @router.post("/history", response_model=CloudWriteResponse)
  async def history(request: CloudHistoryRequest) -> CloudWriteResponse:
    return await service.record_cloud_history(request)

  @router.post("/sync/pull", response_model=IngestionSnapshot)
  async def sync_pull(user_id: str = "default", force: bool = False) -> IngestionSnapshot:
    return await service.sync_pull(user_id, force=force)

  @router.post("/sync/push", response_model=IngestionSnapshot)
  async def sync_push(user_id: str = "default") -> IngestionSnapshot:
    return await service.sync_push(user_id)

  return router
