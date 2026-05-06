use std::env;
use std::time::Duration as StdDuration;

use base64::{engine::general_purpose::URL_SAFE_NO_PAD, Engine as _};
use chrono::{Duration, Utc};
use rand::{distributions::Alphanumeric, Rng};
use serde::Deserialize;
use sha2::{Digest, Sha256};
use tokio::sync::oneshot;
use tokio::sync::RwLock;
use url::Url;

use crate::error::{AppError, AppResult};
use crate::mock::auth_status as mock_auth_status;
use crate::types::{AuthStatus, TokenBundle};

const KEYRING_SERVICE: &str = "TrueShuffle";
const KEYRING_ACCOUNT: &str = "spotify_tokens";

#[derive(Clone)]
struct AuthConfig {
  client_id: String,
  client_secret: Option<String>,
  redirect_uri: String,
  scopes: Vec<String>,
}

pub struct AuthManager {
  config: AuthConfig,
  tokens: RwLock<Option<TokenBundle>>,
  demo_mode: bool,
}

struct LoginFlow {
  state: String,
  verifier: String,
  challenge: String,
}

#[derive(Debug, Deserialize)]
struct TokenResponse {
  access_token: String,
  refresh_token: Option<String>,
  expires_in: i64,
  scope: Option<String>
}

impl AuthManager {
  pub fn new() -> Self {
    let client_id = env::var("SPOTIFY_CLIENT_ID").unwrap_or_default();
    let client_secret = env::var("SPOTIFY_CLIENT_SECRET").ok();
    let redirect_uri = env::var("SPOTIFY_REDIRECT_URI")
      .unwrap_or_else(|_| "http://127.0.0.1:17171/callback".to_string());
    let scopes = env::var("SPOTIFY_SCOPES")
      .unwrap_or_else(|_| {
        "playlist-read-private playlist-read-collaborative user-read-playback-state user-modify-playback-state user-read-currently-playing".to_string()
      })
      .split_whitespace()
      .map(|scope| scope.to_string())
      .collect::<Vec<_>>();

    let demo_mode = matches!(env::var("TRUESHUFFLE_DEMO_MODE").ok().as_deref(), Some("1" | "true" | "yes"))
      || client_id.is_empty();

    let tokens = load_tokens().ok().flatten();

    Self {
      config: AuthConfig {
        client_id,
        client_secret,
        redirect_uri,
        scopes
      },
      tokens: RwLock::new(tokens),
      demo_mode
    }
  }

  pub fn is_demo_mode(&self) -> bool {
    self.demo_mode
  }

  pub async fn has_session(&self) -> bool {
    self.tokens.read().await.is_some()
  }

  pub async fn status(&self) -> AppResult<AuthStatus> {
    if self.demo_mode || !self.has_session().await {
      return Ok(mock_auth_status(true, false, None));
    }

    match self.access_token().await {
      Ok(_) => {
        let expires_at = self.tokens.read().await.as_ref().map(|bundle| bundle.expires_at);
        Ok(AuthStatus {
          authenticated: true,
          demo_mode: false,
          display_name: "Spotify connected".to_string(),
          expires_at
        })
      }
      Err(_) => Ok(AuthStatus {
        authenticated: false,
        demo_mode: true,
        display_name: "Demo Mode".to_string(),
        expires_at: None
      })
    }
  }

  pub async fn logout(&self) -> AppResult<()> {
    self.tokens.write().await.take();
    clear_tokens()?;
    Ok(())
  }

  pub async fn begin_login(&self) -> AppResult<AuthStatus> {
    if self.demo_mode {
      return self.status().await;
    }

    if self.config.client_id.is_empty() {
      return Err(AppError::MissingClientId);
    }

    let flow = LoginFlow::new();
    let auth_url = self.build_authorize_url(&flow)?;
    let _ = webbrowser::open(&auth_url);

    let code = self.wait_for_authorization_code(flow.state.clone()).await?;
    let tokens = self.exchange_code(&code, &flow.verifier).await?;
    self.store_tokens(tokens).await?;
    self.status().await
  }

