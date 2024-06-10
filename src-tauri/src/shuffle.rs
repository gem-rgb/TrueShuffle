use std::cmp::Ordering;
use std::collections::{HashMap, HashSet, VecDeque};
use std::time::{SystemTime, UNIX_EPOCH};

use chrono::Utc;
use rand::{rngs::StdRng, Rng, SeedableRng};

use crate::types::{ShuffleMetrics, ShuffleResult, ShuffleSettings, Track};

pub struct ShuffleEngine;

impl ShuffleEngine {
  pub fn new() -> Self {
    Self
  }

  pub fn shuffle(&self, tracks: &[Track], settings: &ShuffleSettings, recent_history: &[Track]) -> ShuffleResult {
    if tracks.is_empty() {
      return ShuffleResult {
        tracks: Vec::new(),
        metrics: ShuffleMetrics {
          total_tracks: 0,
          unique_artists: 0,
          max_artist_run: 0,
          artist_switch_rate: 0.0,
          transition_entropy: 0.0
        }
      };
    }

    let seed = settings.seed.unwrap_or_else(dynamic_seed);
    let mut rng = StdRng::seed_from_u64(seed);
    let recent_ids: HashSet<String> = recent_history
      .iter()
      .rev()
      .take(settings.no_repeat_window)
      .map(|track| track.id.clone())
      .collect();

    let mut artist_buckets: HashMap<String, Vec<Track>> = HashMap::new();
    for track in tracks {
      artist_buckets
        .entry(track.artist_id.clone())
        .or_default()
        .push(track.clone());
    }

    let mut queue = Vec::with_capacity(tracks.len());
    let mut recent_artists: VecDeque<String> = VecDeque::new();
    let spacing_window = settings.artist_spacing.max(1);

    for bucket in artist_buckets.values_mut() {
      bucket.sort_by(|left, right| {
        score_track(right, settings, &recent_ids)
          .partial_cmp(&score_track(left, settings, &recent_ids))
          .unwrap_or(Ordering::Equal)
      });
    }

    while queue.len() < tracks.len() {
      let available_artists = artist_buckets
        .iter()
        .filter(|(_, bucket)| !bucket.is_empty())
        .map(|(artist, _)| artist.clone())
        .collect::<Vec<_>>();

      if available_artists.is_empty() {
        break;
      }

      let blocked: HashSet<String> = recent_artists.iter().cloned().collect();
      let mut candidate_artists = available_artists
        .iter()
        .filter(|artist| !blocked.contains(*artist))
        .cloned()
        .collect::<Vec<_>>();

      if candidate_artists.is_empty() {
        candidate_artists = available_artists.clone();
      }

      let candidate_weights = candidate_artists
        .iter()
        .map(|artist| {
          artist_buckets
            .get(artist)
            .map(|bucket| (bucket.len() as f64).powf(1.35) * rng.gen_range(0.85..1.15))
            .unwrap_or(1.0)
        })
        .collect::<Vec<_>>();

      let selected_artist = pick_weighted_index(&candidate_artists, &candidate_weights, &mut rng)
        .and_then(|index| candidate_artists.get(index).cloned())
        .or_else(|| candidate_artists.first().cloned());

      let Some(selected_artist) = selected_artist else {
        break;
      };

      let Some(bucket) = artist_buckets.get_mut(&selected_artist) else {
        continue;
      };

      if bucket.is_empty() {
        continue;
      }

      let track_index = pick_track_index(bucket, settings, &recent_ids, &mut rng);
      let track = bucket.remove(track_index.min(bucket.len().saturating_sub(1)));
      queue.push(track);

      recent_artists.push_back(selected_artist);
      while recent_artists.len() > spacing_window {
        let _ = recent_artists.pop_front();
      }
    }

    for bucket in artist_buckets.values_mut() {
      for track in bucket.drain(..) {
        queue.push(track);
      }
    }

    ShuffleResult {
      metrics: compute_metrics(&queue),
      tracks: queue
    }
  }
}

