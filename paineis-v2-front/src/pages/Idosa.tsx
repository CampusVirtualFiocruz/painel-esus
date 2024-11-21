import { useSearchParams } from "react-router-dom";
import { content } from "../assets/content/content";

import { Bar, Donut, ShallowTreemap, ValueCard } from "../components/charts";
import { charts } from "../components/charts/idoso.mock";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";

const reportHeader = [
  {
    "total-ubs": {
      Chart: ValueCard,
      config: {
        description: "Total de pessoas idosas na UBS",
        icon: "paperdark",
      },
    },
    "total-atendidas": {
      Chart: ValueCard,
      config: {
        description: "Total de pessoas idosas atendidas",
        icon: "paper",
      },
    },
  },
];

const reportSections = [
  {
    "total-raca-cor": {
      Chart: ShallowTreemap,
      config: {
        colors: ["#0b5b98", "#6595ff", "#0066b4", "#49e8db", "#0066b4"],
      },
    },
    "total-imc": {
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
    row: {
      "total-proporcao-vacina-influenza": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radiusStart: "0%",
          colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
          componentStyle: {
            width: "100%",
            minWidth: "140px",
            height: "140px",
          },
        },
      },
      "total-proporcao-atendimento-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radiusStart: "0%",
          colors: ["#0a406a", "#e4e4e4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
          componentStyle: {
            width: "100%",
            minWidth: "140px",
            height: "140px",
          },
        },
      },
    },
  },
  {
    "pessoas-por-faixa-etaria": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "pessoas-por-sexo": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["rgba(57,150,193,255)", "rgba(92,210,200,255)", "#dddddd"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "pessoas-por-diagnostico": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["rgba(57,150,193,255)", "rgba(92,210,200,255)", "#dddddd"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
        invertAxis: true,
      },
    },
  },
];

const RenderChartGroup = ({ chartList, renderSmall }: any) => {
  return Object.keys(chartList).map((chartKey) => {
    const CustomChart = chartList?.[chartKey]?.Chart;
    const chartConfigs = chartList?.[chartKey]?.config;
    const data = (charts as any)?.[chartKey]?.data;
    const isRow = chartKey === "row";

    if (chartConfigs) {
      const xAxisNames = data?.map((d: any) => content?.[d?.tag] ?? d?.tag);
      chartConfigs.xAxis = {};
      chartConfigs.xAxis.data = xAxisNames;
    }

    if (isRow) {
      return (
        <div
          style={{
            width: "100%",
            display: "flex",
            flexDirection: "row",
            gap: "20px",
          }}
        >
          <RenderChartGroup chartList={chartList?.[chartKey]} renderSmall />
        </div>
      );
    }

    return (
      <div style={{ marginBottom: "40px" }}>
        <h5 style={{ fontWeight: "bold", textAlign: "center" }}>
          {content?.[chartKey] || chartKey}
        </h5>
        <CustomChart data={data} config={chartConfigs} />
      </div>
    );
  });
};

const Idosa = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe");

  return (
    <ReportWrapper
      title="UBS Sérgio Arouca / Cuidado da Pessoa Idosa"
      subtitle="(referente aos últimos 12 meses)"
      footer={<ReportFooter chaveListaNominal="Idosa" equipe={equipe} />}
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
                    gap: "50px",
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
                      const data = (charts as any)?.[chartKey]?.data;

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
          <RenderChartGroup chartList={chartList} />
        </div>
      ))}
    </ReportWrapper>
  );
};

export default Idosa;
