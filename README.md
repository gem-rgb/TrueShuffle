# TrueShuffle

TrueShuffle is a cross-platform desktop app that replaces Spotify's default shuffle with a custom queue builder that:

- avoids immediate artist repetition
- spreads artists across the queue
- penalizes recently played tracks
- keeps a local preview queue for inspection
- adapts to session context, feedback, embeddings, and graph discovery
- learns across Spotify, YouTube Music, Apple Music, and podcasts
- generates a unified AI playlist with live backend status feedback in the UI

## Stack

- React + TypeScript frontend
- Tauri 1 backend in Rust
- FastAPI adaptive and cross-platform AI service in Python
- Spotify Web API for playlists, queueing, and playback

## What is implemented

- Spotify OAuth PKCE flow in Rust
- playlist and track fetch commands
- weighted shuffle engine with artist spacing and recency bias
- queue snapshot events from Rust to the UI
- demo fallback data so the app is still usable before Spotify credentials are configured
- FastAPI adaptive recommendation service with reinforcement learning, audio features, graph traversal, embeddings, voice narration, and simulation
- cross-platform connectors, preference learning, playlist generation, async sync, Redis cache, and PostgreSQL storage scaffolding
- unified assistant stack with device context, Bluetooth/Wi-Fi/USB/CarPlay/Android Auto connectivity, translation, voice narration, edge recommendation, and optional cloud forwarding
- browser-side fallback logic when the Python service is offline

## Run locally

1. Create a Spotify app in the Spotify Developer Dashboard.
2. Add `http://127.0.0.1:17171/callback` as a redirect URI.
3. Copy `.env.example` to `.env` and set `SPOTIFY_CLIENT_ID`.
4. Install dependencies:
   - `npm install`
   - `cargo` and `rustc` must be available for the Tauri backend
   - `python -m pip install -r backend/requirements.txt` for the adaptive AI service
5. Start the app:
   - `npm run tauri:dev`
   - the Tauri shell auto-launches the Python AI service on startup when Python and the backend dependencies are installed

If you want to run the AI service manually, use `npm run backend:dev`.

If no Spotify session is available, the app stays in demo mode and uses mock playlists. If the Python backend is unavailable, the frontend falls back to local adaptive scoring.

## Environment

- `SPOTIFY_CLIENT_ID`
- `SPOTIFY_CLIENT_SECRET` optional
- `SPOTIFY_REDIRECT_URI` defaults to `http://127.0.0.1:17171/callback`
- `SPOTIFY_SCOPES` defaults to the playback and playlist scopes needed by TrueShuffle
- `TRUESHUFFLE_DEMO_MODE=1` forces demo-only behavior
- `VITE_TRUESHUFFLE_AI_API_URL=http://127.0.0.1:8000` points the frontend at the local FastAPI service
- `TRUESHUFFLE_AI_AUTO_LAUNCH=0` disables desktop auto-launch of the Python AI service
- `TRUESHUFFLE_AI_PYTHON=python` overrides the Python executable used by the launcher
- `TRUESHUFFLE_AI_HOST=127.0.0.1` and `TRUESHUFFLE_AI_PORT=8000` configure the AI service bind address
- `TRUESHUFFLE_CLOUD_AI_URL=http://127.0.0.1:8000` optionally points the assistant cloud mirror at another TrueShuffle instance
- `REDIS_URL=redis://127.0.0.1:6379/0` enables Redis caching when available
- `DATABASE_URL=postgresql://user:pass@127.0.0.1:5432/trueshuffle` enables PostgreSQL storage when available

## Project layout

- `src/` React frontend
- `src-tauri/` Rust backend and Tauri config
- `backend/` FastAPI adaptive recommendation and cross-platform learning service
- `backend/assistant/` unified assistant, connectivity, data ingestion, edge/cloud routing, and translation layers

## Assistant API

- `GET /assistant/health`
- `GET /assistant/connectivity`
- `POST /assistant/connect/{transport}`
- `POST /assistant/context`
- `POST /assistant/recommend`
- `POST /assistant/translate`
- `POST /assistant/command`
- `POST /assistant/feedback`
- `POST /assistant/sync/pull`
- `POST /assistant/sync/push`
- `POST /assistant/profile`
- `POST /assistant/history`

## Notes

- The Rust backend stores tokens through the OS keyring when available.
- Spotify's playback queue API is incremental, so long playlists are queued progressively.
- The app can be previewed in a normal browser, but the real command bridge only activates inside Tauri.
- The Python service can be run independently for simulation, feature extraction, and adaptive queue generation.
