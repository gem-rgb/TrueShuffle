import type { AuthStatus, Playlist } from "../types";

interface SidebarProps {
  auth: AuthStatus;
  playlists: Playlist[];
  selectedPlaylistId: string | null;
  busy: boolean;
  onLogin: () => void;
  onLogout: () => void;
  onRefresh: () => void;
  onSelectPlaylist: (playlistId: string) => void;
}

export function Sidebar({
  auth,
  playlists,
  selectedPlaylistId,
  busy,
  onLogin,
  onLogout,
  onRefresh,
  onSelectPlaylist
}: SidebarProps) {
  return (
    <div className="sidebar-stack">
      <div className="sidebar-auth">
        <div className="section-label">Account</div>
        <h2>Spotify access</h2>
        <p className="muted">
          {auth.authenticated ? `Connected as ${auth.displayName}.` : "No live Spotify session yet. Demo data is active."}
        </p>
        <div className="chip-row">
          <span className={`status-chip ${auth.authenticated ? "success" : "warning"}`}>
            {auth.authenticated ? "Connected" : "Demo mode"}
          </span>
          <span className="status-chip subtle">{auth.demoMode ? "Mock fallback ready" : "Live backend"}</span>
        </div>
        <div className="button-row">
          <button className="button-primary" type="button" onClick={onLogin} disabled={busy}>
            {auth.authenticated ? "Reconnect Spotify" : "Login with Spotify"}
          </button>
          <button className="button-secondary" type="button" onClick={onLogout} disabled={busy || !auth.authenticated}>
            Logout
          </button>
          <button className="ghost-button" type="button" onClick={onRefresh} disabled={busy}>
            Refresh library
          </button>
        </div>
      </div>

      <div className="sidebar-playlists">
        <div className="section-head">
          <div>
            <div className="section-label">Library</div>
            <h2>Playlists</h2>
          </div>
          <span className="count-pill">{playlists.length}</span>
        </div>
        <div className="playlist-list">
          {playlists.map((playlist) => {
            const active = playlist.id === selectedPlaylistId;
            return (
              <button
                type="button"
                key={playlist.id}
                className={`playlist-card ${active ? "active" : ""}`}
                onClick={() => onSelectPlaylist(playlist.id)}
              >
                <span className="playlist-swatch" style={{ background: playlist.accent ?? "#7ef0c7" }} />
                <span className="playlist-copy">
                  <strong>{playlist.name}</strong>
                  <span>
                    {playlist.trackCount} tracks - {playlist.ownerName}
                  </span>
                </span>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}

# style(nav): update sidebar navigation icons\n