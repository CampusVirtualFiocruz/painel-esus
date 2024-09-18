import { useQuery } from "react-query";
import { useParams } from "react-router";

import { ReportFooter } from "../../components/ui/ReportFooter";
import { Api } from "../../services/api";
import { useInfo } from "../../context/infoProvider/useInfo";
import { getNomeUbs } from "../../utils";

import FaixaEtaria, { PainelParams } from "./faixa-etaria/FaixaEtaria";
import AtendimentoLinhaCuidado from "./atendimentos-linha-cuidado/AtendimentoLinhaCuidado";
import TotalAtendimentos from "./total-atendimentos/TotalAtendimentos";
import TipoConsulta from "./tipo-consulta/TipoConsulta";
import Exodontia from "./exodontia/Exodontia";
import LocalAtendimento from "./local-atendimento/LocalAtendimento";
import Desfecho from "./desfecho/Desfecho";
import Sexo from "./sexo/Sexo";

import "./style.scss";
import ReportWrapper from "../../components/ui/ReportWrapper";
import TwoColumnSection from "../../components/ui/TwoColumnSection";

type TypeUbs = {
  label: string;
  value: number | string;
  id: string;
};
type Lista = {
  co_dim_unidade_saude_1: number;
  no_unidade_saude: string;
  nu_cnes: number;
};
type ResponseDataListUbs = {
  data: Lista[];
};

export const SaudeBucal = () => {
  const { id } = useParams<PainelParams>();
  const { city } = useInfo();

  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<ResponseDataListUbs>("get-units");
      const data = response.data;

      const listData: TypeUbs[] = data.data.map((ubs: any) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
          id: ubs.co_seq_dim_unidade_saude,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : city;
  const UBS = id ? (!isLoadingUbs ? nomeUbs : "Carregando...") : nomeUbs;
  const title = `${UBS} / Painel Saúde Bucal`;

  return (
    <ReportWrapper title={title} subtitle="(referente aos últimos 12 meses)">
      <TwoColumnSection>
        <TwoColumnSection.Col>
          <TotalAtendimentos />
          <TipoConsulta />
          <FaixaEtaria />
          <div style={{ height: "20px" }} />
          <LocalAtendimento />
        </TwoColumnSection.Col>
        <TwoColumnSection.Col>
          <AtendimentoLinhaCuidado />
          <Exodontia />
          <Sexo />
          <div style={{ height: "20px" }} />
          <Desfecho />
        </TwoColumnSection.Col>
      </TwoColumnSection>
      <ReportFooter />
    </ReportWrapper>
  );
};
