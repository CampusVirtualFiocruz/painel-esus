import { useParams, useSearchParams } from "react-router-dom";
import { useQuery } from "react-query";

import { content } from "../assets/content/content";
import { Bar, Donut, ShallowTreemap, ValueCard } from "../components/charts";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import useReportDataQualidade from "../hooks/sections/qualidade/useReportDataQualidade";
import { PainelParams } from "./Hipertensao";
import { getNomeUbs } from "../utils";
import { Api } from "../services/api";
import { useInfo } from "../context/infoProvider/useInfo";

let reportHeader = [
  {
    "total-cadastros-ubs": {
      Chart: ValueCard,
      config: {
        description: "Total de Cadastros na Unidade Básica de Saúde",
        icon: "paperdark",
      },
    },
    "porcentagem-cadastros-atualizados": {
      Chart: ValueCard,
      config: {
        percent: true,
        description: "Porcentagem de cadastros atualizados*",
        info: "nos últimos 24 meses",
        icon: "paper",
      },
    },
  },
];

const reportSections = [
  {
    "total-cadastros-cidadaos-por-tipo-identificacao": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        colors: ["#b9b9b9", "#09406a"],
      },
    },
    "status-cadastros-cidadaos": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        colors: ["#5CD2C8", "#b9b9b9"],
      },
    },
    "localizacao-domicilios-cadastrados": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        radiusStart: "0%",
        colors: ["#e4e4e4", "#84aaff", "#0069d0", "#5c7ea0"],
      },
    },
  },
  {
    "via-cadastros-cidadaos": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["rgba(57,150,193,255)", "rgba(92,210,200,255)", "#dddddd"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "total-cadastros-pessoas-raca-cor": {
      Chart: ShallowTreemap,
      config: {
        colors: ["#0b5b98", "#6595ff", "#0066b4", "#49e8db", "#0066b4"],
      },
    },
  },
];

const Qualidade = () => {
  const { id } = useParams<PainelParams>();
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  const { city } = useInfo();
  if (id == undefined) {
    reportHeader[0]["total-cadastros-ubs"].config.description =
      "Total de Cadastros no Município";
  }
  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<any>("get-units");
      const data = response.data;

      const listData: any[] = data.data.map((ubs: any) => {
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

  const reportData = useReportDataQualidade({ ubsId: id, squadId: equipe });
  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  return (
    <ReportWrapper
      title="Qualidade de Cadastro"
      subtitle={"(Pessoas registradas a partir de 2019)"}
      header={
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            marginTop: "50px",
            marginBottom: "66px",
          }}
        >
          <div
            style={{
              display: "flex",
              flex: "1",
              flexDirection: "row",
              gap: "30px",
              width: "100%",
              maxWidth: "600px",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            {reportHeader.map((chartList: any) =>
              Object.keys(chartList).map((chartKey) => {
                const CustomChart = chartList?.[chartKey]?.Chart;
                const chartConfigs = chartList?.[chartKey]?.config;
                const data = (report as any)?.[chartKey]?.data;
                return <CustomChart data={data} config={chartConfigs} />;
              })
            )}
          </div>
        </div>
      }
      footer={<ReportFooter chaveListaNominal="Qualidade" equipe={equipe} />}
    >
      {reportSections.map((chartList: any) => (
        <div className="col-12 col-md-6">
          {Object.keys(chartList).map((chartKey) => {
            const CustomChart = chartList?.[chartKey]?.Chart;
            const chartConfigs = chartList?.[chartKey]?.config;
            const data = (report as any)?.[chartKey]?.data;

            if (chartConfigs) {
              const xAxisNames = data?.map(
                (d: any) => content?.[d?.tag] ?? d?.tag
              );
              chartConfigs.xAxis = {};
              chartConfigs.xAxis.data = xAxisNames;
            }

            return (
              <div style={{ marginBottom: "70px" }}>
                <h5 style={{ fontWeight: "bold", textAlign: "center" }}>
                  {content?.[chartKey] || chartKey}
                </h5>
                <CustomChart data={data} config={chartConfigs} />
              </div>
            );
          })}
        </div>
      ))}
    </ReportWrapper>
  );
};

export default Qualidade;
