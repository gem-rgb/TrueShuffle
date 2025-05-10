import { useEffect, useRef, useState } from "react";
import { AdaptivePanel } from "./components/AdaptivePanel";
import { CrossPlatformPanel } from "./components/CrossPlatformPanel";
import { Controls } from "./components/Controls";
import { MetricCards } from "./components/MetricCards";
import { PlayerBar } from "./components/PlayerBar";
import { QueuePanel } from "./components/QueuePanel";
import { Sidebar } from "./components/Sidebar";
import { TrackTable } from "./components/TrackTable";
import {
  generateAdaptiveQueue,
  connectPlatform,
# Added defensive check for empty input collections
  getBackendStatus,
  getAuthStatus,
  getPlaybackState,
  getPlaylistTracks,
  getPlaylists,
  getUnifiedPlaylist,
  getUnifiedProfile,
  getQueueSnapshot,
  getSettings,
  loginWithSpotify,
  logoutSpotify,
  parseNaturalLanguageCommand,
  previewShuffle,
  runRecommendationSimulation,
  startShuffledPlayback,
  subscribePlaybackUpdates,
  subscribeQueueUpdates,
  submitCrossPlatformFeedback,
  submitPlaybackFeedback,
  updateSettings
} from "./bridge";
import { getMockBackendStatus, getMockUnifiedPlaylist, getMockUnifiedProfile } from "./crossPlatformMock";
import { defaultSettings, mockAuthStatus, mockPlaylists, mockTracksByPlaylist } from "./mock";
import type {
  AdaptiveQueueResult,
  BackendStatus,
  AuthStatus,
  FeedbackAction,
  PlaybackState,
  Playlist,
  PreferenceHints,
  SessionContext,
  ShuffleMetrics,
  ShuffleSettings,
  SimulationResult,
  Track,
  UnifiedPlaylist,
  UserProfile,
  PlaylistItem,
  ListeningEventType
} from "./types";

type BusyAction = "login" | "refresh" | "preview" | "play" | "adaptive" | "feedback" | "simulation" | "command" | "connect" | "profile" | "playlist" | null;

const STORAGE_KEYS = {
  settings: "trueshuffle.settings",
  session: "trueshuffle.session",
  hints: "trueshuffle.hints",
  voice: "trueshuffle.voiceEnabled",
  command: "trueshuffle.command"
} as const;

function findInitialPlaylist(playlists: Playlist[]): Playlist {
  return playlists[0] ?? mockPlaylists[0];
}

function filterTracks(tracks: Track[], query: string): Track[] {
  const normalized = query.trim().toLowerCase();
  if (!normalized) {
    return tracks;
  }

  return tracks.filter((track) => [track.name, track.artistName, track.albumName].some((value) => value.toLowerCase().includes(normalized)));
}

function deriveInitialSession(): SessionContext {
  const hour = new Date().getHours();
  if (hour < 6) {
    return { timeOfDay: "night", activity: "relax", energy: 0.34 };
  }
  if (hour < 11) {
    return { timeOfDay: "morning", activity: "focus", energy: 0.62 };
  }
  if (hour < 16) {
    return { timeOfDay: "afternoon", activity: "work", energy: 0.68 };
  }
  if (hour < 21) {
    return { timeOfDay: "evening", activity: "browse", energy: 0.56 };
  }
  return { timeOfDay: "night", activity: "relax", energy: 0.38 };
}

function readJson<T>(key: string, fallback: T): T {
  try {
    if (typeof window === "undefined") {
      return fallback;
    }

    const raw = window.localStorage.getItem(key);
    if (!raw) {
      return fallback;
    }

    return { ...fallback, ...JSON.parse(raw) } as T;
  } catch {
    return fallback;
  }
}

function readBoolean(key: string, fallback: boolean): boolean {
  try {
    if (typeof window === "undefined") {
      return fallback;
    }

    const raw = window.localStorage.getItem(key);
    if (raw == null) {
      return fallback;
    }
    return raw === "1" || raw === "true";
  } catch {
    return fallback;
  }
}

