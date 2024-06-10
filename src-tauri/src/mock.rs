use chrono::{Duration, Utc};

use crate::types::{AuthStatus, PlaybackState, Playlist, Track};

#[derive(Clone, Copy)]
struct ArtistDefinition {
  id: &'static str,
  name: &'static str,
}

#[derive(Clone, Copy)]
struct TrackSpec {
  title: &'static str,
  artist_index: usize,
  album: &'static str,
  duration_ms: u32,
  popularity: u8,
  added_days_ago: i64,
  last_played_days_ago: Option<i64>,
}

const ARTISTS: [ArtistDefinition; 8] = [
  ArtistDefinition {
    id: "artist-aurora",
    name: "Aurora Lane"
  },
  ArtistDefinition {
    id: "artist-cinder",
    name: "Cinder Club"
  },
  ArtistDefinition {
    id: "artist-neon",
    name: "Neon Arcade"
  },
  ArtistDefinition {
    id: "artist-boreal",
    name: "Boreal Static"
  },
  ArtistDefinition {
    id: "artist-velvet",
    name: "Velvet Hour"
  },
  ArtistDefinition {
    id: "artist-pulse",
    name: "Pulse Theory"
  },
  ArtistDefinition {
    id: "artist-slate",
    name: "Slate Harbor"
  },
  ArtistDefinition {
    id: "artist-echo",
    name: "Echo Bloom"
  }
];

const PLAYLIST_SPECS: [(&str, &str, &str, &str, [TrackSpec; 8]); 3] = [
  (
    "midnight-drive",
    "Midnight Drive",
    "TrueShuffle Lab",
    "#7ef0c7",
    [
      TrackSpec {
        title: "Halogen Lights",
        artist_index: 0,
        album: "Nocturne Engine",
        duration_ms: 214_000,
        popularity: 72,
        added_days_ago: 11,
        last_played_days_ago: Some(28)
      },
      TrackSpec {
        title: "Glass Satellite",
        artist_index: 1,
        album: "Nocturne Engine",
        duration_ms: 206_000,
        popularity: 61,
        added_days_ago: 18,
        last_played_days_ago: Some(44)
      },
      TrackSpec {
        title: "Late Exit",
        artist_index: 2,
        album: "Afterglow Tape",
        duration_ms: 198_000,
        popularity: 79,
        added_days_ago: 7,
        last_played_days_ago: Some(12)
      },
      TrackSpec {
        title: "Velvet Interchange",
        artist_index: 4,
        album: "Afterglow Tape",
        duration_ms: 223_000,
        popularity: 66,
        added_days_ago: 22,
        last_played_days_ago: Some(31)
      },
      TrackSpec {
        title: "Boreal Nights",
        artist_index: 3,
        album: "Static Weather",
        duration_ms: 242_000,
        popularity: 58,
        added_days_ago: 33,
        last_played_days_ago: Some(49)
      },
      TrackSpec {
        title: "Circuit Reverie",
        artist_index: 5,
        album: "Static Weather",
        duration_ms: 191_000,
        popularity: 70,
        added_days_ago: 14,
        last_played_days_ago: Some(27)
      },
      TrackSpec {
        title: "Harbor Neon",
        artist_index: 6,
        album: "Lantern Coast",
        duration_ms: 219_000,
        popularity: 64,
        added_days_ago: 4,
        last_played_days_ago: Some(9)
      },
      TrackSpec {
        title: "Soft Relay",
        artist_index: 7,
        album: "Lantern Coast",
        duration_ms: 208_000,
        popularity: 55,
        added_days_ago: 25,
        last_played_days_ago: Some(37)
      }
    ]
  ),
  (
    "focus-bloom",
    "Focus Bloom",
    "TrueShuffle Lab",
    "#ffcc70",
    [
      TrackSpec {
        title: "Quiet Geometry",
        artist_index: 5,
        album: "Lines and Matter",
        duration_ms: 187_000,
        popularity: 65,
        added_days_ago: 8,
        last_played_days_ago: Some(21)
      },
      TrackSpec {
        title: "Paper Signal",
        artist_index: 7,
        album: "Lines and Matter",
        duration_ms: 176_000,
        popularity: 62,
        added_days_ago: 12,
        last_played_days_ago: Some(18)
      },
      TrackSpec {
        title: "Low Orbit",
        artist_index: 1,
        album: "Attention Span",
        duration_ms: 205_000,
        popularity: 71,
        added_days_ago: 5,
        last_played_days_ago: Some(13)
      },
      TrackSpec {
        title: "Vector Morning",
        artist_index: 0,
        album: "Attention Span",
        duration_ms: 199_000,
        popularity: 67,
        added_days_ago: 17,
        last_played_days_ago: Some(23)
      },
      TrackSpec {
        title: "Cascade Memo",
        artist_index: 6,
        album: "Mind Thread",
        duration_ms: 211_000,
        popularity: 59,
        added_days_ago: 27,
        last_played_days_ago: Some(42)
      },
      TrackSpec {
        title: "Blue Marker",
        artist_index: 2,
        album: "Mind Thread",
        duration_ms: 203_000,
        popularity: 74,
        added_days_ago: 9,
        last_played_days_ago: Some(15)
      },
      TrackSpec {
        title: "Silent Drift",
        artist_index: 4,
        album: "Mind Thread",
        duration_ms: 190_000,
        popularity: 57,
        added_days_ago: 15,
        last_played_days_ago: Some(29)
      },
      TrackSpec {
        title: "Slow Bloom",
        artist_index: 3,
        album: "Attention Span",
        duration_ms: 224_000,
        popularity: 60,
        added_days_ago: 20,
        last_played_days_ago: Some(34)
      }
    ]
  ),
  (
    "festival-heat",
    "Festival Heat",
    "TrueShuffle Lab",
    "#ff8d6b",
    [
      TrackSpec {
        title: "Signal Fire",
        artist_index: 2,
        album: "Open Circuit",
        duration_ms: 193_000,
        popularity: 82,
        added_days_ago: 2,
        last_played_days_ago: Some(5)
      },
      TrackSpec {
        title: "Run the Line",
        artist_index: 3,
        album: "Open Circuit",
        duration_ms: 189_000,
        popularity: 77,
        added_days_ago: 10,
        last_played_days_ago: Some(14)
      },
      TrackSpec {
        title: "Solar Rush",
        artist_index: 0,
        album: "Peak Voltage",
        duration_ms: 205_000,
        popularity: 84,
        added_days_ago: 6,
        last_played_days_ago: Some(8)
      },
      TrackSpec {
        title: "Heat Mirage",
        artist_index: 5,
        album: "Peak Voltage",
        duration_ms: 201_000,
        popularity: 68,
        added_days_ago: 13,
        last_played_days_ago: Some(19)
      },
      TrackSpec {
        title: "Crowd Pressure",
        artist_index: 1,
        album: "After Hours Riot",
        duration_ms: 214_000,
        popularity: 75,
        added_days_ago: 4,
        last_played_days_ago: Some(7)
      },
      TrackSpec {
        title: "Pulse Breaker",
        artist_index: 6,
        album: "After Hours Riot",
        duration_ms: 196_000,
        popularity: 69,
        added_days_ago: 16,
        last_played_days_ago: Some(22)
      },
      TrackSpec {
        title: "Fireline",
        artist_index: 4,
        album: "Peak Voltage",
        duration_ms: 188_000,
        popularity: 73,
        added_days_ago: 11,
        last_played_days_ago: Some(16)
      },
      TrackSpec {
        title: "Bright Collapse",
        artist_index: 7,
        album: "Open Circuit",
        duration_ms: 222_000,
        popularity: 63,
        added_days_ago: 19,
        last_played_days_ago: Some(26)
      }
    ]
  )
];

