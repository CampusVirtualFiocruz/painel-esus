import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataQualidade = ({ ubsId, squadId }: reportBasicInfo) => {
  const ubsParam = ubsId ? `/${ubsId}` : "";
  const defaultParam = {
    params: {
      equipe: squadId,
    },
  };

  // Chamadas individuais para cada endpoint
  const indicadoresQuery = useQuery(
    ["relatorio-qualidade-indicadores", ubsId, squadId],
    async () => {
      const response = await Api.get(`/cadastros/total${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const cpfCnsRateQuery = useQuery(
    ["relatorio-qualidade-cpf-cns-rate", ubsId, squadId],
    async () => {
      const response = await Api.get(`/cadastros/cpf_cns_rate${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const groupByStatusQuery = useQuery(
    ["relatorio-qualidade-group-by-status", ubsId, squadId],
    async () => {
      const response = await Api.get(`/cadastros/group-by-status${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const groupByLocationQuery = useQuery(
    ["relatorio-qualidade-group-by-location", ubsId, squadId],
    async () => {
      const response = await Api.get(`/cadastros/group-by-location${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const peopleWhoGetCareQuery = useQuery(
    ["relatorio-qualidade-people-who-get-care", ubsId, squadId],
    async () => {
      const response = await Api.get(`/cadastros/people-who-get-care${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const groupByRaceQuery = useQuery(
    ["relatorio-qualidade-group-by-race", ubsId, squadId],
    async () => {
      const response = await Api.get(`/cadastros/group-by-race${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  // Estados individuais para cada seção
  const loadings = {
    indicadores: indicadoresQuery.isLoading,
    cpfCnsRate: cpfCnsRateQuery.isLoading,
    groupByStatus: groupByStatusQuery.isLoading,
    groupByLocation: groupByLocationQuery.isLoading,
    peopleWhoGetCare: peopleWhoGetCareQuery.isLoading,
    groupByRace: groupByRaceQuery.isLoading,
  };

  const errors = {
    indicadores: indicadoresQuery.error,
    cpfCnsRate: cpfCnsRateQuery.error,
    groupByStatus: groupByStatusQuery.error,
    groupByLocation: groupByLocationQuery.error,
    peopleWhoGetCare: peopleWhoGetCareQuery.error,
    groupByRace: groupByRaceQuery.error,
  };

  // Dados organizados
  const data = {
    indicadores: indicadoresQuery.data,
    cpfCnsRate: cpfCnsRateQuery.data,
    groupByStatus: groupByStatusQuery.data,
    groupByLocation: groupByLocationQuery.data,
    peopleWhoGetCare: peopleWhoGetCareQuery.data,
    groupByRace: groupByRaceQuery.data,
    // Mantém compatibilidade com o formato anterior
    "total-cadastros-cidadaos-por-tipo-identificacao": cpfCnsRateQuery.data,
    "total-cidadaos-conforme-situação-cadastral": groupByStatusQuery.data,
    "localizacao-imoveis-cadastrados": groupByLocationQuery.data,
    "total-cidadaos-acompanhados": peopleWhoGetCareQuery.data,
    "total-cadastros-pessoas-raca-cor": groupByRaceQuery.data,
    ...indicadoresQuery.data,
  };

  // Função para refetch de todas as queries
  const refetchAll = () => {
    indicadoresQuery.refetch();
    cpfCnsRateQuery.refetch();
    groupByStatusQuery.refetch();
    groupByLocationQuery.refetch();
    peopleWhoGetCareQuery.refetch();
    groupByRaceQuery.refetch();
  };

  return {
    data,
    loadings,
    errors,
    refetchAll,
  };
};

export default useReportDataQualidade;
