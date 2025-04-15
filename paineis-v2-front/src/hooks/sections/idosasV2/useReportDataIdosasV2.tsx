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
      const requests = {
        "total-ubs": Api.get(`/elderly/total-ubs`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-atendidas": Api.get(`/elderly/total-medical-cares`, {
          params: {
            equipe: squadId,
          },
        }),
        "pessoas-por-sexo": Api.get(`/elderly/by-gender`, {
          params: {
            equipe: squadId,
          },
        }),
        "distribuicao-pessoas-raca-cor": Api.get(`/elderly/by-race`, {
          params: {
            equipe: squadId,
          },
        }),
        "duas-consultas-medicas-enfermagem": Api.get(`/elderly/two-acs-visits`, {
          params: {
            equipe: squadId,
          },
        }), 
        "dois-registros-peso-altura": Api.get(`/elderly/two-height-records`, {
          params: {
            equipe: squadId,
          },
        }),
        "duas-visitas-domiciliares-acs-tacs": Api.get(`/elderly/two-acs-visits`, {
          params: {
            equipe: squadId,
          },
        }),
        "avalicao-creatina": Api.get(`/elderly/creatinine`, {
          params: {
            equipe: squadId,
          },
        }),
        "registro-vacina-influenza": Api.get(`/elderly/influenza-vaccines`, {
          params: {
            equipe: squadId,
          },
        }),
        "consulta-com-dentista-aps": Api.get(`/elderly/dentist-appointment`, {
          params: {
            equipe: squadId,
          },
        }),
        "ivcf-20": Api.get(`/elderly/ivcf-20`, {
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
