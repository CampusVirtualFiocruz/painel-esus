import { useEffect, useState } from "react";
import { useQuery } from "react-query";
import { Api } from "../../services/api";

const usePaginatedList = ({ condicao, id, searchTerm }: any) => {
  const [params, setParams] = useState<any>({
    page: 1,
    size: 10,
    totalElements: 0,
    totalPages: 0,
    sort: ["name", "alert", "zone"],
  });

  const pathToReport = {
    Diabetes: "diabetes",
    Hipertensão: "arterial-hypertension",
  } as any;

  const { data: info, isLoading: isLoadingInfo } = useQuery(
    ["diabetes-list", { condicao, id, pathToReport, searchTerm, ...params }],
    async () => {
      let path = `${pathToReport?.[condicao]}/get-nominal-list/${id}`;
      const response = await Api.get(path, {
        params: {
          itemsPerPage: params.size,
          page: params.page,
          cpf: searchTerm,
        },
      });
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
    isLoadingInfo,
    setParams,
    pathToReport,
  };
};

export default usePaginatedList;
