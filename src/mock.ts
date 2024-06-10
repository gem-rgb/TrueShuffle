import type {
  AudioFeatures,
  AuthStatus,
  PlaybackState,
  Playlist,
  ShuffleMetrics,
  ShuffleResult,
  ShuffleSettings,
  Track
} from "./types";

interface ArtistDefinition {
  id: string;
  name: string;
}

interface TrackSpec {
  title: string;
  artistIndex: number;
  album: string;
  durationMs: number;
  popularity: number;
  addedDaysAgo: number;
  lastPlayedDaysAgo?: number;
}

const playlistGenres: Record<string, string[]> = {
  "midnight-drive": ["synthwave", "electronic", "night-drive"],
  "focus-bloom": ["ambient", "instrumental", "lo-fi"],
  "festival-heat": ["dance", "electronic", "pop"]
};

const artists: ArtistDefinition[] = [
  { id: "artist-aurora", name: "Aurora Lane" },
  { id: "artist-cinder", name: "Cinder Club" },
  { id: "artist-neon", name: "Neon Arcade" },
  { id: "artist-boreal", name: "Boreal Static" },
  { id: "artist-velvet", name: "Velvet Hour" },
  { id: "artist-pulse", name: "Pulse Theory" },
  { id: "artist-slate", name: "Slate Harbor" },
  { id: "artist-echo", name: "Echo Bloom" }
];

