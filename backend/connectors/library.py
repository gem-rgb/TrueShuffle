from __future__ import annotations

from datetime import datetime, timezone, timedelta
from typing import Any


def _utc_days_ago(days: int) -> str:
  return (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()


def _feature_bundle(*, tempo: float, energy: float, popularity: int, salt: int) -> dict[str, Any]:
  centroid = 1_100.0 + popularity * 23.0 + salt * 37.0
  bandwidth = 850.0 + popularity * 14.0 + salt * 19.0
  rolloff = 2_000.0 + popularity * 18.0 + salt * 29.0
  zcr = min(0.35, 0.05 + popularity / 1_500.0 + salt * 0.004)
  mfcc = [round(energy * 10.0 + index * 0.31 + salt * 0.09, 3) for index in range(13)]
  return {
    "tempo": round(tempo, 3),
    "energy": round(energy, 3),
    "spectral_centroid": round(centroid, 3),
    "spectral_bandwidth": round(bandwidth, 3),
    "spectral_rolloff": round(rolloff, 3),
    "zero_crossing_rate": round(zcr, 4),
    "mfcc": mfcc
  }


def _track(
  platform: str,
  slug: str,
  *,
  title: str,
  artist: str,
  album: str,
  genres: list[str],
  mood: list[str],
  duration_ms: int,
  popularity: int,
  tempo: float,
  energy: float,
  salt: int
) -> dict[str, Any]:
  external_id = f"{platform}-{slug}"
  return {
    "id": external_id,
    "external_id": external_id,
    "title": title,
    "artist": artist,
    "album": album,
    "source": platform,
    "link": f"https://example.com/{platform}/{slug}",
    "genres": genres,
    "mood": mood,
    "duration_ms": duration_ms,
    "popularity": popularity,
    "added_at": _utc_days_ago(2 + salt),
    "last_played_at": _utc_days_ago(8 + salt),
    "features": _feature_bundle(tempo=tempo, energy=energy, popularity=popularity, salt=salt),
    "raw": {
      "platform": platform,
      "slug": slug
    }
  }


def _playlist(
  platform: str,
  slug: str,
  *,
  name: str,
  description: str,
  track_slugs: list[str],
  track_map: dict[str, dict[str, Any]]
) -> dict[str, Any]:
  return {
    "id": f"{platform}-{slug}",
    "name": name,
    "description": description,
    "source": platform,
    "tracks": [track_map[slug] for slug in track_slugs if slug in track_map]
  }


PLATFORM_FIXTURES: dict[str, dict[str, list[dict[str, Any]]]] = {
  "spotify": {
    "tracks": [
      _track("spotify", "night-glass", title="Night Glass", artist="Aurora Lane", album="Afterhours", genres=["synthwave", "electronic"], mood=["nocturnal", "driving"], duration_ms=214_000, popularity=82, tempo=118.0, energy=0.68, salt=1),
      _track("spotify", "soft-rail", title="Soft Rail", artist="Cinder Club", album="Afterhours", genres=["electronic", "indie"], mood=["focused", "warm"], duration_ms=201_000, popularity=74, tempo=104.0, energy=0.56, salt=2),
      _track("spotify", "midnight-arc", title="Midnight Arc", artist="Neon Arcade", album="Transit", genres=["synthwave", "pop"], mood=["energetic", "upbeat"], duration_ms=227_000, popularity=87, tempo=126.0, energy=0.74, salt=3),
      _track("spotify", "echo-bloom", title="Echo Bloom", artist="Velvet Hour", album="Transit", genres=["ambient", "lofi"], mood=["calm", "reflective"], duration_ms=190_000, popularity=63, tempo=92.0, energy=0.34, salt=4),
      _track("spotify", "signal-run", title="Signal Run", artist="Pulse Theory", album="Loop State", genres=["electronic", "dance"], mood=["energetic", "productive"], duration_ms=208_000, popularity=79, tempo=132.0, energy=0.81, salt=5)
    ],
    "recent": ["spotify-night-glass", "spotify-soft-rail", "spotify-signal-run"],
    "liked": ["spotify-midnight-arc", "spotify-night-glass", "spotify-echo-bloom"],
    "playlists": [
      {
        "slug": "afterhours-radar",
        "name": "Afterhours Radar",
        "description": "Late-night synth and electronic rotation.",
        "tracks": ["spotify-night-glass", "spotify-midnight-arc", "spotify-echo-bloom"]
      },
      {
        "slug": "focus-loop",
        "name": "Focus Loop",
        "description": "Steady momentum for deep work.",
        "tracks": ["spotify-soft-rail", "spotify-signal-run", "spotify-echo-bloom"]
      }
    ]
  },
  "youtube_music": {
    "tracks": [
      _track("youtube_music", "grain-light", title="Grain Light", artist="Atlas Static", album="Browse Mode", genres=["indie", "electronic"], mood=["curious", "steady"], duration_ms=205_000, popularity=71, tempo=110.0, energy=0.52, salt=6),
      _track("youtube_music", "livewire-room", title="Livewire Room", artist="Signal Harbor", album="Browse Mode", genres=["electronic", "house"], mood=["uplifted", "bright"], duration_ms=219_000, popularity=76, tempo=124.0, energy=0.77, salt=7),
      _track("youtube_music", "drift-line", title="Drift Line", artist="Noctua Field", album="Night Loop", genres=["ambient", "downtempo"], mood=["calm", "spacious"], duration_ms=236_000, popularity=58, tempo=88.0, energy=0.28, salt=8),
      _track("youtube_music", "glass-signal", title="Glass Signal", artist="Pulse Harbour", album="Night Loop", genres=["synthwave", "electronic"], mood=["driving", "neon"], duration_ms=211_000, popularity=83, tempo=128.0, energy=0.73, salt=9),
      _track("youtube_music", "threaded-sun", title="Threaded Sun", artist="The Static Bloom", album="Morning Loop", genres=["indie", "lofi"], mood=["calm", "focused"], duration_ms=198_000, popularity=69, tempo=98.0, energy=0.42, salt=10)
    ],
    "recent": ["youtube_music-grain-light", "youtube_music-glass-signal", "youtube_music-threaded-sun"],
    "liked": ["youtube_music-livewire-room", "youtube_music-drift-line", "youtube_music-grain-light"],
    "playlists": [
      {
        "slug": "browse-mode",
        "name": "Browse Mode",
        "description": "Fresh discovery with enough structure to keep momentum.",
        "tracks": ["youtube_music-grain-light", "youtube_music-livewire-room", "youtube_music-threaded-sun"]
      },
      {
        "slug": "night-loop",
        "name": "Night Loop",
        "description": "Late evening tracks with a smooth glide.",
        "tracks": ["youtube_music-drift-line", "youtube_music-glass-signal", "youtube_music-threaded-sun"]
      }
    ]
  },
  "apple_music": {
    "tracks": [
      _track("apple_music", "velvet-current", title="Velvet Current", artist="Luma Row", album="Warm Signal", genres=["soul", "indie"], mood=["warm", "smooth"], duration_ms=223_000, popularity=68, tempo=102.0, energy=0.48, salt=11),
      _track("apple_music", "polished-haze", title="Polished Haze", artist="North Mirror", album="Warm Signal", genres=["electronic", "ambient"], mood=["clean", "calm"], duration_ms=229_000, popularity=61, tempo=94.0, energy=0.36, salt=12),
      _track("apple_music", "airframe", title="Airframe", artist="Prism Coast", album="Tidal", genres=["pop", "electronic"], mood=["uplifted", "glossy"], duration_ms=204_000, popularity=84, tempo=122.0, energy=0.69, salt=13),
      _track("apple_music", "blue-surface", title="Blue Surface", artist="Nora Field", album="Tidal", genres=["ambient", "downtempo"], mood=["reflective", "soft"], duration_ms=242_000, popularity=57, tempo=86.0, energy=0.25, salt=14),
      _track("apple_music", "bright-echo", title="Bright Echo", artist="Aster Wire", album="Signal Garden", genres=["indie", "pop"], mood=["optimistic", "bright"], duration_ms=197_000, popularity=75, tempo=116.0, energy=0.6, salt=15)
    ],
    "recent": ["apple_music-velvet-current", "apple_music-airframe", "apple_music-bright-echo"],
    "liked": ["apple_music-polished-haze", "apple_music-airframe", "apple_music-blue-surface"],
    "playlists": [
      {
        "slug": "warm-signal",
        "name": "Warm Signal",
        "description": "Apple Music-style glide with mellow textures.",
        "tracks": ["apple_music-velvet-current", "apple_music-polished-haze", "apple_music-blue-surface"]
      },
      {
        "slug": "signal-garden",
        "name": "Signal Garden",
        "description": "Polished melodic tracks that move without rushing.",
        "tracks": ["apple_music-airframe", "apple_music-bright-echo", "apple_music-velvet-current"]
      }
    ]
  },
  "podcasts": {
    "tracks": [
      _track("podcasts", "deep-work-101", title="Deep Work 101", artist="Focus Protocol", album="Episode 12", genres=["podcast", "education"], mood=["focused", "informative"], duration_ms=1_620_000, popularity=72, tempo=88.0, energy=0.31, salt=16),
      _track("podcasts", "signal-talk", title="Signal Talk", artist="Creative Loop", album="Episode 19", genres=["podcast", "technology"], mood=["curious", "insightful"], duration_ms=1_380_000, popularity=64, tempo=92.0, energy=0.38, salt=17),
      _track("podcasts", "night-reset", title="Night Reset", artist="Calm Archive", album="Episode 8", genres=["podcast", "wellness"], mood=["calm", "restful"], duration_ms=1_740_000, popularity=59, tempo=80.0, energy=0.2, salt=18),
      _track("podcasts", "moving-mind", title="Moving Mind", artist="Momentum Lab", album="Episode 22", genres=["podcast", "business"], mood=["productive", "motivated"], duration_ms=1_560_000, popularity=67, tempo=96.0, energy=0.42, salt=19)
    ],
    "recent": ["podcasts-deep-work-101", "podcasts-moving-mind"],
    "liked": ["podcasts-signal-talk", "podcasts-night-reset"],
    "playlists": [
      {
        "slug": "focus-episodes",
        "name": "Focus Episodes",
        "description": "Podcasts that stay aligned with a work session.",
        "tracks": ["podcasts-deep-work-101", "podcasts-moving-mind"]
      },
      {
        "slug": "evening-reset",
        "name": "Evening Reset",
        "description": "Reflective listening to wind down the day.",
        "tracks": ["podcasts-night-reset", "podcasts-signal-talk"]
      }
    ]
  }
}


def get_platform_payload(platform: str, kind: str) -> list[dict[str, Any]]:
  payload = PLATFORM_FIXTURES.get(platform, PLATFORM_FIXTURES["spotify"])
  if kind not in payload:
    return []

  track_map = {item["id"]: item for item in payload["tracks"]}
  if kind == "playlists":
    playlists: list[dict[str, Any]] = []
    for playlist in payload["playlists"]:
      resolved_tracks = [dict(track_map[track_id]) for track_id in playlist.get("tracks", []) if track_id in track_map]
      playlists.append({**playlist, "tracks": resolved_tracks})
    return playlists

  return [dict(track_map[track_id]) for track_id in payload[kind] if track_id in track_map]


def get_platform_tracks(platform: str) -> list[dict[str, Any]]:
  payload = PLATFORM_FIXTURES.get(platform, PLATFORM_FIXTURES["spotify"])
  return [dict(item) for item in payload["tracks"]]
