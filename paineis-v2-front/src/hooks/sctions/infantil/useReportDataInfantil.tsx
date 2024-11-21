import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataInfantil = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-infantil", ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = {
        indicadores: Api.get(`/children/total`),
        "total-cadastros-criancas-raca-cor": Api.get(
          `/children/group-by-race${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "distribuicao-criancas-faixa-etaria": Api.get(
          `/children/group-by-age-location`
        ),
        "distribuicao-criancas-sexo": Api.get(
          `/children/group-by-gender${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "distribuicao-criancas-local": Api.get(
          `/children/group-by-location-rate${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "total-extratificacao-por-profissional": Api.get(
          `/children/group-cares-by-professionals${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
      };

      const results = await Promise.all(Object.values(requests));

      const reducedData:any = results.reduce(
        (prev, curr, currIndex) => ({
          ...prev,
          [Object.keys(requests)?.[currIndex]]: {
            ["data"]: curr?.data?.data || curr.data,
          },
        }),
        {}
      );

      return {
        ...reducedData,
        ...reducedData?.indicadores?.data
      };
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );
};

export default useReportDataInfantil;
