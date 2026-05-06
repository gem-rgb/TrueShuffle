import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface ImportWizardProps {
  prop0: string;
  prop1?: number;
  prop2?: boolean;
  prop3?: string;
  prop4: number;
}

interface ImportWizardState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
  state4: string;
  state5: number;
  state6: string;
}

export const ImportWizard: React.FC<ImportWizardProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<ImportWizardState[]>([]);

  const handleImportWizardAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_importwizard_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleImportWizardAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_importwizard_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleImportWizardAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_importwizard_data_2");
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
    <div className="importwizard-container">
      <h2>ImportWizard</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="importwizard-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default ImportWizard;