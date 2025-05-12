from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .schemas import TranslationRequest, TranslationResponse


def _preserve_case(source: str, translated: str) -> str:
  if source.isupper():
    return translated.upper()
  if source[:1].isupper():
    return translated[:1].upper() + translated[1:]
  return translated


@dataclass(slots=True)
class LanguageEngine:
  aliases: dict[str, str] = field(default_factory=lambda: {
    "english": "en",
    "en": "en",
    "spanish": "es",
    "es": "es",
    "french": "fr",
    "fr": "fr",
    "swahili": "sw",
    "kiswahili": "sw",
    "sw": "sw",
    "german": "de",
    "de": "de",
    "italian": "it",
    "it": "it",
    "portuguese": "pt",
    "pt": "pt"
  })
  translation_keywords: tuple[str, ...] = ("translate", "translation", "translator", "say in", "speak in")
  music_keywords: tuple[str, ...] = ("play", "queue", "shuffle", "song", "track", "music", "podcast", "dj")
  phrasebooks: dict[tuple[str, str], dict[str, str]] = field(default_factory=dict)

  def __post_init__(self) -> None:
    if not self.phrasebooks:
      self.phrasebooks = self._build_phrasebooks()

  def normalize_language(self, value: str | None, default: str = "en") -> str:
    if not value:
      return default
    normalized = value.strip().lower()
    return self.aliases.get(normalized, normalized)

  def detect_language(self, text: str) -> str:
    lowered = text.lower()
    scores = {
      "en": self._score_language(lowered, {"the", "and", "please", "music", "play", "translate"}),
      "es": self._score_language(lowered, {"hola", "por", "favor", "gracias", "música", "reproducir"}),
      "fr": self._score_language(lowered, {"bonjour", "merci", "musique", "joue", "s'il"}),
      "sw": self._score_language(lowered, {"habari", "tafadhali", "asante", "muziki", "cheza"})
    }
    return max(scores.items(), key=lambda item: item[1])[0]

  def is_translation_request(self, text: str) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in self.translation_keywords)

  def is_music_request(self, text: str) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in self.music_keywords)

  def extract_target_language(self, text: str, default: str = "en") -> str:
    lowered = text.lower()
    for alias, normalized in self.aliases.items():
      if re.search(rf"\b(?:to|into|in)\s+{re.escape(alias)}\b", lowered):
        return normalized
    return default

  async def translate(self, request: TranslationRequest) -> TranslationResponse:
    return self.translate_text(
      request.text,
      source_lang=request.source_lang,
      target_lang=request.target_lang,
      user_id=request.user_id,
      voice=request.voice
    )

  def translate_text(
    self,
    text: str,
    *,
    source_lang: str | None = None,
    target_lang: str | None = None,
    user_id: str = "default",
    voice: bool = True
  ) -> TranslationResponse:
    source = self.normalize_language(source_lang or self.detect_language(text))
    target = self.normalize_language(target_lang or "en")
    if target == "en" and self.is_translation_request(text):
      candidate = self.extract_target_language(text, target)
      target = candidate or target

    if source == target:
      voice_line = f"The text is already in {target}."
      return TranslationResponse(
        user_id=user_id,
        source_lang=source,
        target_lang=target,
        detected_lang=source,
        original_text=text,
        translated_text=text,
        confidence=1.0,
        voice_line=voice_line if voice else ""
      )

    translated_text, confidence = self._translate_tokens(text, source, target)
    voice_line = f"Translated from {source} to {target}: {translated_text}"
    return TranslationResponse(
      user_id=user_id,
      source_lang=source,
      target_lang=target,
      detected_lang=source,
      original_text=text,
      translated_text=translated_text,
      confidence=confidence,
      voice_line=voice_line if voice else ""
    )

  def _translate_tokens(self, text: str, source: str, target: str) -> tuple[str, float]:
    dictionary = self.phrasebooks.get((source, target), {})
    if not dictionary:
      return f"[{target}] {text}", 0.12

    translated = text
    translated_count = 0
    for word, replacement in sorted(dictionary.items(), key=lambda item: len(item[0]), reverse=True):
      pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)

      def _replace(match: re.Match[str]) -> str:
        nonlocal translated_count
        translated_count += 1
        return _preserve_case(match.group(0), replacement)

      translated = pattern.sub(_replace, translated)

    confidence = min(1.0, 0.4 + (translated_count / max(1, len(dictionary))) * 0.6)
    return translated, round(confidence, 3)

  def _score_language(self, text: str, terms: set[str]) -> int:
    return sum(1 for term in terms if term in text)

  def _build_phrasebooks(self) -> dict[tuple[str, str], dict[str, str]]:
    return {
      ("en", "es"): {
        "hello": "hola",
        "please": "por favor",
        "thanks": "gracias",
        "music": "música",
        "play": "reproducir",
        "message": "mensaje",
        "translate": "traducir",
        "calm": "tranquilo",
        "drive": "conducir",
        "work": "trabajo"
      },
      ("es", "en"): {
        "hola": "hello",
        "por favor": "please",
        "gracias": "thanks",
        "música": "music",
        "reproducir": "play",
        "mensaje": "message",
        "traducir": "translate",
        "tranquilo": "calm",
        "conducir": "drive",
        "trabajo": "work"
      },
      ("en", "fr"): {
        "hello": "bonjour",
        "please": "s'il vous plaît",
        "thanks": "merci",
        "music": "musique",
        "play": "jouer",
        "message": "message",
        "translate": "traduire",
        "calm": "calme"
      },
      ("fr", "en"): {
        "bonjour": "hello",
        "s'il vous plaît": "please",
        "merci": "thanks",
        "musique": "music",
        "jouer": "play",
        "message": "message",
        "traduire": "translate",
        "calme": "calm"
      },
      ("en", "sw"): {
        "hello": "habari",
        "please": "tafadhali",
        "thanks": "asante",
        "music": "muziki",
        "play": "cheza",
        "message": "ujumbe",
        "translate": "tafsiri",
        "calm": "tulivu",
        "drive": "endesha",
        "work": "kazi"
      },
      ("sw", "en"): {
        "habari": "hello",
        "tafadhali": "please",
        "asante": "thanks",
        "muziki": "music",
        "cheza": "play",
        "ujumbe": "message",
        "tafsiri": "translate",
        "tulivu": "calm",
        "endesha": "drive",
        "kazi": "work"
      }
    }