  pub async fn access_token(&self) -> AppResult<String> {
    if self.demo_mode {
      return Err(AppError::MissingSession);
    }

    let snapshot = self.tokens.read().await.clone().ok_or(AppError::MissingSession)?;
    if snapshot.expires_at - Utc::now() > Duration::minutes(5) {
      return Ok(snapshot.access_token);
    }

    if snapshot.refresh_token.is_empty() {
      return Err(AppError::MissingSession);
    }

    let refreshed = match self.refresh_access_token(&snapshot.refresh_token).await {
      Ok(bundle) => bundle,
      Err(error) => {
        self.tokens.write().await.take();
        let _ = clear_tokens();
        return Err(error);
      }
    };
    self.store_tokens(refreshed.clone()).await?;
    Ok(refreshed.access_token)
  }

  fn build_authorize_url(&self, flow: &LoginFlow) -> AppResult<String> {
    let mut url = Url::parse("https://accounts.spotify.com/authorize")?;
    url.query_pairs_mut()
      .append_pair("client_id", &self.config.client_id)
      .append_pair("response_type", "code")
      .append_pair("redirect_uri", &self.config.redirect_uri)
      .append_pair("code_challenge_method", "S256")
      .append_pair("code_challenge", &flow.challenge)
      .append_pair("state", &flow.state)
      .append_pair("scope", &self.config.scopes.join(" "));
    Ok(url.to_string())
  }

  async fn exchange_code(&self, code: &str, verifier: &str) -> AppResult<TokenBundle> {
    let mut params = vec![
      ("grant_type", "authorization_code".to_string()),
      ("code", code.to_string()),
      ("redirect_uri", self.config.redirect_uri.clone()),
      ("client_id", self.config.client_id.clone()),
      ("code_verifier", verifier.to_string())
    ];
    if let Some(secret) = &self.config.client_secret {
      params.push(("client_secret", secret.clone()));
    }
    let payload = self.request_token_raw(&params).await?;
    self.token_bundle_from_response(payload, None)
  }

  async fn refresh_access_token(&self, refresh_token: &str) -> AppResult<TokenBundle> {
    let mut params = vec![
      ("grant_type", "refresh_token".to_string()),
      ("refresh_token", refresh_token.to_string()),
      ("client_id", self.config.client_id.clone())
    ];
    if let Some(secret) = &self.config.client_secret {
      params.push(("client_secret", secret.clone()));
    }
    let payload = self.request_token_raw(&params).await?;
    self.token_bundle_from_response(payload, Some(refresh_token))
  }

  async fn request_token_raw(&self, params: &[(&str, String)]) -> AppResult<TokenResponse> {
    let response = reqwest::Client::new()
      .post("https://accounts.spotify.com/api/token")
      .form(&params)
      .send()
      .await?;

    if !response.status().is_success() {
      let status = response.status();
      let body = response.text().await.unwrap_or_default();
      return Err(AppError::Spotify(format!("token request failed with {status}: {body}")));
    }

    Ok(response.json::<TokenResponse>().await?)
  }

  fn token_bundle_from_response(&self, payload: TokenResponse, refresh_token: Option<&str>) -> AppResult<TokenBundle> {
    let expires_in = payload.expires_in.max(120);
    Ok(TokenBundle {
      access_token: payload.access_token,
      refresh_token: payload
        .refresh_token
        .or_else(|| refresh_token.map(|value| value.to_string()))
        .ok_or_else(|| AppError::Message("Spotify did not return a refresh token".to_string()))?,
      expires_at: Utc::now() + Duration::seconds(expires_in - 60),
      scope: payload.scope.unwrap_or_else(|| self.config.scopes.join(" "))
    })
  }

