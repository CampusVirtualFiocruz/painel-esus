import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  equipe?: string | undefined;
  recorte?: string | undefined;
};

const useReportDataBucal = ({ ubsId, equipe, recorte }: reportBasicInfo) => {
  const ubsParam = ubsId ? `/${ubsId}` : "";
  const defaultParam = {
    params: {
      equipe: equipe,
      recorte: recorte,
    },
  };

  // Chamadas individuais para cada endpoint
  const totalQuery = useQuery(
    ["relatorio-bucal-total", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-total${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const pessoasPorSexoQuery = useQuery(
    ["relatorio-bucal-pessoas-por-sexo", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-cares-by-gender${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const distribuicaoPessoasRacaCorQuery = useQuery(
    ["relatorio-bucal-distribuicao-pessoas-raca-cor", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-group-by-race${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const primeiraConsultaOdontoQuery = useQuery(
    ["relatorio-bucal-primeira-consulta-odonto", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-first-appointment${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const realizouExodontiaQuery = useQuery(
    ["relatorio-bucal-realizou-exodontia", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-extraction${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const realizouPreventivoOdontoQuery = useQuery(
    ["relatorio-bucal-realizou-preventivo-odonto", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-prevention-procedures${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const concluidoTratamentoQuery = useQuery(
    ["relatorio-bucal-concluido-tratamento", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-conclued-treatment${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const realizouTraOdontoQuery = useQuery(
    ["relatorio-bucal-realizou-tra-odonto", ubsId, equipe, recorte],
    async () => {
      const response = await Api.get(`/oral-health/get-atraumatic-treatment${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  // Estados individuais para cada seção
  const loadings = {
    total: totalQuery.isLoading,
    "pessoas-por-sexo": pessoasPorSexoQuery.isLoading,
    "distribuicao-pessoas-raca-cor": distribuicaoPessoasRacaCorQuery.isLoading,
    "primeira-consulta-odonto": primeiraConsultaOdontoQuery.isLoading,
    "realizou-exodontia": realizouExodontiaQuery.isLoading,
    "realizou-preventivo-odonto": realizouPreventivoOdontoQuery.isLoading,
    "concluido-tratamento": concluidoTratamentoQuery.isLoading,
    "realizou-tra-odonto": realizouTraOdontoQuery.isLoading,
  };

  const errors = {
    total: totalQuery.error,
    "pessoas-por-sexo": pessoasPorSexoQuery.error,
    "distribuicao-pessoas-raca-cor": distribuicaoPessoasRacaCorQuery.error,
    "primeira-consulta-odonto": primeiraConsultaOdontoQuery.error,
    "realizou-exodontia": realizouExodontiaQuery.error,
    "realizou-preventivo-odonto": realizouPreventivoOdontoQuery.error,
    "concluido-tratamento": concluidoTratamentoQuery.error,
    "realizou-tra-odonto": realizouTraOdontoQuery.error,
  };

  // Dados organizados
  const data = {
    total: { data: totalQuery.data },
    "pessoas-por-sexo": { data: pessoasPorSexoQuery.data },
    "distribuicao-pessoas-raca-cor": { data: distribuicaoPessoasRacaCorQuery.data },
    "primeira-consulta-odonto": { data: primeiraConsultaOdontoQuery.data },
    "realizou-exodontia": { data: realizouExodontiaQuery.data },
    "realizou-preventivo-odonto": { data: realizouPreventivoOdontoQuery.data },
    "concluido-tratamento": { data: concluidoTratamentoQuery.data },
    "realizou-tra-odonto": { data: realizouTraOdontoQuery.data },
  };

  // Função para refetch de todas as queries
  const refetchAll = () => {
    totalQuery.refetch();
    pessoasPorSexoQuery.refetch();
    distribuicaoPessoasRacaCorQuery.refetch();
    primeiraConsultaOdontoQuery.refetch();
    realizouExodontiaQuery.refetch();
    realizouPreventivoOdontoQuery.refetch();
    concluidoTratamentoQuery.refetch();
    realizouTraOdontoQuery.refetch();
  };

  return {
    data,
    loadings,
    errors,
    refetchAll,
  };
};

export default useReportDataBucal;
