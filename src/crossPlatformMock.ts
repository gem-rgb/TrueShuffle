import type {
  BackendStatus,
  CrossPlatformFeedbackRequest,
  CrossPlatformFeedbackResponse,
  ListeningStats,
  PlatformConnectRequest,
  PlatformConnectResponse,
  PlaylistItem,
  UnifiedPlaylist,
  UnifiedTrack,
  UserProfile
} from "./types";

type DemoState = {
  trackMap: Map<string, UnifiedTrack>;
  trackOrder: string[];
  stats: ListeningStats;
  preferences: UserProfile["preferences"];
  connections: PlatformConnectResponse[];
  history: Array<Record<string, unknown>>;
  eventCount: number;
};

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

function createTrack(
  id: string,
  title: string,
  artist: string,
  source: UnifiedTrack["source"],
  genre: string,
  mood: string,
  energy: number,
  tempo: number,
  popularity: number,
  album: string,
  durationMs: number
): UnifiedTrack {
  return {
    id,
    title,
    artist,
    source,
    features: {
      energy,
      tempo,
      spectral_centroid: 1_400 + popularity * 18,
      spectral_bandwidth: 900 + popularity * 12,
      spectral_rolloff: 2_100 + popularity * 22,
      zero_crossing_rate: 0.05 + popularity / 1_000,
      mfcc: Array.from({ length: 13 }, (_, index) => Number((energy * 10 + index * 0.28).toFixed(3)))
    },
    link: `https://example.com/${source}/${id}`,
    genres: [genre],
    mood: [mood],
    album,
    durationMs,
    popularity,
    externalId: id,
    raw: {
      demo: true
    }
  };
}

const DEMO_TRACKS = [
  createTrack("spotify-night-glass", "Night Glass", "Aurora Lane", "spotify", "synthwave", "driving", 0.72, 122, 82, "Afterhours", 214_000),
  createTrack("youtube-grain-light", "Grain Light", "Atlas Static", "youtube_music", "indie", "focused", 0.52, 108, 71, "Browse Mode", 205_000),
  createTrack("apple-velvet-current", "Velvet Current", "Luma Row", "apple_music", "soul", "warm", 0.48, 102, 68, "Warm Signal", 223_000),
  createTrack("podcast-deep-work", "Deep Work 101", "Focus Protocol", "podcasts", "education", "informative", 0.31, 88, 72, "Episode 12", 1_620_000),
  createTrack("spotify-midnight-arc", "Midnight Arc", "Neon Arcade", "spotify", "synthwave", "energetic", 0.78, 130, 87, "Transit", 227_000),
  createTrack("youtube-drift-line", "Drift Line", "Noctua Field", "youtube_music", "ambient", "calm", 0.26, 86, 58, "Night Loop", 236_000),
  createTrack("apple-airframe", "Airframe", "Prism Coast", "apple_music", "pop", "uplifted", 0.69, 124, 84, "Tidal", 204_000),
  createTrack("podcast-night-reset", "Night Reset", "Calm Archive", "podcasts", "wellness", "restful", 0.2, 80, 59, "Episode 8", 1_740_000)
];

