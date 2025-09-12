import { useQuery } from 'react-query';
import { Api } from '../../../services/api';

type reportBasicInfo = {
  ubsId?: string | undefined | null;
  squadId?: string | undefined | null;
};

const useReportDataHome = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ['relatorio-home', ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : '';

      const requests = {
        'piramide-etaria': Api.get(`demographic/age-groups${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        'total-por-sexo': Api.get(`demographic/gender${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        'tipo-localizacao': Api.get(`demographic/location-area${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        'tematico-diabetes': Api.get(
          `demographic/location-area/diabetes${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        'tematico-hipertensao': Api.get(
          `demographic/location-area/hypertension${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        'tematico-idoso': Api.get(
          `demographic/location-area/elderly${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        'total-cidadaos-cadastrados': Api.get(
          `demographic/total-people${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        'tematico-qualidade': Api.get(`demographic/location-area${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        'tematico-infantil': Api.get(
          `demographic/location-area/child${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        'tematico-bucal': Api.get(`demographic/location-area${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
      };

      const results = await Promise.all(Object.values(requests));

      const reducedData: any = results.reduce(
        (prev, curr, currIndex) => ({
          ...prev,
          [Object.keys(requests)?.[currIndex]]: {
            data: curr?.data?.data || curr.data,
          },
        }),
        {}
      );

      return reducedData;
    },
    {
      staleTime: 1000 * 60 * 10,
    }
  );
};

export default useReportDataHome;
