import { useEffect, useState } from "react";
import { useQuery } from "react-query";
import { Api } from "../../services/api";

const usePaginatedList = ({ condicao, equipe, id, searchTerm, config }: any) => {
  const [params, setParams] = useState<any>({
    page: 1,
    size: 10,
    totalElements: 0,
    totalPages: 0,
    sort: ["-name"],
  });

  const pathToReport = {
    Diabetes: "diabetes",
    Hipertensão: "arterial-hypertension",
    Idosa: "elderly",
    Infantil: "children",
    Qualidade: "cadastros",
    Bucal: "oral-health",
  } as any;

  const { data: info, isLoading: isLoadingInfo } = useQuery(
    [
      "nominal-list" + condicao + equipe + id,
      { condicao, equipe, id, pathToReport, searchTerm, ...params },
      config
    ],
    async () => {
      let path = `${pathToReport?.[condicao]}/get-nominal-list/${id}`;

      const requestParams = {
        params: {
          itemsPerPage: params.size,
          page: params.page,
          q: searchTerm,
          sort: (params?.sort || []).map((item: string) => ({
            field: item.split("-").join(""),
            direction: item[0] === "-" ? "asc" : "desc",
          })),
          equipe,
        },
      } as any;

      if(config?.possuiRecorte){
        requestParams.params = { recorte: config?.recorte, ...requestParams.params };
      }

      const response = await Api.get(path, requestParams);

      return response?.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  useEffect(() => {
    setParams({ ...params, page: 1 });
  }, [searchTerm]);

  return {
    info,
    params,
    isLoadingInfo,
    setParams,
    pathToReport,
  };
};

export default usePaginatedList;
