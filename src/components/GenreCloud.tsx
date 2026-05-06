import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface GenreCloudProps {
  prop0?: string;
  prop1?: number;
  prop2?: boolean;
  prop3: string;
  prop4?: number;
  prop5?: boolean;
  prop6: string;
}

interface GenreCloudState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
}

export const GenreCloud: React.FC<GenreCloudProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<GenreCloudState[]>([]);

  const handleGenreCloudAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_genrecloud_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleGenreCloudAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_genrecloud_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleGenreCloudAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_genrecloud_data_2");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleGenreCloudAction3 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_genrecloud_data_3");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleGenreCloudAction4 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_genrecloud_data_4");
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
    <div className="genrecloud-container">
      <h2>GenreCloud</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="genrecloud-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default GenreCloud;