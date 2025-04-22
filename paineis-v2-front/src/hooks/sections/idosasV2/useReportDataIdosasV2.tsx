import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataIdosasV2 = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-idoso", ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = {
        "total-ubs": Api.get(`/elderly/total-ubs${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-atendidas": Api.get(`/elderly/total-medical-cares${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        "pessoas-por-sexo": Api.get(`/elderly/by-gender${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        "distribuicao-pessoas-raca-cor": Api.get(
          `/elderly/by-race${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "duas-consultas-medicas-enfermagem": Api.get(
          `/elderly/two-medical-appointments${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "dois-registros-peso-altura": Api.get(
          `/elderly/two-height-records${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "duas-visitas-domiciliares-acs-tacs": Api.get(
          `/elderly/two-acs-visits${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "avalicao-creatina": Api.get(`/elderly/creatinine${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        "registro-vacina-influenza": Api.get(
          `/elderly/influenza-vaccines${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "consulta-com-dentista-aps": Api.get(
          `/elderly/dentist-appointment${ubsParam}`,
          {
            params: {
              equipe: squadId,
            },
          }
        ),
        "ivcf-20": Api.get(`/elderly/ivcf-20${ubsParam}`, {
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

export default useReportDataIdosasV2;
