import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  equipe?: string | undefined;
  recorte?: string | undefined;
};

const useReportDataBucal = ({ ubsId, equipe, recorte }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-bucal", ubsId, equipe, recorte],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = {
         "total": Api.get(`/oral-health/get-total${ubsParam}`, {
          params: {
            equipe: equipe,
            recorte: recorte,
          },
        }),
        "pessoas-por-sexo": Api.get(
          `/oral-health/get-cares-by-gender${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
            },
          }
        ),
        "distribuicao-pessoas-raca-cor": Api.get(
          `/oral-health/get-group-by-race${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
            },
          }
        ),
        "primeira-consulta-odonto": Api.get(
          `/oral-health/get-first-appointment${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
            },
          }
        ),
        "realizou-exodontia": Api.get(
          `/oral-health/get-extraction${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
            },
          }
        ),
        "realizou-preventivo-odonto": Api.get(
          `/oral-health/get-prevention-procedures${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
            },
          }
        ),
        "concluido-tratamento": Api.get(
          `/oral-health/get-conclued-treatment${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
            },
          }
        ),
        "realizou-tra-odonto": Api.get(
          `/oral-health/get-atraumatic-treatment${ubsParam}`,
          {
            params: {
              equipe: equipe,
              recorte: recorte,
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
