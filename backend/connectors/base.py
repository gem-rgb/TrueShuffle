from __future__ import annotations

import asyncio
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping

from ..models import PlatformConnectRequest, PlatformConnectResponse
from .library import get_platform_payload


@dataclass(slots=True)
class ConnectorState:
  connected: bool = False
  access_token: str | None = None
  refresh_token: str | None = None
  profile_name: str | None = None
  options: dict[str, Any] = field(default_factory=dict)
  connected_at: datetime | None = None
  last_sync_at: datetime | None = None
  preview_count: int = 0


class BaseConnector(ABC):
  platform: str

  def __init__(self, *, platform: str | None = None, state: ConnectorState | None = None) -> None:
    if platform is not None:
      self.platform = platform
    if not hasattr(self, "platform"):
      raise ValueError("Connector subclasses must define a platform name.")
    self.state = state or ConnectorState()
    self._min_interval = 0.15
    self._last_call = 0.0
    self._lock = asyncio.Lock()

  @property
  def connector_name(self) -> str:
    return self.__class__.__name__

  def connection_summary(self) -> PlatformConnectResponse:
    status = "connected" if self.state.connected else "demo"
    detail = "Connected to platform" if self.state.connected else "Demo data available"
    return PlatformConnectResponse(
      platform=self.platform,
      connected=self.state.connected,
      status=status,
      detail=detail,
      connector_name=self.connector_name,
      preview_count=self.state.preview_count,
      last_sync_at=self.state.last_sync_at
    )

  async def connect(self, request: PlatformConnectRequest) -> PlatformConnectResponse:
    self.state.connected = True
    self.state.access_token = request.access_token
    self.state.refresh_token = request.refresh_token
    self.state.profile_name = request.profile_name
    self.state.options = dict(request.options)
    self.state.connected_at = datetime.now(timezone.utc)

    preview_count = len(await self.fetch_recent()) + len(await self.fetch_liked())
    self.state.preview_count = preview_count
    self.state.last_sync_at = datetime.now(timezone.utc)
    return PlatformConnectResponse(
      platform=self.platform,
      connected=True,
      status="connected" if request.access_token else "demo",
      detail=f"Prepared {preview_count} preview items for {self.platform}.",
      connector_name=self.connector_name,
      preview_count=preview_count,
      last_sync_at=self.state.last_sync_at
    )

  async def fetch_recent(self) -> list[dict[str, Any]]:
    await self._throttle()
    return self._clone_payload("recent")

  async def fetch_liked(self) -> list[dict[str, Any]]:
    await self._throttle()
    return self._clone_payload("liked")

  async def fetch_playlists(self) -> list[dict[str, Any]]:
    await self._throttle()
    return self._clone_payload("playlists")

  async def _throttle(self) -> None:
    async with self._lock:
      now = time.monotonic()
      delta = now - self._last_call
      if delta < self._min_interval:
        await asyncio.sleep(self._min_interval - delta)
      self._last_call = time.monotonic()

  def _clone_payload(self, kind: str) -> list[dict[str, Any]]:
    return [dict(item) for item in get_platform_payload(self.platform, kind)]
