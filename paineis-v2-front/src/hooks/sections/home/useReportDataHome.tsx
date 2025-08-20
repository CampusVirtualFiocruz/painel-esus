import { useQuery } from "react-query";
import { Api } from "../../../services/api";
// import { charts as homeData } from "../../../components/charts/home.mock";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataHome = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-home", ubsId, squadId],
    async () => {
      // const ubsParam = ubsId ? `/${ubsId}` : ""; // Não usado nos novos endpoints

      // Mapeamento com os endpoints reais baseado nas chaves do MockRelatorioHome
      const requests = {
        "piramide-etaria": Api.get(`/v1/demographic/age-groups`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-masculino": Api.get(`/v1/demographic/gender`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-feminino": Api.get(`/v1/demographic/gender`, {
          params: {
            equipe: squadId,
          },
        }),
        "tipo-localizacao": Api.get(`/v1/demographic/location-area`, {
          params: {
            equipe: squadId,
          },
        }),
        "tematico-diabetes": Api.get(`/v1/demographic/location-area/diabetes`, {
          params: {
            equipe: squadId,
          },
        }),
        "tematico-hipertensao": Api.get(`/v1/demographic/location-area/hypertension`, {
          params: {
            equipe: squadId,
          },
        }),
        "tematico-idoso": Api.get(`/v1/demographic/location-area/elderly`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-cidadaos-cadastrados": Api.get(`/v1/demographic/total-people`, {
          params: {
            equipe: squadId,
          },
        }),
        "total-populacao-apurada": Api.get(`/v1/demographic/total-people`, {
          params: {
            equipe: squadId,
          },
        }),
        // TODO: Adicionar endpoint específico para qualidade quando disponível
        "tematico-qualidade": Api.get(`/v1/demographic/location-area`, {
          params: {
            equipe: squadId,
          },
        }),
        // Endpoint para desenvolvimento infantil
        "tematico-infantil": Api.get(`/v1/demographic/location-area/child`, {
          params: {
            equipe: squadId,
          },
        }),
        // TODO: Adicionar endpoint específico para saúde bucal quando disponível
        "tematico-bucal": Api.get(`/v1/demographic/location-area`, {
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

      // TEMPORÁRIO: Para usar mock durante desenvolvimento, descomente a linha abaixo
      // return homeData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );
};

export default useReportDataHome;
