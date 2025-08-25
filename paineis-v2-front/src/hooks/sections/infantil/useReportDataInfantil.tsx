import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  equipe?: string | undefined;
  recorte?: string | undefined;
};

const useReportDataInfantil = ({ ubsId, equipe }: reportBasicInfo) => {
  const ubsParam = ubsId ? `/${ubsId}` : "";
  const defaultParam = {
    params: {
      equipe: equipe,
    },
  };

  // Chamadas individuais para cada endpoint
  const totalQuery = useQuery(
    ["relatorio-infantil-total", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/total${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const totalAtendimentosQuery = useQuery(
    ["relatorio-infantil-total-atendimentos", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/total-medical-cares${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const criancasFaixaEtariaSexoQuery = useQuery(
    ["relatorio-infantil-criancas-faixa-etaria-sexo", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/by-age${ubsParam}`, defaultParam);
      return response.data?.["criancas-por-sexo"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const distribuicaoCriancasRacaCorQuery = useQuery(
    ["relatorio-infantil-distribuicao-criancas-raca-cor", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/by-race${ubsParam}`, defaultParam);
      return response.data?.["distribuicao-criancas-raca-cor"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const primeiraConsulta8DiaQuery = useQuery(
    ["relatorio-infantil-primeira-consulta-8-dia", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/first-consult-8d${ubsParam}`, defaultParam);
      return response.data?.["primeira-consulta-ate-8-dia"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const noveConsultas2AnosQuery = useQuery(
    ["relatorio-infantil-nove-consultas-2-anos", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/appointments-until-2-years${ubsParam}`, defaultParam);
      return response.data?.["nove-consultas-puericultura-2-anos"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const umaVisita30DiasQuery = useQuery(
    ["relatorio-infantil-uma-visita-30-dias", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/acs-visit-until-30days${ubsParam}`, defaultParam);
      return response.data?.["uma-visita-domiciliar-acs-tacs-30dias"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const umaVisita31Dia6MesesQuery = useQuery(
    ["relatorio-infantil-uma-visita-31-dia-6-meses", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/acs-visit-until-6month${ubsParam}`, defaultParam);
      return response.data?.["uma-visita-domiciliar-acs-tacs-31dias-a-6meses"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const umaConsulta12MesesQuery = useQuery(
    ["relatorio-infantil-uma-consulta-12-meses", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/dental-appointment-until-12month${ubsParam}`, defaultParam);
      return response.data?.["consulta-odonto-ate-12-meses"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const umaConsulta12_24MesesQuery = useQuery(
    ["relatorio-infantil-uma-consulta-12-24-meses", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/dental-appointment-until-24months${ubsParam}`, defaultParam);
      return response.data?.["consulta-odonto-12-24-meses"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const registroPesoAlturaQuery = useQuery(
    ["relatorio-infantil-registro-peso-altura", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/high-weight-records${ubsParam}`, defaultParam);
      return response.data?.["registro-peso-altura-puericultura-9-consultas"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const marcosDesenvolvimentoAvaliadosQuery = useQuery(
    ["relatorio-infantil-marcos-desenvolvimento-avaliados", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/milestone${ubsParam}`, defaultParam);
      return response.data?.["marco-desenvolvimento-avaliados"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const consumoAlimentarAvaliadoQuery = useQuery(
    ["relatorio-infantil-consumo-alimentar-avaliado", ubsId, equipe],
    async () => {
      const response = await Api.get(`/children/evaluated-feeding${ubsParam}`, defaultParam);
      return response.data?.["consumo-alimentar-avaliado"]?.data || response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  // Estados individuais para cada seção
  const loadings = {
    total: totalQuery.isLoading,
    "total-atendimentos": totalAtendimentosQuery.isLoading,
    "infantil-criancas-faixa-etaria-sexo": criancasFaixaEtariaSexoQuery.isLoading,
    "infantil-distribuicao-criancas-raca-cor": distribuicaoCriancasRacaCorQuery.isLoading,
    "infantil-primeira-consulta-8-dia": primeiraConsulta8DiaQuery.isLoading,
    "infantil-nove-consultas-2-anos": noveConsultas2AnosQuery.isLoading,
    "infantil-uma-visita-30-dias": umaVisita30DiasQuery.isLoading,
    "infantil-uma-visita-31-dia-6-meses": umaVisita31Dia6MesesQuery.isLoading,
    "infantil-uma-consulta-12-meses": umaConsulta12MesesQuery.isLoading,
    "infantil-uma-consulta-12-24-meses": umaConsulta12_24MesesQuery.isLoading,
    "infantil-registro-peso-altura": registroPesoAlturaQuery.isLoading,
    "infantil-marcos-desenvolvimento-avaliados": marcosDesenvolvimentoAvaliadosQuery.isLoading,
    "infantil-consumo-alimentar-avaliado": consumoAlimentarAvaliadoQuery.isLoading,
  };

  const errors = {
    total: totalQuery.error,
    "total-atendimentos": totalAtendimentosQuery.error,
    "infantil-criancas-faixa-etaria-sexo": criancasFaixaEtariaSexoQuery.error,
    "infantil-distribuicao-criancas-raca-cor": distribuicaoCriancasRacaCorQuery.error,
    "infantil-primeira-consulta-8-dia": primeiraConsulta8DiaQuery.error,
    "infantil-nove-consultas-2-anos": noveConsultas2AnosQuery.error,
    "infantil-uma-visita-30-dias": umaVisita30DiasQuery.error,
    "infantil-uma-visita-31-dia-6-meses": umaVisita31Dia6MesesQuery.error,
    "infantil-uma-consulta-12-meses": umaConsulta12MesesQuery.error,
    "infantil-uma-consulta-12-24-meses": umaConsulta12_24MesesQuery.error,
    "infantil-registro-peso-altura": registroPesoAlturaQuery.error,
    "infantil-marcos-desenvolvimento-avaliados": marcosDesenvolvimentoAvaliadosQuery.error,
    "infantil-consumo-alimentar-avaliado": consumoAlimentarAvaliadoQuery.error,
  };

  // Dados organizados
  const data = {
    total: totalQuery.data,
    "total-atendimentos": totalAtendimentosQuery.data,
    "infantil-criancas-faixa-etaria-sexo": criancasFaixaEtariaSexoQuery.data,
    "infantil-distribuicao-criancas-raca-cor": distribuicaoCriancasRacaCorQuery.data,
    "infantil-primeira-consulta-8-dia": primeiraConsulta8DiaQuery.data,
    "infantil-nove-consultas-2-anos": noveConsultas2AnosQuery.data,
    "infantil-uma-visita-30-dias": umaVisita30DiasQuery.data,
    "infantil-uma-visita-31-dia-6-meses": umaVisita31Dia6MesesQuery.data,
    "infantil-uma-consulta-12-meses": umaConsulta12MesesQuery.data,
    "infantil-uma-consulta-12-24-meses": umaConsulta12_24MesesQuery.data,
    "infantil-registro-peso-altura": registroPesoAlturaQuery.data,
    "infantil-marcos-desenvolvimento-avaliados": marcosDesenvolvimentoAvaliadosQuery.data,
    "infantil-consumo-alimentar-avaliado": consumoAlimentarAvaliadoQuery.data,
  };

  // Função para refetch de todas as queries
  const refetchAll = () => {
    totalQuery.refetch();
    totalAtendimentosQuery.refetch();
    criancasFaixaEtariaSexoQuery.refetch();
    distribuicaoCriancasRacaCorQuery.refetch();
    primeiraConsulta8DiaQuery.refetch();
    noveConsultas2AnosQuery.refetch();
    umaVisita30DiasQuery.refetch();
    umaVisita31Dia6MesesQuery.refetch();
    umaConsulta12MesesQuery.refetch();
    umaConsulta12_24MesesQuery.refetch();
    registroPesoAlturaQuery.refetch();
    marcosDesenvolvimentoAvaliadosQuery.refetch();
    consumoAlimentarAvaliadoQuery.refetch();
  };

  return {
    data,
    loadings,
    errors,
    refetchAll,
  };
};

export default useReportDataInfantil;
