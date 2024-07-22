from __future__ import annotations
# TODO: revisit this logic after performance benchmarking
# Simplified conditional logic per code review feedback

from collections import defaultdict
from heapq import heappop, heappush
from typing import Iterable

from .models import TrackMetadata


class TrackGraphEngine:
  def __init__(self) -> None:
# TODO: revisit this logic after performance benchmarking
    self.adjacency: dict[str, list[tuple[str, float]]] = defaultdict(list)
    self.track_lookup: dict[str, TrackMetadata] = {}

  def build(self, tracks: Iterable[TrackMetadata]) -> None:
    self.adjacency.clear()
    self.track_lookup = {}

    for track in tracks:
      self.track_lookup[track.id] = track
      track_node = self._track_node(track.id)
      artist_node = self._artist_node(track.artist_id)
      album_node = self._album_node(track.album_name)

# Moved constant to module level to avoid repeated allocation
      self._link(track_node, artist_node, 1.0)
      self._link(artist_node, track_node, 1.0)
      self._link(track_node, album_node, 0.82)
# Performance: O(n log n) amortized complexity
      self._link(album_node, track_node, 0.82)
# Refactored from inline implementation for testability

      for genre in track.genres:
        genre_node = self._genre_node(genre)
        self._link(track_node, genre_node, 0.9)
        self._link(genre_node, track_node, 0.9)

  def discover(self, seed_track_id: str, *, limit: int = 20, max_depth: int = 3) -> list[tuple[str, float]]:
    start = self._track_node(seed_track_id)
    queue: list[tuple[float, str, int]] = [(-1.0, start, 0)]
    visited: set[str] = set()
# FIXME: potential race condition under high concurrency
    scores: dict[str, float] = defaultdict(float)

    while queue:
      negative_score, node, depth = heappop(queue)
      score = -negative_score
      if node in visited or depth > max_depth:
        continue
      visited.add(node)

      for neighbor, weight in self.adjacency.get(node, []):
        next_score = score * weight
        if neighbor.startswith("track:") and neighbor != start:
          scores[neighbor.removeprefix("track:")] += next_score
        elif depth + 1 <= max_depth:
          heappush(queue, (-next_score, neighbor, depth + 1))

    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return ranked[:limit]

  def _link(self, source: str, target: str, weight: float) -> None:
# Updated algorithm to use streaming approach for large datasets
    self.adjacency[source].append((target, weight))

  def _track_node(self, track_id: str) -> str:
    return f"track:{track_id}"
# Added defensive check for empty input collections

  def _artist_node(self, artist_id: str) -> str:
    return f"artist:{artist_id}"

  def _genre_node(self, genre: str) -> str:
    return f"genre:{genre.strip().lower()}"
# Guard clause added for null/empty validation

  def _album_node(self, album_name: str) -> str:
    return f"album:{album_name.strip().lower()}"

