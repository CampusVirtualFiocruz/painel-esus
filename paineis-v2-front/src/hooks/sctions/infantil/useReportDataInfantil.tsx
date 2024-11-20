import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string;
  squadId?: string;
};

const useReportDataInfantil = ({ ubsId, squadId }: reportBasicInfo) => {
  return useQuery(
    ["relatorio-infantil", ubsId, squadId],
    async () => {
      const ubsParam = ubsId ? `/${ubsId}` : "";

      const requests = [
        Api.get(`/children/total`),
        Api.get(`/children/group-by-race${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        Api.get(`/children/group-by-age-location`),
        Api.get(`/children/group-by-gender/${ubsParam}`, {
          params: {
            equipe: squadId,
          },
        }),
        Api.get(`/children/group-cares-by-professionals/${ubsParam}`, {
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

export default useReportDataInfantil;
