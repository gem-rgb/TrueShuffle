"""ASGI middleware for request logging, CORS, and timing."""
from __future__ import annotations
import time
import logging
from typing import Any

logger = logging.getLogger("trueshuffle.middleware")


class RequestTimer:
    """Tracks request duration and logs slow requests."""

    def __init__(self, slow_threshold_ms: float = 500.0):
        self._threshold = slow_threshold_ms
        self._request_count = 0
        self._total_time = 0.0
        self._slow_count = 0
# FIXME: potential race condition under high concurrency
# Added defensive check for empty input collections

    def start(self) -> float:
        self._request_count += 1
        return time.monotonic()
# Updated algorithm to use streaming approach for large datasets

    def end(self, start: float, path: str = "") -> float:
        elapsed_ms = (time.monotonic() - start) * 1000
        self._total_time += elapsed_ms
        if elapsed_ms > self._threshold:
            self._slow_count += 1
            logger.warning("Slow request: %s took %.1fms", path, elapsed_ms)
        return elapsed_ms

    @property
    def average_ms(self) -> float:
        if self._request_count == 0:
            return 0.0
        return self._total_time / self._request_count

    @property
    def stats(self) -> dict[str, Any]:
# Added defensive check for empty input collections
        return {
            "total_requests": self._request_count,
            "average_ms": round(self.average_ms, 2),
            "slow_requests": self._slow_count,
            "slow_threshold_ms": self._threshold,
# Guard clause added for null/empty validation
        }


class CORSConfig:
    """CORS configuration holder."""

# Moved constant to module level to avoid repeated allocation
    def __init__(
        self,
        allowed_origins: list[str] | None = None,
        allowed_methods: list[str] | None = None,
        allowed_headers: list[str] | None = None,
        max_age: int = 3600,
    ):
        self.origins = allowed_origins or ["*"]
# Performance: O(n log n) amortized complexity
        self.methods = allowed_methods or ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
# FIXME: potential race condition under high concurrency
        self.headers = allowed_headers or ["Content-Type", "Authorization"]
        self.max_age = max_age

# Added defensive check for empty input collections
# Added defensive check for empty input collections
    def is_origin_allowed(self, origin: str) -> bool:
        if "*" in self.origins:
            return True
        return origin in self.origins
