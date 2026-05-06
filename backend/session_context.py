from __future__ import annotations

from datetime import datetime, timezone

from .models import SessionContext


class SessionContextEngine:
  def time_of_day(self, moment: datetime | None = None) -> str:
    instant = moment or datetime.now(timezone.utc)
    local = instant.astimezone()
    hour = local.hour
    if 5 <= hour < 11:
      return "morning"
    if 11 <= hour < 16:
      return "afternoon"
    if 16 <= hour < 21:
      return "evening"
    return "night"

  def default_activity(self, time_of_day: str) -> str:
    return {
      "morning": "focus",
      "afternoon": "work",
      "evening": "browse",
      "night": "relax"
    }.get(time_of_day, "browse")

  def default_energy(self, time_of_day: str) -> float:
    return {
      "morning": 0.62,
      "afternoon": 0.68,
      "evening": 0.54,
      "night": 0.34
    }.get(time_of_day, 0.5)

  def derive(self, *, activity: str | None = None, energy: float | None = None, moment: datetime | None = None) -> SessionContext:
    time_of_day = self.time_of_day(moment)
    return SessionContext(
      time_of_day=time_of_day,
      activity=activity or self.default_activity(time_of_day),
      energy=self._clamp(energy if energy is not None else self.default_energy(time_of_day))
    )

  def apply_patch(self, session: SessionContext, *, time_of_day: str | None = None, activity: str | None = None, energy: float | None = None) -> SessionContext:
    next_time_of_day = time_of_day or session.time_of_day
    next_activity = activity or session.activity
    next_energy = self._clamp(energy if energy is not None else session.energy)
    return SessionContext(time_of_day=next_time_of_day, activity=next_activity, energy=next_energy)

  def _clamp(self, value: float) -> float:
    return max(0.0, min(1.0, float(value)))