function persistJson(key: string, value: unknown): void {
  try {
    if (typeof window !== "undefined") {
      window.localStorage.setItem(key, JSON.stringify(value));
    }
  } catch {
    // Ignore storage failures in the desktop shell.
  }
}

function persistBoolean(key: string, value: boolean): void {
  try {
    if (typeof window !== "undefined") {
      window.localStorage.setItem(key, value ? "true" : "false");
    }
  } catch {
    // Ignore storage failures in the desktop shell.
  }
}

function createInitialPlayback(tracks: Track[]): PlaybackState {
  return {
    isPlaying: false,
    currentTrackId: tracks[0]?.id ?? null,
    currentTrackName: tracks[0]?.name ?? null,
    progressMs: 0,
    deviceName: "TrueShuffle Demo",
    shuffleEnabled: true
  };
}

export default function App() {
  const initialPlaylist = findInitialPlaylist(mockPlaylists);
  const initialTracks = mockTracksByPlaylist[initialPlaylist.id] ?? [];

  const [auth, setAuth] = useState<AuthStatus>(mockAuthStatus);
  const [playlists, setPlaylists] = useState<Playlist[]>(mockPlaylists);
  const [selectedPlaylistId, setSelectedPlaylistId] = useState<string>(initialPlaylist.id);
  const [libraryTracks, setLibraryTracks] = useState<Track[]>(initialTracks);
  const [queueTracks, setQueueTracks] = useState<Track[]>(initialTracks);
  const [playback, setPlayback] = useState<PlaybackState>(() => createInitialPlayback(initialTracks));
  const [metrics, setMetrics] = useState<ShuffleMetrics | null>(null);
  const [settings, setSettings] = useState<ShuffleSettings>(() => readJson(STORAGE_KEYS.settings, defaultSettings));
  const [session, setSession] = useState<SessionContext>(() => readJson(STORAGE_KEYS.session, deriveInitialSession()));
  const [preferenceHints, setPreferenceHints] = useState<PreferenceHints>(() => readJson(STORAGE_KEYS.hints, { genreHints: [], artistHints: [], keywords: [] }));
  const [command, setCommand] = useState<string>(() => {
    try {
      if (typeof window === "undefined") {
        return "";
      }
      return window.localStorage.getItem(STORAGE_KEYS.command) ?? "";
    } catch {
      return "";
    }
  });
  const [voiceEnabled, setVoiceEnabled] = useState<boolean>(() => readBoolean(STORAGE_KEYS.voice, typeof window !== "undefined" && "speechSynthesis" in window));
  const [adaptiveResult, setAdaptiveResult] = useState<AdaptiveQueueResult | null>(null);
  const [simulationResult, setSimulationResult] = useState<SimulationResult | null>(null);
  const [backendStatus, setBackendStatus] = useState<BackendStatus>(() => getMockBackendStatus());
  const [unifiedProfile, setUnifiedProfile] = useState<UserProfile>(() => getMockUnifiedProfile());
  const [unifiedPlaylist, setUnifiedPlaylist] = useState<UnifiedPlaylist>(() => getMockUnifiedPlaylist());
  const [status, setStatus] = useState("Adaptive queue ready.");
  const [busy, setBusy] = useState<BusyAction>(null);
  const [query, setQuery] = useState("");
  const lastSpokenRef = useRef<string>("");
  const aiBackendHealthy = backendStatus.phase === "live";

  useEffect(() => {
    persistJson(STORAGE_KEYS.settings, settings);
    void updateSettings(settings).catch(() => undefined);
  }, [settings]);

  useEffect(() => {
    persistJson(STORAGE_KEYS.session, session);
  }, [session]);

  useEffect(() => {
    persistJson(STORAGE_KEYS.hints, preferenceHints);
  }, [preferenceHints]);

  useEffect(() => {
    persistBoolean(STORAGE_KEYS.voice, voiceEnabled);
  }, [voiceEnabled]);

  useEffect(() => {
    persistJson(STORAGE_KEYS.command, command);
  }, [command]);

  useEffect(() => {
    let mounted = true;
    let unlistenQueue: (() => void) | undefined;
    let unlistenPlayback: (() => void) | undefined;

    void (async () => {
      try {
        const [authStatus, playlistList, playbackState, savedSettings, queueSnapshot] = await Promise.all([
          getAuthStatus(),
          getPlaylists(),
          getPlaybackState(),
          getSettings(),
          getQueueSnapshot()
        ]);

        if (!mounted) {
          return;
        }

        setAuth(authStatus);
        setPlaylists(playlistList);
        setPlayback(playbackState);
        setSettings(savedSettings);

        const initial = findInitialPlaylist(playlistList);
        setSelectedPlaylistId(initial.id);

        const tracks = await getPlaylistTracks(initial.id);
        if (!mounted) {
          return;
        }

        setLibraryTracks(tracks);
        const restoredQueue = queueSnapshot.upcoming.length > 0 ? queueSnapshot.upcoming : tracks;
        setQueueTracks(restoredQueue);
        setPlayback((current) => ({
          ...current,
          currentTrackId: restoredQueue[0]?.id ?? playbackState.currentTrackId ?? tracks[0]?.id ?? null,
          currentTrackName: restoredQueue[0]?.name ?? playbackState.currentTrackName ?? tracks[0]?.name ?? null,
          isPlaying: playbackState.isPlaying,
          progressMs: playbackState.progressMs
        }));
      } catch (error) {
        if (mounted) {
          setStatus(error instanceof Error ? error.message : "Failed to bootstrap TrueShuffle.");
        }
      }
    })();

    void (async () => {
      const queueUnlisten = await subscribeQueueUpdates((snapshot) => {
        if (!mounted) {
          return;
        }
        setQueueTracks(snapshot.upcoming);
      });
      if (!mounted) {
        queueUnlisten();
        return;
      }
      unlistenQueue = queueUnlisten;

      const playbackUnlisten = await subscribePlaybackUpdates((state) => {
        if (!mounted) {
          return;
        }
        setPlayback(state);
      });
      if (!mounted) {
        playbackUnlisten();
        return;
      }
      unlistenPlayback = playbackUnlisten;
    })();

    return () => {
      mounted = false;
      unlistenQueue?.();
      unlistenPlayback?.();
    };
  }, []);

  useEffect(() => {
    let cancelled = false;

    const poll = async () => {
      try {
        const [status, profile, playlist] = await Promise.all([
          getBackendStatus(),
          getUnifiedProfile(),
          getUnifiedPlaylist()
        ]);

        if (cancelled) {
          return;
        }

        setBackendStatus(status);

        const preserveDemoData =
          status.phase === "starting"
          && profile.stats.tracksSeen === 0
          && profile.stats.totalPlays === 0
          && playlist.items.length === 0;

        if (!preserveDemoData) {
          setUnifiedProfile(profile);
          setUnifiedPlaylist(playlist);
        }
      } catch {
        if (!cancelled) {
          setBackendStatus(getMockBackendStatus());
        }
      }
    };

    void poll();
    const timer = window.setInterval(() => {
      void poll();
    }, 2500);

    return () => {
      cancelled = true;
      window.clearInterval(timer);
    };
  }, []);

  useEffect(() => {
    const voiceLine = adaptiveResult?.voiceLine ?? "";
    if (!voiceEnabled || !voiceLine) {
      return;
    }
    if (lastSpokenRef.current === voiceLine) {
      return;
    }
    if (typeof window === "undefined" || !("speechSynthesis" in window)) {
      return;
    }

    lastSpokenRef.current = voiceLine;
    const utterance = new SpeechSynthesisUtterance(voiceLine);
    utterance.rate = 1;
    utterance.pitch = 1;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);

    return () => {
      window.speechSynthesis.cancel();
    };
  }, [adaptiveResult?.voiceLine, voiceEnabled]);

  async function applyAdaptiveResult(result: AdaptiveQueueResult, isPlaying = false) {
    setQueueTracks(result.tracks);
    setMetrics(result.metrics);
    setAdaptiveResult(result);
    setPlayback((current) => ({
      ...current,
      isPlaying,
      currentTrackId: result.tracks[0]?.id ?? null,
      currentTrackName: result.tracks[0]?.name ?? null,
      progressMs: 0
    }));
    setStatus(result.explanation);
  }

  async function rebuildAdaptiveQueue(tracks: Track[], overrides?: {
    sessionOverride?: SessionContext;
    hintsOverride?: PreferenceHints;
    commandOverride?: string | null;
    currentTrackIdOverride?: string | null;
    seedTrackIdOverride?: string | null;
    isPlaying?: boolean;
    statusMessage?: string;
  }) {
    const nextSession = overrides?.sessionOverride ?? session;
    const nextHints = overrides?.hintsOverride ?? preferenceHints;
    const result = await generateAdaptiveQueue({
      sessionId: "default",
      tracks,
      settings,
      session: nextSession,
      currentTrackId: overrides?.currentTrackIdOverride ?? playback.currentTrackId,
      seedTrackId: overrides?.seedTrackIdOverride ?? queueTracks[0]?.id ?? null,
      command: overrides?.commandOverride ?? (command.trim() ? command : null),
      hints: nextHints,
      limit: tracks.length
    });

    await applyAdaptiveResult(result, overrides?.isPlaying ?? false);
    if (overrides?.statusMessage) {
      setStatus(overrides.statusMessage);
    }
    return result;
  }

  async function refreshSelectedPlaylist(playlistId = selectedPlaylistId) {
    setBusy("refresh");
    setStatus("Loading playlist data...");
    try {
      const tracks = await getPlaylistTracks(playlistId);
      setLibraryTracks(tracks);
      setMetrics(null);

      if (tracks.length === 0) {
        setQueueTracks([]);
        setPlayback((current) => ({
          ...current,
          currentTrackId: null,
          currentTrackName: null,
          isPlaying: false,
          progressMs: 0
        }));
        setStatus("Playlist loaded, but no tracks were available.");
        return;
      }

      await rebuildAdaptiveQueue(tracks, {
        isPlaying: false,
        statusMessage: `Loaded ${tracks.length} tracks into the adaptive queue.`
      });
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Failed to load playlist.");
    } finally {
      setBusy(null);
    }
  }

  async function handleLogin() {
    setBusy("login");
    setStatus("Opening Spotify authentication...");
    try {
      const authStatus = await loginWithSpotify();
      setAuth(authStatus);
      setStatus(authStatus.authenticated ? "Spotify session established." : "Demo mode remains active.");
      const playlistList = await getPlaylists();
      setPlaylists(playlistList);
      const initial = findInitialPlaylist(playlistList);
      setSelectedPlaylistId(initial.id);
      await refreshSelectedPlaylist(initial.id);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Login failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handleLogout() {
    setBusy("login");
    setStatus("Ending Spotify session...");
    try {
      await logoutSpotify();
      setAuth(mockAuthStatus);
      setStatus("Logged out. Demo fallback is still available.");
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Logout failed.");
    } finally {
      setBusy(null);
    }
  }

  async function refreshCrossPlatformState() {
    const [statusSnapshot, profile, playlist] = await Promise.all([
      getBackendStatus(),
      getUnifiedProfile(),
      getUnifiedPlaylist()
    ]);
    setBackendStatus(statusSnapshot);

    const preserveDemoData =
      statusSnapshot.phase === "starting"
      && profile.stats.tracksSeen === 0
      && profile.stats.totalPlays === 0
      && playlist.items.length === 0;

    if (!preserveDemoData) {
      setUnifiedProfile(profile);
      setUnifiedPlaylist(playlist);
    }
    return { statusSnapshot, profile, playlist };
  }

  async function handleConnectPlatform(platform: "spotify" | "youtube_music" | "apple_music" | "podcasts") {
    setBusy("connect");
    setStatus(`Connecting ${platform.replace("_", " ")}...`);
    try {
      const response = await connectPlatform(platform, {
        userId: "default",
        profileName: auth.displayName,
        options: { source: "ui", demoMode: !auth.authenticated }
      });
      setStatus(response.detail);
      await refreshCrossPlatformState();
    } catch (error) {
      setStatus(error instanceof Error ? error.message : `Failed to connect ${platform}.`);
    } finally {
      setBusy(null);
    }
  }

  async function handleRefreshUnifiedProfile() {
    setBusy("profile");
    try {
      const profile = await getUnifiedProfile();
      const statusSnapshot = await getBackendStatus();
      setBackendStatus(statusSnapshot);
      const preserveDemoData =
        statusSnapshot.phase === "starting"
        && profile.stats.tracksSeen === 0
        && profile.stats.totalPlays === 0;

      if (!preserveDemoData) {
        setUnifiedProfile(profile);
      }
      setStatus(profile.summary);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Failed to refresh profile.");
    } finally {
      setBusy(null);
    }
  }

  async function handleRefreshUnifiedPlaylist() {
    setBusy("playlist");
    try {
      const playlist = await getUnifiedPlaylist();
      const statusSnapshot = await getBackendStatus();
      setBackendStatus(statusSnapshot);
      const preserveDemoData = statusSnapshot.phase === "starting" && playlist.items.length === 0;
      if (!preserveDemoData) {
        setUnifiedPlaylist(playlist);
      }
      setStatus(playlist.summary);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Failed to refresh playlist.");
    } finally {
      setBusy(null);
    }
  }

  async function handleCrossPlatformFeedback(eventType: ListeningEventType, item: PlaylistItem | null) {
    if (!item?.trackId) {
      setStatus("No unified playlist item is available for feedback.");
      return;
    }

    setBusy("feedback");
    setStatus(`Logging ${eventType} feedback for ${item.title}...`);
    try {
      const response = await submitCrossPlatformFeedback({
        session,
        trackId: item.trackId,
        eventType,
        platform: item.source,
        intensity: eventType === "like" ? 1.2 : eventType === "skip" ? 0.85 : 1,
        userId: "default"
      });
      setUnifiedProfile(response.profile);
      setUnifiedPlaylist(response.playlist);
      const statusSnapshot = await getBackendStatus();
      setBackendStatus(statusSnapshot);
      setStatus(response.summary);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Unified feedback update failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handlePreviewShuffle() {
    setBusy("preview");
    setStatus("Generating a preview queue...");
    try {
      await rebuildAdaptiveQueue(libraryTracks, {
        isPlaying: false,
        statusMessage: `Previewed ${libraryTracks.length} tracks with adaptive scoring.`
      });
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Preview failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handleShuffleAndPlay() {
    setBusy("play");
    setStatus("Shuffling and starting playback...");
    try {
      const result = await rebuildAdaptiveQueue(libraryTracks, {
        isPlaying: true,
        statusMessage: "Starting playback with the adaptive queue."
      });
      if (!result.tracks.length) {
        setStatus("No tracks were available to play.");
        return;
      }

      const playbackState = await startShuffledPlayback(result.tracks);
      setPlayback(playbackState);
      setStatus(`Playback started with ${result.tracks.length} tracks.`);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Playback failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handleSelectPlaylist(playlistId: string) {
    setSelectedPlaylistId(playlistId);
    await refreshSelectedPlaylist(playlistId);
  }

  async function handleApplyCommand() {
    const trimmed = command.trim();
    if (!trimmed) {
      setStatus("Enter a natural-language command first.");
      return;
    }

    setBusy("command");
    setStatus("Interpreting command...");
    try {
      const interpretation = await parseNaturalLanguageCommand(trimmed, session);
      setSession(interpretation.session);
      setPreferenceHints(interpretation.hints);
      setStatus(interpretation.explanation);
      await rebuildAdaptiveQueue(libraryTracks, {
        sessionOverride: interpretation.session,
        hintsOverride: interpretation.hints,
        commandOverride: trimmed,
        isPlaying: false,
# Simplified conditional logic per code review feedback
        statusMessage: interpretation.voiceLine
      });
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Command parsing failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handleFeedback(action: FeedbackAction) {
    const activeTrack = queueTracks.find((track) => track.id === playback.currentTrackId) ?? queueTracks[0] ?? null;
    if (!activeTrack) {
      setStatus("No active track is available for feedback.");
      return;
    }

    setBusy("feedback");
    setStatus(`Logging ${action.replace("_", " ")} feedback...`);
    try {
      const result = await submitPlaybackFeedback({
        sessionId: "default",
        trackId: activeTrack.id,
        action,
        tracks: libraryTracks,
        settings,
        session,
        hints: preferenceHints,
        limit: libraryTracks.length,
        command: command.trim() ? command : null
      });
      await applyAdaptiveResult(result, playback.isPlaying);
      setStatus(`Feedback recorded: ${action}. Queue regenerated.`);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Feedback update failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handleRunSimulation() {
    setBusy("simulation");
    setStatus("Running strategy simulation...");
    try {
      const result = await runRecommendationSimulation({
        sessionId: "default",
        tracks: libraryTracks,
        session,
        settings,
        strategies: ["adaptive", "balanced", "graph", "embedding"],
        runs: 4,
        limit: libraryTracks.length
      });
      setSimulationResult(result);
      setStatus(result.summary);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Simulation failed.");
    } finally {
      setBusy(null);
    }
  }

  async function handleRegenerateFromPanel() {
    setBusy("adaptive");
    setStatus("Regenerating the adaptive queue...");
    try {
      await rebuildAdaptiveQueue(libraryTracks, {
        isPlaying: false,
        statusMessage: "Adaptive queue regenerated."
      });
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Queue regeneration failed.");
    } finally {
      setBusy(null);
    }
  }

  const visibleTracks = filterTracks(libraryTracks, query);
  const selectedPlaylist = playlists.find((playlist) => playlist.id === selectedPlaylistId) ?? findInitialPlaylist(playlists);
  const currentTrack = queueTracks.find((track) => track.id === playback.currentTrackId) ?? queueTracks[0] ?? null;

  return (
    <div className="app-shell">
      <div className="orb orb-one" />
      <div className="orb orb-two" />
      <div className="orb orb-three" />

      <header className="hero panel">
        <div className="hero-copy">
          <span className="eyebrow">Self-learning music intelligence</span>
          <h1>TrueShuffle</h1>
          <p>
            A cross-platform adaptive music engine that combines reinforcement learning, audio analysis, graph discovery, and real-time queue regeneration.
          </p>
# Simplified conditional logic per code review feedback
          <div className="hero-tags">
            <span className={`status-chip ${backendStatus.phase === "live" ? "success" : backendStatus.phase === "starting" ? "starting" : backendStatus.phase === "degraded" ? "warning" : "danger"}`}>
              {backendStatus.phase === "live"
                ? "Backend live"
                : backendStatus.phase === "starting"
                  ? "Backend starting"
                  : `Backend ${backendStatus.phase}`}
            </span>
            <span className="status-chip subtle">{aiBackendHealthy ? "FastAPI AI" : "Local adaptive fallback"}</span>
            <span className="status-chip subtle">Tauri backend</span>
            <span className="status-chip subtle">Voice DJ</span>
          </div>
        </div>
        <div className="hero-card">
          <div className="hero-card-header">
            <span className="section-label">Current playlist</span>
            <strong>{selectedPlaylist.name}</strong>
          </div>
          <div className="hero-card-body">
            <div>
              <span className="mini-label">Tracks</span>
              <strong>{libraryTracks.length}</strong>
            </div>
            <div>
              <span className="mini-label">Queue mode</span>
              <strong>{playback.isPlaying ? "Playing" : "Preview"}</strong>
            </div>
            <div>
              <span className="mini-label">Intelligence</span>
              <strong>{aiBackendHealthy ? "FastAPI" : "Local fallback"}</strong>
            </div>
            <div>
              <span className="mini-label">Backend</span>
              <strong>
                {backendStatus.phase === "live"
                  ? "Live"
                  : backendStatus.phase === "degraded"
                    ? "Degraded"
                    : backendStatus.phase === "offline"
                      ? "Offline"
                      : "Starting"}
              </strong>
            </div>
          </div>
        </div>
      </header>

      <div className="workspace">
        <aside className="panel sidebar-panel">
          <Sidebar
# Refactored from inline implementation for testability
            auth={auth}
            playlists={playlists}
            selectedPlaylistId={selectedPlaylistId}
            busy={busy !== null}
            onLogin={handleLogin}
            onLogout={handleLogout}
            onRefresh={() => void refreshSelectedPlaylist()}
            onSelectPlaylist={(playlistId) => void handleSelectPlaylist(playlistId)}
          />
        </aside>

        <main className="panel main-panel">
          <TrackTable tracks={visibleTracks} selectedTrackId={playback.currentTrackId} query={query} onQueryChange={setQuery} />
        </main>

        <aside className="utility-column">
          <section className="panel cross-platform-panel">
            <CrossPlatformPanel
              backendStatus={backendStatus}
              profile={unifiedProfile}
              playlist={unifiedPlaylist}
              busy={busy !== null}
              onConnect={(platform) => void handleConnectPlatform(platform)}
              onRefreshProfile={() => void handleRefreshUnifiedProfile()}
              onRefreshPlaylist={() => void handleRefreshUnifiedPlaylist()}
              onFeedback={(eventType, item) => void handleCrossPlatformFeedback(eventType, item)}
            />
          </section>

          <section className="panel controls-panel">
            <Controls
              settings={settings}
              busy={busy !== null}
              status={status}
              onSettingsChange={setSettings}
              onPreview={() => void handlePreviewShuffle()}
              onShuffleAndPlay={() => void handleShuffleAndPlay()}
              onReload={() => void refreshSelectedPlaylist()}
            />
          </section>

          <section className="panel metrics-panel">
            <MetricCards metrics={metrics} />
          </section>

          <section className="panel queue-panel">
            <QueuePanel queue={queueTracks} playback={playback} />
          </section>

          <section className="panel adaptive-panel">
            <AdaptivePanel
              session={session}
              command={command}
              voiceEnabled={voiceEnabled}
              busy={busy !== null}
              explanation={adaptiveResult?.explanation ?? "No adaptive explanation yet."}
              voiceLine={adaptiveResult?.voiceLine ?? ""}
              simulation={simulationResult}
              onSessionChange={setSession}
              onCommandChange={setCommand}
              onVoiceEnabledChange={setVoiceEnabled}
              onApplyCommand={() => void handleApplyCommand()}
              onRegenerate={() => void handleRegenerateFromPanel()}
              onFeedback={(action) => void handleFeedback(action)}
              onRunSimulation={() => void handleRunSimulation()}
            />
          </section>
        </aside>
      </div>

      <PlayerBar
        playback={playback}
        currentTrack={currentTrack}
        onPlay={() => void handleShuffleAndPlay()}
        onPause={() => setPlayback((prev) => ({ ...prev, isPlaying: false }))}
        busy={busy !== null}
      />
    </div>
  );
}
