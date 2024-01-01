# Unify Track Popularity Scaling

The TrueShuffle backend currently has a type and scaling mismatch in how track popularity is represented. 
In the `UnifiedTrack` model, `popularity` is scaled as a `float` bounded between `0.0` and `1.0`. However, in `TrackMetadata`, `popularity` is still defined as an `int` with a default of `50` (representing a `0` to `100` scale).

This mismatch causes scaling issues in the `AdaptiveQueueManager`. Specifically, when the queue manager uses `track.popularity` as a fallback for calculating preference scores (such as tempo approximations, energy approximations, and the general popularity bias), the mathematical formulas implicitly assume it is still on the `0` to `100` scale. This leads to wildly incorrect heuristic scoring when it receives a normalized float.

Your task is to unify `popularity` to be a normalized `float` between `0.0` and `1.0` in the `TrackMetadata` model, and update the queue manager's fallback calculation logic so that the resulting scores and approximate values (like tempo and energy) remain mathematically identical to what they were before the normalization.

## Requirements
* `TrackMetadata` must use a normalized float for `popularity`.
* The `_preference_score` logic in `AdaptiveQueueManager` must properly scale the new normalized float so that the resulting `tempo`, `energy`, and `popularity_bias` fallback values are mathematically identical to the original `0-100` scale logic.
* Do not modify the `UnifiedTrack` model.
