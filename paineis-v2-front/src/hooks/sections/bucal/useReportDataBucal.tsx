import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  equipe?: string | undefined;
  recorte?: string | undefined;
};

const useReportDataBucal = ({ ubsId, equipe }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-infantil", ubsId, equipe],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = {
        total: Api.get(`/children/total${ubsParam}`, {
          params: {
            equipe: equipe,
          },
        }),
        "infantil-criancas-faixa-etaria-sexo": Api.get(
          `/children/by-age${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-distribuicao-criancas-raca-cor": Api.get(
          `/children/by-race${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
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

      return {
        ...reducedData,
      };
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );
};

export default useReportDataBucal;
