import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataIdosas = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-infantil", ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = {
        indicadores: Api.get(`/elderly/total${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-raca-cor": Api.get(`/elderly/group-by-race${ubsParam}`),
        "total-imc": Api.get(`/elderly/group-by-age-location${ubsParam}`),
        "total-proporcao-vacina-influenza": Api.get(
          `/elderly/group-by-influenza-rate${ubsParam}`
        ),
        "total-proporcao-atendimento-odonto": Api.get(
          `/elderly/group-by-odonto-rate${ubsParam}`
        ),
        "pessoas-por-faixa-etaria": Api.get(`/elderly/group-by-age-location${ubsParam}`),
        "pessoas-por-sexo": Api.get(`/elderly/group-by-gender${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        "pessoas-por-diagnostico": Api.get(
          `/elderly/group-hipertesnion-diabetes-rate${ubsParam}`,
          {
            params: {
              equipe: squadId,
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
        ...reducedData?.indicadores?.data,
      };
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );
};

export default useReportDataIdosas;
