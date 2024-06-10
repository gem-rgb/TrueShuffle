import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface AccessibilityPanelProps {
  prop0?: string;
  prop1?: number;
  prop2?: boolean;
  prop3: string;
  prop4?: number;
  prop5: boolean;
  prop6?: string;
  prop7?: number;
  prop8: boolean;
  prop9?: string;
  prop10: number;
  prop11?: boolean;
}

interface AccessibilityPanelState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
  state4: string;
  state5: number;
}

export const AccessibilityPanel: React.FC<AccessibilityPanelProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<AccessibilityPanelState[]>([]);

  const handleAccessibilityPanelAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_accessibilitypanel_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleAccessibilityPanelAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_accessibilitypanel_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleAccessibilityPanelAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_accessibilitypanel_data_2");
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
    <div className="accessibilitypanel-container">
      <h2>AccessibilityPanel</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="accessibilitypanel-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default AccessibilityPanel;