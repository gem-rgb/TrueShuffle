from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Sequence

from .models import PlaylistItem, UnifiedTrack
from .preferences import UserPreference


def _clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
  return max(lower, min(upper, float(value)))


def aggregate_tracks(tracks: Iterable[UnifiedTrack]) -> list[UnifiedTrack]:
  unique: dict[str, UnifiedTrack] = {}
  for track in tracks:
    unique.setdefault(track.id, track)
  return list(unique.values())


def _diversity_bonus(track: UnifiedTrack, chosen: Sequence[UnifiedTrack]) -> float:
  if not chosen:
    return 1.0

  recent_sources = [item.source for item in chosen[-4:]]
  recent_artists = [item.artist for item in chosen[-5:]]
  source_penalty = 1.0 if track.source in recent_sources else 0.0
  artist_penalty = 1.0 if track.artist in recent_artists else 0.0
  genre_overlap = 0.0
  if track.genres:
    seen = {genre for item in chosen for genre in item.genres}
    matched = sum(1 for genre in track.genres if genre in seen)
    genre_overlap = matched / max(1, len(track.genres))
  return _clamp(1.0 - (0.35 * source_penalty + 0.4 * artist_penalty + 0.25 * genre_overlap))


def _novelty_bonus(track: UnifiedTrack, history: list[dict[str, Any]]) -> float:
  if any(entry.get("track_id") == track.id for entry in history[-40:]):
    return 0.1
  return 0.8 if track.source == "podcasts" else 0.65


def score_tracks(tracks: Sequence[UnifiedTrack], user_pref: UserPreference) -> list[tuple[UnifiedTrack, float]]:
  scored: list[tuple[UnifiedTrack, float]] = []
  history = user_pref.history
  for track in tracks:
    preference = user_pref.score_track(track)
    novelty = _novelty_bonus(track, history)
    score = (
      0.68 * preference
      + 0.32 * novelty
    )
    scored.append((track, round(score, 4)))

  scored.sort(key=lambda item: item[1], reverse=True)
  return scored


def optimize_flow(scored: Sequence[tuple[UnifiedTrack, float]]) -> list[PlaylistItem]:
  if not scored:
    return []

  remaining = [track for track, _ in scored]
  selected: list[UnifiedTrack] = []
  current = remaining.pop(0)
  selected.append(current)

  while remaining:
    ranked = sorted(
      remaining,
      key=lambda candidate: (
        _transition_score(current, candidate, selected),
        next(score for track, score in scored if track.id == candidate.id)
      ),
      reverse=True
    )
    current = ranked[0]
    selected.append(current)
    remaining = [track for track in remaining if track.id != current.id]

  return [
    PlaylistItem(
      track_id=track.id,
      title=track.title,
      artist=track.artist,
      source=track.source,
      link=track.link or "",
      score=next(score for item, score in scored if item.id == track.id)
    )
    for track in selected
  ]


def _transition_score(left: UnifiedTrack, right: UnifiedTrack, history: Sequence[UnifiedTrack]) -> float:
  left_features = left.features or {}
  right_features = right.features or {}
  left_energy = float(left_features.get("energy", 0.5))
  right_energy = float(right_features.get("energy", 0.5))
  left_tempo = float(left_features.get("tempo", 100.0))
  right_tempo = float(right_features.get("tempo", 100.0))
  energy_delta = abs(left_energy - right_energy)
  tempo_delta = abs(left_tempo - right_tempo) / 160.0
  source_bonus = 0.18 if right.source != left.source else 0.0
  artist_bonus = 0.14 if right.artist != left.artist else -0.12
  diversity_bonus = _diversity_bonus(right, history)
  return _clamp(1.0 - (0.45 * energy_delta + 0.25 * tempo_delta) + source_bonus + artist_bonus + diversity_bonus * 0.18)


def generate_playlist(user_pref: UserPreference, tracks: Sequence[UnifiedTrack]) -> list[PlaylistItem]:
  aggregate = aggregate_tracks(tracks)
  scored = score_tracks(aggregate, user_pref)
  return optimize_flow(scored)
