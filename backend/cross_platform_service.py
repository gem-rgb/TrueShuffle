from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .cache import CacheBackend, create_cache
from .connectors import AppleMusicConnector, PodcastConnector, SpotifyConnector, YouTubeMusicConnector
from .models import (
  BackendStatusResponse,
  CrossPlatformFeedbackResponse,
  PlatformConnectRequest,
  PlatformConnectResponse,
  PlaylistResponse,
  UserProfileResponse
)
from .preferences import UserPreference
from .storage import StorageBackend, create_storage
from .sync_engine import MusicSyncEngine


def _supported_connectors() -> dict[str, Any]:
  return {
    "spotify": SpotifyConnector(),
    "youtube_music": YouTubeMusicConnector(),
    "apple_music": AppleMusicConnector(),
    "podcasts": PodcastConnector()
  }


@dataclass(slots=True)
class CrossPlatformMusicService:
  user_id: str = "default"
  storage: StorageBackend = field(default_factory=create_storage)
  cache: CacheBackend = field(default_factory=create_cache)
  preference: UserPreference = field(default_factory=UserPreference)
  connectors: dict[str, Any] = field(default_factory=_supported_connectors)
  sync_interval_seconds: int = 300
  _sync_engine: MusicSyncEngine | None = None
  _startup_complete: bool = False
  _startup_lock: asyncio.Lock = field(default_factory=asyncio.Lock)

  def __post_init__(self) -> None:
    self._sync_engine = MusicSyncEngine(
      user_id=self.user_id,
      connectors=self.connectors,
      preference=self.preference,
      storage=self.storage,
      cache=self.cache,
      sync_interval_seconds=self.sync_interval_seconds
    )

  async def start(self) -> None:
    async with self._startup_lock:
      if self._startup_complete:
        return
      if self._sync_engine is None:
        self.__post_init__()
      await self._sync_engine.start()
      self._startup_complete = True

  async def stop(self) -> None:
    if self._sync_engine is not None:
      await self._sync_engine.stop()
    self._startup_complete = False

  async def health(self) -> BackendStatusResponse:
    detail = "Unified playlist engine live." if self._startup_complete else "Booting unified playlist engine."
    connected = [name for name, connector in self.connectors.items() if connector.state.connected]
    last_sync = self._sync_engine.last_sync_at if self._sync_engine is not None else None
    phase = "live" if self._startup_complete else "starting"
    return BackendStatusResponse(
      status="ok",
      service="trueshuffle-ai",
      phase=phase,
      detail=detail,
      connected_platforms=connected,
      syncing=self._sync_engine.syncing if self._sync_engine is not None else False,
      last_sync_at=last_sync
    )

  async def connect_platform(self, platform: str, request: PlatformConnectRequest) -> PlatformConnectResponse:
    connector = self.connectors.get(platform)
    if connector is None:
      raise KeyError(platform)

    response = await connector.connect(request)
    assert self._sync_engine is not None
    await self._sync_engine.sync_once(platforms=[platform])
    return response

  async def profile(self, user_id: str = "default") -> UserProfileResponse:
    assert self._sync_engine is not None
    return await self._sync_engine.profile()

  async def playlist(self, user_id: str = "default") -> PlaylistResponse:
    assert self._sync_engine is not None
    return await self._sync_engine.playlist()

  async def feedback(self, request: Any) -> CrossPlatformFeedbackResponse:
    assert self._sync_engine is not None
    return await self._sync_engine.record_feedback(request)