const demoLibrary: Array<{
  playlist: Playlist;
  specs: TrackSpec[];
}> = [
  {
    playlist: {
      id: "midnight-drive",
      name: "Midnight Drive",
      ownerName: "TrueShuffle Lab",
      trackCount: 8,
      accent: "#7ef0c7",
      description: "Warm, nocturnal synths with a tight artist spread."
    },
    specs: [
      { title: "Halogen Lights", artistIndex: 0, album: "Nocturne Engine", durationMs: 214000, popularity: 72, addedDaysAgo: 11, lastPlayedDaysAgo: 28 },
      { title: "Glass Satellite", artistIndex: 1, album: "Nocturne Engine", durationMs: 206000, popularity: 61, addedDaysAgo: 18, lastPlayedDaysAgo: 44 },
      { title: "Late Exit", artistIndex: 2, album: "Afterglow Tape", durationMs: 198000, popularity: 79, addedDaysAgo: 7, lastPlayedDaysAgo: 12 },
      { title: "Velvet Interchange", artistIndex: 4, album: "Afterglow Tape", durationMs: 223000, popularity: 66, addedDaysAgo: 22, lastPlayedDaysAgo: 31 },
      { title: "Boreal Nights", artistIndex: 3, album: "Static Weather", durationMs: 242000, popularity: 58, addedDaysAgo: 33, lastPlayedDaysAgo: 49 },
      { title: "Circuit Reverie", artistIndex: 5, album: "Static Weather", durationMs: 191000, popularity: 70, addedDaysAgo: 14, lastPlayedDaysAgo: 27 },
      { title: "Harbor Neon", artistIndex: 6, album: "Lantern Coast", durationMs: 219000, popularity: 64, addedDaysAgo: 4, lastPlayedDaysAgo: 9 },
      { title: "Soft Relay", artistIndex: 7, album: "Lantern Coast", durationMs: 208000, popularity: 55, addedDaysAgo: 25, lastPlayedDaysAgo: 37 }
    ]
  },
  {
    playlist: {
      id: "focus-bloom",
      name: "Focus Bloom",
      ownerName: "TrueShuffle Lab",
      trackCount: 8,
      accent: "#ffcc70",
      description: "Instrumental momentum without artist clumping."
    },
    specs: [
      { title: "Quiet Geometry", artistIndex: 5, album: "Lines and Matter", durationMs: 187000, popularity: 65, addedDaysAgo: 8, lastPlayedDaysAgo: 21 },
      { title: "Paper Signal", artistIndex: 7, album: "Lines and Matter", durationMs: 176000, popularity: 62, addedDaysAgo: 12, lastPlayedDaysAgo: 18 },
      { title: "Low Orbit", artistIndex: 1, album: "Attention Span", durationMs: 205000, popularity: 71, addedDaysAgo: 5, lastPlayedDaysAgo: 13 },
      { title: "Vector Morning", artistIndex: 0, album: "Attention Span", durationMs: 199000, popularity: 67, addedDaysAgo: 17, lastPlayedDaysAgo: 23 },
      { title: "Cascade Memo", artistIndex: 6, album: "Mind Thread", durationMs: 211000, popularity: 59, addedDaysAgo: 27, lastPlayedDaysAgo: 42 },
      { title: "Blue Marker", artistIndex: 2, album: "Mind Thread", durationMs: 203000, popularity: 74, addedDaysAgo: 9, lastPlayedDaysAgo: 15 },
      { title: "Silent Drift", artistIndex: 4, album: "Mind Thread", durationMs: 190000, popularity: 57, addedDaysAgo: 15, lastPlayedDaysAgo: 29 },
      { title: "Slow Bloom", artistIndex: 3, album: "Attention Span", durationMs: 224000, popularity: 60, addedDaysAgo: 20, lastPlayedDaysAgo: 34 }
    ]
  },
  {
    playlist: {
      id: "festival-heat",
      name: "Festival Heat",
      ownerName: "TrueShuffle Lab",
      trackCount: 8,
      accent: "#ff8d6b",
      description: "Fast cuts, energetic artists, and controlled chaos."
    },
    specs: [
      { title: "Signal Fire", artistIndex: 2, album: "Open Circuit", durationMs: 193000, popularity: 82, addedDaysAgo: 2, lastPlayedDaysAgo: 5 },
      { title: "Run the Line", artistIndex: 3, album: "Open Circuit", durationMs: 189000, popularity: 77, addedDaysAgo: 10, lastPlayedDaysAgo: 14 },
      { title: "Solar Rush", artistIndex: 0, album: "Peak Voltage", durationMs: 205000, popularity: 84, addedDaysAgo: 6, lastPlayedDaysAgo: 8 },
      { title: "Heat Mirage", artistIndex: 5, album: "Peak Voltage", durationMs: 201000, popularity: 68, addedDaysAgo: 13, lastPlayedDaysAgo: 19 },
      { title: "Crowd Pressure", artistIndex: 1, album: "After Hours Riot", durationMs: 214000, popularity: 75, addedDaysAgo: 4, lastPlayedDaysAgo: 7 },
      { title: "Pulse Breaker", artistIndex: 6, album: "After Hours Riot", durationMs: 196000, popularity: 69, addedDaysAgo: 16, lastPlayedDaysAgo: 22 },
      { title: "Fireline", artistIndex: 4, album: "Peak Voltage", durationMs: 188000, popularity: 73, addedDaysAgo: 11, lastPlayedDaysAgo: 16 },
      { title: "Bright Collapse", artistIndex: 7, album: "Open Circuit", durationMs: 222000, popularity: 63, addedDaysAgo: 19, lastPlayedDaysAgo: 26 }
    ]
  }
];

function isoDaysAgo(daysAgo: number): string {
  return new Date(Date.now() - daysAgo * 86_400_000).toISOString();
}

function makeAudioFeatures(playlistId: string, spec: TrackSpec, index: number): AudioFeatures {
  const popularityFactor = spec.popularity / 100;
  const tempo = Math.min(190, Math.max(68, 74 + popularityFactor * 70 + index * 3.2));
  const energy = Math.min(1, Math.max(0.1, 0.28 + popularityFactor * 0.52 + (index % 3) * 0.05));
  const spectralCentroid = 1200 + popularityFactor * 2400 + index * 90;
  const spectralBandwidth = 900 + popularityFactor * 1600 + index * 75;
  const spectralRolloff = 2200 + popularityFactor * 3100 + index * 110;
  const zeroCrossingRate = Math.min(0.35, 0.06 + popularityFactor * 0.08 + index * 0.004);
  const mfcc = Array.from({ length: 13 }, (_, featureIndex) => Number((energy * 10 + featureIndex * 0.35 + index * 0.2).toFixed(3)));

  return {
    tempo,
    energy,
    spectralCentroid,
    spectralBandwidth,
    spectralRolloff,
    zeroCrossingRate,
    mfcc
  };
}