function createInitialState(): DemoState {
  const trackMap = new Map(DEMO_TRACKS.map((track) => [track.id, track]));
  const trackOrder = DEMO_TRACKS.map((track) => track.id);
  const stats: ListeningStats = {
    totalPlays: 128,
    skips: 17,
    likes: 46,
    sessions: 28,
    tracksSeen: DEMO_TRACKS.length,
    sources: {
      spotify: 40,
      youtube_music: 28,
      apple_music: 22,
      podcasts: 38
    },
    lastSyncAt: new Date().toISOString()
  };

  const previewCounts = DEMO_TRACKS.reduce<Record<string, number>>((counts, track) => {
    counts[track.source] = (counts[track.source] ?? 0) + 1;
    return counts;
  }, {});
  const connections: PlatformConnectResponse[] = [
    {
      platform: "spotify",
      connected: false,
      status: "demo",
      detail: "Spotify demo connector ready.",
      connectorName: "SpotifyConnector",
      previewCount: previewCounts.spotify ?? 0,
      lastSyncAt: new Date().toISOString()
    },
    {
      platform: "youtube_music",
      connected: false,
      status: "demo",
      detail: "YouTube Music demo connector ready.",
      connectorName: "YouTubeMusicConnector",
      previewCount: previewCounts.youtube_music ?? 0,
      lastSyncAt: new Date().toISOString()
    },
    {
      platform: "apple_music",
      connected: false,
      status: "demo",
      detail: "Apple Music demo connector ready.",
      connectorName: "AppleMusicConnector",
      previewCount: previewCounts.apple_music ?? 0,
      lastSyncAt: new Date().toISOString()
    },
    {
      platform: "podcasts",
      connected: false,
      status: "demo",
      detail: "Podcast demo connector ready.",
      connectorName: "PodcastConnector",
      previewCount: previewCounts.podcasts ?? 0,
      lastSyncAt: new Date().toISOString()
    }
  ];

  const preferences: UserProfile["preferences"] = {
    genres: {
      synthwave: 2.4,
      indie: 1.8,
      ambient: 1.1,
      education: 0.8,
      pop: 1.2,
      wellness: 0.7
    },
    artists: {
      "aurora lane": 2.3,
      "neon arcade": 2.1,
      "prism coast": 1.7,
      "focus protocol": 1.4
    },
    mood: {
      driving: 1.9,
      focused: 1.4,
      warm: 1.2,
      calm: 0.9,
      informative: 1.1,
      restful: 0.6
    },
    sources: {
      spotify: 1.7,
      youtube_music: 1.1,
      apple_music: 1.0,
      podcasts: 1.4
    },
    history: []
  };

  return {
    trackMap,
    trackOrder,
    stats,
    preferences,
    connections,
    history: [],
    eventCount: 0
  };
}

const demoState = createInitialState();

function inferSourceCounts(tracks: UnifiedTrack[]): Record<string, number> {
  return tracks.reduce<Record<string, number>>((counts, track) => {
    counts[track.source] = (counts[track.source] ?? 0) + 1;
    return counts;
  }, {});
}

function buildPlaylist(): UnifiedPlaylist {
  const items = demoState.trackOrder
    .map((trackId) => demoState.trackMap.get(trackId))
    .filter((track): track is UnifiedTrack => track != null)
    .map((track): PlaylistItem => ({
      trackId: track.id,
      title: track.title,
      artist: track.artist,
      source: track.source,
      link: track.link ?? "",
      score: 0.75
    }));

  return {
    items,
    generatedAt: new Date().toISOString(),
    sourceCounts: inferSourceCounts(items.map((item) => demoState.trackMap.get(item.trackId ?? "")!).filter(Boolean)),
    summary: "Demo cross-platform playlist ready."
  };
}

function buildProfile(): UserProfile {
  const tracks = demoState.trackOrder.map((trackId) => demoState.trackMap.get(trackId)).filter((track): track is UnifiedTrack => track != null);
  const sourceCounts = inferSourceCounts(tracks);

  return {
    userId: "default",
    stats: clone(demoState.stats),
    preferences: clone(demoState.preferences),
    connections: clone(demoState.connections),
    topGenres: Object.entries(demoState.preferences.genres).sort((left, right) => right[1] - left[1]).map(([genre]) => genre).slice(0, 5),
    topArtists: Object.entries(demoState.preferences.artists).sort((left, right) => right[1] - left[1]).map(([artist]) => artist).slice(0, 5),
    topMoods: Object.entries(demoState.preferences.mood).sort((left, right) => right[1] - left[1]).map(([mood]) => mood).slice(0, 5),
    summary: `Demo listener model favors ${Object.keys(sourceCounts)[0] ?? "multiple"} platforms with balanced discovery.`,
    updatedAt: new Date().toISOString()
  };
}

