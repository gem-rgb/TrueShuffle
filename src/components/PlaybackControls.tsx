import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface PlaybackControlsProps {
  prop0: string;
  prop1: number;
  prop2?: boolean;
  prop3: string;
  prop4?: number;
}

interface PlaybackControlsState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
  state4: string;
  state5: number;
}

export const PlaybackControls: React.FC<PlaybackControlsProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<PlaybackControlsState[]>([]);

  const handlePlaybackControlsAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_playbackcontrols_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handlePlaybackControlsAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_playbackcontrols_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handlePlaybackControlsAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_playbackcontrols_data_2");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handlePlaybackControlsAction3 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_playbackcontrols_data_3");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handlePlaybackControlsAction4 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_playbackcontrols_data_4");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handlePlaybackControlsAction5 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_playbackcontrols_data_5");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const computed = useMemo(() => {
    return data.length > 0 ? data.reduce((a, b) => ({ ...a, ...b })) : {};
  }, [data]);

  return (
    <div className="playbackcontrols-container">
      <h2>PlaybackControls</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="playbackcontrols-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default PlaybackControls;