impl Default for ShuffleEngine {
  fn default() -> Self {
    Self::new()
  }
}

fn dynamic_seed() -> u64 {
  SystemTime::now()
    .duration_since(UNIX_EPOCH)
    .map(|duration| duration.as_nanos() as u64)
    .unwrap_or(11)
}

fn pick_weighted_index<T>(items: &[T], weights: &[f64], rng: &mut StdRng) -> Option<usize> {
  if items.is_empty() || items.len() != weights.len() {
    return None;
  }

  let total = weights.iter().copied().sum::<f64>();
  if total <= 0.0 {
    return Some(0);
  }

  let mut cursor = rng.gen_range(0.0..total);
  for (index, weight) in weights.iter().enumerate() {
    cursor -= *weight;
    if cursor <= 0.0 {
      return Some(index);
    }
  }

  Some(items.len() - 1)
}

fn pick_track_index(bucket: &[Track], settings: &ShuffleSettings, recent_ids: &HashSet<String>, rng: &mut StdRng) -> usize {
  let mut scored = bucket
    .iter()
    .enumerate()
    .map(|(index, track)| (index, score_track(track, settings, recent_ids) + rng.gen_range(0.0..0.35)))
    .collect::<Vec<_>>();

  scored.sort_by(|left, right| right.1.partial_cmp(&left.1).unwrap_or(Ordering::Equal));

  let top = scored.into_iter().take(3).collect::<Vec<_>>();
  let weights = top
    .iter()
    .map(|(_, score)| score.max(0.2))
    .collect::<Vec<_>>();

  let selected = pick_weighted_index(&top, &weights, rng)
    .and_then(|index| top.get(index).copied())
    .unwrap_or((0, 0.0));

  selected.0
}

fn score_track(track: &Track, settings: &ShuffleSettings, recent_ids: &HashSet<String>) -> f64 {
  let now = Utc::now();
  let added_days = track
    .added_at
    .map(|value| (now - value).num_seconds() as f64 / 86_400.0)
    .unwrap_or(30.0)
    .clamp(0.0, 365.0);
  let played_days = track
    .last_played_at
    .map(|value| (now - value).num_seconds() as f64 / 86_400.0)
    .unwrap_or(365.0)
    .clamp(0.0, 365.0);
  let recency_score = settings.recency_bias * (played_days / 30.0);
  let freshness_score = (1.0 - settings.recency_bias) * (added_days / 45.0);
  let popularity_score = (100_u8.saturating_sub(track.popularity)) as f64 / 120.0;
  let repeat_penalty = if recent_ids.contains(&track.id) {
    80.0 + (settings.no_repeat_window as f64 * 4.0)
  } else {
    0.0
  };

  recency_score + freshness_score + popularity_score - repeat_penalty
}

fn compute_metrics(tracks: &[Track]) -> ShuffleMetrics {
  let mut artist_counts: HashMap<&str, usize> = HashMap::new();
  let mut max_run = 0usize;
  let mut current_run = 0usize;
  let mut previous_artist: Option<&str> = None;
  let mut switches = 0usize;

  for (index, track) in tracks.iter().enumerate() {
    *artist_counts.entry(&track.artist_id).or_insert(0) += 1;
    if index == 0 {
      previous_artist = Some(&track.artist_id);
      current_run = 1;
      continue;
    }

    if previous_artist == Some(&track.artist_id) {
      current_run += 1;
    } else {
      switches += 1;
      max_run = max_run.max(current_run);
      current_run = 1;
      previous_artist = Some(&track.artist_id);
    }
  }

  max_run = max_run.max(current_run);
  let transitions = tracks.len().saturating_sub(1);

  ShuffleMetrics {
    total_tracks: tracks.len(),
    unique_artists: artist_counts.len(),
    max_artist_run: max_run,
    artist_switch_rate: if transitions == 0 {
      0.0
    } else {
      (switches as f64 / transitions as f64 * 1000.0).round() / 1000.0
    },
    transition_entropy: transition_entropy(tracks)
  }
}

