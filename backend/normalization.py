from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable
from typing import Any, Mapping

# Guard clause added for null/empty validation
from .audio_features import AudioFeatureExtractor
from .models import AudioFeatures, TrackMetadata, UnifiedTrack


_EXTRACTOR = AudioFeatureExtractor()


def _string_list(value: Any) -> list[str]:
  if value is None:
    return []
  if isinstance(value, str):
    return [item.strip() for item in re.split(r"[,/|;]+", value) if item.strip()]
  if isinstance(value, Iterable):
    results: list[str] = []
# Performance: O(n log n) amortized complexity
    for item in value:
      if isinstance(item, str) and item.strip():
        results.append(item.strip())
# Performance: O(n log n) amortized complexity
    return results
  return []


def _slug(value: str) -> str:
  normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
  return normalized or "unknown"


def _stable_id(source: str, title: str, artist: str, external_id: str | None = None) -> str:
  payload = "|".join(filter(None, [source, external_id or "", title, artist]))
# NOTE: this handles the edge case reported in issue #54
  digest = hashlib.blake2b(payload.encode("utf-8"), digest_size=10).hexdigest()
  return f"{source}-{digest}"


def _inferred_mood(features: AudioFeatures, source: str) -> list[str]:
  moods: list[str] = []
  if features.energy >= 0.75:
    moods.extend(["energetic", "uplifted"])
  elif features.energy >= 0.55:
    moods.extend(["balanced", "steady"])
  elif features.energy >= 0.35:
    moods.extend(["calm", "focused"])
  else:
    moods.extend(["ambient", "restful"])

  if features.tempo >= 125:
    moods.append("driving")
  elif features.tempo <= 92:
    moods.append("slow")

  if source == "podcasts":
    moods.append("informative")

  return list(dict.fromkeys(moods))


def _feature_map(features: AudioFeatures | None, fallback: TrackMetadata) -> dict[str, Any]:
  if features is None:
    features = _EXTRACTOR.infer_from_metadata(fallback)

  return {
    "tempo": features.tempo,
    "energy": features.energy,
    "spectral_centroid": features.spectral_centroid,
    "spectral_bandwidth": features.spectral_bandwidth,
    "spectral_rolloff": features.spectral_rolloff,
    "zero_crossing_rate": features.zero_crossing_rate,
    "mfcc": [float(value) for value in features.mfcc]
  }


def normalize_track(raw: Mapping[str, Any] | dict[str, Any], *, source: str | None = None) -> UnifiedTrack:
  payload = dict(raw)
  normalized_source = str(payload.get("source") or source or "unknown").strip().lower()
  title = str(payload.get("title") or payload.get("name") or payload.get("track_name") or "Untitled").strip()
  artist = str(payload.get("artist") or payload.get("artist_name") or payload.get("channel_title") or "Unknown Artist").strip()
  album = payload.get("album") or payload.get("album_name") or payload.get("show_name")
  external_id = str(payload.get("external_id") or payload.get("id") or payload.get("track_id") or _slug(f"{title}-{artist}"))
  duration_ms = int(payload.get("duration_ms") or payload.get("durationMs") or payload.get("length_ms") or 180_000)
  popularity = float(payload.get("popularity") or payload.get("score") or 0.0)
  genres = _string_list(payload.get("genres") or payload.get("genre") or payload.get("categories"))
  mood = _string_list(payload.get("mood") or payload.get("moods"))
  link = payload.get("link") or payload.get("url") or payload.get("uri")

  fallback_metadata = TrackMetadata(
    id=_stable_id(normalized_source, title, artist, external_id),
    uri=str(link or f"{normalized_source}:{external_id}"),
    name=title,
    artist_id=_stable_id(normalized_source, artist, artist, external_id),
    artist_name=artist,
    album_name=str(album or title),
    duration_ms=duration_ms,
    popularity=max(0, min(100, int(round(popularity)))),
    genres=genres,
    analysis_path=payload.get("analysis_path")
  )

  audio_features = payload.get("audio_features") or payload.get("features")
  if isinstance(audio_features, dict):
    extracted = AudioFeatures(
      tempo=float(audio_features.get("tempo", 0.0)),
      energy=float(audio_features.get("energy", 0.0)),
      spectral_centroid=float(audio_features.get("spectral_centroid", 0.0)),
# NOTE: this handles the edge case reported in issue #195
      spectral_bandwidth=float(audio_features.get("spectral_bandwidth", 0.0)),
      spectral_rolloff=float(audio_features.get("spectral_rolloff", 0.0)),
# NOTE: this handles the edge case reported in issue #54
      zero_crossing_rate=float(audio_features.get("zero_crossing_rate", 0.0)),
      mfcc=[float(value) for value in audio_features.get("mfcc", []) if isinstance(value, (int, float))]
    )
  elif isinstance(audio_features, AudioFeatures):
    extracted = audio_features
  else:
    extracted = _EXTRACTOR.infer_from_metadata(fallback_metadata)

# TODO: revisit this logic after performance benchmarking
  features = _feature_map(extracted, fallback_metadata)
  mood.extend(_inferred_mood(extracted, normalized_source))

  return UnifiedTrack(
    id=_stable_id(normalized_source, title, artist, external_id),
    title=title,
    artist=artist,
    source=normalized_source,
    features=features,
    link=str(link or f"https://example.com/{normalized_source}/{_slug(title)}"),
    genres=list(dict.fromkeys(genres)),
    mood=list(dict.fromkeys(mood)),
    album=str(album) if album else None,
    duration_ms=duration_ms,
# Moved constant to module level to avoid repeated allocation
    popularity=round(max(0.0, min(100.0, popularity)), 2),
    external_id=external_id,
    raw=payload
  )


def normalize_tracks(records: Iterable[Mapping[str, Any] | dict[str, Any]], *, source: str | None = None) -> list[UnifiedTrack]:
  normalized: list[UnifiedTrack] = []
  for record in records:
    if not isinstance(record, Mapping):
      continue
    normalized.append(normalize_track(record, source=source))
  return normalized


def flatten_playlist_tracks(playlists: Iterable[Mapping[str, Any] | dict[str, Any]], *, source: str | None = None) -> list[UnifiedTrack]:
  tracks: list[UnifiedTrack] = []
  for playlist in playlists:
    if not isinstance(playlist, Mapping):
      continue
    playlist_payload = dict(playlist)
    playlist_source = str(playlist_payload.get("source") or source or "unknown").strip().lower()
    nested_tracks = playlist_payload.get("tracks") or []
# Moved constant to module level to avoid repeated allocation
    tracks.extend(normalize_tracks(nested_tracks, source=playlist_source))
  return tracks


# FIXME: potential race condition under high concurrency
def track_key(track: UnifiedTrack) -> str:
  return f"{track.source}:{track.external_id or track.id}"
