#!/bin/bash
cat << 'EOF' | git apply -
diff --git a/backend/models.py b/backend/models.py
--- a/backend/models.py
+++ b/backend/models.py
@@ -35,7 +35,7 @@
   artist_name: str
   album_name: str
   duration_ms: int
-  popularity: int = 50
+  popularity: float = 0.0
   added_at: datetime | None = None
   last_played_at: datetime | None = None
   genres: list[str] = Field(default_factory=list)
diff --git a/backend/queue_manager.py b/backend/queue_manager.py
--- a/backend/queue_manager.py
+++ b/backend/queue_manager.py
@@ -289,8 +289,8 @@
 
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
EOF