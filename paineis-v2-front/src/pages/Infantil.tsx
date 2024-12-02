import { useParams, useSearchParams } from "react-router-dom";
import { useQuery } from "react-query";

import { content } from "../assets/content/content";
import {
  Bar,
  Donut,
  ShallowTreemap,
  ValueCard,
  ProgressBar,
} from "../components/charts";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import useReportDataInfantil from "../hooks/sections/infantil/useReportDataInfantil";
import { PainelParams } from "./Hipertensao";
import { getNomeUbs } from "../utils";
import { Api } from "../services/api";
import { useInfo } from "../context/infoProvider/useInfo";

const reportHeader = [
  {
    "total-criancas-cadastradas-2-anos": {
      Chart: ValueCard,
      config: {
        description: "Total de crianças até 2 anos cadastradas",
        icon: "paperdark",
      },
    },
    "total-criancas-atendidas-2-anos": {
      Chart: ValueCard,
      config: {
        description: "Total de crianças até 2 anos atendidas",
        icon: "paper",
      },
    },
  },
];

const reportSections = [
  {
    "total-cadastros-criancas-raca-cor": {
      Chart: ShallowTreemap,
      config: {
        colors: ["#0b5b98", "#6595ff", "#0066b4", "#49e8db", "#0066b4"],
      },
    },
    "total-extratificacao-por-profissional": {
      Chart: ProgressBar,
    },
  },
  {
    "distribuicao-criancas-faixa-etaria": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "distribuicao-criancas-sexo": {
      Chart: Bar,
      config: {
        colors: ["rgba(57,150,193,255)", "rgba(92,210,200,255)", "#dddddd"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "distribuicao-criancas-local": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        radiusStart: "0%",
        colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
  },
];

const Infantil = () => {
  const { id } = useParams<PainelParams>();
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  const { city } = useInfo();
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

  const reportData = useReportDataInfantil({ ubsId: id, squadId: equipe });
  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  return (
    <ReportWrapper
      title={"Desenvolvimento Infantil"}
      subtitle="(cuidado até o 2º ano de vida de acordo com a data da última atualização pelo município)"
      footer={<ReportFooter chaveListaNominal="Infantil" equipe={equipe} />}
    >
      {reportSections.map((chartList: any, colIndex) => (
        <div className="col-12 col-md-6">
          {colIndex === 0 && (
            <>
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
            </>
          )}
          {colIndex === 1 && (
            <div style={{ paddingTop: "60px", content: " " }} />
          )}
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
              <div style={{ marginBottom: "40px" }}>
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

export default Infantil;
