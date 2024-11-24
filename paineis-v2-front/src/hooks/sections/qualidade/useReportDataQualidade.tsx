import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataQualidade = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-qualidade", ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";
      const defaultParam = {
        params: {
          equipe: squadId,
        },
      };

      const requests = {
        indicadores: Api.get(`/cadastros/total${ubsParam}`, defaultParam),
        "total-cadastros-cidadaos-por-tipo-identificacao": Api.get(
          `/cadastros/cpf_cns_rate${ubsParam}`,
          defaultParam
        ),
        "status-cadastros-cidadaos": Api.get(
          `/cadastros/group-by-status${ubsParam}`,
          defaultParam
        ),
        "localizacao-domicilios-cadastrados": Api.get(
          `/cadastros/group-by-location${ubsParam}`,
          defaultParam
        ),
        "via-cadastros-cidadaos": Api.get(
          `/cadastros/group-by-origin${ubsParam}`,
          defaultParam
        ),
        "total-cadastros-pessoas-raca-cor": Api.get(
          `/cadastros/group-by-race${ubsParam}`,
          defaultParam
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

export default useReportDataQualidade;
