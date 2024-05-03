import { createContext, useEffect, useState } from "react";
import { useQuery } from "react-query";
import { Api } from "../../services/api";
import { ICityInfomation, IContext, IInfoProvider } from "./types";
import { STALE_TIME } from "../../config/stale-time";

export const InfoContext = createContext<IContext>({} as IContext);
interface CityResponse {
  cep: string;
  codIgbe: string;
  estado: string;
  municipio: string
  uf: string;
}
interface CityInformationResponse {
  data: CityResponse
}

export const InfoProvider = ({ children }: IInfoProvider) => {
  const [cityInformation, setCityInformation] = useState<ICityInfomation | null>(null);
  const [city, setCity] = useState<string | null>(null);

  useQuery('city-informations-2', async () => {
    const response = await Api.get('city-informations');
    const data: CityResponse = response.data;
    setCity(`${data.municipio} - ${data.uf}`)
    setCityInformation(data);
  }, {
    staleTime: STALE_TIME
  });

  return (
    <InfoContext.Provider value={{ cityInformation, setCityInformation, city }}>
      {children}
    </InfoContext.Provider>
  );
};