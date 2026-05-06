import type { FeedbackAction, SessionContext, SimulationResult } from "../types";

interface AdaptivePanelProps {
  session: SessionContext;
  command: string;
  voiceEnabled: boolean;
  busy: boolean;
  explanation: string;
  voiceLine: string;
  simulation: SimulationResult | null;
  onSessionChange: (next: SessionContext) => void;
  onCommandChange: (value: string) => void;
  onVoiceEnabledChange: (enabled: boolean) => void;
  onApplyCommand: () => void;
  onRegenerate: () => void;
  onFeedback: (action: FeedbackAction) => void;
  onRunSimulation: () => void;
}

export function AdaptivePanel({
  session,
  command,
  voiceEnabled,
  busy,
  explanation,
  voiceLine,
  simulation,
  onSessionChange,
  onCommandChange,
  onVoiceEnabledChange,
  onApplyCommand,
  onRegenerate,
  onFeedback,
  onRunSimulation
}: AdaptivePanelProps) {
  const bestStrategy = simulation?.strategies.slice().sort((left, right) => right.averageReward - left.averageReward)[0] ?? null;

  return (
    <div className="adaptive-stack">
      <div className="section-head">
        <div>
          <div className="section-label">Adaptive AI</div>
          <h2>Session brain</h2>
        </div>
        <span className={`status-chip ${voiceEnabled ? "success" : "subtle"}`}>{voiceEnabled ? "Voice on" : "Silent"}</span>
      </div>

      <div className="context-grid">
        <label className="field-group" htmlFor="time-of-day">
          <span className="mini-label">Time of day</span>
          <select
            id="time-of-day"
            value={session.timeOfDay}
            onChange={(event) => onSessionChange({ ...session, timeOfDay: event.target.value })}
          >
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
            <option value="night">Night</option>
          </select>
        </label>

        <label className="field-group" htmlFor="activity-mode">
          <span className="mini-label">Activity</span>
          <select
            id="activity-mode"
            value={session.activity}
            onChange={(event) => onSessionChange({ ...session, activity: event.target.value })}
          >
            <option value="focus">Focus</option>
            <option value="work">Work</option>
            <option value="workout">Workout</option>
            <option value="drive">Drive</option>
            <option value="browse">Browse</option>
            <option value="relax">Relax</option>
            <option value="party">Party</option>
          </select>
        </label>

        <div className="field-group">
          <label htmlFor="session-energy">
            Energy
            <span>{Math.round(session.energy * 100)}%</span>
          </label>
          <input
            id="session-energy"
            type="range"
            min={0}
            max={1}
            step={0.05}
            value={session.energy}
            onChange={(event) => onSessionChange({ ...session, energy: Number(event.target.value) })}
          />
        </div>
      </div>

      <label className="search-box" htmlFor="nl-command">
        <span>Natural language command</span>
        <input
          id="nl-command"
          type="search"
          value={command}
          placeholder="e.g. focus music with more synthwave and higher energy"
          onChange={(event) => onCommandChange(event.target.value)}
        />
      </label>

      <div className="button-row">
        <button className="button-secondary" type="button" disabled={busy} onClick={onApplyCommand}>
          Interpret command
        </button>
        <button className="button-primary" type="button" disabled={busy} onClick={onRegenerate}>
          Regenerate queue
        </button>
      </div>

      <div className="feedback-row">
        <button className="ghost-button" type="button" disabled={busy} onClick={() => onFeedback("skip")}>
          Mark skip
        </button>
        <button className="ghost-button" type="button" disabled={busy} onClick={() => onFeedback("full_play")}>
          Full play
        </button>
        <button className="ghost-button" type="button" disabled={busy} onClick={() => onFeedback("replay")}>
          Replay
        </button>
      </div>

      <label className="toggle-row">
        <input
          type="checkbox"
          checked={voiceEnabled}
          onChange={(event) => onVoiceEnabledChange(event.target.checked)}
        />
        <span>Voice DJ narration</span>
      </label>

      <article className="summary-card">
        <span className="mini-label">Queue rationale</span>
        <p>{explanation || "No adaptive explanation yet."}</p>
      </article>

      <article className="summary-card">
        <span className="mini-label">DJ line</span>
        <p>{voiceLine || "The voice engine will narrate the next queue here."}</p>
      </article>

      <article className="summary-card">
        <span className="mini-label">Simulation</span>
        <p>{simulation?.summary || "Run the simulator to compare recommendation strategies."}</p>
        {bestStrategy ? (
          <div className="summary-list">
            <span>
              Best: <strong>{bestStrategy.name}</strong>
            </span>
            <span>Reward {bestStrategy.averageReward.toFixed(3)}</span>
            <span>Diversity {Math.round(bestStrategy.diversityScore * 100)}%</span>
          </div>
        ) : null}
        <button className="ghost-button" type="button" disabled={busy} onClick={onRunSimulation}>
          Run simulation
        </button>
      </article>
    </div>
  );
}

