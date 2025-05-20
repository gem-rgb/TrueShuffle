from __future__ import annotations

from .models import QueueMetrics, SessionContext, TrackMetadata


class VoiceDJ:
  def explain_queue(
    self,
    queue: list[TrackMetadata],
    session: SessionContext,
    metrics: QueueMetrics,
    *,
    command: str | None = None
  ) -> str:
    if not queue:
      return "I could not build a queue for this session."

    first = queue[0]
    tempo = self._first_tempo(first)
    command_clause = f"after interpreting '{command.strip()}'" if command else "for the current context"
    return (
      f"I built a {session.activity} queue for {session.time_of_day} listening "
      f"{command_clause}. It opens with {first.name} by {first.artist_name}, "
      f"lands near {tempo:.0f} BPM, and keeps artist repetition low while preserving novelty."
    )

  def voice_line(self, queue: list[TrackMetadata], session: SessionContext, metrics: QueueMetrics) -> str:
    if not queue:
      return "No tracks were available."

    first = queue[0]
    diversity = self._format_ratio(metrics.diversity_score)
    return (
      f"Starting with {first.name} by {first.artist_name}. "
      f"That fits your {session.activity} mode and keeps diversity at about {diversity}."
    )

  def _first_tempo(self, track: TrackMetadata) -> float:
    if track.audio_features is not None:
      return track.audio_features.tempo
    return 110.0

  def _format_ratio(self, value: float | None) -> str:
    if value is None:
      return "unknown"
    return f"{max(0, min(100, round(value * 100)))}%"

