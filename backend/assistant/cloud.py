from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence
from urllib import error as urllib_error
from urllib import request as urllib_request
from urllib.parse import urljoin

from ..models import UnifiedTrack
from .edge import EdgeRecommendationEngine
from .schemas import AssistantRecommendationRequest, AssistantRecommendationResponse


@dataclass(slots=True)
class CloudAIEngine:
  base_url: str | None = None
  timeout_seconds: float = 8.0
  profile_store: dict[str, dict[str, Any]] = field(default_factory=dict)
  history_store: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
  last_error: str | None = None

  def is_ready(self) -> bool:
    return bool(self.base_url)

  async def fetch_recommendations(
    self,
    request: AssistantRecommendationRequest,
    *,
    edge_engine: EdgeRecommendationEngine,
    tracks: Sequence[UnifiedTrack]
  ) -> AssistantRecommendationResponse:
    if not self.base_url:
      return await edge_engine.recommend(
        tracks,
        request.context,
        limit=request.limit,
        command=request.command,
        seed_track_id=request.seed_track_id,
        mode=request.mode
      )

    payload = request.model_dump(mode="json", by_alias=True)
    payload["forwarded"] = True
    remote = await self._request_json("POST", "/assistant/recommend", payload)
    if isinstance(remote, dict):
      try:
        response = AssistantRecommendationResponse.model_validate(remote)
        if response.mode not in {"edge", "cloud", "hybrid"}:
          response = response.model_copy(update={"mode": request.mode})
        return response
      except Exception:
        self.last_error = "Cloud recommendation payload could not be parsed."

    fallback_mode = request.mode if request.mode in {"edge", "cloud", "hybrid"} else "cloud"
    return await edge_engine.recommend(
      tracks,
      request.context,
      limit=request.limit,
      command=request.command,
      seed_track_id=request.seed_track_id,
      mode=fallback_mode
    )

  async def update_preferences(self, user_id: str, profile: dict[str, Any], *, forward: bool = True) -> None:
    self.profile_store[user_id] = dict(profile)
    if not self.base_url or not forward:
      return
    await self._request_json("POST", "/assistant/profile", {"user_id": user_id, "profile": profile, "forwarded": True})

  async def store_history(self, user_id: str, events: list[dict[str, Any]], *, forward: bool = True) -> None:
    self.history_store.setdefault(user_id, []).extend(dict(event) for event in events)
    if not self.base_url or not forward:
      return
    await self._request_json("POST", "/assistant/history", {"user_id": user_id, "events": events, "forwarded": True})

  async def _request_json(self, method: str, path: str, payload: dict[str, Any] | None) -> Any | None:
    if not self.base_url:
      return None

    def _call() -> Any | None:
      url = urljoin(self.base_url.rstrip("/") + "/", path.lstrip("/"))
      data = None if payload is None else json.dumps(payload).encode("utf-8")
      request = urllib_request.Request(url, data=data, method=method.upper())
      request.add_header("Content-Type", "application/json")
      try:
        with urllib_request.urlopen(request, timeout=self.timeout_seconds) as response:
          raw = response.read().decode("utf-8")
      except (urllib_error.URLError, TimeoutError) as error:
        self.last_error = str(error)
        return None

      if not raw:
        return None
      try:
        return json.loads(raw)
      except json.JSONDecodeError as error:
        self.last_error = str(error)
        return None

    return await asyncio.to_thread(_call)
