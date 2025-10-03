import { useState, useEffect } from "react";
import { Api } from "../services/api";

interface InstalationReadyResponse {
  completed: boolean;
  percentual: number;
}

export function useInstalationReady() {
  const [loading, setLoading] = useState(true);
  const [isReady, setIsReady] = useState(false);
  const [percentual, setPercentual] = useState(0);

    const checkInstalationReady = async () => {
      setLoading(true);
      try {
        const response = await Api.get<InstalationReadyResponse>(
          "/settings/instalation-ready"
        );
        const data = response.data;
        setIsReady(data.completed);
        setPercentual(data.percentual);
        setLoading(false);
      } catch (error) {
        console.error("Error checking instalation readiness:", error);
      } 
    };

  useEffect(() => {
    const interval = setInterval(
      checkInstalationReady,
      isReady ? 10 * 1000 : 1000
    );
    return () => clearInterval(interval);
  }, [isReady]);

  return { isReady, percentual, loading };
}