function makeTrack(playlistId: string, spec: TrackSpec, index: number): Track {
  const artist = artists[spec.artistIndex % artists.length];
  const slug = spec.title.toLowerCase().replace(/[^a-z0-9]+/g, "-");
  return {
    id: `${playlistId}-${slug}-${index}`,
    uri: `spotify:track:${playlistId}-${slug}-${index}`,
    name: spec.title,
    artistId: artist.id,
    artistName: artist.name,
    albumName: spec.album,
    durationMs: spec.durationMs,
    popularity: spec.popularity,
    addedAt: isoDaysAgo(spec.addedDaysAgo),
    lastPlayedAt: spec.lastPlayedDaysAgo == null ? undefined : isoDaysAgo(spec.lastPlayedDaysAgo),
    genres: playlistGenres[playlistId] ?? ["eclectic"],
    audioFeatures: makeAudioFeatures(playlistId, spec, index)
  };
}

function buildDemoTracks(playlistId: string, specs: TrackSpec[]): Track[] {
  return specs.map((spec, index) => makeTrack(playlistId, spec, index));
}

export const mockTracksByPlaylist: Record<string, Track[]> = Object.fromEntries(
  demoLibrary.map(({ playlist, specs }) => [playlist.id, buildDemoTracks(playlist.id, specs)])
);

export const mockPlaylists: Playlist[] = demoLibrary.map(({ playlist }) => playlist);

export const defaultSettings: ShuffleSettings = {
  artistSpacing: 2,
  recencyBias: 0.7,
  noRepeatWindow: 8,
  seed: undefined,
  preferenceWeight: 0.5,
  diversityWeight: 0.3,
  noveltyWeight: 0.2
};

export const mockAuthStatus: AuthStatus = {
  authenticated: false,
  demoMode: true,
  displayName: "Demo Mode"
};

export const mockPlaybackState: PlaybackState = {
  isPlaying: false,
  currentTrackId: mockTracksByPlaylist[mockPlaylists[0].id]?.[0]?.id ?? null,
  currentTrackName: mockTracksByPlaylist[mockPlaylists[0].id]?.[0]?.name ?? null,
  progressMs: 0,
  deviceName: "Demo Device",
  shuffleEnabled: false
};

function mulberry32(seed: number): () => number {
  let t = seed >>> 0;
  return () => {
    t += 0x6d2b79f5;
    let r = Math.imul(t ^ (t >>> 15), t | 1);
    r ^= r + Math.imul(r ^ (r >>> 7), r | 61);
    return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
  };
}

function trackRecencyScore(track: Track, settings: ShuffleSettings): number {
  const now = Date.now();
  const addedDays = track.addedAt ? Math.max(0, (now - Date.parse(track.addedAt)) / 86_400_000) : 30;
  const playedDays = track.lastPlayedAt ? Math.max(0, (now - Date.parse(track.lastPlayedAt)) / 86_400_000) : 365;
  const freshness = addedDays / 30;
  const distance = playedDays / 30;
  return settings.recencyBias * distance + (1 - settings.recencyBias) * freshness + track.popularity / 500;
}

function chooseTrackIndex(tracks: Track[], settings: ShuffleSettings, rng: () => number): number {
  if (tracks.length <= 1) {
    return 0;
  }

  const scored = tracks
    .map((track, index) => ({
      index,
      score: trackRecencyScore(track, settings) + rng() * 0.25
    }))
    .sort((left, right) => right.score - left.score);

  const top = scored.slice(0, Math.min(3, scored.length));
  const weights = top.map((entry) => Math.max(0.2, entry.score));
  const total = weights.reduce((sum, value) => sum + value, 0);
  let cursor = rng() * total;

  for (let index = 0; index < top.length; index += 1) {
    cursor -= weights[index];
    if (cursor <= 0) {
      return top[index]?.index ?? 0;
    }
  }

  return top[0]?.index ?? 0;
}

