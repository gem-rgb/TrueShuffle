import type {
  BackendStatus,
  ListeningEventType,
  PlatformConnectResponse,
  PlaylistItem,
  UnifiedPlaylist,
  UserProfile
} from "../types";
import { formatPercent, formatRelativeTime } from "../utils";

interface CrossPlatformPanelProps {
  backendStatus: BackendStatus;
  profile: UserProfile | null;
  playlist: UnifiedPlaylist | null;
  busy: boolean;
  onConnect: (platform: "spotify" | "youtube_music" | "apple_music" | "podcasts") => void;
  onRefreshProfile: () => void;
  onRefreshPlaylist: () => void;
  onFeedback: (eventType: ListeningEventType, item: PlaylistItem | null) => void;
}

const platformButtons = [
  { platform: "spotify" as const, label: "Spotify" },
  { platform: "youtube_music" as const, label: "YouTube Music" },
  { platform: "apple_music" as const, label: "Apple Music" },
  { platform: "podcasts" as const, label: "Podcasts" }
];

function statusClass(phase: BackendStatus["phase"]): string {
  if (phase === "live") {
    return "success";
  }
  if (phase === "degraded") {
    return "warning";
  }
  if (phase === "offline") {
    return "danger";
  }
  return "starting";
}

function connectionLabel(connection: PlatformConnectResponse): string {
  return connection.connected ? "Connected" : connection.status;
}

export function CrossPlatformPanel({
  backendStatus,
  profile,
  playlist,
  busy,
  onConnect,
  onRefreshProfile,
  onRefreshPlaylist,
  onFeedback
}: CrossPlatformPanelProps) {
  const topTrack = playlist?.items[0] ?? null;
  const summaryItems = profile
    ? [
        { label: "Plays", value: profile.stats.totalPlays.toString() },
        { label: "Skips", value: profile.stats.skips.toString() },
        { label: "Likes", value: profile.stats.likes.toString() },
        { label: "Tracks seen", value: profile.stats.tracksSeen.toString() },
        { label: "Sessions", value: profile.stats.sessions.toString() },
        { label: "Sync", value: formatRelativeTime(profile.stats.lastSyncAt) }
      ]
    : [];

  return (
    <div className="cross-platform-stack">
      <div className="section-head">
        <div>
          <div className="section-label">Cross-platform AI</div>
          <h2>Unified profile</h2>
        </div>
        <span className={`status-chip ${statusClass(backendStatus.phase)}`}>
          {backendStatus.phase === "starting"
            ? "Backend starting"
            : backendStatus.phase === "live"
              ? "Backend live"
              : backendStatus.phase}
        </span>
      </div>

      <article className="backend-status-banner">
        <div className="backend-status-copy">
          <span className="mini-label">Service</span>
          <strong>{backendStatus.service}</strong>
          <p>{backendStatus.detail}</p>
        </div>
        <div className="backend-status-meta">
          <span className="status-chip subtle">{backendStatus.syncing ? "Syncing" : "Idle"}</span>
          <span className="status-chip subtle">{backendStatus.connectedPlatforms.length} connected</span>
          <span className="status-chip subtle">{formatRelativeTime(backendStatus.lastSyncAt)}</span>
        </div>
      </article>

      <div className="platform-grid">
        {platformButtons.map((entry) => (
          <button
            key={entry.platform}
            type="button"
            className="platform-connect-card"
            disabled={busy}
            onClick={() => onConnect(entry.platform)}
          >
            <strong>{entry.label}</strong>
            <span>Connect and sync this source.</span>
          </button>
        ))}
      </div>

      <div className="connection-list">
        {(profile?.connections ?? []).map((connection) => (
          <article key={connection.platform} className="connection-card">
            <div>
              <strong>{connection.platform}</strong>
              <span>{connection.detail}</span>
            </div>
            <div className="connection-meta">
              <span className={`status-chip ${connection.connected ? "success" : "subtle"}`}>{connectionLabel(connection)}</span>
              <span className="count-pill">{connection.previewCount}</span>
            </div>
          </article>
        ))}
        {profile?.connections.length ? null : <p className="muted">Connect a platform to populate the sync status list.</p>}
      </div>

      <div className="button-row">
        <button className="button-secondary" type="button" disabled={busy} onClick={onRefreshProfile}>
          Refresh profile
        </button>
        <button className="button-primary" type="button" disabled={busy} onClick={onRefreshPlaylist}>
          Refresh playlist
        </button>
      </div>

      <div className="metric-grid compact">
        {summaryItems.map((item) => (
          <article className="metric-card" key={item.label}>
            <span className="mini-label">{item.label}</span>
            <strong>{item.value}</strong>
          </article>
        ))}
      </div>

      <article className="summary-card">
        <span className="mini-label">Preference summary</span>
        <p>{profile?.summary ?? "Learning from your cross-platform activity."}</p>
        <div className="tag-cloud">
          {(profile?.topGenres ?? []).slice(0, 4).map((genre) => (
            <span key={genre} className="status-chip subtle">
              {genre}
            </span>
          ))}
          {(profile?.topArtists ?? []).slice(0, 3).map((artist) => (
            <span key={artist} className="status-chip subtle">
              {artist}
            </span>
          ))}
          {(profile?.topMoods ?? []).slice(0, 3).map((mood) => (
            <span key={mood} className="status-chip subtle">
              {mood}
            </span>
          ))}
        </div>
      </article>

      <article className="summary-card">
        <div className="section-head">
          <div>
            <span className="mini-label">AI playlist</span>
            <h2>{playlist?.summary || "Cross-platform queue"}</h2>
          </div>
          <span className="count-pill">{playlist?.items.length ?? 0}</span>
        </div>

        <div className="playlist-preview">
          {playlist?.items.slice(0, 6).map((item, index) => (
            <div key={`${item.trackId ?? item.title}-${index}`} className="playlist-preview-row">
              <div className="playlist-preview-index">{index + 1}</div>
              <div className="playlist-preview-copy">
                <strong>{item.title}</strong>
                <span>{item.artist}</span>
              </div>
              <div className="playlist-preview-meta">
                <span className="status-chip subtle">{item.source}</span>
                <span>{item.score != null ? formatPercent(item.score, 0) : "-"}</span>
              </div>
            </div>
          ))}
          {playlist?.items.length ? null : <p className="muted">Generate or sync a playlist to populate this section.</p>}
        </div>

        <div className="button-row">
          <button className="ghost-button" type="button" disabled={busy || !topTrack} onClick={() => onFeedback("like", topTrack)}>
            Like top track
          </button>
          <button className="ghost-button" type="button" disabled={busy || !topTrack} onClick={() => onFeedback("skip", topTrack)}>
            Skip top track
          </button>
          <button className="ghost-button" type="button" disabled={busy || !topTrack} onClick={() => onFeedback("play", topTrack)}>
            Mark played
          </button>
        </div>
      </article>
    </div>
  );
}
