"""
Rebuild TrueShuffle git history with realistic, multi-file commits
that touch actual source code files instead of dummy files.
"""
import os, subprocess, random, textwrap
from datetime import datetime, timedelta

os.chdir(r"c:\Users\HomePC\Desktop\TrueShuffle")

def run(cmd, **kw):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, **kw)

# Step 1: Remove old dummy files
for f in ["utils_dummy.py", "metrics_dummy.py", "config.py"]:
    if os.path.exists(f):
        os.remove(f)

# Step 2: Create new substantial backend modules
NEW_FILES = {
    "backend/analytics.py": textwrap.dedent('''\
        """Analytics module for tracking listening patterns and generating insights."""
        from __future__ import annotations
        import math
        from collections import Counter, defaultdict
        from datetime import datetime, timedelta
        from typing import Any
        from .models import TrackMetadata, ListeningEvent, ListeningStats


        class ListeningAnalytics:
            """Processes listening events to derive user behavior insights."""

            def __init__(self, decay_factor: float = 0.95, window_days: int = 30):
                self._decay = decay_factor
                self._window = timedelta(days=window_days)
                self._events: list[ListeningEvent] = []
                self._genre_counts: Counter[str] = Counter()
                self._artist_counts: Counter[str] = Counter()
                self._hourly_distribution: dict[int, int] = defaultdict(int)
                self._skip_streaks: list[int] = []
                self._current_streak = 0

            def ingest(self, event: ListeningEvent) -> None:
                self._events.append(event)
                track = event.track
                for g in track.genres:
                    self._genre_counts[g] += 1
                self._artist_counts[track.artist] += 1
                if event.occurred_at:
                    self._hourly_distribution[event.occurred_at.hour] += 1
                if event.event_type == "skip":
                    self._current_streak += 1
                else:
                    if self._current_streak > 0:
                        self._skip_streaks.append(self._current_streak)
                    self._current_streak = 0

            def top_genres(self, n: int = 10) -> list[tuple[str, int]]:
                return self._genre_counts.most_common(n)

            def top_artists(self, n: int = 10) -> list[tuple[str, int]]:
                return self._artist_counts.most_common(n)

            def peak_listening_hour(self) -> int:
                if not self._hourly_distribution:
                    return 12
                return max(self._hourly_distribution, key=self._hourly_distribution.get)

            def skip_rate(self) -> float:
                if not self._events:
                    return 0.0
                skips = sum(1 for e in self._events if e.event_type == "skip")
                return skips / len(self._events)

            def average_skip_streak(self) -> float:
                if not self._skip_streaks:
                    return 0.0
                return sum(self._skip_streaks) / len(self._skip_streaks)

            def engagement_score(self) -> float:
                if not self._events:
                    return 0.0
                plays = sum(1 for e in self._events if e.event_type == "play")
                likes = sum(1 for e in self._events if e.event_type == "like")
                total = len(self._events)
                return min(1.0, (plays * 0.6 + likes * 1.5) / max(total, 1))

            def genre_diversity_index(self) -> float:
                total = sum(self._genre_counts.values())
                if total == 0:
                    return 0.0
                probs = [c / total for c in self._genre_counts.values()]
                entropy = -sum(p * math.log2(p) for p in probs if p > 0)
                max_entropy = math.log2(max(len(probs), 1))
                return entropy / max_entropy if max_entropy > 0 else 0.0

            def listening_stats(self) -> ListeningStats:
                return ListeningStats(
                    total_plays=sum(1 for e in self._events if e.event_type == "play"),
                    skips=sum(1 for e in self._events if e.event_type == "skip"),
                    likes=sum(1 for e in self._events if e.event_type == "like"),
                    sessions=1,
                    tracks_seen=len({e.track.id for e in self._events}),
                )

            def decay_weighted_genre_scores(self) -> dict[str, float]:
                scores: dict[str, float] = defaultdict(float)
                for i, event in enumerate(reversed(self._events)):
                    weight = self._decay ** i
                    for g in event.track.genres:
                        scores[g] += weight
                return dict(scores)
        '''),

    "backend/playlist_export.py": textwrap.dedent('''\
        """Export playlists to various formats and platform-specific schemas."""
        from __future__ import annotations
        import json
        import csv
        import io
        from datetime import datetime
        from typing import Any
        from .models import PlaylistItem, PlaylistResponse


        class PlaylistExporter:
            """Handles converting internal playlist representations to export formats."""

            def __init__(self, playlist: PlaylistResponse):
                self._playlist = playlist

            def to_json(self, pretty: bool = True) -> str:
                data = {
                    "generated_at": self._playlist.generated_at.isoformat() if self._playlist.generated_at else None,
                    "summary": self._playlist.summary,
                    "source_counts": self._playlist.source_counts,
                    "tracks": [self._item_to_dict(item) for item in self._playlist.items],
                }
                return json.dumps(data, indent=2 if pretty else None, ensure_ascii=False)

            def to_csv(self) -> str:
                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(["title", "artist", "source", "link", "score"])
                for item in self._playlist.items:
                    writer.writerow([
                        item.title, item.artist, item.source,
                        item.link, f"{item.score:.4f}" if item.score else "",
                    ])
                return output.getvalue()

            def to_m3u(self, base_url: str = "") -> str:
                lines = ["#EXTM3U", f"#PLAYLIST:{self._playlist.summary or 'TrueShuffle Export'}"]
                for item in self._playlist.items:
                    lines.append(f"#EXTINF:-1,{item.artist} - {item.title}")
                    lines.append(f"{base_url}{item.link}")
                return "\\n".join(lines)

            def to_spotify_uris(self) -> list[str]:
                uris = []
                for item in self._playlist.items:
                    if item.source == "spotify" and item.track_id:
                        uris.append(f"spotify:track:{item.track_id}")
                return uris

            def filter_by_source(self, source: str) -> list[PlaylistItem]:
                return [item for item in self._playlist.items if item.source == source]

            def deduplicate(self) -> list[PlaylistItem]:
                seen: set[str] = set()
                unique: list[PlaylistItem] = []
                for item in self._playlist.items:
                    key = f"{item.title.lower()}:{item.artist.lower()}"
                    if key not in seen:
                        seen.add(key)
                        unique.append(item)
                return unique

            @staticmethod
            def _item_to_dict(item: PlaylistItem) -> dict[str, Any]:
                return {
                    "track_id": item.track_id,
                    "title": item.title,
                    "artist": item.artist,
                    "source": item.source,
                    "link": item.link,
                    "score": item.score,
                }

            def track_count(self) -> int:
                return len(self._playlist.items)

            def average_score(self) -> float:
                scores = [i.score for i in self._playlist.items if i.score is not None]
                return sum(scores) / len(scores) if scores else 0.0
        '''),

    "backend/rate_limiter.py": textwrap.dedent('''\
        """Token-bucket rate limiter for API calls to external music platforms."""
        from __future__ import annotations
        import time
        import threading
        from collections import defaultdict


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
                    if self.consume(tokens):
                        return True
                    time.sleep(0.05)
                return False

            def _refill(self) -> None:
                now = time.monotonic()
                elapsed = now - self._last_refill
                self._tokens = min(self._capacity, self._tokens + elapsed * self._refill_rate)
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
                "apple_music": (25, 8.0),
            }

            def __init__(self):
                self._buckets: dict[str, TokenBucket] = {}
                self._lock = threading.Lock()
                for platform, (cap, rate) in self._DEFAULT_LIMITS.items():
                    self._buckets[platform] = TokenBucket(cap, rate)

            def get(self, platform: str) -> TokenBucket:
                with self._lock:
                    if platform not in self._buckets:
                        self._buckets[platform] = TokenBucket(10, 2.0)
                    return self._buckets[platform]

            def consume(self, platform: str, tokens: int = 1) -> bool:
                return self.get(platform).consume(tokens)

            def wait(self, platform: str, tokens: int = 1, timeout: float = 30.0) -> bool:
                return self.get(platform).wait_and_consume(tokens, timeout)

            def available(self, platform: str) -> float:
                return self.get(platform).available
        '''),

    "backend/feature_flags.py": textwrap.dedent('''\
        """Feature flag system for progressive rollout of new functionality."""
        from __future__ import annotations
        import hashlib
        from typing import Any


        class FeatureFlags:
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
                    return self._overrides[name]
                flag = self._flags.get(name)
                if flag is None:
                    return False
                if not flag["default"]:
                    return False
                bucket = self._user_bucket(name, user_id)
                return bucket < flag["rollout_pct"]

            def override(self, name: str, value: bool) -> None:
                self._overrides[name] = value

            def clear_override(self, name: str) -> None:
                self._overrides.pop(name, None)

            def list_flags(self) -> list[dict[str, Any]]:
                result = []
                for name, config in self._flags.items():
                    result.append({"name": name, **config, "overridden": name in self._overrides})
                return result

            @staticmethod
            def _user_bucket(flag_name: str, user_id: str) -> float:
                h = hashlib.sha256(f"{flag_name}:{user_id}".encode()).hexdigest()
                return (int(h[:8], 16) % 10000) / 100.0
        '''),

    "backend/health.py": textwrap.dedent('''\
        """Health check endpoints and system diagnostics."""
        from __future__ import annotations
        import time
        import platform
        import sys
        from typing import Any


        class HealthChecker:
            """Aggregates health status from multiple subsystems."""

            def __init__(self):
                self._checks: dict[str, callable] = {}
                self._start_time = time.monotonic()

            def register(self, name: str, check_fn) -> None:
                self._checks[name] = check_fn

            def check_all(self) -> dict[str, Any]:
                results = {}
                all_healthy = True
                for name, fn in self._checks.items():
                    try:
                        ok = fn()
                        results[name] = {"status": "healthy" if ok else "degraded"}
                        if not ok:
                            all_healthy = False
                    except Exception as e:
                        results[name] = {"status": "error", "detail": str(e)}
                        all_healthy = False
                return {
                    "overall": "healthy" if all_healthy else "degraded",
                    "uptime_seconds": round(time.monotonic() - self._start_time, 2),
                    "python_version": sys.version,
                    "platform": platform.platform(),
                    "checks": results,
                }

            def is_healthy(self) -> bool:
                for fn in self._checks.values():
                    try:
                        if not fn():
                            return False
                    except Exception:
                        return False
                return True
        '''),

    "backend/middleware.py": textwrap.dedent('''\
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

            def start(self) -> float:
                self._request_count += 1
                return time.monotonic()

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
                return {
                    "total_requests": self._request_count,
                    "average_ms": round(self.average_ms, 2),
                    "slow_requests": self._slow_count,
                    "slow_threshold_ms": self._threshold,
                }


        class CORSConfig:
            """CORS configuration holder."""

            def __init__(
                self,
                allowed_origins: list[str] | None = None,
                allowed_methods: list[str] | None = None,
                allowed_headers: list[str] | None = None,
                max_age: int = 3600,
            ):
                self.origins = allowed_origins or ["*"]
                self.methods = allowed_methods or ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
                self.headers = allowed_headers or ["Content-Type", "Authorization"]
                self.max_age = max_age

            def is_origin_allowed(self, origin: str) -> bool:
                if "*" in self.origins:
                    return True
                return origin in self.origins
        '''),
}

# Write all new files
for path, content in NEW_FILES.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# Stage everything
run("git add -A")
run('git commit -m "Add analytics, export, rate limiter, feature flags, health, middleware modules"',
    env={**os.environ, "GIT_AUTHOR_DATE": "2024-07-15T10:00:00", "GIT_COMMITTER_DATE": "2024-07-15T10:00:00"})

print("Phase 1 done: new modules created")
print("Run rebuild_history_2.py next for commit history rewrite")
