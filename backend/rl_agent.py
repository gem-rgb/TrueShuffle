from __future__ import annotations

import hashlib
import json
import random
from collections import defaultdict
from typing import Any, Mapping


class RLAgent:
  def __init__(self, *, learning_rate: float = 0.28, epsilon: float = 0.12, seed: int | None = None) -> None:
    self.learning_rate = learning_rate
    self.epsilon = epsilon
    self._rng = random.Random(seed)
    self._q_table: dict[str, dict[str, float]] = defaultdict(dict)
    self._update_count = 0
    self._reward_total = 0.0

  def choose_action(self, state: Mapping[str, Any]) -> str | None:
    actions = [str(action) for action in state.get("actions", []) if action is not None]
    if not actions:
      return None

    if self._rng.random() < self.epsilon:
      return self._rng.choice(actions)

    state_key = self._state_key(state)
    q_values = self._q_table.get(state_key, {})
    return max(actions, key=lambda action: (q_values.get(action, 0.0), -actions.index(action)))

  def update(self, state: Mapping[str, Any], action: str, reward: float) -> None:
    state_key = self._state_key(state)
    q_values = self._q_table[state_key]
    current = q_values.get(action, 0.0)
    q_values[action] = current + self.learning_rate * (reward - current)
    self._update_count += 1
    self._reward_total += reward

  def q_value(self, state: Mapping[str, Any], action: str) -> float:
    state_key = self._state_key(state)
    return self._q_table.get(state_key, {}).get(action, 0.0)

  def confidence(self) -> float:
    if self._update_count <= 0:
      return 0.0
    exploration_penalty = max(0.0, 1.0 - self.epsilon)
    learning_progress = min(1.0, self._update_count / 24.0)
    return round(exploration_penalty * learning_progress, 3)

  def average_reward(self) -> float:
    if self._update_count <= 0:
      return 0.0
    return round(self._reward_total / self._update_count, 3)

  def _state_key(self, state: Mapping[str, Any]) -> str:
    payload = json.dumps(state, sort_keys=True, default=str)
    digest = hashlib.blake2b(payload.encode("utf-8"), digest_size=12).hexdigest()
    return digest

