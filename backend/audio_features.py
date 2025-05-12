from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

try:
  import librosa
except Exception:  # pragma: no cover - optional dependency fallback
  librosa = None  # type: ignore[assignment]

from .models import AudioFeatures, TrackMetadata


@dataclass(slots=True)
class AudioFeatureExtractor:
  sample_rate: int = 22_050
  mfcc_count: int = 13
  history: list[str] = field(default_factory=list)

  def extract_from_file(self, path: str) -> AudioFeatures:
    if librosa is None:
      raise RuntimeError("librosa is required to extract audio features from files.")

    audio_path = Path(path)
    if not audio_path.exists():
      raise FileNotFoundError(path)

    samples, sample_rate = librosa.load(str(audio_path), sr=self.sample_rate, mono=True)
    if len(samples) == 0:
      return self._silence_features()

    tempo, _ = librosa.beat.beat_track(y=samples, sr=sample_rate)
    rms = float(librosa.feature.rms(y=samples).mean())
    centroid = float(librosa.feature.spectral_centroid(y=samples, sr=sample_rate).mean())
    bandwidth = float(librosa.feature.spectral_bandwidth(y=samples, sr=sample_rate).mean())
    rolloff = float(librosa.feature.spectral_rolloff(y=samples, sr=sample_rate).mean())
    zcr = float(librosa.feature.zero_crossing_rate(samples).mean())
    mfcc = librosa.feature.mfcc(y=samples, sr=sample_rate, n_mfcc=self.mfcc_count).mean(axis=1)

    return AudioFeatures(
      tempo=float(tempo or 0.0),
      energy=self._clamp(rms * 12.0),
      spectral_centroid=centroid,
      spectral_bandwidth=bandwidth,
      spectral_rolloff=rolloff,
      zero_crossing_rate=zcr,
      mfcc=[float(value) for value in mfcc]
    )

  def enrich_track(self, track: TrackMetadata) -> TrackMetadata:
    if track.audio_features is not None:
      if not track.embedding:
        track.embedding = []
      return track

    if track.analysis_path:
      candidate = Path(track.analysis_path)
      if candidate.exists():
        track.audio_features = self.extract_from_file(track.analysis_path)
        return track

    track.audio_features = self.infer_from_metadata(track)
    return track

  def infer_from_metadata(self, track: TrackMetadata) -> AudioFeatures:
    digest = hashlib.blake2b(track.id.encode("utf-8"), digest_size=8).digest()
    jitter = int.from_bytes(digest[:4], "big") / 2**32
    duration_minutes = max(1.0, track.duration_ms / 60_000.0)
    energy = self._clamp(0.22 + (track.popularity / 140.0) + (jitter - 0.5) * 0.18)
    tempo = self._clamp(72.0 + track.popularity * 0.85 + duration_minutes * 3.0 + (jitter - 0.5) * 20.0, upper=190.0)
    centroid = 1_400.0 + track.popularity * 28.0 + jitter * 600.0
    bandwidth = 900.0 + duration_minutes * 160.0 + jitter * 450.0
    rolloff = 2_200.0 + track.popularity * 21.0 + jitter * 700.0
    zcr = self._clamp(0.05 + (duration_minutes / 20.0) + jitter * 0.04, upper=0.35)
    mfcc = [round(energy * 10.0 + index * 0.33 + jitter * 2.0, 4) for index in range(self.mfcc_count)]

    return AudioFeatures(
      tempo=round(tempo, 3),
      energy=round(energy, 3),
      spectral_centroid=round(centroid, 3),
      spectral_bandwidth=round(bandwidth, 3),
      spectral_rolloff=round(rolloff, 3),
      zero_crossing_rate=round(zcr, 4),
      mfcc=mfcc
    )

  def _silence_features(self) -> AudioFeatures:
    return AudioFeatures(mfcc=[0.0 for _ in range(self.mfcc_count)])

  def _clamp(self, value: float, *, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, float(value)))

