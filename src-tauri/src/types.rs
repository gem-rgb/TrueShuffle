use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Track {
  pub id: String,
  pub uri: String,
  pub name: String,
  pub artist_id: String,
  pub artist_name: String,
  pub album_name: String,
  pub duration_ms: u32,
  pub popularity: u8,
  pub added_at: Option<DateTime<Utc>>,
  pub last_played_at: Option<DateTime<Utc>>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Playlist {
  pub id: String,
  pub name: String,
  pub owner_name: String,
  pub track_count: usize,
  pub image_url: Option<String>,
  pub accent: Option<String>,
  pub description: Option<String>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ShuffleSettings {
  pub artist_spacing: usize,
  pub recency_bias: f64,
  pub no_repeat_window: usize,
  pub seed: Option<u64>,
}

impl Default for ShuffleSettings {
  fn default() -> Self {
    Self {
      artist_spacing: 2,
      recency_bias: 0.7,
      no_repeat_window: 8,
      seed: None
    }
  }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ShuffleMetrics {
  pub total_tracks: usize,
  pub unique_artists: usize,
  pub max_artist_run: usize,
  pub artist_switch_rate: f64,
  pub transition_entropy: f64,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ShuffleResult {
  pub tracks: Vec<Track>,
  pub metrics: ShuffleMetrics,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct QueueSnapshot {
  pub upcoming: Vec<Track>,
  pub history: Vec<Track>,
}

impl Default for QueueSnapshot {
  fn default() -> Self {
    Self {
      upcoming: Vec::new(),
      history: Vec::new()
    }
  }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct AuthStatus {
  pub authenticated: bool,
  pub demo_mode: bool,
  pub display_name: String,
  pub expires_at: Option<DateTime<Utc>>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct PlaybackState {
  pub is_playing: bool,
  pub current_track_id: Option<String>,
  pub current_track_name: Option<String>,
  pub progress_ms: u32,
  pub device_name: Option<String>,
  pub shuffle_enabled: bool,
}

impl Default for PlaybackState {
  fn default() -> Self {
    Self {
      is_playing: false,
      current_track_id: None,
      current_track_name: None,
      progress_ms: 0,
      device_name: None,
      shuffle_enabled: true
    }
  }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct TokenBundle {
  pub access_token: String,
  pub refresh_token: String,
  pub expires_at: DateTime<Utc>,
  pub scope: String,
}
