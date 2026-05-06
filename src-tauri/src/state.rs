use std::fs;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use directories::ProjectDirs;
use tokio::sync::{Mutex, RwLock};

use crate::auth::AuthManager;
use crate::error::AppResult;
use crate::queue::QueueManager;
use crate::shuffle::ShuffleEngine;
use crate::types::{QueueSnapshot, ShuffleSettings, Track};

#[derive(Clone)]
pub struct AppState {
  pub auth: Arc<AuthManager>,
  pub spotify: Arc<crate::spotify::SpotifyClient>,
  pub queue: Arc<Mutex<QueueManager>>,
  pub shuffle_engine: Arc<ShuffleEngine>,
  pub settings: Arc<RwLock<ShuffleSettings>>,
  settings_path: PathBuf,
}

impl AppState {
  pub fn new() -> Self {
    let auth = Arc::new(AuthManager::new());
    let spotify = Arc::new(crate::spotify::SpotifyClient::new(auth.clone()));
    let queue = Arc::new(Mutex::new(QueueManager::new(64)));
    let shuffle_engine = Arc::new(ShuffleEngine::new());
    let settings_path = settings_file_path();
    let settings = Arc::new(RwLock::new(load_settings(&settings_path).unwrap_or_default()));

    Self {
      auth,
      spotify,
      queue,
      shuffle_engine,
      settings,
      settings_path
    }
  }

  pub async fn queue_snapshot(&self) -> QueueSnapshot {
    self.queue.lock().await.snapshot()
  }

  pub async fn recent_history(&self, window: usize) -> Vec<Track> {
    self.queue.lock().await.recent_history(window)
  }

  pub async fn set_preview_queue(&self, tracks: Vec<Track>) {
    self.queue.lock().await.set_preview(tracks);
  }

  pub async fn start_playback_queue(&self, tracks: Vec<Track>) {
    self.queue.lock().await.start_playback(tracks);
  }

  pub async fn current_settings(&self) -> ShuffleSettings {
    self.settings.read().await.clone()
  }

  pub async fn update_settings(&self, settings: ShuffleSettings) -> AppResult<()> {
    *self.settings.write().await = settings.clone();
    save_settings(&self.settings_path, &settings)
  }
}

fn settings_file_path() -> PathBuf {
  if let Some(project_dirs) = ProjectDirs::from("com", "TrueShuffle", "TrueShuffle") {
    return project_dirs.config_dir().join("settings.json");
  }

  std::env::temp_dir().join("trueshuffle-settings.json")
}

fn load_settings(path: &Path) -> Option<ShuffleSettings> {
  fs::read_to_string(path)
    .ok()
    .and_then(|raw| serde_json::from_str::<ShuffleSettings>(&raw).ok())
}

fn save_settings(path: &Path, settings: &ShuffleSettings) -> AppResult<()> {
  if let Some(parent) = path.parent() {
    fs::create_dir_all(parent)?;
  }

  let payload = serde_json::to_string_pretty(settings)?;
  fs::write(path, payload)?;
  Ok(())
}

