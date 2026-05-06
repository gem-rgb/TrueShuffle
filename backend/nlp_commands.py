from __future__ import annotations

import re

from .models import PreferenceHints, SessionContext
from .session_context import SessionContextEngine


class CommandParser:
  def __init__(self) -> None:
    self.session_engine = SessionContextEngine()

  def parse(self, text: str, session: SessionContext) -> tuple[SessionContext, PreferenceHints, str, str]:
    normalized = text.strip().lower()
    if not normalized:
      explanation = "No command was provided. I kept the current session context."
      return session, PreferenceHints(), "general", explanation

    parsed_session = session
    intent = "general"
    genre_hints: list[str] = []
    artist_hints: list[str] = []
    keywords: list[str] = []

    activity_map = {
      "focus": ("focus", 0.35),
      "study": ("focus", 0.35),
      "work": ("work", 0.6),
      "workout": ("workout", 0.88),
      "gym": ("workout", 0.9),
      "run": ("workout", 0.88),
      "drive": ("drive", 0.72),
      "commute": ("drive", 0.66),
      "relax": ("relax", 0.28),
      "chill": ("relax", 0.32),
      "sleep": ("relax", 0.18),
      "party": ("party", 0.92),
      "dance": ("party", 0.92)
    }

    for keyword, (activity, energy) in activity_map.items():
      if keyword in normalized:
        parsed_session = self.session_engine.apply_patch(session, activity=activity, energy=energy)
        intent = activity
        keywords.append(keyword)
        break

    if "morning" in normalized:
      parsed_session = self.session_engine.apply_patch(parsed_session, time_of_day="morning")
      keywords.append("morning")
    elif "afternoon" in normalized:
      parsed_session = self.session_engine.apply_patch(parsed_session, time_of_day="afternoon")
      keywords.append("afternoon")
    elif "evening" in normalized:
      parsed_session = self.session_engine.apply_patch(parsed_session, time_of_day="evening")
      keywords.append("evening")
    elif "night" in normalized:
      parsed_session = self.session_engine.apply_patch(parsed_session, time_of_day="night")
      keywords.append("night")

    explicit_energy = self._extract_energy(normalized)
    if explicit_energy is not None:
      parsed_session = self.session_engine.apply_patch(parsed_session, energy=explicit_energy)
      keywords.append("energy")

    genre_map = {
      "synth": "synthwave",
      "electronic": "electronic",
      "ambient": "ambient",
      "dance": "dance",
      "house": "house",
      "indie": "indie",
      "pop": "pop",
      "jazz": "jazz",
      "acoustic": "acoustic",
      "lofi": "lo-fi"
    }
    for keyword, genre in genre_map.items():
      if keyword in normalized:
        genre_hints.append(genre)
        keywords.append(keyword)

    artist_match = re.search(r"more like ([a-z0-9\s'&-]{2,})", normalized)
    if artist_match:
      artist_hints.append(artist_match.group(1).strip())
      keywords.append("artist")

    explanation = self._build_explanation(intent, parsed_session, genre_hints, explicit_energy, keywords)
    voice_line = self._build_voice_line(intent, parsed_session, genre_hints)

    hints = PreferenceHints(
      genre_hints=self._unique(genre_hints),
      artist_hints=self._unique(artist_hints),
      keywords=self._unique(keywords)
    )
    return parsed_session, hints, intent, f"{explanation} {voice_line}"

  def _extract_energy(self, text: str) -> float | None:
    match = re.search(r"(\d{1,3}(?:\.\d+)?)\s*%", text)
    if match:
      value = float(match.group(1)) / 100.0
      return max(0.0, min(1.0, value))

    match = re.search(r"energy\s*(?:to|at|around)?\s*(\d{1,3}(?:\.\d+)?)", text)
    if match:
      value = float(match.group(1))
      if value > 1.0:
        value /= 100.0
      return max(0.0, min(1.0, value))

    if "higher energy" in text or "more energy" in text or "upbeat" in text:
      return 0.82
    if "lower energy" in text or "slower" in text or "calm" in text:
      return 0.28
    return None

  def _build_explanation(
    self,
    intent: str,
    session: SessionContext,
    genre_hints: list[str],
    explicit_energy: float | None,
    keywords: list[str]
  ) -> str:
    pieces = [f"Interpreted the command as {intent} mode."]
    if genre_hints:
      pieces.append(f"Genre hints: {', '.join(self._unique(genre_hints[:3]))}.")
    if explicit_energy is not None:
      pieces.append(f"Target energy updated to {round(explicit_energy * 100)}%.")
    pieces.append(f"Session set to {session.time_of_day} listening with {round(session.energy * 100)}% energy.")
    if keywords:
      pieces.append(f"Matched keywords: {', '.join(self._unique(keywords[:4]))}.")
    return " ".join(pieces)

  def _build_voice_line(self, intent: str, session: SessionContext, genre_hints: list[str]) -> str:
    flavor = f" with a {', '.join(self._unique(genre_hints[:2]))} bias" if genre_hints else ""
    return f"Okay. I am shifting the queue toward {intent} mode{flavor} for your {session.time_of_day} session."

  def _unique(self, values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))

