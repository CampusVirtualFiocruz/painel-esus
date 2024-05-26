import { content } from "../assets/content/content";
import { Bar, Pie, Donut } from "../components/charts";
import { tabagismoCharts } from "../components/charts/tabagismo.mock";
import ReportWrapper from "../components/ui/ReportWrapper";

const reportKeys = [
  {
    "proporcao-tabagistas-acompanhadas": {
      Chart: Donut,
    },
    "tabagistas-faixa-etaria": {
      Chart: Bar,
    },
    "pessoas-tabagistas-sexo": {
      Chart: Bar,
    },
  },
  {
    "proporcao-fatores-riscos-por-dant": {
      Chart: Bar,
    },
    "consulta-odontologica-tabagistas": {
      Chart: Pie,
    },
    "pessoas-tabagistas-escolaridade": {
      Chart: Bar,
    },
  },
];

const Tabagismo = () => {
  return (
    <ReportWrapper title="UBS abc / Painel Tabagismo (últimos 12 meses)">
      <div className="container" style={{ marginTop: "80px" }}>
        <div className="row justify-content-center">
          {reportKeys.map((chartList: any) => (
            <div className="col-12 col-md-6">
              {Object.keys(chartList).map((chartKey) => {
                const CustomChart = chartList?.[chartKey]?.Chart;
                return (
                  <div style={{ marginBottom: "30px" }}>
                    <h3 style={{ fontWeight: "bold", textAlign: "center" }}>
                      {content?.[chartKey] || chartKey}
                    </h3>
                    <CustomChart
                      data={(tabagismoCharts as any)?.[chartKey]?.data}
                    />
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      </div>
    </ReportWrapper>
  );
};

export default Tabagismo;
