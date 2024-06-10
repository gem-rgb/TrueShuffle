from __future__ import annotations

from dataclasses import dataclass

from .models import ObjectiveWeights, SessionContext, SimulationResponse, SimulationStrategyResult, TrackMetadata
from .queue_manager import AdaptiveQueueManager, clamp


STRATEGY_PRESETS: dict[str, ObjectiveWeights] = {
  "adaptive": ObjectiveWeights(preference_weight=0.5, diversity_weight=0.25, novelty_weight=0.25),
  "balanced": ObjectiveWeights(preference_weight=0.45, diversity_weight=0.35, novelty_weight=0.2),
  "graph": ObjectiveWeights(preference_weight=0.35, diversity_weight=0.28, novelty_weight=0.37),
  "embedding": ObjectiveWeights(preference_weight=0.56, diversity_weight=0.16, novelty_weight=0.28),
  "discovery": ObjectiveWeights(preference_weight=0.3, diversity_weight=0.3, novelty_weight=0.4)
}


@dataclass(slots=True)
class SimulationEngine:
  def run(
    self,
    tracks: list[TrackMetadata],
    session: SessionContext,
    strategies: list[str],
    *,
    runs: int = 5,
    limit: int | None = None
  ) -> SimulationResponse:
    if not tracks:
      return SimulationResponse(
        session_id="default",
        summary="Simulation skipped because no tracks were supplied.",
        strategies=[]
      )

    results: list[SimulationStrategyResult] = []
    strategy_names = strategies or ["adaptive"]

    for strategy_name in strategy_names:
      preset = STRATEGY_PRESETS.get(strategy_name, STRATEGY_PRESETS["balanced"])
      samples: list[dict[str, float]] = []
      for _ in range(max(1, runs)):
        manager = AdaptiveQueueManager()
        response = manager.build_queue(
          tracks,
          session,
          preset,
          limit=limit or len(tracks),
          strategy=strategy_name
        )
        samples.append(self._score_queue(response.tracks, session))

      results.append(self._aggregate(strategy_name, samples))

    best = max(results, key=lambda result: result.average_reward, default=None)
    if best is None:
      summary = "Simulation completed, but no strategies produced a score."
    else:
      summary = (
        f"Simulation suggests {best.name} as the strongest strategy with "
        f"{best.average_reward:.3f} expected reward and {best.diversity_score:.3f} diversity."
      )

    return SimulationResponse(session_id="default", summary=summary, strategies=results)

  def _score_queue(self, queue: list[TrackMetadata], session: SessionContext) -> dict[str, float]:
    if not queue:
      return {
        "average_reward": 0.0,
        "diversity_score": 0.0,
        "novelty_score": 0.0,
        "skip_rate": 1.0,
        "replay_rate": 0.0,
        "queue_entropy": 0.0,
        "preference_score": 0.0
      }

    artist_counts: dict[str, int] = {}
    skips = 0.0
    replays = 0.0
    rewards = 0.0
    preference_total = 0.0
    novelty_total = 0.0

    for index, track in enumerate(queue):
      artist_counts[track.artist_id] = artist_counts.get(track.artist_id, 0) + 1
      preference = self._preference_score(track, session)
      novelty = self._novelty_score(track, artist_counts[track.artist_id])
      skip_probability = clamp(0.65 - preference * 0.4 - novelty * 0.15, 0.05, 0.9)
      replay_probability = clamp(0.05 + preference * 0.22 + novelty * 0.16, 0.0, 0.5)
      full_play_probability = max(0.0, 1.0 - skip_probability - replay_probability)
      reward = (-1.0 * skip_probability) + (1.0 * full_play_probability) + (2.0 * replay_probability)

      skips += skip_probability
      replays += replay_probability
      rewards += reward
      preference_total += preference
      novelty_total += novelty

    entropy = self._entropy(queue)
    total = max(1, len(queue))
    return {
      "average_reward": rewards / total,
      "diversity_score": len(artist_counts) / total,
      "novelty_score": novelty_total / total,
      "skip_rate": skips / total,
      "replay_rate": replays / total,
      "queue_entropy": entropy,
      "preference_score": preference_total / total
    }

  def _aggregate(self, name: str, samples: list[dict[str, float]]) -> SimulationStrategyResult:
    total = max(1, len(samples))
    return SimulationStrategyResult(
      name=name,
      average_reward=sum(sample["average_reward"] for sample in samples) / total,
      diversity_score=sum(sample["diversity_score"] for sample in samples) / total,
      novelty_score=sum(sample["novelty_score"] for sample in samples) / total,
      skip_rate=sum(sample["skip_rate"] for sample in samples) / total,
      replay_rate=sum(sample["replay_rate"] for sample in samples) / total,
      queue_entropy=sum(sample["queue_entropy"] for sample in samples) / total,
      preference_score=sum(sample["preference_score"] for sample in samples) / total,
      rl_confidence=0.0
    )

  def _preference_score(self, track: TrackMetadata, session: SessionContext) -> float:
    features = track.audio_features
    tempo = features.tempo if features is not None else 100.0
    energy = features.energy if features is not None else track.popularity / 100.0
    target_tempo = {
      "workout": 150.0,
      "party": 138.0,
      "drive": 118.0,
      "focus": 96.0,
      "work": 102.0,
      "browse": 110.0,
      "relax": 84.0
    }.get(session.activity, 108.0)
    tempo_fit = 1.0 - min(1.0, abs(tempo - target_tempo) / 140.0)
    energy_fit = 1.0 - min(1.0, abs(energy - session.energy))
    popularity_bias = track.popularity / 400.0
    return clamp(0.5 * tempo_fit + 0.4 * energy_fit + popularity_bias)

  def _novelty_score(self, track: TrackMetadata, repeat_count: int) -> float:
    return clamp(1.0 - min(1.0, repeat_count / 4.0) + (1.0 - track.popularity / 120.0) * 0.05)

  def _entropy(self, queue: list[TrackMetadata]) -> float:
    if not queue:
      return 0.0

    counts: dict[str, int] = {}
    for track in queue:
      counts[track.artist_id] = counts.get(track.artist_id, 0) + 1

    total = len(queue)
    entropy = 0.0
    for count in counts.values():
      probability = count / total
      entropy -= probability * __import__("math").log2(probability)
    max_entropy = __import__("math").log2(max(2, len(counts)))
    return 0.0 if max_entropy == 0.0 else entropy / max_entropy

