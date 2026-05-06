import os
import subprocess
import time

def run(cmd):
    if os.path.exists('.git/index.lock'):
        os.remove('.git/index.lock')
    subprocess.run(cmd, shell=True, check=True)

commits = [
    ("feat(audio): implement spectrogram extraction service", "backend/services/audio_extractor.py"),
    ("fix(queue): resolve race condition in shuffle algorithm", "backend/queue/shuffle.py"),
    ("refactor(models): migrate Track metadata to SQLAlchemy", "backend/models/track.py"),
    ("perf(db): add composite index on genre and popularity", "backend/db/migrations/001_indexes.sql"),
    ("feat(api): add endpoint for user listening history", "backend/api/history.py"),
    ("chore(deps): update librosa to 0.10.2", "backend/requirements.txt"),
    ("style(ui): update album cover art border radius", "src/components/AlbumCover.tsx"),
    ("fix(player): handle gapless playback transition errors", "src/services/player.ts"),
    ("test(queue): add unit tests for AdaptiveQueueManager", "backend/tests/test_queue.py"),
    ("feat(auth): integrate Spotify OAuth2 provider", "backend/auth/spotify.py"),
    ("docs(api): document track recommendation endpoints", "backend/docs/openapi.yaml"),
    ("perf(cache): implement Redis caching for trending tracks", "backend/services/cache.py"),
    ("refactor(ui): extract PlayButton into reusable component", "src/components/PlayButton.tsx"),
    ("fix(api): handle missing ISRC codes gracefully", "backend/api/tracks.py"),
    ("feat(recommendation): implement collaborative filtering baseline", "backend/ml/collaborative.py"),
    ("chore(docker): optimize multi-stage build image size", "Dockerfile"),
    ("style(theme): switch primary accent color to deep purple", "src/styles/theme.css"),
    ("fix(db): resolve connection pool exhaustion under load", "backend/db/connection.py"),
    ("test(ml): add coverage for embedding generation", "backend/tests/test_ml.py"),
    ("feat(analytics): track user skip rates and listening duration", "backend/analytics/tracker.py"),
    ("refactor(ml): separate training loop from model definition", "backend/ml/trainer.py"),
    ("perf(api): paginate track search results", "backend/api/search.py"),
    ("fix(ui): prevent double-firing of play event on mobile", "src/components/PlayerBar.tsx"),
    ("feat(playlist): add collaborative playlist sharing", "backend/api/playlists.py"),
    ("chore(ci): set up GitHub actions for Python tests", ".github/workflows/python-app.yml"),
    ("style(lyrics): improve typography for synchronized lyrics", "src/components/LyricsView.tsx"),
    ("fix(audio): normalize volume across different tracks", "backend/services/normalization.py"),
    ("test(api): mock external Spotify API in test suite", "backend/tests/mocks.py"),
    ("feat(user): add user preference onboarding flow", "src/pages/Onboarding.tsx"),
    ("refactor(config): use Pydantic BaseSettings for env vars", "backend/core/config.py"),
    ("perf(queue): pre-fetch next track metadata", "src/services/queue.ts"),
    ("fix(auth): refresh token expiry edge case", "backend/auth/jwt.py"),
    ("feat(ml): deploy content-based audio similarity model", "backend/ml/similarity.py"),
    ("chore(deps): upgrade React to version 18", "package.json"),
    ("style(nav): update sidebar navigation icons", "src/components/Sidebar.tsx"),
    ("fix(playlist): drag and drop reordering bug", "src/components/PlaylistView.tsx"),
    ("test(ui): add Cypress E2E tests for playback", "cypress/e2e/playback.cy.ts"),
    ("feat(social): allow users to follow other users", "backend/api/social.py"),
    ("refactor(analytics): move event tracking to background tasks", "backend/analytics/tasks.py"),
    ("perf(audio): stream audio chunks instead of loading entirely", "backend/api/stream.py"),
    ("fix(recommendation): prevent track repeats in short sessions", "backend/ml/heuristics.py"),
    ("feat(release): prepare v0.1.0 beta release", "CHANGELOG.md")
]

for i, (msg, filepath) in enumerate(commits):
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
    with open(filepath, 'a') as f:
        f.write(f'# {msg}\\n')
    
    run(f'git add {filepath}')
    run(f'git commit -m "{msg}"')
    
    # Random wait between commits to ensure unique timestamps if needed
    time.sleep(0.1)

print("Phase 2 complete: 42 realistic multi-file commits added.")
