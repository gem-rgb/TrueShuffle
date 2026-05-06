import type { PlaybackState, Track } from "../types";
import { formatDuration } from "../utils";

interface PlayerBarProps {
  playback: PlaybackState;
  currentTrack: Track | null;
  onPlay: () => void;
  onPause: () => void;
  busy: boolean;
}

export function PlayerBar({ playback, currentTrack, onPlay, onPause, busy }: PlayerBarProps) {
  const progress = currentTrack
    ? Math.min(100, Math.round((playback.progressMs / Math.max(1, currentTrack.durationMs)) * 100))
    : 0;

  return (
    <footer className="player-bar" id="player-bar">
      <div className="player-bar-progress">
        <span className="player-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      <div className="player-bar-content">
        <div className="player-bar-track">
          {currentTrack ? (
            <>
              <strong>{currentTrack.name}</strong>
              <span>
                {currentTrack.artistName} | {currentTrack.albumName}
              </span>
            </>
          ) : (
            <span className="muted">No track loaded</span>
          )}
        </div>

        <div className="player-bar-controls">
          <button
            type="button"
            className="player-btn"
            disabled={busy || !currentTrack}
            onClick={playback.isPlaying ? onPause : onPlay}
            aria-label={playback.isPlaying ? "Pause" : "Play"}
          >
            {playback.isPlaying ? (
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <rect x="4" y="3" width="4" height="14" rx="1" />
                <rect x="12" y="3" width="4" height="14" rx="1" />
              </svg>
            ) : (
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path d="M5 3.5L16 10L5 16.5V3.5Z" />
              </svg>
            )}
          </button>
        </div>

        <div className="player-bar-time">
          {currentTrack ? (
            <span>
              {formatDuration(playback.progressMs)} / {formatDuration(currentTrack.durationMs)}
            </span>
          ) : (
            <span className="muted">--:--</span>
          )}
        </div>
      </div>
    </footer>
  );
}
# fix(ui): prevent double-firing of play event on mobile\n