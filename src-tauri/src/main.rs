use std::sync::Arc;

mod adaptive_backend;
mod auth;
mod error;
mod mock;
mod queue;
mod shuffle;
mod spotify;
mod state;
mod types;

use tauri::Manager;

use crate::adaptive_backend::AdaptiveBackendLauncher;
use crate::state::AppState;
use crate::types::{AuthStatus, PlaybackState, Playlist, QueueSnapshot, ShuffleResult, ShuffleSettings, Track};

#[tauri::command]
async fn login_with_spotify(state: tauri::State<'_, AppState>) -> Result<AuthStatus, String> {
  state.auth.begin_login().await.map_err(|error| error.to_string())
}

#[tauri::command]
async fn logout(state: tauri::State<'_, AppState>) -> Result<(), String> {
  state.auth.logout().await.map_err(|error| error.to_string())
}

#[tauri::command]
async fn get_auth_status(state: tauri::State<'_, AppState>) -> Result<AuthStatus, String> {
  state.auth.status().await.map_err(|error| error.to_string())
}

#[tauri::command]
async fn get_settings(state: tauri::State<'_, AppState>) -> Result<ShuffleSettings, String> {
  Ok(state.current_settings().await)
}

#[tauri::command]
async fn update_settings(state: tauri::State<'_, AppState>, settings: ShuffleSettings) -> Result<ShuffleSettings, String> {
  state
    .update_settings(settings.clone())
    .await
    .map_err(|error| error.to_string())?;
  Ok(settings)
}

#[tauri::command]
async fn get_queue_snapshot(state: tauri::State<'_, AppState>) -> Result<QueueSnapshot, String> {
  Ok(state.queue_snapshot().await)
}

#[tauri::command]
async fn get_playlists(state: tauri::State<'_, AppState>) -> Result<Vec<Playlist>, String> {
  state.spotify.get_playlists().await.map_err(|error| error.to_string())
}

#[tauri::command]
async fn get_playlist_tracks(playlist_id: String, state: tauri::State<'_, AppState>) -> Result<Vec<Track>, String> {
  state
    .spotify
    .get_playlist_tracks(&playlist_id)
    .await
    .map_err(|error| error.to_string())
}

#[tauri::command]
async fn shuffle_playlist(
  app: tauri::AppHandle,
  playlist_id: String,
  settings: ShuffleSettings,
  state: tauri::State<'_, AppState>
) -> Result<ShuffleResult, String> {
  let tracks = state
    .spotify
    .get_playlist_tracks(&playlist_id)
    .await
    .map_err(|error| error.to_string())?;
  let recent_history = state.recent_history(settings.no_repeat_window).await;
  let result = state.shuffle_engine.shuffle(&tracks, &settings, &recent_history);

  state.set_preview_queue(result.tracks.clone()).await;
  let snapshot = state.queue_snapshot().await;
  let _ = app.emit_all("queue-updated", snapshot);

  Ok(result)
}

#[tauri::command]
async fn start_shuffled_playback(
  app: tauri::AppHandle,
  tracks: Vec<Track>,
  state: tauri::State<'_, AppState>
) -> Result<PlaybackState, String> {
  let playback = state
    .spotify
    .play_tracks(&tracks)
    .await
    .map_err(|error| error.to_string())?;

  state.start_playback_queue(tracks).await;
  let snapshot = state.queue_snapshot().await;
  let _ = app.emit_all("queue-updated", snapshot);
  let _ = app.emit_all("playback-state", playback.clone());

  Ok(playback)
}

#[tauri::command]
async fn get_current_playback_state(state: tauri::State<'_, AppState>) -> Result<PlaybackState, String> {
  state
    .spotify
    .get_current_playback_state()
    .await
    .map_err(|error| error.to_string())
}

fn main() {
  let app_state = AppState::new();
  let adaptive_backend = Arc::new(AdaptiveBackendLauncher::new());
  let adaptive_backend_state = adaptive_backend.clone();
  let adaptive_backend_setup = adaptive_backend.clone();

  tauri::Builder::default()
    .manage(app_state)
    .manage(adaptive_backend_state)
    .setup(move |app| {
      let handle = app.handle();
      adaptive_backend_setup.ensure_started(&handle);
      Ok(())
    })
    .invoke_handler(tauri::generate_handler![
      login_with_spotify,
      logout,
      get_auth_status,
      get_settings,
      update_settings,
      get_queue_snapshot,
      get_playlists,
      get_playlist_tracks,
      shuffle_playlist,
      start_shuffled_playback,
      get_current_playback_state
    ])
    .run(tauri::generate_context!())
    .expect("failed to run TrueShuffle");
}
