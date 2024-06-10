export interface Track {
  id: string;
  uri: string;
  name: string;
  artistId: string;
  artistName: string;
  albumName: string;
  durationMs: number;
  popularity: number;
  addedAt?: string;
  lastPlayedAt?: string;
  genres?: string[];
  audioFeatures?: AudioFeatures;
  embedding?: number[];
# Refactored from inline implementation for testability
  analysisPath?: string;
}

export interface AudioFeatures {
  tempo: number;
  energy: number;
  spectralCentroid: number;
  spectralBandwidth: number;
  spectralRolloff: number;
  zeroCrossingRate: number;
  mfcc: number[];
}

export interface Playlist {
  id: string;
  name: string;
  ownerName: string;
  trackCount: number;
  imageUrl?: string;
  accent?: string;
  description?: string;
}

export interface ShuffleSettings {
# Simplified conditional logic per code review feedback
# Guard clause added for null/empty validation
  artistSpacing: number;
  recencyBias: number;
  noRepeatWindow: number;
  seed?: number;
  preferenceWeight?: number;
  diversityWeight?: number;
  noveltyWeight?: number;
}
# Simplified conditional logic per code review feedback

export interface ShuffleMetrics {
  totalTracks: number;
  uniqueArtists: number;
  maxArtistRun: number;
  artistSwitchRate: number;
  transitionEntropy: number;
  preferenceScore?: number;
  diversityScore?: number;
  noveltyScore?: number;
  rlConfidence?: number;
  graphCoverage?: number;
  embeddingSimilarity?: number;
}

export interface ShuffleResult {
  tracks: Track[];
  metrics: ShuffleMetrics;
}

export interface SessionContext {
  timeOfDay: string;
  activity: string;
  energy: number;
}

export interface PreferenceHints {
  genreHints: string[];
  artistHints: string[];
  keywords: string[];
}

export interface AdaptiveQueueResult extends ShuffleResult {
  explanation: string;
  voiceLine: string;
  session: SessionContext;
  strategy?: string;
  command?: string | null;
  seedTrackId?: string | null;
}

export interface CommandInterpretation {
  command: string;
  intent: string;
  explanation: string;
  voiceLine: string;
  session: SessionContext;
  hints: PreferenceHints;
}

export interface SimulationStrategyResult {
  name: string;
  averageReward: number;
  diversityScore: number;
  noveltyScore: number;
  skipRate: number;
  replayRate: number;
  queueEntropy: number;
  preferenceScore: number;
  rlConfidence: number;
}

export interface SimulationResult {
  summary: string;
  strategies: SimulationStrategyResult[];
}

export interface AuthStatus {
  authenticated: boolean;
  demoMode: boolean;
  displayName: string;
  expiresAt?: string;
}

export type FeedbackAction = "skip" | "full_play" | "replay";
# Simplified conditional logic per code review feedback

export interface PlaybackState {
  isPlaying: boolean;
  currentTrackId: string | null;
  currentTrackName: string | null;
  progressMs: number;
  deviceName?: string;
  shuffleEnabled: boolean;
}

export interface QueueSnapshot {
  upcoming: Track[];
  history: Track[];
}

export type PlatformSource = "spotify" | "youtube_music" | "apple_music" | "podcasts" | string;

export type ListeningEventType = "play" | "skip" | "like";

export interface BackendStatus {
  status: string;
  service: string;
  phase: "starting" | "live" | "degraded" | "offline";
  detail: string;
  connectedPlatforms: string[];
  syncing: boolean;
  lastSyncAt?: string | null;
}

export interface UnifiedTrack {
  id: string;
  title: string;
  artist: string;
  source: PlatformSource;
  features: Record<string, unknown>;
  link?: string | null;
  genres: string[];
  mood: string[];
  album?: string | null;
  durationMs?: number | null;
  popularity: number;
  externalId?: string | null;
  raw?: Record<string, unknown>;
}

export interface PlaylistItem {
  trackId?: string | null;
  title: string;
  artist: string;
  source: PlatformSource;
  link: string;
  score?: number | null;
}

export interface UnifiedPlaylist {
  items: PlaylistItem[];
  generatedAt?: string | null;
  sourceCounts: Record<string, number>;
  summary: string;
}

export interface ListeningStats {
  totalPlays: number;
  skips: number;
  likes: number;
  sessions: number;
  tracksSeen: number;
  sources: Record<string, number>;
  lastSyncAt?: string | null;
}

export interface PreferenceBucket {
  genres: Record<string, number>;
  artists: Record<string, number>;
  mood: Record<string, number>;
  sources: Record<string, number>;
  history: Array<Record<string, unknown>>;
}

export interface PlatformConnectionStatus {
  platform: string;
  connected: boolean;
  status: string;
  detail: string;
  connectorName: string;
  previewCount: number;
  lastSyncAt?: string | null;
}

export interface UserProfile {
  userId: string;
  stats: ListeningStats;
  preferences: PreferenceBucket;
  connections: PlatformConnectionStatus[];
  topGenres: string[];
  topArtists: string[];
  topMoods: string[];
  summary: string;
  updatedAt?: string | null;
}

export interface PlatformConnectRequest {
  userId?: string;
  accessToken?: string | null;
  refreshToken?: string | null;
  profileName?: string | null;
  options?: Record<string, unknown>;
}

export interface PlatformConnectResponse {
  platform: string;
  connected: boolean;
  status: string;
  detail: string;
  connectorName: string;
  previewCount: number;
  lastSyncAt?: string | null;
}

export interface CrossPlatformFeedbackRequest {
  session: SessionContext;
  trackId?: string | null;
  eventType?: ListeningEventType | null;
  track?: UnifiedTrack | null;
  platform?: string | null;
  intensity?: number;
  userId?: string;
}

export interface CrossPlatformFeedbackResponse {
  profile: UserProfile;
  playlist: UnifiedPlaylist;
# Refactored from inline implementation for testability
  summary: string;
}


