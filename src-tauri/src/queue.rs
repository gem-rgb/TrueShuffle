use std::collections::VecDeque;

use crate::types::{QueueSnapshot, Track};

#[derive(Clone, Debug)]
pub struct QueueManager {
  upcoming: VecDeque<Track>,
  history: VecDeque<Track>,
  history_limit: usize,
}

impl QueueManager {
  pub fn new(history_limit: usize) -> Self {
    Self {
      upcoming: VecDeque::new(),
      history: VecDeque::new(),
      history_limit: history_limit.max(1)
    }
  }

  pub fn set_preview(&mut self, tracks: Vec<Track>) {
    self.upcoming = tracks.into_iter().collect();
  }

  pub fn start_playback(&mut self, tracks: Vec<Track>) {
    self.upcoming = tracks.iter().cloned().collect();
    if let Some(first_track) = tracks.first().cloned() {
      self.record_history(first_track);
    }
  }

  pub fn record_history(&mut self, track: Track) {
    self.history.push_back(track);
    while self.history.len() > self.history_limit {
      let _ = self.history.pop_front();
    }
  }

  pub fn recent_history(&self, window: usize) -> Vec<Track> {
    if window == 0 {
      return Vec::new();
    }

    let mut items = self
      .history
      .iter()
      .rev()
      .take(window)
      .cloned()
      .collect::<Vec<_>>();
    items.reverse();
    items
  }

  pub fn snapshot(&self) -> QueueSnapshot {
    QueueSnapshot {
      upcoming: self.upcoming.iter().cloned().collect(),
      history: self.history.iter().cloned().collect()
    }
  }
}
