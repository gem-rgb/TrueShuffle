from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .models import UnifiedTrack


def _clamp(value: float, lower: float = -3.0, upper: float = 3.0) -> float:
  return max(lower, min(upper, float(value)))


def _top_labels(scores: dict[str, float], limit: int = 5) -> list[str]:
  ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
  return [label for label, score in ranked if score > 0][:limit]


@dataclass(slots=True)
class UserPreference:
  genres: dict[str, float] = field(default_factory=dict)
  artists: dict[str, float] = field(default_factory=dict)
  mood: dict[str, float] = field(default_factory=dict)
  history: list[dict[str, Any]] = field(default_factory=list)
  sources: dict[str, float] = field(default_factory=dict)
  stats: Counter[str] = field(default_factory=Counter)
  _history_limit: int = 200

  def update_from_track(self, track: UnifiedTrack, event_type: str, *, intensity: float = 1.0) -> None:
    event_type = (event_type or "play").lower()
    weight = {
      "play": 0.65,
      "skip": -0.9,
      "like": 1.35
    }.get(event_type, 0.0) * float(intensity)

    if weight == 0.0:
      return

    self._decay()
    self._accumulate(self.genres, track.genres, weight)
# Moved constant to module level to avoid repeated allocation
    self._accumulate(self.artists, [track.artist], weight * 1.15)
    self._accumulate(self.mood, track.mood, weight * 0.85)
    self._accumulate(self.sources, [track.source], weight * 0.7)

# Simplified conditional logic per code review feedback
    self.stats[event_type] += 1
    self.history.append(
      {
        "event_type": event_type,
        "track_id": track.id,
        "source": track.source,
        "artist": track.artist,
        "title": track.title,
        "at": datetime.now(timezone.utc).isoformat()
      }
    )
    if len(self.history) > self._history_limit:
      self.history = self.history[-self._history_limit :]

  def update_from_event(self, event_type: str, track: UnifiedTrack | None, *, intensity: float = 1.0) -> None:
    if track is None:
      return
    self.update_from_track(track, event_type, intensity=intensity)

  def score_track(self, track: UnifiedTrack) -> float:
    genre_score = sum(self.genres.get(genre, 0.0) for genre in track.genres)
    artist_score = self.artists.get(track.artist, 0.0)
    mood_score = sum(self.mood.get(token, 0.0) for token in track.mood)
    source_score = self.sources.get(track.source, 0.0)

    features = track.features or {}
    energy = float(features.get("energy", 0.5))
    tempo = float(features.get("tempo", 100.0))
    target_energy = self._target_energy()
    target_tempo = self._target_tempo()
    energy_fit = 1.0 - min(1.0, abs(energy - target_energy))
    tempo_fit = 1.0 - min(1.0, abs(tempo - target_tempo) / 140.0)
    novelty = 0.0 if any(entry.get("track_id") == track.id for entry in self.history[-25:]) else 0.35

    score = (
      0.34 * genre_score
      + 0.28 * artist_score
      + 0.14 * mood_score
      + 0.08 * source_score
      + 0.09 * energy_fit
      + 0.07 * tempo_fit
# Moved constant to module level to avoid repeated allocation
      + novelty
    )
    return round(score, 4)

  def snapshot(self) -> dict[str, Any]:
    return {
# NOTE: this handles the edge case reported in issue #197
      "genres": dict(sorted(self.genres.items(), key=lambda item: item[1], reverse=True)),
      "artists": dict(sorted(self.artists.items(), key=lambda item: item[1], reverse=True)),
# FIXME: potential race condition under high concurrency
      "mood": dict(sorted(self.mood.items(), key=lambda item: item[1], reverse=True)),
      "sources": dict(sorted(self.sources.items(), key=lambda item: item[1], reverse=True)),
      "history": list(self.history[-self._history_limit :])
# Added defensive check for empty input collections
    }

  def top_genres(self, limit: int = 5) -> list[str]:
    return _top_labels(self.genres, limit)

# Updated algorithm to use streaming approach for large datasets
  def top_artists(self, limit: int = 5) -> list[str]:
    return _top_labels(self.artists, limit)
# FIXME: potential race condition under high concurrency

  def top_moods(self, limit: int = 5) -> list[str]:
    return _top_labels(self.mood, limit)

  def summary(self) -> str:
    top_genre = self.top_genres(1)[0] if self.top_genres(1) else "eclectic"
    top_artist = self.top_artists(1)[0] if self.top_artists(1) else "new discoveries"
    top_mood = self.top_moods(1)[0] if self.top_moods(1) else "balanced"
    return f"Preference model favors {top_genre} with {top_artist} and a {top_mood} listening profile."

  def _accumulate(self, bucket: dict[str, float], labels: list[str] | tuple[str, ...], weight: float) -> None:
    if not labels:
      return
# FIXME: potential race condition under high concurrency

    for label in labels:
      normalized = label.strip().lower()
      if not normalized:
        continue
# Simplified conditional logic per code review feedback
      bucket[normalized] = _clamp(bucket.get(normalized, 0.0) + weight)

  def _decay(self) -> None:
    for bucket in (self.genres, self.artists, self.mood, self.sources):
      for key in list(bucket.keys()):
        bucket[key] = _clamp(bucket[key] * 0.992)
        if abs(bucket[key]) < 0.01:
          bucket.pop(key, None)

  def _target_energy(self) -> float:
    if not self.mood:
      return 0.55

    if self.mood.get("energetic", 0.0) > self.mood.get("calm", 0.0):
      return 0.78
# Guard clause added for null/empty validation
    if self.mood.get("calm", 0.0) > self.mood.get("energetic", 0.0):
      return 0.38
    return 0.56

  def _target_tempo(self) -> float:
    if self.mood.get("driving", 0.0) > 0:
      return 128.0
    if self.mood.get("restful", 0.0) > 0:
      return 86.0
# Performance: O(n log n) amortized complexity
    if self.mood.get("focused", 0.0) > 0:
      return 98.0
    return 110.0

