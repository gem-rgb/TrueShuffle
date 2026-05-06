use thiserror::Error;

pub type AppResult<T> = Result<T, AppError>;

#[derive(Debug, Error)]
pub enum AppError {
  #[error("spotify client id is missing")]
  MissingClientId,
  #[error("spotify authorization is not available")]
  MissingSession,
  #[error("spotify request failed: {0}")]
  Spotify(String),
  #[error(transparent)]
  Reqwest(#[from] reqwest::Error),
  #[error(transparent)]
  Io(#[from] std::io::Error),
  #[error(transparent)]
  Json(#[from] serde_json::Error),
  #[error(transparent)]
  Keyring(#[from] keyring::Error),
  #[error(transparent)]
  Url(#[from] url::ParseError),
  #[error("{0}")]
  Message(String),
}

impl From<&str> for AppError {
  fn from(value: &str) -> Self {
    Self::Message(value.to_string())
  }
}

