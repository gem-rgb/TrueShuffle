import type { ShuffleMetrics } from "../types";
import { formatPercent } from "../utils";

interface MetricCardsProps {
  metrics: ShuffleMetrics | null;
}

function scoreLabel(value: number | undefined): string {
  if (value == null) {
    return "-";
  }
  return formatPercent(value, 0);
}

function decimalLabel(value: number | undefined): string {
  if (value == null) {
    return "-";
  }
  return value.toFixed(2);
}

export function MetricCards({ metrics }: MetricCardsProps) {
  return (
    <div className="metric-cards">
      <div className="section-head">
        <div>
          <div className="section-label">Quality</div>
          <h2>Shuffle metrics</h2>
        </div>
      </div>

      <div className="metric-grid">
        <article className="metric-card">
          <span className="mini-label">Unique artists</span>
          <strong>{metrics?.uniqueArtists ?? "-"}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">Max run</span>
          <strong>{metrics?.maxArtistRun ?? "-"}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">Switch rate</span>
          <strong>{metrics?.artistSwitchRate != null ? `${Math.round(metrics.artistSwitchRate * 100)}%` : "-"}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">Entropy</span>
          <strong>{decimalLabel(metrics?.transitionEntropy)}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">Preference</span>
          <strong>{scoreLabel(metrics?.preferenceScore)}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">Diversity</span>
          <strong>{scoreLabel(metrics?.diversityScore)}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">Novelty</span>
          <strong>{scoreLabel(metrics?.noveltyScore)}</strong>
        </article>
        <article className="metric-card">
          <span className="mini-label">RL confidence</span>
          <strong>{scoreLabel(metrics?.rlConfidence)}</strong>
        </article>
      </div>
    </div>
  );
}
