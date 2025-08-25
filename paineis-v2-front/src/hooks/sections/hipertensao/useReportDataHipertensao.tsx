import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  equipe?: string | undefined;
  recorte?: string | undefined;
};

const reportQueryKey = "relatorio-hipertensao--";
const reportRoute = "/arterial-hypertension/";
const config = {
  staleTime: 1000 * 60 * 10,
};

const useReportDataHipertensao = ({ ubsId, equipe }: reportBasicInfo) => {
  const ubsParam = ubsId ? `/${ubsId}` : "";
  const defaultParam = {
    params: {
      equipe: equipe,
    },
  };

  const totalQuery = useQuery(
    [reportQueryKey + "total", ubsId, equipe],
    async () => {
      const response = await Api.get(
        reportRoute + `total${ubsParam}`,
        defaultParam
      );
      return response?.data?.data || response.data;
    },
    config
  );

  const byGenderQuery = useQuery(
    [reportQueryKey + "by-gender", ubsId, equipe],
    async () => {
      const response = await Api.get(
        reportRoute + `by-gender${ubsParam}`,
        defaultParam
      );
      return response?.data?.data || response.data;
    },
    config
  );

  const byRaceQuery = useQuery(
    [reportQueryKey + "by-race", ubsId, equipe],
    async () => {
      const response = await Api.get(
        reportRoute + `by-race${ubsParam}`,
        defaultParam
      );
      return response?.data?.data || response.data;
    },
    config
  );

  const examsQuery = useQuery(
    [reportQueryKey + "exams", ubsId, equipe],
    async () => {
      const response = await Api.get(
        reportRoute + `exams${ubsParam}`,
        defaultParam
      );
      return response?.data?.data || response.data;
    },
    config
  );

  const complicationsQuery = useQuery(
    [reportQueryKey + "complications", ubsId, equipe],
    async () => {
      const response = await Api.get(
        reportRoute + `complications${ubsParam}`,
        defaultParam
      );
      return response?.data?.data || response.data;
    },
    config
  );

  const imcQuery = useQuery(
    [reportQueryKey + "imc", ubsId, equipe],
    async () => {
      const response = await Api.get(
        reportRoute + `imc${ubsParam}`,
        defaultParam
      );
      return response?.data?.data || response.data;
    },
    config
  );

  const loadings = {
    total: totalQuery.isLoading,
    "por-sexo": byGenderQuery.isLoading,
    "por-raca-cor": byRaceQuery.isLoading,
    exames: examsQuery.isLoading,
    complicacoes: complicationsQuery.isLoading,
    imc: imcQuery.isLoading,
  };

  const errors = {
    total: totalQuery.error,
    "por-sexo": byGenderQuery.error,
    "por-raca-cor": byRaceQuery.error,
    exames: examsQuery.error,
    complicacoes: complicationsQuery.error,
    imc: imcQuery.error,
  };

  // Dados organizados
  const data = {
    total: totalQuery.data,
    "por-sexo": byGenderQuery.data,
    "por-raca-cor": byRaceQuery.data,
    exames: examsQuery.data,
    complicacoes: complicationsQuery.data,
    imc: imcQuery.data,
  };

  const refetchAll = () => {
    totalQuery.refetch();
    byGenderQuery.refetch();
    byRaceQuery.refetch();
    examsQuery.refetch();
    complicationsQuery.refetch();
    imcQuery.refetch();
  };

  return {
    data,
    loadings,
    errors,
    refetchAll,
  };
};

export default useReportDataHipertensao;