  async fn wait_for_authorization_code(&self, expected_state: String) -> AppResult<String> {
    let redirect_url = Url::parse(&self.config.redirect_uri)?;
    let port = redirect_url
      .port_or_known_default()
      .ok_or_else(|| AppError::Message("redirect URI must contain a port".to_string()))?;
    let expected_path = redirect_url.path().to_string();
    let (tx, rx) = oneshot::channel::<Result<String, String>>();

    std::thread::spawn(move || {
      let bind_address = format!("127.0.0.1:{port}");
      let server = match tiny_http::Server::http(&bind_address) {
        Ok(server) => server,
        Err(error) => {
          let _ = tx.send(Err(error.to_string()));
          return;
        }
      };

      for request in server.incoming_requests() {
        let parsed = match Url::parse(&format!("http://localhost{}", request.url())) {
          Ok(url) => url,
          Err(error) => {
            let _ = request.respond(tiny_http::Response::from_string("Invalid callback request"));
            let _ = tx.send(Err(error.to_string()));
            break;
          }
        };

        if parsed.path() != expected_path {
          let _ = request.respond(tiny_http::Response::from_string("TrueShuffle ignored this path"));
          continue;
        }

        let code = parsed
          .query_pairs()
          .find(|(key, _)| key == "code")
          .map(|(_, value)| value.to_string());
        let returned_state = parsed
          .query_pairs()
          .find(|(key, _)| key == "state")
          .map(|(_, value)| value.to_string());

        let result = match (code, returned_state) {
          (Some(code), Some(state)) if state == expected_state => Ok(code),
          (Some(_), Some(_)) => Err("Spotify authorization state mismatch".to_string()),
          _ => Err("Spotify authorization callback did not contain a code".to_string())
        };

        let body = match &result {
          Ok(_) => "TrueShuffle received the Spotify authorization. You can close this window.",
          Err(_) => "TrueShuffle could not complete Spotify authorization."
        };
        let _ = request.respond(tiny_http::Response::from_string(body));
        let _ = tx.send(result);
        break;
      }
    });

    let received = tokio::time::timeout(StdDuration::from_secs(120), rx)
      .await
      .map_err(|_| AppError::Message("Timed out waiting for Spotify authorization".to_string()))?
      .map_err(|_| AppError::Message("Spotify authorization callback closed unexpectedly".to_string()))?;

    received.map_err(AppError::Message)
  }

  async fn store_tokens(&self, bundle: TokenBundle) -> AppResult<()> {
    self.tokens.write().await.replace(bundle.clone());
    save_tokens(&bundle)?;
    Ok(())
  }
}

impl LoginFlow {
  fn new() -> Self {
    let state = random_string(28);
    let verifier = random_string(96);
    let challenge = pkce_challenge(&verifier);
    Self {
      state,
      verifier,
      challenge
    }
  }
}

fn random_string(length: usize) -> String {
  rand::thread_rng()
    .sample_iter(Alphanumeric)
    .take(length)
    .map(char::from)
    .collect()
}

fn pkce_challenge(verifier: &str) -> String {
  let digest = Sha256::digest(verifier.as_bytes());
  URL_SAFE_NO_PAD.encode(digest)
}

fn token_entry() -> AppResult<keyring::Entry> {
  Ok(keyring::Entry::new(KEYRING_SERVICE, KEYRING_ACCOUNT)?)
}

fn load_tokens() -> AppResult<Option<TokenBundle>> {
  let entry = token_entry()?;
  match entry.get_password() {
    Ok(raw) => Ok(serde_json::from_str::<TokenBundle>(&raw).ok()),
    Err(keyring::Error::NoEntry) => Ok(None),
    Err(error) => Err(error.into())
  }
}

fn save_tokens(bundle: &TokenBundle) -> AppResult<()> {
  let entry = token_entry()?;
  entry.set_password(&serde_json::to_string(bundle)?)?;
  Ok(())
}

fn clear_tokens() -> AppResult<()> {
  let entry = token_entry()?;
  match entry.delete_password() {
    Ok(_) => Ok(()),
    Err(keyring::Error::NoEntry) => Ok(()),
    Err(error) => Err(error.into())
  }
}
