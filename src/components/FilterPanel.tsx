import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface FilterPanelProps {
  prop0: string;
  prop1: number;
  prop2?: boolean;
  prop3: string;
  prop4?: number;
  prop5?: boolean;
  prop6?: string;
  prop7?: number;
  prop8: boolean;
  prop9?: string;
}

interface FilterPanelState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
}

export const FilterPanel: React.FC<FilterPanelProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<FilterPanelState[]>([]);

  const handleFilterPanelAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_filterpanel_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleFilterPanelAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_filterpanel_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleFilterPanelAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_filterpanel_data_2");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleFilterPanelAction3 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_filterpanel_data_3");
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
    <div className="filterpanel-container">
      <h2>FilterPanel</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="filterpanel-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default FilterPanel;