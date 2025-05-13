from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from math import log2

from .embedding_engine import EmbeddingEngine
from .graph_engine import TrackGraphEngine
from .models import (
  ObjectiveWeights,
  PreferenceHints,
  QueueMetrics,
  RecommendationResponse,
  SessionContext,
  TrackMetadata
)
from .rl_agent import RLAgent
from .voice_dj import VoiceDJ


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
  return max(lower, min(upper, float(value)))


def stable_ratio(value: float) -> float:
  return round(clamp(value), 3)


@dataclass(slots=True)
class AdaptiveQueueManager:
  rl_agent: RLAgent = field(default_factory=RLAgent)
  embedding_engine: EmbeddingEngine = field(default_factory=EmbeddingEngine)
  graph_engine: TrackGraphEngine = field(default_factory=TrackGraphEngine)
  voice_dj: VoiceDJ = field(default_factory=VoiceDJ)
  recent_tracks: deque[str] = field(default_factory=lambda: deque(maxlen=16))
  play_counts: Counter[str] = field(default_factory=Counter)
  tracks_by_id: dict[str, TrackMetadata] = field(default_factory=dict)

  def ingest_tracks(self, tracks: list[TrackMetadata]) -> None:
    self.tracks_by_id = {track.id: track for track in tracks}
    self.embedding_engine.fit(tracks)
    self.graph_engine.build(tracks)

  def build_queue(
    self,
    tracks: list[TrackMetadata],
    session: SessionContext,
    weights: ObjectiveWeights,
    *,
    current_track_id: str | None = None,
    seed_track_id: str | None = None,
    limit: int | None = None,
    hints: PreferenceHints | None = None,
    command: str | None = None,
    strategy: str = "adaptive"
  ) -> RecommendationResponse:
    if not tracks:
      empty_metrics = QueueMetrics(
        total_tracks=0,
        unique_artists=0,
        max_artist_run=0,
        artist_switch_rate=0.0,
        transition_entropy=0.0,
        preference_score=0.0,
        diversity_score=0.0,
        novelty_score=0.0,
        rl_confidence=self.rl_agent.confidence(),
        graph_coverage=0.0,
        embedding_similarity=0.0
      )
      return RecommendationResponse(
        session_id="default",
        tracks=[],
        metrics=empty_metrics,
        explanation="No tracks were available for adaptive recommendation.",
        voice_line="No tracks were available.",
        session=session,
        strategy=strategy,
        command=command
      )

    self.ingest_tracks(tracks)
    hints = hints or PreferenceHints()
    max_tracks = limit or len(tracks)
    remaining = [track for track in tracks if track.id not in self.recent_tracks]
    if not remaining:
      remaining = tracks[:]

    seed_track = self._select_seed_track(remaining, session, hints, seed_track_id=seed_track_id, current_track_id=current_track_id)
    queue: list[TrackMetadata] = []
    component_snapshots: list[dict[str, float]] = []
    recent_artist_window: deque[str] = deque(maxlen=max(1, 2))

    while remaining and len(queue) < max_tracks:
      state = self._build_state(session, seed_track, queue, hints, command, strategy)
      graph_scores = dict(self.graph_engine.discover(seed_track.id if seed_track else remaining[0].id, limit=len(remaining)))
      nearest_scores = {track_id: score for track_id, score in self.embedding_engine.nearest(seed_track or remaining[0], k=len(remaining))}

      ranked_candidates = []
      for track in remaining:
        if track.id in self.recent_tracks and track.id not in {current_track_id, seed_track_id}:
          continue

        components = self._score_track(
          track,
          session,
          weights,
          hints,
          queue,
          recent_artist_window,
          graph_scores.get(track.id, 0.0),
          nearest_scores.get(track.id, 0.0),
          state
        )
        ranked_candidates.append((track, components))

      if not ranked_candidates:
        ranked_candidates = [
          (track, self._score_track(track, session, weights, hints, queue, recent_artist_window, 0.0, 0.0, state))
          for track in remaining
        ]

      ranked_candidates.sort(key=lambda item: item[1]["total"], reverse=True)
      top_actions = [track.id for track, _ in ranked_candidates[:5]]
      chosen_action = self.rl_agent.choose_action({**state, "actions": top_actions})

      selected_track = None
      selected_components: dict[str, float] | None = None
      if chosen_action is not None:
        for track, components in ranked_candidates:
          if track.id == chosen_action:
            selected_track = track
            selected_components = components
            break

      if selected_track is None:
        selected_track, selected_components = ranked_candidates[0]

      queue.append(selected_track)
      component_snapshots.append(selected_components or {})
      self.recent_tracks.append(selected_track.id)
      self.play_counts[selected_track.id] += 1
      self.rl_agent.update(state, selected_track.id, selected_components.get("reward", 0.0) if selected_components else 0.0)
      remaining = [track for track in remaining if track.id != selected_track.id]
      seed_track = selected_track
      recent_artist_window.append(selected_track.artist_id)

    metrics = self._compute_metrics(queue, component_snapshots)
    explanation = self.voice_dj.explain_queue(queue, session, metrics, command=command)
    voice_line = self.voice_dj.voice_line(queue, session, metrics)

    return RecommendationResponse(
      session_id="default",
      tracks=queue,
      metrics=metrics,
      explanation=explanation,
      voice_line=voice_line,
      session=session,
      strategy=strategy,
      command=command,
      seed_track_id=seed_track.id if seed_track else None
    )

  def record_feedback(
    self,
    track_id: str,
    action: str,
    session: SessionContext,
    weights: ObjectiveWeights,
    *,
    hints: PreferenceHints | None = None,
    command: str | None = None,
    limit: int | None = None
  ) -> RecommendationResponse:
    track = self.tracks_by_id.get(track_id)
    if track is not None:
      self.recent_tracks.append(track.id)
      self.play_counts[track.id] += 1

    reward = {
      "skip": -1.0,
      "full_play": 1.0,
      "replay": 2.0
    }.get(action, 0.0)
    state = self._build_state(session, track, [], hints or PreferenceHints(), command, "feedback")
    self.rl_agent.update(state, track_id, reward)

    all_tracks = list(self.tracks_by_id.values())
    return self.build_queue(
      all_tracks,
      session,
      weights,
      current_track_id=track_id,
      seed_track_id=track_id,
      limit=limit,
      hints=hints,
      command=command,
      strategy=f"feedback:{action}"
    )

  def _select_seed_track(
    self,
    tracks: list[TrackMetadata],
    session: SessionContext,
    hints: PreferenceHints,
    *,
    seed_track_id: str | None = None,
    current_track_id: str | None = None
  ) -> TrackMetadata:
    lookup = {track.id: track for track in tracks}
    for identifier in (seed_track_id, current_track_id):
      if identifier and identifier in lookup:
        return lookup[identifier]

    ranked = sorted(
      tracks,
      key=lambda track: (
        self._preference_score(track, session, hints),
        track.popularity,
        -len(track.genres)
      ),
      reverse=True
    )
    return ranked[0]

  def _build_state(
    self,
    session: SessionContext,
    seed_track: TrackMetadata | None,
    queue: list[TrackMetadata],
    hints: PreferenceHints,
    command: str | None,
    strategy: str
  ) -> dict[str, object]:
    recent_artist_ids = [track.artist_id for track in queue[-4:]]
    return {
      "time_of_day": session.time_of_day,
      "activity": session.activity,
      "energy": round(session.energy, 2),
      "seed_track_id": seed_track.id if seed_track else None,
      "seed_artist_id": seed_track.artist_id if seed_track else None,
      "recent_artists": recent_artist_ids,
      "genre_hints": hints.genre_hints,
      "artist_hints": hints.artist_hints,
      "command": command or "",
      "strategy": strategy
    }

  def _score_track(
    self,
    track: TrackMetadata,
    session: SessionContext,
    weights: ObjectiveWeights,
    hints: PreferenceHints,
    queue: list[TrackMetadata],
    recent_artist_window: deque[str],
    graph_score: float,
    embedding_score: float,
    state: dict[str, object]
  ) -> dict[str, float]:
    preference = self._preference_score(track, session, hints)
    diversity = self._diversity_score(track, queue, recent_artist_window, hints)
    novelty = self._novelty_score(track)
    rl_bonus = self.rl_agent.q_value(state, track.id)
    graph_bonus = clamp(graph_score)
    embedding_bonus = clamp((embedding_score + 1.0) / 2.0)

    total = (
      weights.preference_weight * preference
      + weights.diversity_weight * diversity
      + weights.novelty_weight * novelty
      + 0.12 * graph_bonus
      + 0.12 * embedding_bonus
      + 0.08 * rl_bonus
    )
    reward = (-1.0 * self._skip_probability(track, session, novelty, diversity)) + (1.0 * (1.0 - self._skip_probability(track, session, novelty, diversity))) + (2.0 * self._replay_probability(track, session, novelty, preference))

    return {
      "preference": preference,
      "diversity": diversity,
      "novelty": novelty,
      "graph": graph_bonus,
      "embedding": embedding_bonus,
      "rl": rl_bonus,
      "total": total,
      "reward": reward
    }

  def _preference_score(self, track: TrackMetadata, session: SessionContext, hints: PreferenceHints) -> float:
    features = track.audio_features
    tempo = features.tempo if features is not None else 100.0 + (track.popularity * 0.6)
    energy = features.energy if features is not None else clamp(track.popularity / 100.0)
    target_tempo = self._target_tempo(session.activity)
    tempo_fit = 1.0 - min(1.0, abs(tempo - target_tempo) / 140.0)
    energy_fit = 1.0 - min(1.0, abs(energy - session.energy))
    hint_bonus = 0.0

    lowered_name = track.name.lower()
    lowered_artist = track.artist_name.lower()
    lowered_genres = [genre.lower() for genre in track.genres]
    for genre_hint in hints.genre_hints:
      if genre_hint.lower() in lowered_name or genre_hint.lower() in lowered_artist or genre_hint.lower() in lowered_genres:
        hint_bonus += 0.08
    for artist_hint in hints.artist_hints:
      if artist_hint.lower() in lowered_artist:
        hint_bonus += 0.1
    for keyword in hints.keywords:
      if keyword in lowered_name or keyword in lowered_artist:
        hint_bonus += 0.03

    popularity_bias = track.popularity / 400.0
    score = 0.48 * tempo_fit + 0.42 * energy_fit + popularity_bias + hint_bonus
    return clamp(score)

  def _diversity_score(self, track: TrackMetadata, queue: list[TrackMetadata], recent_artist_window: deque[str], hints: PreferenceHints) -> float:
    if not queue:
      return 1.0

    artist_repeat_penalty = 1.0 if track.artist_id in recent_artist_window else 0.0
    genre_overlap = 0.0
    if track.genres:
      seen = {genre.lower() for queued in queue for genre in queued.genres}
      matches = sum(1 for genre in track.genres if genre.lower() in seen)
      genre_overlap = matches / max(1, len(track.genres))

    hint_overlap = 0.0
    if hints.genre_hints:
      hint_overlap = sum(1 for genre in track.genres for hint in hints.genre_hints if hint.lower() in genre.lower()) / max(1, len(track.genres))

    score = 1.0 - (0.5 * artist_repeat_penalty + 0.3 * genre_overlap + 0.2 * hint_overlap)
    return clamp(score)

  def _novelty_score(self, track: TrackMetadata) -> float:
    repeat_count = self.play_counts[track.id]
    recency_penalty = 0.0
    if track.last_played_at is not None:
      age_days = max(0.0, (datetime.now(timezone.utc) - track.last_played_at).total_seconds() / 86_400.0)
      recency_penalty = min(1.0, age_days / 40.0)
    play_penalty = min(1.0, repeat_count / 5.0)
    return clamp(1.0 - (0.55 * play_penalty + 0.45 * (1.0 - recency_penalty)))

  def _skip_probability(self, track: TrackMetadata, session: SessionContext, novelty: float, diversity: float) -> float:
    preference = self._preference_score(track, session, PreferenceHints())
    return clamp(0.62 - (preference * 0.38) - (novelty * 0.12) - (diversity * 0.08), 0.05, 0.9)

  def _replay_probability(self, track: TrackMetadata, session: SessionContext, novelty: float, preference: float) -> float:
    return clamp(0.04 + (preference * 0.24) + (novelty * 0.18), 0.0, 0.5)

  def _target_tempo(self, activity: str) -> float:
    return {
      "workout": 150.0,
      "party": 138.0,
      "drive": 118.0,
      "focus": 96.0,
      "work": 102.0,
      "browse": 110.0,
      "relax": 84.0
    }.get(activity, 108.0)

  def _compute_metrics(self, queue: list[TrackMetadata], component_snapshots: list[dict[str, float]]) -> QueueMetrics:
    artist_counts = Counter(track.artist_id for track in queue)
    max_run = 0
    current_run = 0
    previous_artist: str | None = None
    switches = 0

    for index, track in enumerate(queue):
      if index == 0:
        current_run = 1
        previous_artist = track.artist_id
        continue

      if track.artist_id == previous_artist:
        current_run += 1
      else:
        switches += 1
        max_run = max(max_run, current_run)
        current_run = 1
        previous_artist = track.artist_id

    max_run = max(max_run, current_run)
    transitions = max(0, len(queue) - 1)
    total = max(1, len(queue))
    preference_avg = sum(snapshot.get("preference", 0.0) for snapshot in component_snapshots) / total
    diversity_avg = sum(snapshot.get("diversity", 0.0) for snapshot in component_snapshots) / total
    novelty_avg = sum(snapshot.get("novelty", 0.0) for snapshot in component_snapshots) / total
    graph_avg = sum(snapshot.get("graph", 0.0) for snapshot in component_snapshots) / total
    embedding_avg = sum(snapshot.get("embedding", 0.0) for snapshot in component_snapshots) / total

    entropy = 0.0
    for count in artist_counts.values():
      probability = count / total
      entropy -= probability * log2(probability)
    max_entropy = log2(max(2, len(artist_counts)))
    transition_entropy = 0.0 if max_entropy == 0.0 else entropy / max_entropy

    return QueueMetrics(
      total_tracks=len(queue),
      unique_artists=len(artist_counts),
      max_artist_run=max_run,
      artist_switch_rate=0.0 if transitions == 0 else stable_ratio(switches / transitions),
      transition_entropy=stable_ratio(transition_entropy),
      preference_score=stable_ratio(preference_avg),
      diversity_score=stable_ratio(diversity_avg),
      novelty_score=stable_ratio(novelty_avg),
      rl_confidence=self.rl_agent.confidence(),
      graph_coverage=stable_ratio(graph_avg),
      embedding_similarity=stable_ratio(embedding_avg)
    )

