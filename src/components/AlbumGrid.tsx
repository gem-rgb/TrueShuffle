import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface AlbumGridProps {
  prop0?: string;
  prop1: number;
  prop2?: boolean;
  prop3: string;
  prop4: number;
  prop5?: boolean;
  prop6?: string;
  prop7: number;
  prop8?: boolean;
  prop9?: string;
  prop10: number;
  prop11: boolean;
}

interface AlbumGridState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
  state4: string;
}

export const AlbumGrid: React.FC<AlbumGridProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<AlbumGridState[]>([]);

  const handleAlbumGridAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_albumgrid_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleAlbumGridAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_albumgrid_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleAlbumGridAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_albumgrid_data_2");
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
    <div className="albumgrid-container">
      <h2>AlbumGrid</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="albumgrid-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default AlbumGrid;