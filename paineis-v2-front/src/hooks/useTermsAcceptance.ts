import { useState } from 'react';
import { Api } from '../services/api';
import { getUserLocalStorage } from '../context/AuthProvider/util';

interface TermsAcceptanceParams {
  username?: string;
  codIbge?: string;
  version?: string;
}

interface UseTermsAcceptanceReturn {
  checkTermsAcceptance: (params?: TermsAcceptanceParams) => Promise<boolean>;
  acceptTerms: (params?: TermsAcceptanceParams) => Promise<void>;
  loading: boolean;
  error: string | null;
}

export const useTermsAcceptance = (): UseTermsAcceptanceReturn => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const getDefaultParams = (): TermsAcceptanceParams => {
    const user = getUserLocalStorage();

    console.log("User from local storage:", user);

    return {
      username: user?.username,
      codIbge: user?.municipio || "000000",
      version: process.env.REACT_APP_VERSION
    };
  };

  const checkTermsAcceptance = async (params?: TermsAcceptanceParams): Promise<boolean> => {
    const finalParams = { ...getDefaultParams(), ...params };
    
    if (!finalParams.username) {
      return false;
    }

    try {
      setError(null);
      const response = await Api.get("/settings/term-acceptance", {
        params: finalParams
      });
      
      return Array.isArray(response.data) && response.data.length > 0;
    } catch (error) {
      console.error("Error checking term acceptance:", error);
      setError("Erro ao verificar aceite dos termos");
      return false;
    }
  };

  const acceptTerms = async (params?: TermsAcceptanceParams): Promise<void> => {
    const finalParams = { ...getDefaultParams(), ...params };
    
    setLoading(true);
    setError(null);
    
    try {
      await Api.post("/settings/term-acceptance", finalParams);
    } catch (error) {
      console.error("Error saving term acceptance:", error);
      setError("Erro ao salvar aceite dos termos");
      throw error;
    } finally {
      setLoading(false);
    }
  };

  return {
    checkTermsAcceptance,
    acceptTerms,
    loading,
    error
  };
};