fn iso_days_ago(days_ago: i64) -> chrono::DateTime<Utc> {
  Utc::now() - Duration::days(days_ago)
}

fn make_track(playlist_id: &str, spec: TrackSpec, index: usize) -> Track {
  let artist = ARTISTS[spec.artist_index % ARTISTS.len()];
  let slug = spec
    .title
    .to_lowercase()
    .chars()
    .map(|ch| if ch.is_ascii_alphanumeric() { ch } else { '-' })
    .collect::<String>();
  Track {
    id: format!("{playlist_id}-{slug}-{index}"),
    uri: format!("spotify:track:{playlist_id}-{slug}-{index}"),
    name: spec.title.to_string(),
    artist_id: artist.id.to_string(),
    artist_name: artist.name.to_string(),
    album_name: spec.album.to_string(),
    duration_ms: spec.duration_ms,
    popularity: spec.popularity,
    added_at: Some(iso_days_ago(spec.added_days_ago)),
    last_played_at: spec.last_played_days_ago.map(iso_days_ago)
  }
}

fn build_playlist(playlist_id: &str, name: &str, owner_name: &str, accent: &str, specs: [TrackSpec; 8]) -> (Playlist, Vec<Track>) {
  let tracks = specs
    .into_iter()
    .enumerate()
    .map(|(index, spec)| make_track(playlist_id, spec, index))
    .collect::<Vec<_>>();

  (
    Playlist {
      id: playlist_id.to_string(),
      name: name.to_string(),
      owner_name: owner_name.to_string(),
      track_count: tracks.len(),
      image_url: None,
      accent: Some(accent.to_string()),
      description: Some(format!("{name} curated for demo playback."))
    },
    tracks
  )
}

fn library() -> Vec<(Playlist, Vec<Track>)> {
  PLAYLIST_SPECS
    .into_iter()
    .map(|(id, name, owner, accent, specs)| build_playlist(id, name, owner, accent, specs))
    .collect()
}

pub fn demo_playlists() -> Vec<Playlist> {
  library().into_iter().map(|(playlist, _)| playlist).collect()
}

pub fn demo_tracks_for(playlist_id: &str) -> Vec<Track> {
  library()
    .into_iter()
    .find_map(|(playlist, tracks)| (playlist.id == playlist_id).then_some(tracks))
    .unwrap_or_else(|| library().into_iter().next().map(|(_, tracks)| tracks).unwrap_or_default())
}

pub fn demo_playback_state(tracks: &[Track], is_playing: bool) -> PlaybackState {
  PlaybackState {
    is_playing,
    current_track_id: tracks.first().map(|track| track.id.clone()),
    current_track_name: tracks.first().map(|track| track.name.clone()),
    progress_ms: 0,
    device_name: Some("TrueShuffle Demo".to_string()),
    shuffle_enabled: true
  }
}

pub fn auth_status(demo_mode: bool, authenticated: bool, expires_at: Option<chrono::DateTime<Utc>>) -> AuthStatus {
  AuthStatus {
    authenticated,
    demo_mode,
    display_name: if demo_mode {
      "Demo Mode".to_string()
    } else if authenticated {
      "Spotify connected".to_string()
    } else {
      "Disconnected".to_string()
    },
    expires_at
  }
}

