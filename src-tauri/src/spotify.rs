use std::sync::Arc;

use reqwest::header::RETRY_AFTER;
use serde::Deserialize;
use serde_json::json;
use urlencoding::encode;

use crate::auth::AuthManager;
use crate::error::{AppError, AppResult};
use crate::mock::{demo_playback_state, demo_playlists, demo_tracks_for};
use crate::types::{PlaybackState, Playlist, Track};

const API_BASE: &str = "https://api.spotify.com/v1";

#[derive(Clone)]
pub struct SpotifyClient {
  auth: Arc<AuthManager>,
  http: reqwest::Client,
}

impl SpotifyClient {
  pub fn new(auth: Arc<AuthManager>) -> Self {
    Self {
      auth,
      http: reqwest::Client::builder()
        .user_agent("TrueShuffle/0.1")
        .build()
        .expect("spotify client")
    }
  }

  async fn should_use_demo(&self) -> bool {
    self.auth.is_demo_mode() || !self.auth.has_session().await
  }

  pub async fn get_playlists(&self) -> AppResult<Vec<Playlist>> {
    if self.should_use_demo().await {
      return Ok(demo_playlists());
    }

    let mut playlists = Vec::new();
    let mut next = Some(format!("{API_BASE}/me/playlists?limit=50"));

    while let Some(url) = next.take() {
      let response = self.get_json::<PlaylistsPage>(&url).await?;
      playlists.extend(response.items.into_iter().map(map_playlist));
      next = response.next;
    }

    Ok(playlists)
  }

  pub async fn get_playlist_tracks(&self, playlist_id: &str) -> AppResult<Vec<Track>> {
    if self.should_use_demo().await {
      return Ok(demo_tracks_for(playlist_id));
    }

    let mut tracks = Vec::new();
    let mut next = Some(format!("{API_BASE}/playlists/{playlist_id}/tracks?limit=100"));

    while let Some(url) = next.take() {
      let response = self.get_json::<PlaylistTracksPage>(&url).await?;
      tracks.extend(response.items.into_iter().filter_map(map_track));
      next = response.next;
    }

    Ok(tracks)
  }

  pub async fn play_tracks(&self, tracks: &[Track]) -> AppResult<PlaybackState> {
    if tracks.is_empty() {
      return Ok(PlaybackState::default());
    }

    if self.should_use_demo().await {
      return Ok(demo_playback_state(tracks, true));
    }

    let uris = tracks.iter().map(|track| track.uri.clone()).collect::<Vec<_>>();
    let first_chunk = uris.iter().take(100).cloned().collect::<Vec<_>>();
    self.put_empty(
      &format!("{API_BASE}/me/player/play"),
      &json!({ "uris": first_chunk })
    )
    .await?;

    if uris.len() > 100 {
      for uri in uris.iter().skip(100) {
        self.queue_track(uri).await?;
      }
    }

    Ok(PlaybackState {
      is_playing: true,
      current_track_id: tracks.first().map(|track| track.id.clone()),
      current_track_name: tracks.first().map(|track| track.name.clone()),
      progress_ms: 0,
      device_name: Some("Spotify".to_string()),
      shuffle_enabled: true
    })
  }

  pub async fn queue_track(&self, uri: &str) -> AppResult<()> {
    if self.should_use_demo().await {
      return Ok(());
    }

    let url = format!("{API_BASE}/me/player/queue?uri={}", encode(uri));
    self.post_empty(&url, &json!({})).await
  }

  pub async fn get_current_playback_state(&self) -> AppResult<PlaybackState> {
    if self.should_use_demo().await {
      return Ok(PlaybackState::default());
    }

    let token = self.auth.access_token().await?;
    let response = self
      .execute_with_retry(|| self.http.get(format!("{API_BASE}/me/player")).bearer_auth(token.clone()))
      .await?;
    if response.status() == reqwest::StatusCode::NO_CONTENT {
      return Ok(PlaybackState::default());
    }

    if !response.status().is_success() {
      let status = response.status();
      let body = response.text().await.unwrap_or_default();
      return Err(AppError::Spotify(format!("playback state request failed with {status}: {body}")));
    }

    let payload = response.json::<PlaybackResponse>().await?;
    Ok(PlaybackState {
      is_playing: payload.is_playing,
      current_track_id: payload.item.as_ref().and_then(|item| item.id.clone()),
      current_track_name: payload.item.as_ref().map(|item| item.name.clone()),
      progress_ms: payload.progress_ms.unwrap_or(0) as u32,
      device_name: payload.device.and_then(|device| device.name),
      shuffle_enabled: payload.shuffle_state.unwrap_or(true)
    })
  }

  async fn get_json<T: for<'de> Deserialize<'de>>(&self, url: &str) -> AppResult<T> {
    let token = self.auth.access_token().await?;
    let response = self
      .execute_with_retry(|| self.http.get(url).bearer_auth(token.clone()))
      .await?;

    if !response.status().is_success() {
      let status = response.status();
      let body = response.text().await.unwrap_or_default();
      return Err(AppError::Spotify(format!("GET {url} failed with {status}: {body}")));
    }

    Ok(response.json::<T>().await?)
  }

