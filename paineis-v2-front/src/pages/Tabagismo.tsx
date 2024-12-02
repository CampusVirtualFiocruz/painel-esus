import { content } from "../assets/content/content";
import { Bar, Pie, Donut } from "../components/charts";
import { tabagismoCharts } from "../components/charts/tabagismo.mock";
import ReportWrapper from "../components/ui/ReportWrapper";

const reportSections = [
  {
    "proporcao-tabagistas-acompanhadas": {
      Chart: Donut,
    },
    "tabagistas-faixa-etaria": {
      Chart: Bar,
      config: {
        yAxis: {
          name: content?.["total-pessoas-acompanhadas"],
        },
      },
    },
    "pessoas-tabagistas-sexo": {
      Chart: Bar,
      config: {
        yAxis: {
          name: content?.["total-pessoas-acompanhadas"],
        },
      },
    },
  },
  {
    "proporcao-fatores-riscos-por-dant": {
      Chart: Bar,
      config: {
        yAxis: {
          name: content?.["total-pessoas-acompanhadas"],
        },
      },
    },
    "consulta-odontologica-tabagistas": {
      Chart: Pie,
    },
    "pessoas-tabagistas-escolaridade": {
      Chart: Bar,
      config: {
        yAxis: {
          name: content?.["total-pessoas"],
        },
      },
    },
  },
];

const Tabagismo = () => {
  return (
    <ReportWrapper
      title="Tabagismo"
      subtitle="(últimos 12 meses)"
    >
      {reportSections.map((chartList: any) => (
        <div className="col-12 col-md-6">
          {Object.keys(chartList).map((chartKey) => {
            const CustomChart = chartList?.[chartKey]?.Chart;
            const chartConfigs = chartList?.[chartKey]?.config;
            const data = (tabagismoCharts as any)?.[chartKey]?.data;

            if (chartConfigs) {
              const xAxisNames = data?.map(
                (d: any) => content?.[d?.tag] ?? d?.tag
              );
              chartConfigs.xAxis = {};
              chartConfigs.xAxis.data = xAxisNames;
            }

            return (
              <div style={{ marginBottom: "70px" }}>
                <h4 style={{ fontWeight: "bold", textAlign: "center" }}>
                  {content?.[chartKey] || chartKey}
                </h4>
                <CustomChart data={data} config={chartConfigs} />
              </div>
            );
          })}
        </div>
      ))}
    </ReportWrapper>
  );
};

export default Tabagismo;
