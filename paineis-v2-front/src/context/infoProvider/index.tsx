import { createContext, useState } from 'react';
import { useQuery } from 'react-query';
import { Api } from '../../services/api';
import { ICityInfomation, IContext, IInfoProvider } from './types';

export const InfoContext = createContext<IContext>({} as IContext);
interface CityResponse {
  cep: string;
  codIgbe: string;
  estado: string;
  municipio: string;
  uf: string;
}
type CityInformationResponse = CityResponse;

export const InfoProvider = ({ children }: IInfoProvider) => {
  const [cityInformation, setCityInformation] =
    useState<ICityInfomation | null>(null);
  const [city, setCity] = useState<string | null>(null);

  useQuery('city-informations', async () => {
    const response =
      await Api.get<CityInformationResponse>('city-informations');
    const data: CityResponse = response.data;
    setCity(`${data.municipio} - ${data.uf}`);
    setCityInformation(data);
  });

  return (
    <InfoContext.Provider value={{ cityInformation, setCityInformation, city }}>
      {children}
    </InfoContext.Provider>
  );
};
