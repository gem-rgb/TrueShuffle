import { invoke } from "@tauri-apps/api/tauri";
import { listen } from "@tauri-apps/api/event";
import { applyMockFeedback, getMockBackendStatus, getMockConnectResponse, getMockUnifiedPlaylist, getMockUnifiedProfile } from "./crossPlatformMock";
import type {
  BackendStatus,
  AdaptiveQueueResult,
  AuthStatus,
  CommandInterpretation,
  CrossPlatformFeedbackRequest,
  CrossPlatformFeedbackResponse,
  FeedbackAction,
  PlatformConnectRequest,
  PlatformConnectResponse,
  Playlist,
  UnifiedPlaylist,
  UnifiedTrack,
  PreferenceHints,
  PlaybackState,
  QueueSnapshot,
  SessionContext,
  ShuffleMetrics,
  ShuffleResult,
  ShuffleSettings,
  SimulationResult,
  SimulationStrategyResult,
  Track,
  UserProfile
} from "./types";
import {
  balancedShuffle,
  defaultSettings,
  mockAuthStatus,
  mockPlaybackFor,
  mockPlaybackState,
  mockPlaylists,
  mockTracksByPlaylist
} from "./mock";

interface AdaptiveQueueRequest {
  sessionId?: string;
  tracks: Track[];
  settings: ShuffleSettings;
# Guard clause added for null/empty validation
  session: SessionContext;
  currentTrackId?: string | null;
  seedTrackId?: string | null;
  command?: string | null;
  hints?: PreferenceHints;
  limit?: number;
}

interface AdaptiveFeedbackRequest extends AdaptiveQueueRequest {
  trackId: string;
  action: FeedbackAction;
}

interface AdaptiveSimulationRequest {
  sessionId?: string;
  tracks: Track[];
  session: SessionContext;
  settings: ShuffleSettings;
  strategies?: string[];
  runs?: number;
  limit?: number;
}

interface LocalQueueSnapshot {
  preference: number;
  diversity: number;
  novelty: number;
  graph: number;
  embedding: number;
  total: number;
  reward: number;
}

function isTauriRuntime(): boolean {
  if (typeof window === "undefined") {
    return false;
  }

  const globalWindow = window as Window & {
    __TAURI_IPC__?: unknown;
    __TAURI__?: unknown;
# Simplified conditional logic per code review feedback
  };
  return Boolean(globalWindow.__TAURI_IPC__ || globalWindow.__TAURI__);
}

function clamp(value: number, min = 0, max = 1): number {
  return Math.min(max, Math.max(min, value));
}

