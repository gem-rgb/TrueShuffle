from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping

from ..models import SessionContext
from ..session_context import SessionContextEngine
from .schemas import DeviceContext


@dataclass(slots=True)
class ContextEngine:
  session_engine: SessionContextEngine = field(default_factory=SessionContextEngine)
  state: DeviceContext = field(default_factory=DeviceContext)
  history: list[DeviceContext] = field(default_factory=list)

  def merge(self, context: DeviceContext | Mapping[str, Any] | None = None) -> DeviceContext:
    if context is None:
      self._ensure_time_context()
      return self.state.model_copy(deep=True)

    incoming = context if isinstance(context, DeviceContext) else DeviceContext.model_validate(dict(context))
    merged_preferences = dict(self.state.preferences)
    merged_preferences.update(incoming.preferences)
    merged_metadata = dict(self.state.metadata)
    merged_metadata.update(incoming.metadata)
    self.state = self.state.model_copy(
      update={
        "user_id": incoming.user_id or self.state.user_id,
        "location": incoming.location if incoming.location is not None else self.state.location,
        "activity": incoming.activity or self.state.activity,
        "time_of_day": incoming.time_of_day if incoming.time_of_day != "unknown" else self.state.time_of_day,
        "energy": self._clamp(incoming.energy if incoming.energy is not None else self.state.energy),
        "online": incoming.online or self.state.online,
        "driving": incoming.driving or self.state.driving,
        "transport": incoming.transport,
        "language": incoming.language or self.state.language,
        "target_language": incoming.target_language or self.state.target_language,
        "preferences": merged_preferences,
        "metadata": merged_metadata
      }
    )
    self._ensure_time_context()
    self.history.append(self.state.model_copy(deep=True))
    if len(self.history) > 256:
      self.history = self.history[-256:]
    return self.state.model_copy(deep=True)

  def apply_transport(self, transport: str, *, online: bool | None = None, driving: bool | None = None) -> DeviceContext:
    updates = {
      "transport": transport,
      "online": online if online is not None else transport in {"wifi", "usb", "android_auto", "apple_carplay"},
      "driving": driving if driving is not None else transport in {"android_auto", "apple_carplay"},
      "activity": "drive" if transport in {"android_auto", "apple_carplay"} else self.state.activity
    }
    self.state = self.state.model_copy(update=updates)
    self._ensure_time_context()
    self.history.append(self.state.model_copy(deep=True))
    return self.state.model_copy(deep=True)

  def apply_session(self, session: SessionContext) -> DeviceContext:
    self.state = self.state.model_copy(
      update={
        "time_of_day": session.time_of_day,
        "activity": session.activity,
        "energy": self._clamp(session.energy)
      }
    )
    self._ensure_time_context()
    return self.state.model_copy(deep=True)

  def to_session(self, context: DeviceContext | None = None) -> SessionContext:
    current = self.merge(context)
    return self.session_engine.apply_patch(
      self.session_engine.derive(moment=datetime.now(timezone.utc), activity=current.activity, energy=current.energy),
      time_of_day=current.time_of_day,
      activity=current.activity,
      energy=current.energy
    )

  def mode(self) -> str:
    if not self.state.online:
      return "edge"
    return "hybrid"

  def snapshot(self) -> DeviceContext:
    return self.state.model_copy(deep=True)

  def _ensure_time_context(self) -> None:
    if self.state.time_of_day == "unknown":
      self.state = self.state.model_copy(
        update={
          "time_of_day": self.session_engine.time_of_day(datetime.now(timezone.utc))
        }
      )
    if self.state.activity == "idle":
      default_activity = self.session_engine.default_activity(self.state.time_of_day)
      self.state = self.state.model_copy(update={"activity": default_activity})
    if self.state.energy <= 0.0:
      self.state = self.state.model_copy(
        update={
          "energy": self.session_engine.default_energy(self.state.time_of_day)
        }
      )

  def _clamp(self, value: float) -> float:
    return max(0.0, min(1.0, float(value)))
