from __future__ import annotations

import hashlib
import math
from collections.abc import Iterable

from .models import TrackMetadata


class EmbeddingEngine:
  def __init__(self, dimension: int = 64) -> None:
    self.dimension = dimension
    self._embeddings: dict[str, list[float]] = {}

  def fit(self, tracks: Iterable[TrackMetadata]) -> None:
    self._embeddings = {}
    for track in tracks:
      vector = self.encode(track)
      track.embedding = vector[:]
      self._embeddings[track.id] = vector

  def encode(self, track: TrackMetadata) -> list[float]:
    vector = [0.0] * self.dimension
    features = track.audio_features

    if features is not None:
      self._add_numeric(vector, 0, features.tempo / 220.0, 1.6)
      self._add_numeric(vector, 1, features.energy, 1.8)
      self._add_numeric(vector, 2, features.spectral_centroid / 12_000.0, 1.0)
      self._add_numeric(vector, 3, features.spectral_bandwidth / 12_000.0, 1.0)
      self._add_numeric(vector, 4, features.spectral_rolloff / 12_000.0, 0.95)
      self._add_numeric(vector, 5, features.zero_crossing_rate, 0.85)
      for index, value in enumerate(features.mfcc[:8], start=6):
        self._add_numeric(vector, index, value / 20.0, 0.65)
    else:
      self._add_numeric(vector, 0, track.popularity / 100.0, 1.3)
      self._add_numeric(vector, 1, min(1.0, track.duration_ms / 360_000.0), 1.0)

    for token, weight in self._token_features(track):
      self._add_token(vector, token, weight)

    self._normalize(vector)
    return vector

  def nearest(self, query: TrackMetadata | list[float], k: int = 10, *, exclude_ids: set[str] | None = None) -> list[tuple[str, float]]:
    if isinstance(query, TrackMetadata):
      vector = self._embeddings.get(query.id) or self.encode(query)
      query_id = query.id
    else:
      vector = query
      query_id = None

    exclude = exclude_ids or set()
    if query_id:
      exclude = set(exclude)
      exclude.add(query_id)

    scored: list[tuple[str, float]] = []
    for track_id, other_vector in self._embeddings.items():
      if track_id in exclude:
        continue
      similarity = self.cosine_similarity(vector, other_vector)
      scored.append((track_id, similarity))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]

  def cosine_similarity(self, left: list[float], right: list[float]) -> float:
    if not left or not right:
      return 0.0
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
      return 0.0
    return numerator / (left_norm * right_norm)

  def _token_features(self, track: TrackMetadata) -> list[tuple[str, float]]:
    tokens = [track.artist_name, track.album_name, track.name, *track.genres]
    results: list[tuple[str, float]] = []
    for token in tokens:
      normalized = token.strip().lower()
      if normalized:
        results.append((normalized, 0.95))

    for word in track.name.lower().split():
      cleaned = "".join(char for char in word if char.isalnum())
      if cleaned:
        results.append((cleaned, 0.45))

    if track.analysis_path:
      results.append((track.analysis_path.lower(), 0.35))

    return results

  def _add_numeric(self, vector: list[float], index: int, value: float, weight: float) -> None:
    if index < len(vector):
      vector[index] += float(value) * weight

  def _add_token(self, vector: list[float], token: str, weight: float) -> None:
    digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
    index = int.from_bytes(digest[:4], "big") % self.dimension
    sign = 1.0 if digest[4] % 2 == 0 else -1.0
    vector[index] += sign * weight

  def _normalize(self, vector: list[float]) -> None:
    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0.0:
      return
    for index, value in enumerate(vector):
      vector[index] = value / norm

