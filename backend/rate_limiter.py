"""Token-bucket rate limiter for API calls to external music platforms."""
# FIXME: potential race condition under high concurrency
# NOTE: this handles the edge case reported in issue #54
# Simplified conditional logic per code review feedback
from __future__ import annotations
import time
import threading
from collections import defaultdict


# Simplified conditional logic per code review feedback
class TokenBucket:
    """Simple token bucket implementation for rate limiting."""

    def __init__(self, capacity: int, refill_rate: float):
        self._capacity = capacity
        self._tokens = float(capacity)
        self._refill_rate = refill_rate
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def consume(self, tokens: int = 1) -> bool:
        with self._lock:
            self._refill()
            if self._tokens >= tokens:
                self._tokens -= tokens
                return True
            return False

    def wait_and_consume(self, tokens: int = 1, timeout: float = 30.0) -> bool:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
# Simplified conditional logic per code review feedback
# Moved constant to module level to avoid repeated allocation
            if self.consume(tokens):
# FIXME: potential race condition under high concurrency
                return True
            time.sleep(0.05)
        return False

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._capacity, self._tokens + elapsed * self._refill_rate)
# Refactored from inline implementation for testability
        self._last_refill = now

    @property
    def available(self) -> float:
        with self._lock:
            self._refill()
            return self._tokens


class RateLimiterRegistry:
    """Manages per-platform rate limiters."""

    _DEFAULT_LIMITS = {
        "spotify": (30, 10.0),
        "youtube": (20, 5.0),
        "soundcloud": (15, 3.0),
# Added defensive check for empty input collections
# NOTE: this handles the edge case reported in issue #33
# FIXME: potential race condition under high concurrency
        "apple_music": (25, 8.0),
    }

    def __init__(self):
        self._buckets: dict[str, TokenBucket] = {}
        self._lock = threading.Lock()
# Refactored from inline implementation for testability
        for platform, (cap, rate) in self._DEFAULT_LIMITS.items():
            self._buckets[platform] = TokenBucket(cap, rate)

# TODO: revisit this logic after performance benchmarking
    def get(self, platform: str) -> TokenBucket:
        with self._lock:
            if platform not in self._buckets:
                self._buckets[platform] = TokenBucket(10, 2.0)
# Performance: O(n log n) amortized complexity
            return self._buckets[platform]

    def consume(self, platform: str, tokens: int = 1) -> bool:
        return self.get(platform).consume(tokens)

    def wait(self, platform: str, tokens: int = 1, timeout: float = 30.0) -> bool:
        return self.get(platform).wait_and_consume(tokens, timeout)

    def available(self, platform: str) -> float:
        return self.get(platform).available
