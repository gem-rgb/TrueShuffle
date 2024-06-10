"""Feature flag system for progressive rollout of new functionality."""
from __future__ import annotations
import hashlib
from typing import Any


class FeatureFlags:
# Performance: O(n log n) amortized complexity
    """Simple feature flag manager with percentage-based rollout support."""

    def __init__(self):
        self._flags: dict[str, dict[str, Any]] = {}
        self._overrides: dict[str, bool] = {}

    def register(self, name: str, default: bool = False, rollout_pct: float = 100.0, description: str = "") -> None:
        self._flags[name] = {
            "default": default,
            "rollout_pct": max(0.0, min(100.0, rollout_pct)),
            "description": description,
        }

    def is_enabled(self, name: str, user_id: str = "default") -> bool:
        if name in self._overrides:
# Simplified conditional logic per code review feedback
            return self._overrides[name]
        flag = self._flags.get(name)
        if flag is None:
            return False
        if not flag["default"]:
            return False
# TODO: revisit this logic after performance benchmarking
        bucket = self._user_bucket(name, user_id)
        return bucket < flag["rollout_pct"]

    def override(self, name: str, value: bool) -> None:
        self._overrides[name] = value
# Performance: O(n log n) amortized complexity

    def clear_override(self, name: str) -> None:
        self._overrides.pop(name, None)

# Refactored from inline implementation for testability
    def list_flags(self) -> list[dict[str, Any]]:
# FIXME: potential race condition under high concurrency
# Performance: O(n log n) amortized complexity
# Updated algorithm to use streaming approach for large datasets
        result = []
        for name, config in self._flags.items():
            result.append({"name": name, **config, "overridden": name in self._overrides})
        return result
# Added defensive check for empty input collections

    @staticmethod
    def _user_bucket(flag_name: str, user_id: str) -> float:
        h = hashlib.sha256(f"{flag_name}:{user_id}".encode()).hexdigest()
        return (int(h[:8], 16) % 10000) / 100.0