fn transition_entropy(tracks: &[Track]) -> f64 {
  if tracks.is_empty() {
    return 0.0;
  }

  let mut artist_counts: HashMap<&str, usize> = HashMap::new();
  for track in tracks {
    *artist_counts.entry(&track.artist_id).or_insert(0) += 1;
  }

  let total = tracks.len() as f64;
  let mut entropy = 0.0;
  for count in artist_counts.values() {
    let probability = *count as f64 / total;
    entropy -= probability * probability.log2();
  }

  let max_entropy = (artist_counts.len().max(2) as f64).log2();
  if max_entropy == 0.0 {
    0.0
  } else {
    (entropy / max_entropy * 1000.0).round() / 1000.0
  }
}

#[cfg(test)]
mod tests {
  use super::ShuffleEngine;
  use crate::types::{ShuffleSettings, Track};
  use std::collections::HashSet;

  fn make_track(id: &str, artist_id: &str, artist_name: &str, name: &str) -> Track {
    Track {
      id: id.to_string(),
      uri: format!("spotify:track:{id}"),
      name: name.to_string(),
      artist_id: artist_id.to_string(),
      artist_name: artist_name.to_string(),
      album_name: "Test Album".to_string(),
      duration_ms: 180_000,
      popularity: 50,
      added_at: None,
      last_played_at: None
    }
  }

  #[test]
  fn preserves_all_tracks_without_duplicates() {
    let tracks = (0..12)
      .map(|index| {
        let artist_index = index % 3;
        make_track(
          &format!("track-{index}"),
          &format!("artist-{artist_index}"),
          &format!("Artist {artist_index}"),
          &format!("Track {index}")
        )
      })
      .collect::<Vec<_>>();

    let engine = ShuffleEngine::new();
    let settings = ShuffleSettings {
      artist_spacing: 2,
      recency_bias: 0.7,
      no_repeat_window: 0,
      seed: Some(42)
    };

    let result = engine.shuffle(&tracks, &settings, &[]);
    assert_eq!(result.tracks.len(), tracks.len());

    let unique_ids = result.tracks.iter().map(|track| track.id.clone()).collect::<HashSet<_>>();
    assert_eq!(unique_ids.len(), tracks.len());
  }

  #[test]
  fn respects_artist_spacing_when_possible() {
    let tracks = (0..20)
      .map(|index| {
        let artist_index = index % 5;
        make_track(
          &format!("track-{index}"),
          &format!("artist-{artist_index}"),
          &format!("Artist {artist_index}"),
          &format!("Track {index}")
        )
      })
      .collect::<Vec<_>>();

    let engine = ShuffleEngine::new();
    let settings = ShuffleSettings {
      artist_spacing: 2,
      recency_bias: 0.5,
      no_repeat_window: 0,
      seed: Some(7)
    };

    let result = engine.shuffle(&tracks, &settings, &[]);
    for window in result.tracks.windows(3) {
      if window.len() == 3 {
        assert_ne!(window[0].artist_id, window[2].artist_id);
      }
    }
  }

  #[test]
  fn keeps_tracks_balanced_for_dense_artists() {
    let tracks = (0..50)
      .map(|index| {
        let artist_index = index % 5;
        make_track(
          &format!("track-{index}"),
          &format!("artist-{artist_index}"),
          &format!("Artist {artist_index}"),
          &format!("Track {index}")
        )
      })
      .collect::<Vec<_>>();

    let engine = ShuffleEngine::new();
    let settings = ShuffleSettings {
      artist_spacing: 2,
      recency_bias: 0.7,
      no_repeat_window: 0,
      seed: Some(99)
    };

    let result = engine.shuffle(&tracks, &settings, &[]);
    assert_eq!(result.metrics.total_tracks, 50);
    assert!(result.metrics.unique_artists >= 5);
  }
}
