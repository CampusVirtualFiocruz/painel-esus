import { content } from "../assets/content/content";
import { DonutChart } from "../charts/Donut";
import {
  Bar,
  Donut,
  ShallowTreemap,
  ValueCard,
  ProgressBar,
} from "../components/charts";
import { charts } from "../components/charts/infantil.mock";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import useReportDataInfantil from "../hooks/sctions/infantil/useReportDataInfantil";

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
        description: "Porcentagem de cadastros atualizados",
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
        hideLegend: true,
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
  const reportData = useReportDataInfantil({ ubsId: "9" });
  const mockData = { ...charts, ...reportData?.data };

  console.log({ mockData });

  return (
    <ReportWrapper
      title="UBS Sérgio Arouca / Desenvolvimento Infantil de Cadastro"
      subtitle="(cuidado até o 2º ano de vida de acordo com a data da última atualização pelo município)"
      footer={<ReportFooter />}
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
                      const data = (mockData as any)?.[chartKey]?.data;
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
            const data = (mockData as any)?.[chartKey]?.data;

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
