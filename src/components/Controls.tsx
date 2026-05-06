import type { ShuffleSettings } from "../types";
import { clamp, formatPercent } from "../utils";

interface ControlsProps {
  settings: ShuffleSettings;
  busy: boolean;
  status: string;
  onSettingsChange: (next: ShuffleSettings) => void;
  onPreview: () => void;
  onShuffleAndPlay: () => void;
  onReload: () => void;
}

export function Controls({
  settings,
  busy,
  status,
  onSettingsChange,
  onPreview,
  onShuffleAndPlay,
  onReload
}: ControlsProps) {
  return (
    <div className="control-stack">
      <div className="section-head">
        <div>
          <div className="section-label">Shuffle</div>
          <h2>TrueShuffle controls</h2>
        </div>
        <span className="status-chip subtle">{busy ? "Working" : "Idle"}</span>
      </div>

      <div className="field-group">
        <label htmlFor="artist-spacing">
          Artist separation
          <span>{settings.artistSpacing} slots</span>
        </label>
        <input
          id="artist-spacing"
          type="range"
          min={1}
          max={6}
          value={settings.artistSpacing}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              artistSpacing: Number(event.target.value)
            })
          }
        />
      </div>

      <div className="field-group">
        <label htmlFor="recency-bias">
          Recency bias
          <span>{formatPercent(settings.recencyBias, 0)}</span>
        </label>
        <input
          id="recency-bias"
          type="range"
          min={0}
          max={1}
          step={0.05}
          value={settings.recencyBias}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              recencyBias: clamp(Number(event.target.value), 0, 1)
            })
          }
          />
      </div>

      <div className="field-group">
        <label htmlFor="preference-weight">
          Preference weight
          <span>{formatPercent(settings.preferenceWeight ?? 0.5, 0)}</span>
        </label>
        <input
          id="preference-weight"
          type="range"
          min={0}
          max={1}
          step={0.05}
          value={settings.preferenceWeight ?? 0.5}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              preferenceWeight: clamp(Number(event.target.value), 0, 1)
            })
          }
        />
      </div>

      <div className="field-group">
        <label htmlFor="diversity-weight">
          Diversity weight
          <span>{formatPercent(settings.diversityWeight ?? 0.3, 0)}</span>
        </label>
        <input
          id="diversity-weight"
          type="range"
          min={0}
          max={1}
          step={0.05}
          value={settings.diversityWeight ?? 0.3}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              diversityWeight: clamp(Number(event.target.value), 0, 1)
            })
          }
        />
      </div>

      <div className="field-group">
        <label htmlFor="novelty-weight">
          Novelty weight
          <span>{formatPercent(settings.noveltyWeight ?? 0.2, 0)}</span>
        </label>
        <input
          id="novelty-weight"
          type="range"
          min={0}
          max={1}
          step={0.05}
          value={settings.noveltyWeight ?? 0.2}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              noveltyWeight: clamp(Number(event.target.value), 0, 1)
            })
          }
        />
      </div>

      <div className="field-group">
        <label htmlFor="no-repeat-window">
          No-repeat window
          <span>{settings.noRepeatWindow} tracks</span>
        </label>
        <input
          id="no-repeat-window"
          type="range"
          min={0}
          max={16}
          value={settings.noRepeatWindow}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              noRepeatWindow: Number(event.target.value)
            })
          }
        />
      </div>

      <div className="field-group">
        <label htmlFor="seed">
          Seed
          <span>{settings.seed ?? "random"}</span>
        </label>
        <input
          id="seed"
          type="number"
          inputMode="numeric"
          value={settings.seed ?? ""}
          onChange={(event) =>
            onSettingsChange({
              ...settings,
              seed: event.target.value === "" ? undefined : Number(event.target.value)
            })
          }
          placeholder="Optional"
        />
      </div>

      <div className="button-row">
        <button className="button-secondary" type="button" onClick={onPreview} disabled={busy}>
          Preview order
        </button>
        <button className="button-primary" type="button" onClick={onShuffleAndPlay} disabled={busy}>
          TrueShuffle &amp; Play
        </button>
      </div>

      <button className="ghost-button" type="button" onClick={onReload} disabled={busy}>
        Reload selected playlist
      </button>

      <p className="muted">
        The objective weights do not need to sum to 1.0; they shape how strongly the engine favors taste, variety, and discovery.
      </p>

      <p className="muted status-copy">{status}</p>
    </div>
  );
}

