import React, { useState, useEffect, useCallback, useMemo } from "react";
import { invoke } from "@tauri-apps/api/tauri";

interface SocialFeedProps {
  prop0: string;
  prop1?: number;
  prop2: boolean;
  prop3: string;
  prop4?: number;
  prop5: boolean;
  prop6?: string;
}

interface SocialFeedState {
  state0: string;
  state1: number;
  state2: string;
  state3: number;
  state4: string;
}

export const SocialFeed: React.FC<SocialFeedProps> = (props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<SocialFeedState[]>([]);

  const handleSocialFeedAction0 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_socialfeed_data_0");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleSocialFeedAction1 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_socialfeed_data_1");
      setData(prev => [...prev, result as any]);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  const handleSocialFeedAction2 = useCallback(async () => {
    setLoading(true);
    try {
      const result = await invoke("get_socialfeed_data_2");
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
    <div className="socialfeed-container">
      <h2>SocialFeed</h2>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {data.map((item, i) => (
        <div key={i} className="socialfeed-item">
          {JSON.stringify(item)}
        </div>
      ))}
    </div>
  );
};

export default SocialFeed;