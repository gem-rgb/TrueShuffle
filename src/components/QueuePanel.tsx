import type { PlaybackState, Track } from "../types";
import { formatDuration } from "../utils";

interface QueuePanelProps {
  queue: Track[];
  playback: PlaybackState;
}

export function QueuePanel({ queue, playback }: QueuePanelProps) {
  return (
    <div className="queue-stack">
      <div className="section-head">
        <div>
          <div className="section-label">Playback</div>
          <h2>Queue display</h2>
        </div>
        <span className={`status-chip ${playback.isPlaying ? "success" : "subtle"}`}>
          {playback.isPlaying ? "Playing" : "Paused"}
        </span>
      </div>

      <div className="queue-list">
        {queue.slice(0, 12).map((track, index) => {
          const active = track.id === playback.currentTrackId;
          return (
            <article key={track.id} className={`queue-item ${active ? "active" : ""}`}>
              <div className="queue-index">{index + 1}</div>
              <div className="queue-copy">
                <strong>{track.name}</strong>
                <span>{track.artistName}</span>
              </div>
              <div className="queue-duration">{formatDuration(track.durationMs)}</div>
            </article>
          );
        })}
        {queue.length === 0 ? <p className="muted">Preview a playlist to populate the queue.</p> : null}
      </div>
    </div>
  );
}