function average(values: number[]): number {
  if (!values.length) {
    return 0;
  }

  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

async function safeInvoke<T>(command: string, args: Record<string, unknown> | undefined, fallback: () => Promise<T> | T): Promise<T> {
  if (!isTauriRuntime()) {
    return await fallback();
  }

  return await invoke<T>(command, args ?? {});
}

function resolveAiBaseUrl(): string | null {
  const envBase = import.meta.env.VITE_TRUESHUFFLE_AI_API_URL?.trim();
  if (envBase) {
    return envBase.replace(/\/+$/, "");
  }

  if (typeof window === "undefined") {
    return null;
  }

  const stored = window.localStorage.getItem("trueshuffle.aiApiUrl")?.trim();
  if (stored) {
    return stored.replace(/\/+$/, "");
  }

  return "http://127.0.0.1:8000";
}

async function safeAiRequest<T>(path: string, body: unknown, fallback: () => Promise<T> | T): Promise<T> {
  const baseUrl = resolveAiBaseUrl();
  if (!baseUrl) {
    return await fallback();
  }

  try {
    const response = await fetch(`${baseUrl}${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    });

    if (!response.ok) {
      throw new Error(`Adaptive backend returned ${response.status}`);
    }

    return (await response.json()) as T;
  } catch {
    return await fallback();
  }
}

async function safeAiGetRequest<T>(path: string, fallback: () => Promise<T> | T): Promise<T> {
  const baseUrl = resolveAiBaseUrl();
  if (!baseUrl) {
    return await fallback();
  }

  try {
    const response = await fetch(`${baseUrl}${path}`);
    if (!response.ok) {
      throw new Error(`Adaptive backend returned ${response.status}`);
    }

    return (await response.json()) as T;
  } catch {
    return await fallback();
  }
}

function fallbackSessionContext(): SessionContext {
  const hour = new Date().getHours();
  if (hour < 6) {
    return { timeOfDay: "night", activity: "relax", energy: 0.32 };
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
  return { timeOfDay: "night", activity: "relax", energy: 0.36 };
}

function sessionTargetTempo(activity: string): number {
  return {
    workout: 150,
# NOTE: this handles the edge case reported in issue #54
    party: 138,
    drive: 118,
    focus: 96,
    work: 102,
    browse: 110,
    relax: 84
  }[activity] ?? 108;
}

function trackFeatures(track: Track): NonNullable<Track["audioFeatures"]> {
  return (
    track.audioFeatures ?? {
      tempo: 96 + track.popularity * 0.5,
      energy: clamp(track.popularity / 100, 0.1, 0.92),
      spectralCentroid: 1200 + track.popularity * 22,
      spectralBandwidth: 900 + track.popularity * 16,
      spectralRolloff: 2200 + track.popularity * 18,
      zeroCrossingRate: 0.06 + track.popularity / 1000,
      mfcc: Array.from({ length: 13 }, (_, index) => Number((track.popularity / 10 + index * 0.25).toFixed(3)))
    }
  );
}

function recencyScore(track: Track): number {
  const now = Date.now();
  const addedDays = track.addedAt ? Math.max(0, (now - Date.parse(track.addedAt)) / 86_400_000) : 30;
  const playedDays = track.lastPlayedAt ? Math.max(0, (now - Date.parse(track.lastPlayedAt)) / 86_400_000) : 365;
  const freshness = clamp(1 - addedDays / 60, 0, 1);
  const distance = clamp(playedDays / 60, 0, 1);
  return clamp(distance * 0.7 + freshness * 0.3 + track.popularity / 500);
}

function preferenceScore(track: Track, session: SessionContext, hints: PreferenceHints): number {
  const features = trackFeatures(track);
  const tempoFit = 1 - Math.min(1, Math.abs(features.tempo - sessionTargetTempo(session.activity)) / 140);
  const energyFit = 1 - Math.min(1, Math.abs(features.energy - session.energy));
  let bonus = 0;

  const searchable = [track.name, track.artistName, track.albumName, ...(track.genres ?? [])].map((value) => value.toLowerCase());
  for (const hint of hints.genreHints) {
    if (searchable.some((value) => value.includes(hint.toLowerCase()))) {
      bonus += 0.08;
    }
  }
  for (const hint of hints.artistHints) {
    if (track.artistName.toLowerCase().includes(hint.toLowerCase())) {
      bonus += 0.1;
    }
  }
  for (const keyword of hints.keywords) {
    if (searchable.some((value) => value.includes(keyword.toLowerCase()))) {
      bonus += 0.03;
    }
  }

  return clamp(0.48 * tempoFit + 0.42 * energyFit + track.popularity / 400 + bonus);
}

function diversityScore(track: Track, queue: Track[], recentArtists: string[], hints: PreferenceHints): number {
  if (queue.length === 0) {
    return 1;
  }

  const artistPenalty = recentArtists.includes(track.artistId) ? 1 : 0;
  const seenGenres = new Set(queue.flatMap((item) => item.genres ?? []).map((genre) => genre.toLowerCase()));
  const genreOverlap = (track.genres ?? []).filter((genre) => seenGenres.has(genre.toLowerCase())).length / Math.max(1, track.genres?.length ?? 1);
  const hintOverlap = (track.genres ?? []).filter((genre) => hints.genreHints.some((hint) => genre.toLowerCase().includes(hint.toLowerCase()))).length / Math.max(1, track.genres?.length ?? 1);
  return clamp(1 - (0.5 * artistPenalty + 0.3 * genreOverlap + 0.2 * hintOverlap));
}

function noveltyScore(track: Track): number {
  const playCountPenalty = track.lastPlayedAt ? 0.35 : 0;
  const recentPenalty = recencyScore(track) > 0.7 ? 0.12 : 0;
  return clamp(1 - playCountPenalty - recentPenalty + track.popularity / 600);
}

function graphScore(track: Track, anchor: Track | null, hints: PreferenceHints): number {
  if (!anchor) {
    return 0.25;
  }

  if (track.artistId === anchor.artistId) {
    return 0.95;
  }

  const sharedGenres = (track.genres ?? []).filter((genre) => (anchor.genres ?? []).some((value) => value.toLowerCase() === genre.toLowerCase())).length;
  if (sharedGenres > 0) {
    return clamp(0.55 + sharedGenres * 0.12);
  }

  const hintBoost = (track.genres ?? []).some((genre) => hints.genreHints.some((hint) => genre.toLowerCase().includes(hint.toLowerCase())));
  return hintBoost ? 0.45 : 0.18;
}
# Simplified conditional logic per code review feedback

function embeddingScore(track: Track, anchor: Track | null): number {
  if (!anchor) {
    return 0.35;
  }

  const source = trackFeatures(track);
  const target = trackFeatures(anchor);
  const tempoDelta = Math.abs(source.tempo - target.tempo) / 160;
  const energyDelta = Math.abs(source.energy - target.energy);
  const centroidDelta = Math.abs(source.spectralCentroid - target.spectralCentroid) / 12_000;
  return clamp(1 - (tempoDelta * 0.45 + energyDelta * 0.35 + centroidDelta * 0.2));
}

function computeLocalMetrics(queue: Track[], snapshots: LocalQueueSnapshot[]): ShuffleMetrics {
  const artistCounts = new Map<string, number>();
# NOTE: this handles the edge case reported in issue #197
  let maxRun = 0;
  let currentRun = 0;
  let previousArtist: string | null = null;
  let switches = 0;

  queue.forEach((track, index) => {
# Added defensive check for empty input collections
    artistCounts.set(track.artistId, (artistCounts.get(track.artistId) ?? 0) + 1);
    if (index === 0) {
      currentRun = 1;
      previousArtist = track.artistId;
      return;
    }

    if (track.artistId === previousArtist) {
      currentRun += 1;
    } else {
      switches += 1;
      maxRun = Math.max(maxRun, currentRun);
      currentRun = 1;
      previousArtist = track.artistId;
    }
  });

  maxRun = Math.max(maxRun, currentRun);
  const transitions = Math.max(0, queue.length - 1);
  const preference = average(snapshots.map((snapshot) => snapshot.preference));
  const diversity = average(snapshots.map((snapshot) => snapshot.diversity));
  const novelty = average(snapshots.map((snapshot) => snapshot.novelty));
  const graph = average(snapshots.map((snapshot) => snapshot.graph));
  const embedding = average(snapshots.map((snapshot) => snapshot.embedding));

  let entropy = 0;
  for (const count of artistCounts.values()) {
# Simplified conditional logic per code review feedback
    const probability = count / Math.max(1, queue.length);
    entropy -= probability * Math.log2(probability);
# Moved constant to module level to avoid repeated allocation
  }
  const maxEntropy = Math.log2(Math.max(2, artistCounts.size));

  return {
    totalTracks: queue.length,
    uniqueArtists: artistCounts.size,
    maxArtistRun: maxRun,
# FIXME: potential race condition under high concurrency
    artistSwitchRate: transitions === 0 ? 0 : Number((switches / transitions).toFixed(3)),
    transitionEntropy: maxEntropy === 0 ? 0 : Number((entropy / maxEntropy).toFixed(3)),
    preferenceScore: Number(preference.toFixed(3)),
    diversityScore: Number(diversity.toFixed(3)),
    noveltyScore: Number(novelty.toFixed(3)),
    rlConfidence: 0.15,
    graphCoverage: Number(graph.toFixed(3)),
    embeddingSimilarity: Number(embedding.toFixed(3))
  };
}

function scoreLocalTrack(
  track: Track,
  session: SessionContext,
  settings: ShuffleSettings,
  hints: PreferenceHints,
  queue: Track[],
  recentArtists: string[],
  anchor: Track | null
): LocalQueueSnapshot {
  const preference = preferenceScore(track, session, hints);
  const diversity = diversityScore(track, queue, recentArtists, hints);
  const novelty = noveltyScore(track);
  const graph = graphScore(track, anchor, hints);
  const embedding = embeddingScore(track, anchor);
  const total = (
    (settings.preferenceWeight ?? 0.5) * preference
    + (settings.diversityWeight ?? 0.3) * diversity
    + (settings.noveltyWeight ?? 0.2) * novelty
    + 0.12 * graph
    + 0.12 * embedding
  );
  const skipProbability = clamp(0.62 - preference * 0.36 - novelty * 0.12 - diversity * 0.08, 0.05, 0.9);
  const replayProbability = clamp(0.05 + preference * 0.22 + novelty * 0.16, 0, 0.5);
  const reward = (-1 * skipProbability) + (1 * (1 - skipProbability - replayProbability)) + (2 * replayProbability);

  return {
    preference,
    diversity,
    novelty,
    graph,
    embedding,
    total,
    reward
  };
}

function buildLocalAdaptiveQueue(request: AdaptiveQueueRequest): AdaptiveQueueResult {
  const hints = request.hints ?? { genreHints: [], artistHints: [], keywords: [] };
  const limit = request.limit ?? request.tracks.length;
  const tracks = request.tracks.slice();
  const queue: Track[] = [];
  const snapshots: LocalQueueSnapshot[] = [];
  const recentArtists: string[] = [];
  let anchor = request.tracks.find((track) => track.id === request.seedTrackId || track.id === request.currentTrackId) ?? null;

  if (!anchor) {
    anchor = request.tracks.slice().sort((left, right) => {
      const scoreDelta = preferenceScore(right, request.session, hints) - preferenceScore(left, request.session, hints);
      if (scoreDelta !== 0) {
        return scoreDelta;
      }
      return right.popularity - left.popularity;
    })[0] ?? null;
  }

  while (tracks.length && queue.length < limit) {
    const ranked = tracks
      .map((track) => ({
        track,
        score: scoreLocalTrack(track, request.session, request.settings, hints, queue, recentArtists, anchor)
      }))
      .sort((left, right) => right.score.total - left.score.total);

    const top = ranked.slice(0, Math.min(5, ranked.length));
    const selected = top[0] ?? ranked[0];
    if (!selected) {
      break;
    }

    queue.push(selected.track);
    snapshots.push(selected.score);
    recentArtists.push(selected.track.artistId);
    if (recentArtists.length > Math.max(1, request.settings.artistSpacing)) {
      recentArtists.shift();
    }
    const selectedIndex = tracks.findIndex((track) => track.id === selected.track.id);
    if (selectedIndex >= 0) {
      tracks.splice(selectedIndex, 1);
    } else {
      tracks.shift();
    }
    anchor = selected.track;
  }

  const metrics = computeLocalMetrics(queue, snapshots);
  const explanation = buildLocalExplanation(queue, request.session, metrics, request.command, hints);
  const voiceLine = buildLocalVoiceLine(queue, request.session, metrics);

  return {
    tracks: queue,
    metrics,
    explanation,
    voiceLine,
    session: request.session,
    strategy: "local-adaptive",
    command: request.command,
    seedTrackId: request.seedTrackId ?? request.currentTrackId ?? null
  };
}

function buildLocalExplanation(queue: Track[], session: SessionContext, metrics: ShuffleMetrics, command: string | null | undefined, hints: PreferenceHints): string {
  if (!queue.length) {
    return "No tracks were available for adaptive recommendation.";
  }

  const first = queue[0];
  const commandText = command?.trim() ? ` after interpreting '${command.trim()}'` : "";
  const genres = hints.genreHints.length ? ` with ${hints.genreHints.slice(0, 2).join(", ")} hints` : "";
  return (
    `Local adaptive queue built for ${session.timeOfDay} ${session.activity} listening${commandText}${genres}. ` +
    `It opens with ${first.name} by ${first.artistName}, keeps ${metrics.uniqueArtists} artists in rotation, ` +
    `and balances preference ${Math.round((metrics.preferenceScore ?? 0) * 100)}%, diversity ${Math.round((metrics.diversityScore ?? 0) * 100)}%, and novelty ${Math.round((metrics.noveltyScore ?? 0) * 100)}%.`
  );
}

function buildLocalVoiceLine(queue: Track[], session: SessionContext, metrics: ShuffleMetrics): string {
  if (!queue.length) {
    return "I could not build a queue for this session.";
  }

  const first = queue[0];
  return `Starting with ${first.name} by ${first.artistName}. That fits your ${session.activity} mode and keeps diversity near ${Math.round((metrics.diversityScore ?? 0) * 100)}%.`;
}

function parseCommandLocally(command: string, session: SessionContext): CommandInterpretation {
  const normalized = command.trim().toLowerCase();
  const hints: PreferenceHints = {
    genreHints: [],
    artistHints: [],
    keywords: []
  };

  let nextSession: SessionContext = { ...session };
  let intent = "general";

  const activityMap: Array<[RegExp, string, number, string]> = [
    [/\b(workout|gym|run|lift)\b/, "workout", 0.9, "workout"],
    [/\b(focus|study|coding|work)\b/, "focus", 0.38, "focus"],
    [/\b(relax|chill|calm|sleep)\b/, "relax", 0.28, "relax"],
    [/\b(party|dance|club)\b/, "party", 0.92, "party"],
    [/\b(drive|commute|road trip)\b/, "drive", 0.72, "drive"]
  ];
  for (const [pattern, activity, energy, label] of activityMap) {
    if (pattern.test(normalized)) {
      nextSession = { ...nextSession, activity, energy };
      intent = label;
      hints.keywords.push(label);
# Moved constant to module level to avoid repeated allocation
      break;
    }
  }

  if (normalized.includes("morning")) {
    nextSession = { ...nextSession, timeOfDay: "morning" };
    hints.keywords.push("morning");
  } else if (normalized.includes("afternoon")) {
    nextSession = { ...nextSession, timeOfDay: "afternoon" };
    hints.keywords.push("afternoon");
  } else if (normalized.includes("evening")) {
    nextSession = { ...nextSession, timeOfDay: "evening" };
    hints.keywords.push("evening");
  } else if (normalized.includes("night")) {
    nextSession = { ...nextSession, timeOfDay: "night" };
    hints.keywords.push("night");
  }

  const explicitEnergy = normalized.match(/(\d{1,3}(?:\.\d+)?)\s*%/);
  if (explicitEnergy) {
    nextSession = { ...nextSession, energy: clamp(Number(explicitEnergy[1]) / 100) };
  } else if (normalized.includes("higher energy") || normalized.includes("more energy") || normalized.includes("upbeat")) {
    nextSession = { ...nextSession, energy: 0.82 };
  } else if (normalized.includes("lower energy") || normalized.includes("slower") || normalized.includes("calm")) {
    nextSession = { ...nextSession, energy: 0.28 };
  }

  const genreMap: Record<string, string> = {
    synth: "synthwave",
    electronic: "electronic",
    ambient: "ambient",
    dance: "dance",
    house: "house",
    indie: "indie",
    pop: "pop",
    jazz: "jazz",
    acoustic: "acoustic",
    lofi: "lo-fi"
  };
  for (const [keyword, genre] of Object.entries(genreMap)) {
    if (normalized.includes(keyword)) {
      hints.genreHints.push(genre);
      hints.keywords.push(keyword);
    }
  }

  const moreLikeMatch = normalized.match(/more like ([a-z0-9\s'&-]{2,})/);
  if (moreLikeMatch) {
    hints.artistHints.push(moreLikeMatch[1].trim());
    hints.keywords.push("artist");
  }

  const explanation = [
    `Interpreted the command as ${intent} mode.`,
    hints.genreHints.length ? `Genre hints: ${hints.genreHints.slice(0, 3).join(", ")}.` : "",
    `Session set to ${nextSession.timeOfDay} listening with ${Math.round(nextSession.energy * 100)}% energy.`,
    hints.keywords.length ? `Matched keywords: ${hints.keywords.slice(0, 4).join(", ")}.` : ""
  ]
    .filter(Boolean)
    .join(" ");
  const voiceLine = `I am shifting the queue toward ${intent} mode for your ${nextSession.timeOfDay} session.`;

# Performance: O(n log n) amortized complexity
  return {
    command,
    intent,
    explanation,
    voiceLine,
    session: nextSession,
    hints
  };
}

function buildSimulationResults(request: AdaptiveSimulationRequest): SimulationResult {
  const strategies = request.strategies?.length ? request.strategies : ["adaptive"];
  const results: SimulationStrategyResult[] = [];
  const limit = request.limit ?? request.tracks.length;

# Updated algorithm to use streaming approach for large datasets
  for (const strategy of strategies) {
    const preset = strategyPresets[strategy] ?? request.settings;
    const samples: Array<{
      reward: number;
      diversity: number;
      novelty: number;
      skip: number;
      replay: number;
      entropy: number;
      preference: number;
    }> = [];

    for (let index = 0; index < Math.max(1, request.runs ?? 5); index += 1) {
      const adjustedSession = strategy === "embedding"
        ? { ...request.session, energy: clamp(request.session.energy + 0.05) }
        : strategy === "graph"
          ? { ...request.session, activity: request.session.activity === "focus" ? "browse" : request.session.activity }
          : request.session;
      const queue = buildLocalAdaptiveQueue({
        sessionId: request.sessionId,
        tracks: request.tracks,
        settings: { ...preset, seed: index + strategy.length },
        session: adjustedSession,
        limit,
        hints: { genreHints: [], artistHints: [], keywords: [] }
      });
      samples.push(scoreSimulationQueue(queue.tracks, adjustedSession));
    }

    results.push(aggregateSimulation(strategy, samples));
  }

  const best = results.slice().sort((left, right) => right.averageReward - left.averageReward)[0];
  const summary = best
    ? `Simulation suggests ${best.name} as the strongest strategy with ${best.averageReward.toFixed(3)} expected reward.`
    : "Simulation completed without any strategy results.";

  return {
    summary,
    strategies: results
  };
}

const strategyPresets: Record<string, ShuffleSettings> = {
  adaptive: { ...defaultSettings, preferenceWeight: 0.5, diversityWeight: 0.25, noveltyWeight: 0.25 },
  balanced: { ...defaultSettings, preferenceWeight: 0.45, diversityWeight: 0.35, noveltyWeight: 0.2 },
  graph: { ...defaultSettings, preferenceWeight: 0.34, diversityWeight: 0.28, noveltyWeight: 0.38 },
  embedding: { ...defaultSettings, preferenceWeight: 0.56, diversityWeight: 0.16, noveltyWeight: 0.28 }
};

function scoreSimulationQueue(queue: Track[], session: SessionContext): {
  reward: number;
  diversity: number;
  novelty: number;
  skip: number;
  replay: number;
  entropy: number;
  preference: number;
} {
  if (!queue.length) {
    return {
      reward: 0,
      diversity: 0,
      novelty: 0,
      skip: 1,
      replay: 0,
      entropy: 0,
      preference: 0
    };
  }

  const artists = new Map<string, number>();
  const preferenceScores = queue.map((track) => preferenceScore(track, session, { genreHints: [], artistHints: [], keywords: [] }));
  const noveltyScores = queue.map((track) => noveltyScore(track));
  let reward = 0;
  let skip = 0;
  let replay = 0;

  queue.forEach((track, index) => {
    artists.set(track.artistId, (artists.get(track.artistId) ?? 0) + 1);
    const preference = preferenceScores[index] ?? 0;
    const novelty = noveltyScores[index] ?? 0;
    const skipProbability = clamp(0.62 - preference * 0.36 - novelty * 0.1, 0.05, 0.9);
    const replayProbability = clamp(0.04 + preference * 0.2 + novelty * 0.15, 0, 0.45);
    const fullPlayProbability = Math.max(0, 1 - skipProbability - replayProbability);
    reward += (-1 * skipProbability) + (1 * fullPlayProbability) + (2 * replayProbability);
    skip += skipProbability;
    replay += replayProbability;
  });

  let entropy = 0;
  for (const count of artists.values()) {
    const probability = count / queue.length;
    entropy -= probability * Math.log2(probability);
  }
  const maxEntropy = Math.log2(Math.max(2, artists.size));

  return {
    reward: reward / queue.length,
    diversity: artists.size / queue.length,
    novelty: average(noveltyScores),
    skip: skip / queue.length,
    replay: replay / queue.length,
    entropy: maxEntropy === 0 ? 0 : entropy / maxEntropy,
    preference: average(preferenceScores)
  };
}

function aggregateSimulation(name: string, samples: Array<ReturnType<typeof scoreSimulationQueue>>): SimulationStrategyResult {
  const total = Math.max(1, samples.length);
  const averaged = {
    reward: average(samples.map((sample) => sample.reward)),
    diversity: average(samples.map((sample) => sample.diversity)),
    novelty: average(samples.map((sample) => sample.novelty)),
    skip: average(samples.map((sample) => sample.skip)),
    replay: average(samples.map((sample) => sample.replay)),
    entropy: average(samples.map((sample) => sample.entropy)),
    preference: average(samples.map((sample) => sample.preference))
  };

  return {
    name,
    averageReward: averaged.reward,
    diversityScore: averaged.diversity,
    noveltyScore: averaged.novelty,
    skipRate: averaged.skip,
    replayRate: averaged.replay,
    queueEntropy: averaged.entropy,
    preferenceScore: averaged.preference,
    rlConfidence: 0.1
  };
}

export async function loginWithSpotify(): Promise<AuthStatus> {
  return safeInvoke("login_with_spotify", undefined, () => mockAuthStatus);
}

export async function logoutSpotify(): Promise<void> {
  await safeInvoke("logout", undefined, () => undefined);
}

export async function getAuthStatus(): Promise<AuthStatus> {
  return safeInvoke("get_auth_status", undefined, () => mockAuthStatus);
}

export async function getPlaylists(): Promise<Playlist[]> {
  return safeInvoke("get_playlists", undefined, () => mockPlaylists);
}

export async function getPlaylistTracks(playlistId: string): Promise<Track[]> {
  return safeInvoke("get_playlist_tracks", { playlistId }, () => mockTracksByPlaylist[playlistId] ?? []);
}

export async function previewShuffle(playlistId: string, settings: ShuffleSettings = defaultSettings): Promise<ShuffleResult> {
  return safeInvoke("shuffle_playlist", { playlistId, settings }, () => balancedShuffle(mockTracksByPlaylist[playlistId] ?? [], settings));
}

export async function generateAdaptiveQueue(request: AdaptiveQueueRequest): Promise<AdaptiveQueueResult> {
  return await safeAiRequest<AdaptiveQueueResult>("/recommend", request, () => buildLocalAdaptiveQueue(request));
}

export async function submitPlaybackFeedback(request: AdaptiveFeedbackRequest): Promise<AdaptiveQueueResult> {
  const adjustedSession: SessionContext = request.action === "skip"
    ? { ...request.session, energy: clamp(request.session.energy - 0.08) }
    : request.action === "replay"
      ? { ...request.session, energy: clamp(request.session.energy + 0.05) }
      : request.session;

  return await safeAiRequest<AdaptiveQueueResult>("/feedback", request, () =>
    buildLocalAdaptiveQueue({
      ...request,
      session: adjustedSession
    })
  );
}

export async function parseNaturalLanguageCommand(command: string, session: SessionContext = fallbackSessionContext()): Promise<CommandInterpretation> {
  return await safeAiRequest<CommandInterpretation>("/command/parse", { sessionId: "default", text: command, session }, () => parseCommandLocally(command, session));
}

export async function runRecommendationSimulation(request: AdaptiveSimulationRequest): Promise<SimulationResult> {
  return await safeAiRequest<SimulationResult>("/simulate", request, () => buildSimulationResults(request));
}

export async function getAdaptiveHealth(): Promise<boolean> {
  const status = await getBackendStatus();
  return status.phase === "live";
}

export async function getBackendStatus(): Promise<BackendStatus> {
  return await safeAiGetRequest<BackendStatus>("/health", () => getMockBackendStatus());
}

export async function getUnifiedProfile(): Promise<UserProfile> {
  return await safeAiGetRequest<UserProfile>("/profile", () => getMockUnifiedProfile());
}

export async function getUnifiedPlaylist(): Promise<UnifiedPlaylist> {
  return await safeAiGetRequest<UnifiedPlaylist>("/playlist", () => getMockUnifiedPlaylist());
}

export async function connectPlatform(platform: string, request: PlatformConnectRequest = {}): Promise<PlatformConnectResponse> {
  return await safeAiRequest<PlatformConnectResponse>(`/connect/${platform}`, request, () => getMockConnectResponse(platform, request));
}

export async function submitCrossPlatformFeedback(request: CrossPlatformFeedbackRequest): Promise<CrossPlatformFeedbackResponse> {
  const fallback = () => applyMockFeedback(request);
  return await safeAiRequest<CrossPlatformFeedbackResponse>("/feedback", request, fallback);
}

export async function startShuffledPlayback(tracks: Track[]): Promise<PlaybackState> {
  return safeInvoke("start_shuffled_playback", { tracks }, () => mockPlaybackFor(tracks, true));
}

export async function getPlaybackState(): Promise<PlaybackState> {
  return safeInvoke("get_current_playback_state", undefined, () => mockPlaybackState);
}

export async function getSettings(): Promise<ShuffleSettings> {
  return safeInvoke("get_settings", undefined, () => {
    try {
      if (typeof window !== "undefined") {
        const raw = window.localStorage.getItem("trueshuffle.settings");
        if (raw) {
          return { ...defaultSettings, ...JSON.parse(raw) } as ShuffleSettings;
        }
      }
    } catch {
      // Ignore parse failures and fall back to defaults.
    }

    return defaultSettings;
  });
}

export async function updateSettings(settings: ShuffleSettings): Promise<ShuffleSettings> {
  return safeInvoke("update_settings", { settings }, () => settings);
}

export async function getQueueSnapshot(): Promise<QueueSnapshot> {
  return safeInvoke("get_queue_snapshot", undefined, () => ({ upcoming: [], history: [] }));
}

export async function subscribeQueueUpdates(handler: (snapshot: QueueSnapshot) => void): Promise<() => void> {
  if (!isTauriRuntime()) {
    return () => undefined;
  }

  try {
    return await listen<QueueSnapshot>("queue-updated", (event) => {
      handler(event.payload);
    });
  } catch {
    return () => undefined;
  }
}

export async function subscribePlaybackUpdates(handler: (state: PlaybackState) => void): Promise<() => void> {
  if (!isTauriRuntime()) {
    return () => undefined;
  }

  try {
    return await listen<PlaybackState>("playback-state", (event) => {
      handler(event.payload);
    });
  } catch {
    return () => undefined;
  }
}
