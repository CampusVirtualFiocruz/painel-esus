import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string;
  squadId?: string;
};

const useReportDataIdosas = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-idosas", ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = [
        Api.get(`/elderly/total${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
      ];

      const results = await Promise.all(requests);
      const reducedData = results.reduce(
        (prev, curr) => ({ ...prev, ...curr.data }),
        {}
      );

      console.log("resultados :", { reducedData });

      return reducedData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );
};

export default useReportDataIdosas;
