import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface LyricsPanelProps {
  prop0: string;
  prop1: number;
  prop2: boolean;
  prop3: string;
  prop4?: number;
  prop5?: boolean;
}

interface LyricsPanelState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
  state4: string;
  state5: number;
}

export const LyricsPanel: React.FC<LyricsPanelProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<LyricsPanelState[]>([]);

  const handleLyricsPanelAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_lyricspanel_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleLyricsPanelAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_lyricspanel_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleLyricsPanelAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_lyricspanel_data_2");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleLyricsPanelAction3 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_lyricspanel_data_3");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleLyricsPanelAction4 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_lyricspanel_data_4");
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
    <div className="lyricspanel-container">
      <h2>LyricsPanel</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="lyricspanel-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default LyricsPanel;