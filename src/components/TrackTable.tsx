import type { Track } from "../types";
import { formatDuration, formatPercent } from "../utils";

interface TrackTableProps {
  tracks: Track[];
  selectedTrackId: string | null;
  query: string;
  onQueryChange: (query: string) => void;
}

export function TrackTable({ tracks, selectedTrackId, query, onQueryChange }: TrackTableProps) {
  return (
    <div className="track-stack">
      <div className="section-head">
        <div>
          <div className="section-label">Tracks</div>
          <h2>Playlist viewer</h2>
        </div>
        <span className="count-pill">{tracks.length}</span>
      </div>

      <label className="search-box" htmlFor="track-search">
        <span>Search</span>
        <input
          id="track-search"
          type="search"
          value={query}
          placeholder="Track, artist, album"
          onChange={(event) => onQueryChange(event.target.value)}
        />
      </label>

      <div className="track-table">
        <div className="track-table-head">
          <span>#</span>
          <span>Track</span>
          <span>Artist</span>
          <span>Album</span>
          <span>Duration</span>
          <span>Popularity</span>
        </div>
        <div className="track-table-body">
          {tracks.length > 0 ? (
            tracks.map((track, index) => {
              const active = track.id === selectedTrackId;
              const detailLine = track.audioFeatures
                ? `Tempo ${Math.round(track.audioFeatures.tempo)} BPM - Energy ${formatPercent(track.audioFeatures.energy, 0)}`
                : track.addedAt
                  ? `Added ${new Date(track.addedAt).toLocaleDateString()}`
                  : "Spotify track";
              const genreLine = track.genres?.length ? track.genres.slice(0, 3).join(" - ") : null;
              return (
                <div key={track.id} className={`track-row ${active ? "active" : ""}`}>
                  <span className="track-index">{index + 1}</span>
                  <span className="track-title">
                    <strong>{track.name}</strong>
                    <span>{genreLine ? `${detailLine} - ${genreLine}` : detailLine}</span>
                  </span>
                  <span className="track-artist">{track.artistName}</span>
                  <span className="track-album">{track.albumName}</span>
                  <span className="track-duration">{formatDuration(track.durationMs)}</span>
                  <span className="track-popularity">
                    <span className="popularity-bar">
                      <span className="popularity-fill" style={{ width: `${track.popularity}%` }} />
                    </span>
                    <span>{track.popularity}</span>
                  </span>
                </div>
              );
            })
          ) : (
            <div className="empty-state">
              <strong>No tracks found.</strong>
              <span>Try a broader search or pick another playlist.</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
