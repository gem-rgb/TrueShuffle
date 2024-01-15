# Root Cause Analysis

The `TrackMetadata` model defines `popularity` as an `int` defaulting to `50`, scaled `0–100`. The `UnifiedTrack` model defines `popularity` as a `float` defaulting to `0.0`, scaled `0.0–1.0`. This inconsistency is harmless as long as only one model is used at a time, but `AdaptiveQueueManager._preference_score()` operates on `TrackMetadata` and uses `track.popularity` in three fallback expressions that implicitly assume the `0–100` integer scale:

- **Tempo fallback**: `100.0 + (track.popularity * 0.6)` — with a `0.0–1.0` float this yields at most `100.6` instead of the intended `100–160` range.
- **Energy fallback**: `clamp(track.popularity / 100.0)` — with a `0.0–1.0` float this collapses to near-zero.
- **Popularity bias**: `track.popularity / 400.0` — with a `0.0–1.0` float this becomes negligible.

The fix requires changing `TrackMetadata.popularity` to `float` with a `0.0` default, then adjusting each of the three formulas so they produce the same value ranges as before.

# Why This Task Is Fair and Hard

The task is **fair** because the instruction clearly describes the type mismatch and states that formulas must remain mathematically equivalent. No insider knowledge is required.

The task is **genuinely difficult** because:
1. The agent must locate the three specific formula sites in `_preference_score` and reason about the algebra of rescaling each one independently.
2. A naive fix (just changing the type) will make tests pass for the type check but fail for the preference score test, requiring the agent to trace through the scoring logic.
3. The formulas are in different parts of the method, separated by other logic.

# Test Plan

- `test_unified_track_popularity_type` (pass_to_pass): Confirms `UnifiedTrack.popularity` remains a float. Already passes at `base_commit`.
- `test_track_metadata_popularity_type` (fail_to_pass): Asserts `TrackMetadata.popularity` is a `float` with default `0.0`. Fails at `base_commit` because it's currently `int = 50`.
- `test_queue_manager_preference_score` (fail_to_pass): Creates a track with `popularity=0.5` and checks `_preference_score` returns a positive value. Fails at `base_commit` because Pydantic rejects `0.5` for an `int` field (or if coerced, the scoring math breaks).
