import { useQuery } from "react-query";
import { Api } from "../../../services/api";

type reportBasicInfo = {
  ubsId?: string | undefined;
  squadId?: string | undefined;
};

const useReportDataIdosas = ({ ubsId, squadId }: reportBasicInfo) => {
  const ubsParam = ubsId ? `/${ubsId}` : "";
  const defaultParam = {
    params: {
      equipe: squadId,
    },
  };

  const totalUbsQuery = useQuery(
    ["relatorio-idoso-total-ubs", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/total-ubs${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const totalAtendidasQuery = useQuery(
    ["relatorio-idoso-total-atendidas", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/total-medical-cares${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const pessoasPorSexoQuery = useQuery(
    ["relatorio-idoso-pessoas-por-sexo", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/by-gender${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const distribuicaoPessoasRacaCorQuery = useQuery(
    ["relatorio-idoso-distribuicao-pessoas-raca-cor", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/by-race${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const duasConsultasMedicasEnfermagemQuery = useQuery(
    ["relatorio-idoso-duas-consultas-medicas-enfermagem", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/two-medical-appointments${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const doisRegistrosPesoAlturaQuery = useQuery(
    ["relatorio-idoso-dois-registros-peso-altura", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/two-height-records${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const duasVisitasDomiciliaresAcsTacsQuery = useQuery(
    ["relatorio-idoso-duas-visitas-domiciliares-acs-tacs", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/two-acs-visits${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const avalicaoCreatinaQuery = useQuery(
    ["relatorio-idoso-avalicao-creatina", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/creatinine${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const registroVacinaInfluenzaQuery = useQuery(
    ["relatorio-idoso-registro-vacina-influenza", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/influenza-vaccines${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const consultaComDentistaApsQuery = useQuery(
    ["relatorio-idoso-consulta-com-dentista-aps", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/dentist-appointment${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const ivcf20Query = useQuery(
    ["relatorio-idoso-ivcf-20", ubsId, squadId],
    async () => {
      const response = await Api.get(`/elderly/ivcf-20${ubsParam}`, defaultParam);
      return response?.data?.data || response.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const loadings = {
    "total-ubs": totalUbsQuery.isLoading,
    "total-atendidas": totalAtendidasQuery.isLoading,
    "pessoas-por-sexo": pessoasPorSexoQuery.isLoading,
    "distribuicao-pessoas-raca-cor": distribuicaoPessoasRacaCorQuery.isLoading,
    "duas-consultas-medicas-enfermagem": duasConsultasMedicasEnfermagemQuery.isLoading,
    "dois-registros-peso-altura": doisRegistrosPesoAlturaQuery.isLoading,
    "duas-visitas-domiciliares-acs-tacs": duasVisitasDomiciliaresAcsTacsQuery.isLoading,
    "avalicao-creatina": avalicaoCreatinaQuery.isLoading,
    "registro-vacina-influenza": registroVacinaInfluenzaQuery.isLoading,
    "consulta-com-dentista-aps": consultaComDentistaApsQuery.isLoading,
    "ivcf-20": ivcf20Query.isLoading,
  };

  const errors = {
    "total-ubs": totalUbsQuery.error,
    "total-atendidas": totalAtendidasQuery.error,
    "pessoas-por-sexo": pessoasPorSexoQuery.error,
    "distribuicao-pessoas-raca-cor": distribuicaoPessoasRacaCorQuery.error,
    "duas-consultas-medicas-enfermagem": duasConsultasMedicasEnfermagemQuery.error,
    "dois-registros-peso-altura": doisRegistrosPesoAlturaQuery.error,
    "duas-visitas-domiciliares-acs-tacs": duasVisitasDomiciliaresAcsTacsQuery.error,
    "avalicao-creatina": avalicaoCreatinaQuery.error,
    "registro-vacina-influenza": registroVacinaInfluenzaQuery.error,
    "consulta-com-dentista-aps": consultaComDentistaApsQuery.error,
    "ivcf-20": ivcf20Query.error,
  };

  const data = {
    "total-ubs": { data: totalUbsQuery.data },
    "total-atendidas": { data: totalAtendidasQuery.data },
    "pessoas-por-sexo": { data: pessoasPorSexoQuery.data },
    "distribuicao-pessoas-raca-cor": { data: distribuicaoPessoasRacaCorQuery.data },
    "duas-consultas-medicas-enfermagem": { data: duasConsultasMedicasEnfermagemQuery.data },
    "dois-registros-peso-altura": { data: doisRegistrosPesoAlturaQuery.data },
    "duas-visitas-domiciliares-acs-tacs": { data: duasVisitasDomiciliaresAcsTacsQuery.data },
    "avalicao-creatina": { data: avalicaoCreatinaQuery.data },
    "registro-vacina-influenza": { data: registroVacinaInfluenzaQuery.data },
    "consulta-com-dentista-aps": { data: consultaComDentistaApsQuery.data },
    "ivcf-20": { data: ivcf20Query.data },
    ...(totalUbsQuery.data || {}),
  };

  const refetchAll = () => {
    totalUbsQuery.refetch();
    totalAtendidasQuery.refetch();
    pessoasPorSexoQuery.refetch();
    distribuicaoPessoasRacaCorQuery.refetch();
    duasConsultasMedicasEnfermagemQuery.refetch();
    doisRegistrosPesoAlturaQuery.refetch();
    duasVisitasDomiciliaresAcsTacsQuery.refetch();
    avalicaoCreatinaQuery.refetch();
    registroVacinaInfluenzaQuery.refetch();
    consultaComDentistaApsQuery.refetch();
    ivcf20Query.refetch();
  };

  return {
    data,
    loadings,
    errors,
    refetchAll,
  };
};

export default useReportDataIdosas;
