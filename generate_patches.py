import json
import base64

test_code = """import pytest
from backend.models import TrackMetadata, SessionContext, PreferenceHints
from backend.queue_manager import AdaptiveQueueManager

def test_track_metadata_popularity_type():
    track = TrackMetadata(
        id="1", uri="uri", name="name", artist_id="a1", artist_name="artist",
        album_name="album", duration_ms=100
    )
    assert isinstance(track.popularity, float)
    assert track.popularity == 0.0

def test_queue_manager_preference_score():
    track = TrackMetadata(
        id="1", uri="uri", name="name", artist_id="a1", artist_name="artist",
        album_name="album", duration_ms=100, popularity=0.5
    )
    session = SessionContext(time_of_day="morning", activity="workout", energy=0.8)
    hints = PreferenceHints()
    manager = AdaptiveQueueManager()
    
    score = manager._preference_score(track, session, hints)
    # The popularity_bias should be 0.5 / 4.0 = 0.125
    # The tempo fallback should be 100.0 + (0.5 * 60.0) = 130.0
    # The energy fallback should be 0.5
    assert score > 0.0
"""

solution_code_models = """@@ -35,7 +35,7 @@
   artist_name: str
   album_name: str
   duration_ms: int
-  popularity: int = 50
+  popularity: float = 0.0
   added_at: datetime | None = None
   last_played_at: datetime | None = None
   genres: list[str] = Field(default_factory=list)
"""

solution_code_queue = """@@ -289,8 +289,8 @@
 
   def _preference_score(self, track: TrackMetadata, session: SessionContext, hints: PreferenceHints) -> float:
     features = track.audio_features
-    tempo = features.tempo if features is not None else 100.0 + (track.popularity * 0.6)
-    energy = features.energy if features is not None else clamp(track.popularity / 100.0)
+    tempo = features.tempo if features is not None else 100.0 + (track.popularity * 60.0)
+    energy = features.energy if features is not None else clamp(track.popularity)
     target_tempo = self._target_tempo(session.activity)
     tempo_fit = 1.0 - min(1.0, abs(tempo - target_tempo) / 140.0)
     energy_fit = 1.0 - min(1.0, abs(energy - session.energy))
@@ -309,7 +309,7 @@
       if keyword in lowered_name or keyword in lowered_artist:
         hint_bonus += 0.03
 
-    popularity_bias = track.popularity / 400.0
+    popularity_bias = track.popularity / 4.0
     score = 0.48 * tempo_fit + 0.42 * energy_fit + popularity_bias + hint_bonus
     return clamp(score)
"""

test_patch = f"""diff --git a/backend/tests/test_popularity_unification.py b/backend/tests/test_popularity_unification.py
new file mode 100644
index 0000000..1111111
--- /dev/null
+++ b/backend/tests/test_popularity_unification.py
@@ -0,0 +1,25 @@
{chr(10).join(['+' + line for line in test_code.split(chr(10))])}"""

solution_patch = f"""diff --git a/backend/models.py b/backend/models.py
--- a/backend/models.py
+++ b/backend/models.py
{solution_code_models}
diff --git a/backend/queue_manager.py b/backend/queue_manager.py
--- a/backend/queue_manager.py
+++ b/backend/queue_manager.py
{solution_code_queue}"""

config = {
    "base_commit": "21a1600a8093604341aa192aff48dea8ba3d57a7",
    "fail_to_pass": [
        "test_popularity_unification.test_track_metadata_popularity_type",
        "test_popularity_unification.test_queue_manager_preference_score"
    ],
    "pass_to_pass": [],
    "test_patch": test_patch,
    "selected_test_files_to_run": "backend/tests/test_popularity_unification.py"
}

with open("my-task/tests/config.json", "w") as f:
    json.dump(config, f, indent=2)

with open("my-task/solution/solve.sh", "w") as f:
    f.write("#!/bin/bash\\ncat << 'EOF' | git apply -\\n" + solution_patch + "\\nEOF\\n")