function entropy(sequence: Track[]): number {
  if (!sequence.length) {
    return 0;
  }

  const counts = new Map<string, number>();
  for (const track of sequence) {
    counts.set(track.artistId, (counts.get(track.artistId) ?? 0) + 1);
  }

  const total = sequence.length;
  let value = 0;
  for (const count of counts.values()) {
    const probability = count / total;
    value -= probability * Math.log2(probability);
  }

  const maxEntropy = Math.log2(Math.max(2, counts.size));
  return Number((value / maxEntropy).toFixed(3));
}

function computeMetrics(sequence: Track[]): ShuffleMetrics {
  const artistCounts = new Map<string, number>();
  let maxRun = 0;
  let currentRun = 0;
  let previousArtist: string | null = null;
  let switches = 0;

  sequence.forEach((track, index) => {
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
  const transitions = Math.max(0, sequence.length - 1);

  return {
    totalTracks: sequence.length,
    uniqueArtists: artistCounts.size,
    maxArtistRun: maxRun,
    artistSwitchRate: transitions === 0 ? 1 : Number((switches / transitions).toFixed(3)),
    transitionEntropy: entropy(sequence)
  };
}

export function balancedShuffle(tracks: Track[], settings: ShuffleSettings = defaultSettings): ShuffleResult {
  const seed = settings.seed ?? (Date.now() & 0xffffffff);
  const rng = mulberry32(seed);
  const artistBuckets = new Map<string, Track[]>();

  for (const track of tracks) {
    const bucket = artistBuckets.get(track.artistId) ?? [];
    bucket.push(track);
    artistBuckets.set(track.artistId, bucket);
  }

  for (const bucket of artistBuckets.values()) {
    bucket.sort((left, right) => {
      const scoreDelta = trackRecencyScore(right, settings) - trackRecencyScore(left, settings);
      if (scoreDelta !== 0) {
        return scoreDelta;
      }
      return left.name.localeCompare(right.name);
    });
  }

  const queue: Track[] = [];
  const recentArtists: string[] = [];
  const windowSize = Math.max(1, settings.artistSpacing);

  while (queue.length < tracks.length) {
    const available = [...artistBuckets.entries()].filter(([, bucket]) => bucket.length > 0);
    if (!available.length) {
      break;
    }

    const blocked = new Set(recentArtists.slice(-windowSize));
    const preferred = available.filter(([artist]) => !blocked.has(artist));
    const candidateArtists = preferred.length > 0 ? preferred : available;
    candidateArtists.sort((left, right) => right[1].length - left[1].length || left[0].localeCompare(right[0]));

    const topCandidates = candidateArtists.slice(0, Math.min(3, candidateArtists.length));
    const weights = topCandidates.map(([, bucket]) => Math.pow(bucket.length, 1.35));
    const total = weights.reduce((sum, value) => sum + value, 0);
    let choice = rng() * total;
    let selectedArtist = topCandidates[0]?.[0] ?? candidateArtists[0]?.[0] ?? "";

    for (let index = 0; index < topCandidates.length; index += 1) {
      choice -= weights[index];
      if (choice <= 0) {
        selectedArtist = topCandidates[index]?.[0] ?? selectedArtist;
        break;
      }
    }

    const bucket = artistBuckets.get(selectedArtist);
    if (!bucket || bucket.length === 0) {
      break;
    }

    const trackIndex = chooseTrackIndex(bucket, settings, rng);
    const [track] = bucket.splice(trackIndex, 1);
    if (!track) {
      continue;
    }

    queue.push(track);
    recentArtists.push(selectedArtist);
    if (recentArtists.length > windowSize) {
      recentArtists.shift();
    }
  }

  return {
    tracks: queue,
    metrics: computeMetrics(queue)
  };
}

export function mockPlaybackFor(tracks: Track[], isPlaying = false): PlaybackState {
  return {
    isPlaying,
    currentTrackId: tracks[0]?.id ?? null,
    currentTrackName: tracks[0]?.name ?? null,
    progressMs: 0,
    deviceName: "TrueShuffle Demo",
    shuffleEnabled: true
  };
}
