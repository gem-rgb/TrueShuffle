import json

test_code = """import pytest
from backend.models import TrackMetadata, UnifiedTrack, SessionContext, PreferenceHints
from backend.queue_manager import AdaptiveQueueManager

def test_unified_track_popularity_type():
    track = UnifiedTrack(id="1", title="title", artist="artist", source="spotify")
    assert isinstance(track.popularity, float)
    assert track.popularity == 0.0

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
    assert score > 0.0
"""

test_patch = f"""diff --git a/backend/tests/test_popularity_unification.py b/backend/tests/test_popularity_unification.py
new file mode 100644
index 0000000..1111111
--- /dev/null
+++ b/backend/tests/test_popularity_unification.py
@@ -0,0 +1,29 @@
{chr(10).join(['+' + line for line in test_code.split(chr(10))])}"""

with open("my-task/tests/config.json", "r") as f:
    config = json.load(f)

config["test_patch"] = test_patch
config["pass_to_pass"] = [
    "test_popularity_unification.test_unified_track_popularity_type"
]

with open("my-task/tests/config.json", "w") as f:
    json.dump(config, f, indent=2)
