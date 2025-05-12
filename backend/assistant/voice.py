from __future__ import annotations

from dataclasses import dataclass

from .schemas import AssistantCommandResponse, AssistantRecommendationResponse, TranslationResponse


@dataclass(slots=True)
class VoiceEngine:
  default_voice: str = "assistant"

  def synthesize(self, text: str) -> bytes:
    return text.encode("utf-8")

  def narrate_recommendation(self, response: AssistantRecommendationResponse) -> str:
    if response.voice_line:
      return response.voice_line
    if response.explanation:
      return response.explanation
    return "I built the next playlist."

  def narrate_translation(self, response: TranslationResponse) -> str:
    if response.voice_line:
      return response.voice_line
    return f"Translated text: {response.translated_text}"

  def narrate_command(self, response: AssistantCommandResponse) -> str:
    if response.voice_line:
      return response.voice_line
    if response.recommendation is not None:
      return self.narrate_recommendation(response.recommendation)
    if response.translation is not None:
      return self.narrate_translation(response.translation)
    return "Command handled."