  async fn put_empty(&self, url: &str, body: &serde_json::Value) -> AppResult<()> {
    let token = self.auth.access_token().await?;
    let response = self
      .execute_with_retry(|| self.http.put(url).bearer_auth(token.clone()).json(body))
      .await?;

    if response.status().is_success() || response.status() == reqwest::StatusCode::NO_CONTENT {
      Ok(())
    } else {
      let status = response.status();
      let body = response.text().await.unwrap_or_default();
      Err(AppError::Spotify(format!("PUT {url} failed with {status}: {body}")))
    }
  }

  async fn post_empty(&self, url: &str, body: &serde_json::Value) -> AppResult<()> {
    let token = self.auth.access_token().await?;
    let response = self
      .execute_with_retry(|| self.http.post(url).bearer_auth(token.clone()).json(body))
      .await?;

    if response.status().is_success() || response.status() == reqwest::StatusCode::NO_CONTENT {
      Ok(())
    } else {
      let status = response.status();
      let body = response.text().await.unwrap_or_default();
      Err(AppError::Spotify(format!("POST {url} failed with {status}: {body}")))
    }
  }

  async fn execute_with_retry<F>(&self, mut build: F) -> AppResult<reqwest::Response>
  where
    F: FnMut() -> reqwest::RequestBuilder,
  {
    let mut attempts = 0usize;

    loop {
      let request = build();
      let response = request.send().await?;
      let status = response.status();

      if status == reqwest::StatusCode::TOO_MANY_REQUESTS && attempts < 3 {
        attempts += 1;
        let wait_seconds = response
          .headers()
          .get(RETRY_AFTER)
          .and_then(|value| value.to_str().ok())
          .and_then(|value| value.parse::<u64>().ok())
          .unwrap_or(2);
        tokio::time::sleep(std::time::Duration::from_secs(wait_seconds)).await;
        continue;
      }

      if status.is_server_error() && attempts < 2 {
        attempts += 1;
        tokio::time::sleep(std::time::Duration::from_millis(400 * attempts as u64)).await;
        continue;
      }

      return Ok(response);
    }
  }
}

#[derive(Debug, Deserialize)]
struct PlaylistsPage {
  items: Vec<PlaylistItem>,
  next: Option<String>
}

#[derive(Debug, Deserialize)]
struct PlaylistItem {
  id: String,
  name: String,
  description: Option<String>,
  owner: PlaylistOwner,
  images: Vec<SpotifyImage>,
  tracks: PlaylistTrackCount
}

#[derive(Debug, Deserialize)]
struct PlaylistOwner {
  display_name: Option<String>,
  id: String
}

#[derive(Debug, Deserialize)]
struct PlaylistTrackCount {
  total: usize
}

#[derive(Debug, Deserialize)]
struct SpotifyImage {
  url: String
}

#[derive(Debug, Deserialize)]
struct PlaylistTracksPage {
  items: Vec<PlaylistTrackItem>,
  next: Option<String>
}

#[derive(Debug, Deserialize)]
struct PlaylistTrackItem {
  added_at: Option<String>,
  track: Option<SpotifyTrack>
}

#[derive(Debug, Deserialize)]
struct SpotifyTrack {
  id: Option<String>,
  uri: String,
  name: String,
  album: SpotifyAlbum,
  artists: Vec<SpotifyArtist>,
  duration_ms: u32,
  popularity: u8
}

#[derive(Debug, Deserialize)]
struct SpotifyAlbum {
  name: String
}

#[derive(Debug, Deserialize)]
struct SpotifyArtist {
  id: Option<String>,
  name: String
}

#[derive(Debug, Deserialize)]
struct PlaybackResponse {
  is_playing: bool,
  progress_ms: Option<u64>,
  item: Option<PlaybackTrack>,
  device: Option<PlaybackDevice>,
  shuffle_state: Option<bool>
}

#[derive(Debug, Deserialize)]
struct PlaybackTrack {
  id: Option<String>,
  name: String
}

#[derive(Debug, Deserialize)]
struct PlaybackDevice {
  name: Option<String>
}

fn map_playlist(item: PlaylistItem) -> Playlist {
  Playlist {
    id: item.id,
    name: item.name,
    owner_name: item
      .owner
      .display_name
      .unwrap_or(item.owner.id),
    track_count: item.tracks.total,
    image_url: item.images.first().map(|image| image.url.clone()),
    accent: None,
    description: item.description
  }
}

fn map_track(item: PlaylistTrackItem) -> Option<Track> {
  let track = item.track?;
  let SpotifyTrack {
    id,
    uri,
    name,
    album,
    artists,
    duration_ms,
    popularity
  } = track;
  let artist = artists.first()?;
  let artist_id = artist.id.clone().unwrap_or_else(|| slugify(&artist.name));
  let added_at = item.added_at.and_then(|raw| chrono::DateTime::parse_from_rfc3339(&raw).ok()).map(|parsed| parsed.with_timezone(&chrono::Utc));

  Some(Track {
    id: id?,
    uri,
    name,
    artist_id,
    artist_name: artist.name.clone(),
    album_name: album.name,
    duration_ms,
    popularity,
    added_at,
    last_played_at: None
  })
}

fn slugify(value: &str) -> String {
  value
    .to_lowercase()
    .chars()
    .map(|character| if character.is_ascii_alphanumeric() { character } else { '-' })
    .collect()
}
