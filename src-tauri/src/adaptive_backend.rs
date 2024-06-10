use std::env;
use std::net::{SocketAddr, TcpStream};
use std::path::{Path, PathBuf};
use std::process::{Child, Command, Stdio};
use std::sync::Mutex;
use std::time::Duration;

#[cfg(windows)]
use std::os::windows::process::CommandExt;

use tauri::AppHandle;

const DEFAULT_HOST: &str = "127.0.0.1";
const DEFAULT_PORT: u16 = 8000;
const WINDOWS_NO_WINDOW: u32 = 0x0800_0000;

pub struct AdaptiveBackendLauncher {
  child: Mutex<Option<Child>>,
  enabled: bool,
  host: String,
  port: u16,
  candidates: Vec<PythonCandidate>,
}

#[derive(Clone, Debug)]
struct PythonCandidate {
  executable: String,
  args: Vec<String>,
}

impl AdaptiveBackendLauncher {
  pub fn new() -> Self {
    let enabled = env::var("TRUESHUFFLE_AI_AUTO_LAUNCH")
      .map(|value| !matches!(value.trim().to_ascii_lowercase().as_str(), "0" | "false" | "off" | "no"))
      .unwrap_or(true);
    let host = env::var("TRUESHUFFLE_AI_HOST").unwrap_or_else(|_| DEFAULT_HOST.to_string());
    let port = env::var("TRUESHUFFLE_AI_PORT")
      .ok()
      .and_then(|value| value.parse::<u16>().ok())
      .unwrap_or(DEFAULT_PORT);
    let candidates = Self::python_candidates();

    Self {
      child: Mutex::new(None),
      enabled,
      host,
      port,
      candidates
    }
  }

  pub fn ensure_started(&self, app: &AppHandle) {
    if !self.enabled {
      eprintln!("TrueShuffle adaptive backend auto-launch disabled.");
      return;
    }

    if self.is_running() {
      eprintln!("TrueShuffle adaptive backend already running on {}:{}.", self.host, self.port);
      return;
    }

    let Some(workspace_root) = self.workspace_root(app) else {
      eprintln!("TrueShuffle adaptive backend could not resolve a workspace root.");
      return;
    };

    if !workspace_root.join("backend").exists() {
      eprintln!(
        "TrueShuffle adaptive backend resources are missing under {}.",
        workspace_root.display()
      );
      return;
    }

    for candidate in &self.candidates {
      match self.spawn_backend(&workspace_root, candidate) {
        Ok(child) => {
          self.store_child(child);
          eprintln!(
            "TrueShuffle adaptive backend launched with {} on {}:{}.",
            candidate.executable,
            self.host,
            self.port
          );
          return;
        }
        Err(error) => {
          eprintln!(
            "TrueShuffle adaptive backend launch failed with {}: {}",
            candidate.executable, error
          );
        }
      }
    }

    eprintln!("TrueShuffle adaptive backend could not start. Falling back to local scoring.");
  }

  pub fn shutdown(&self) {
    let child = {
      let mut guard = match self.child.lock() {
        Ok(guard) => guard,
        Err(_) => return,
      };
      guard.take()
    };

    if let Some(mut child) = child {
      let _ = child.kill();
      let _ = child.wait();
    }
  }

  fn spawn_backend(&self, workspace_root: &Path, candidate: &PythonCandidate) -> Result<Child, std::io::Error> {
    let mut command = Command::new(&candidate.executable);
    command.args(&candidate.args);
    command.current_dir(workspace_root);
    command.env("PYTHONUNBUFFERED", "1");
    command.env("TRUESHUFFLE_AI_HOST", &self.host);
    command.env("TRUESHUFFLE_AI_PORT", self.port.to_string());
    command.stdin(Stdio::null());
    command.stdout(Stdio::null());
    command.stderr(Stdio::null());

    #[cfg(windows)]
    {
      command.creation_flags(WINDOWS_NO_WINDOW);
    }

    command.spawn()
  }

  fn store_child(&self, child: Child) {
    if let Ok(mut guard) = self.child.lock() {
      *guard = Some(child);
    }
  }

  fn is_running(&self) -> bool {
    let addr = SocketAddr::from(([127, 0, 0, 1], self.port));
    TcpStream::connect_timeout(&addr, Duration::from_millis(250)).is_ok()
  }

  fn workspace_root(&self, app: &AppHandle) -> Option<PathBuf> {
    let mut candidates = Vec::new();

    if let Some(resource_dir) = app.path_resolver().resource_dir() {
      candidates.push(resource_dir);
    }

    if let Ok(current_dir) = env::current_dir() {
      candidates.push(current_dir);
    }

    if let Some(manifest_root) = manifest_root() {
      candidates.push(manifest_root);
    }

    for candidate in candidates {
      let backend_dir = candidate.join("backend");
      if backend_dir.join("__main__.py").exists() || backend_dir.join("app.py").exists() {
        return Some(candidate);
      }
      if candidate.file_name().and_then(|name| name.to_str()) == Some("backend") {
        return candidate.parent().map(Path::to_path_buf);
      }
    }

    None
  }

  fn python_candidates() -> Vec<PythonCandidate> {
    if let Ok(executable) = env::var("TRUESHUFFLE_AI_PYTHON") {
      return vec![PythonCandidate {
        executable,
        args: vec!["-m".to_string(), "backend".to_string()]
      }];
    }

    #[cfg(windows)]
    {
      return vec![
        PythonCandidate {
          executable: "python".to_string(),
          args: vec!["-m".to_string(), "backend".to_string()]
        },
        PythonCandidate {
          executable: "py".to_string(),
          args: vec![
            "-3".to_string(),
            "-m".to_string(),
            "backend".to_string()
          ]
        }
      ];
    }

    #[cfg(not(windows))]
    {
      return vec![
        PythonCandidate {
          executable: "python3".to_string(),
          args: vec!["-m".to_string(), "backend".to_string()]
        },
        PythonCandidate {
          executable: "python".to_string(),
          args: vec!["-m".to_string(), "backend".to_string()]
        }
      ];
    }
  }
}

impl Drop for AdaptiveBackendLauncher {
  fn drop(&mut self) {
    self.shutdown();
  }
}

fn manifest_root() -> Option<PathBuf> {
  let manifest_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
  manifest_dir.parent().map(Path::to_path_buf)
}
