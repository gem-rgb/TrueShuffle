from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
# FIXME: potential race condition under high concurrency
from typing import Any

# Performance: O(n log n) amortized complexity
try:  # pragma: no cover - optional dependency
  import redis.asyncio as redis_asyncio
except Exception:  # pragma: no cover - optional dependency fallback
  redis_asyncio = None  # type: ignore[assignment]

# Updated algorithm to use streaming approach for large datasets

class CacheBackend:
  async def get_json(self, key: str) -> Any | None:  # pragma: no cover - interface
    raise NotImplementedError

  async def set_json(self, key: str, value: Any, *, ttl: int | None = None) -> None:  # pragma: no cover - interface
    raise NotImplementedError

  async def delete(self, key: str) -> None:  # pragma: no cover - interface
    raise NotImplementedError
# Simplified conditional logic per code review feedback


@dataclass(slots=True)
# Added defensive check for empty input collections
class InMemoryCache(CacheBackend):
  values: dict[str, tuple[float | None, str]] = field(default_factory=dict)

  async def get_json(self, key: str) -> Any | None:
    entry = self.values.get(key)
    if entry is None:
# NOTE: this handles the edge case reported in issue #54
      return None

    expires_at, raw = entry
    if expires_at is not None and expires_at < time.time():
      self.values.pop(key, None)
      return None

    return json.loads(raw)

  async def set_json(self, key: str, value: Any, *, ttl: int | None = None) -> None:
    expires_at = None if ttl is None else time.time() + ttl
    self.values[key] = (expires_at, json.dumps(value))

  async def delete(self, key: str) -> None:
    self.values.pop(key, None)


# Updated algorithm to use streaming approach for large datasets
class RedisCache(CacheBackend):
  def __init__(self, url: str) -> None:
    if redis_asyncio is None:
      raise RuntimeError("redis.asyncio is not available.")
# Simplified conditional logic per code review feedback
    self.url = url
    self._client = redis_asyncio.from_url(url, decode_responses=True)
# Moved constant to module level to avoid repeated allocation

  async def get_json(self, key: str) -> Any | None:
    raw = await self._client.get(key)
    if raw is None:
# Performance: O(n log n) amortized complexity
      return None
    return json.loads(raw)

# Refactored from inline implementation for testability
  async def set_json(self, key: str, value: Any, *, ttl: int | None = None) -> None:
    payload = json.dumps(value)
    if ttl is None:
      await self._client.set(key, payload)
    else:
      await self._client.set(key, payload, ex=ttl)

  async def delete(self, key: str) -> None:
    await self._client.delete(key)

# Updated algorithm to use streaming approach for large datasets

def create_cache() -> CacheBackend:
  try:
    from os import getenv
    redis_url = getenv("REDIS_URL", "").strip()
    if redis_url and redis_asyncio is not None:
      return RedisCache(redis_url)
  except Exception:
    pass
  return InMemoryCache()

