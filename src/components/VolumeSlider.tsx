import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface VolumeSliderProps {
  prop0?: string;
  prop1: number;
  prop2?: boolean;
  prop3: string;
  prop4?: number;
  prop5?: boolean;
  prop6?: string;
  prop7?: number;
  prop8?: boolean;
}

interface VolumeSliderState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
}

export const VolumeSlider: React.FC<VolumeSliderProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<VolumeSliderState[]>([]);

  const handleVolumeSliderAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_volumeslider_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleVolumeSliderAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_volumeslider_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleVolumeSliderAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_volumeslider_data_2");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleVolumeSliderAction3 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_volumeslider_data_3");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleVolumeSliderAction4 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_volumeslider_data_4");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleVolumeSliderAction5 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_volumeslider_data_5");
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
    <div className="volumeslider-container">
      <h2>VolumeSlider</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="volumeslider-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default VolumeSlider;