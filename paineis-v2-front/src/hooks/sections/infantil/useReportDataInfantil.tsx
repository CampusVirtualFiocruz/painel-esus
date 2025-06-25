import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  equipe?: string | undefined;
  recorte?: string | undefined;
};

const useReportDataInfantil = ({ ubsId, equipe }: reportBasicInfo) => {
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
        "infantil-primeira-consulta-8-dia": Api.get(
          `/children/first-consult-8d${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-nove-consultas-2-anos": Api.get(
          `/children/appointments-until-2-years${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-uma-visita-30-dias": Api.get(
          `/children/acs-visit-until-30days${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-uma-visita-31-dia-6-meses": Api.get(
          `/children/acs-visit-until-6month${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-uma-consulta-12-meses": Api.get(
          `/children/dental-appointment-until-12month${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-uma-consulta-12-24-meses": Api.get(
          `/children/dental-appointment-until-24months${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-registro-peso-altura": Api.get(
          `/children/high-weight-records${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-marcos-desenvolvimento-avaliados": Api.get(
          `/children/milestone${ubsParam}`,
          {
            params: {
              equipe: equipe,
            },
          }
        ),
        "infantil-consumo-alimentar-avaliado": Api.get(
          `/children/evaluated-feeding${ubsParam}`,
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
            data:
              curr.data?.["total-cadastros"]?.data ||
              curr.data?.["criancas-por-sexo"]?.data ||
              curr.data?.["distribuicao-criancas-raca-cor"]?.data ||
              curr.data?.["primeira-consulta-ate-8-dia"]?.data ||
              curr.data?.["nove-consultas-puericultura-2-anos"]?.data ||
              curr.data?.["uma-visita-domiciliar-acs-tacs-30dias"]?.data ||
              curr.data?.["consulta-odonto-ate-12-meses"]?.data ||
              curr.data?.["consulta-odonto-12-24-meses"]?.data ||
              curr.data?.["marco-desenvolvimento-avaliados"]?.data ||
              curr.data?.["consumo-alimentar-avaliado"]?.data ||
              curr.data?.["uma-visita-domiciliar-acs-tacs-31dias-a-6meses"]
                ?.data ||
              curr.data?.["registro-peso-altura-puericultura-9-consultas"]
                ?.data ||
              curr?.data?.data ||
              curr.data,
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

export default useReportDataInfantil;