function promoteTrack(trackId: string, eventType: "play" | "skip" | "like"): void {
  const index = demoState.trackOrder.indexOf(trackId);
  if (index < 0) {
    return;
  }

  const [track] = demoState.trackOrder.splice(index, 1);
  if (eventType === "skip") {
    demoState.trackOrder.push(track);
  } else if (eventType === "like") {
    demoState.trackOrder.unshift(track);
  } else {
    demoState.trackOrder.splice(Math.min(1, demoState.trackOrder.length), 0, track);
  }
}

function accumulatePreference(track: UnifiedTrack, eventType: "play" | "skip" | "like", intensity = 1): void {
  const base = eventType === "like" ? 1.2 : eventType === "skip" ? -0.75 : 0.55;
  const weight = base * intensity;
  const add = (bucket: Record<string, number>, labels: string[], scale = 1): void => {
    labels.forEach((label) => {
      const normalized = label.toLowerCase();
      bucket[normalized] = (bucket[normalized] ?? 0) + weight * scale;
    });
  };

  add(demoState.preferences.genres, track.genres, 1);
  add(demoState.preferences.artists, [track.artist], 1.12);
  add(demoState.preferences.mood, track.mood, 0.88);
  add(demoState.preferences.sources, [track.source], 0.8);
  demoState.preferences.history.unshift({
    trackId: track.id,
    eventType,
    platform: track.source,
    at: new Date().toISOString()
  });
  demoState.preferences.history = demoState.preferences.history.slice(0, 80);
}

export function getMockBackendStatus(): BackendStatus {
  return {
    status: "ok",
    service: "trueshuffle-ai",
    phase: "starting",
    detail: "Waiting for the Python backend to report live status.",
    connectedPlatforms: demoState.connections.filter((connection) => connection.connected).map((connection) => connection.platform),
    syncing: false,
    lastSyncAt: demoState.stats.lastSyncAt ?? null
  };
}

export function getMockUnifiedProfile(): UserProfile {
  return buildProfile();
}

export function getMockUnifiedPlaylist(): UnifiedPlaylist {
  return buildPlaylist();
}

export function getMockConnectResponse(platform: string, request: PlatformConnectRequest): PlatformConnectResponse {
  const previewCount = demoState.trackOrder.filter((trackId) => demoState.trackMap.get(trackId)?.source === platform).length;
  const existingIndex = demoState.connections.findIndex((item) => item.platform === platform);
  const response: PlatformConnectResponse = {
    platform,
    connected: true,
    status: request.accessToken ? "connected" : "demo",
    detail: `${platform} connected in demo mode.`,
    connectorName: `${platform}Connector`,
    previewCount,
    lastSyncAt: new Date().toISOString()
  };

  if (existingIndex >= 0) {
    demoState.connections.splice(existingIndex, 1, response);
  } else {
    demoState.connections.push(response);
  }

  return clone(response);
}

export function applyMockFeedback(request: CrossPlatformFeedbackRequest): CrossPlatformFeedbackResponse {
  const trackId = request.trackId ?? request.track?.id ?? null;
  const eventType = request.eventType ?? "play";
  const track = trackId ? demoState.trackMap.get(trackId) ?? request.track ?? null : request.track ?? null;

  if (track != null) {
    accumulatePreference(track, eventType, request.intensity ?? 1);
    promoteTrack(track.id, eventType);
    demoState.stats.totalPlays += eventType === "play" ? 1 : 0;
    demoState.stats.skips += eventType === "skip" ? 1 : 0;
    demoState.stats.likes += eventType === "like" ? 1 : 0;
    demoState.stats.lastSyncAt = new Date().toISOString();
    demoState.eventCount += 1;
  }

  const profile = getMockUnifiedProfile();
  const playlist = getMockUnifiedPlaylist();
  return {
    profile,
    playlist,
    summary: track
      ? `Recorded ${eventType} feedback for ${track.title}.`
      : "Recorded demo feedback."
  };
}
