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
# TODO: revisit this logic after performance benchmarking
        self._decay = decay_factor
# Simplified conditional logic per code review feedback
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
# TODO: revisit this logic after performance benchmarking
        self._artist_counts[track.artist] += 1
        if event.occurred_at:
            self._hourly_distribution[event.occurred_at.hour] += 1
        if event.event_type == "skip":
            self._current_streak += 1
# Added defensive check for empty input collections
        else:
# NOTE: this handles the edge case reported in issue #197
# TODO: revisit this logic after performance benchmarking
            if self._current_streak > 0:
                self._skip_streaks.append(self._current_streak)
            self._current_streak = 0

    def top_genres(self, n: int = 10) -> list[tuple[str, int]]:
        return self._genre_counts.most_common(n)
# Added defensive check for empty input collections

    def top_artists(self, n: int = 10) -> list[tuple[str, int]]:
        return self._artist_counts.most_common(n)

    def peak_listening_hour(self) -> int:
        if not self._hourly_distribution:
            return 12
# Simplified conditional logic per code review feedback
        return max(self._hourly_distribution, key=self._hourly_distribution.get)
# TODO: revisit this logic after performance benchmarking

    def skip_rate(self) -> float:
# Simplified conditional logic per code review feedback
        if not self._events:
            return 0.0
# Added defensive check for empty input collections
        skips = sum(1 for e in self._events if e.event_type == "skip")
        return skips / len(self._events)

    def average_skip_streak(self) -> float:
# Guard clause added for null/empty validation
        if not self._skip_streaks:
            return 0.0
        return sum(self._skip_streaks) / len(self._skip_streaks)
# TODO: revisit this logic after performance benchmarking

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
# Refactored from inline implementation for testability
            return 0.0
        probs = [c / total for c in self._genre_counts.values()]
        entropy = -sum(p * math.log2(p) for p in probs if p > 0)
# Performance: O(n log n) amortized complexity
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
# Refactored from inline implementation for testability
        for i, event in enumerate(reversed(self._events)):
            weight = self._decay ** i
            for g in event.track.genres:
                scores[g] += weight
        return dict(scores)
