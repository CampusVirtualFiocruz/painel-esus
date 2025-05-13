import { memo, useState } from "react";
import { Button } from "bold-ui";
import { useParams, useSearchParams } from "react-router-dom";
import { Bar, Donut } from "../components/charts";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import Waffle from "../components/charts/Waffle";
import { charts as mock } from "../components/charts/saude-bucal-v2.mock";
import { content } from "../assets/content/content";
import { PainelParams } from "./Hipertensao";
import "../styles/idosa.scss";
import useReportDataBucalV2 from "../hooks/sections/bucalV2/useReportDataBucalV2";

const fixedLegend = [
  {
    color: "#49E8DB",
    title: "Ótimo",
    text: "≥ 50,0%",
  },
  {
    color: "#84aaff",
    title: "Bom",
    text: "Entre ≥37,5% e < 50,0%",
  },
  {
    color: "#0069D0",
    title: "Suficiente",
    text: "Entre ≥25,0% e < 37,5%",
  },
  {
    color: "#0A406A",
    title: "Regular",
    text: "< 25,0%",
  },
];

const reportSections: any = [
  {
    row: {
      "pessoas-por-sexo": {
        Chart: Bar,
        config: {
          colors: ["#84aaff", "#0069d0", "#e4e4e4", "#5c7ea0"],
          componentStyle: {
            height: "500px",
          },

          yAxis: {
            name: content?.["total-idosas-ubs"],
          },
        },
      },
      /* "distribuicao-pessoas-raca-cor": {
        Chart: Waffle,
        config: {
          formatterKind: "perc",
          radiusStart: "0%",
          sort: [
            "Branca",
            "Preta",
            "Amarela",
            "Parda",
            "Indígena",
            "Não informado",
          ],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      }, */
    },
  },
];

const reportSectionsSecond: any = [
  {
    firstRow: {
      "primeira-consulta-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          sort: ["Com duas ou\nmais visitas", "Com uma ou\nnenhuma visita"],
          componentStyle: {
            height: "250px",
          },
          colors: ["#E4E4E4", "#0069D0", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-exodontia": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          sort: ["Com duas ou\nmais visitas", "Com uma ou\nnenhuma visita"],
          componentStyle: {
            height: "250px",
          },
          colors: ["#49E8DB", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-preventivo-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [50, 80],
          sort: ["Avaliadas", "Sem avaliação"],
          colors: ["#6595FF", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
    secondRow: {
      "realizou-tra-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [50, 80],
          sort: ["Vacinadas", "Não\nVacinadas"],
          colors: ["#49E8DB", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-escovacao-supervisionada": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [50, 80],
          sort: ["Consultadas", "Sem consulta"],
          colors: ["#0069D0", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
  },
];

const RenderChartGroup = ({
  report,
  chartList,
  renderSmall,
  ChartFooter,
}: any) => {
  return Object.keys(chartList).map((chartKey, indexHere) => {
    const CustomChart = chartList?.[chartKey]?.Chart;
    const chartConfigs = chartList?.[chartKey]?.config;
    const data = (report as any)?.[chartKey]?.data;
    const isRow = chartKey === "row" || chartKey.indexOf("Row") !== -1;

    if (chartConfigs) {
      const xAxisNames = data?.map((d: any) => content?.[d?.tag] ?? d?.tag);
      chartConfigs.xAxis = { data: [], ...chartConfigs.xAxis };
      chartConfigs.xAxis.data = xAxisNames;
    }

    if (isRow) {
      return (
        <div className="is-row">
          <RenderChartGroup
            report={report}
            chartList={chartList?.[chartKey]}
            renderSmall
            ChartFooter={ChartFooter}
          />
        </div>
      );
    }

    return (
      <div style={{ position: "relative", marginBottom: "40px" }}>
        <h5
          style={{
            fontWeight: "bold",
            textAlign: "center",
            padding: renderSmall ? "30px" : "initial",
          }}
        >
          {content?.[chartKey] || chartKey}
        </h5>
        {Boolean(chartList?.[chartKey]?.subtitle) && (
          <p
            style={{
              textAlign: "center",
              padding: renderSmall ? "30px" : "initial",
            }}
          >
            {content?.[chartList?.[chartKey]?.subtitle] ??
              chartList?.[chartKey]?.subtitle}
          </p>
        )}
        <CustomChart data={data} config={chartConfigs} />
        {Boolean(chartList?.[chartKey]?.footerNote) && (
          <center>
            <p
              style={{
                width: "100%",
                position: "absolute",
                bottom: "-70px",
                textAlign: "center",
                fontSize: "12px",
                padding: renderSmall ? "20px" : "initial",
              }}
            >
              {content?.[chartList?.[chartKey]?.footerNote] ??
                chartList?.[chartKey]?.footerNote}
            </p>
          </center>
        )}
        {ChartFooter && <ChartFooter />}
      </div>
    );
  });
};

const BucalV2 = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;
  const [recorte, setRecorte] = useState<"atendidos" | "cadastrados">(
    "atendidos"
  );

  const { id } = useParams<PainelParams>();
  const reportData: any = useReportDataBucalV2({ ubsId: id, equipe, recorte });

  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  const FooterCommom = () => {
    return (
      <div>
        {fixedLegend.map(({ color, title, text }) => (
          <div style={{ marginBottom: "6px" }}>
            <span
              style={{
                display: "inline-block",
                width: "20px",
                backgroundColor: color,
              }}
            >
              &nbsp;
            </span>{" "}
            {title}: {text}
          </div>
        ))}
      </div>
    );
  };

  return (
    <>
      <ReportWrapper
        title={"Saúde Bucal"}
        footer={<ReportFooter chaveListaNominal="Idosa" equipe={equipe} />}
        preheader={
          <div
            style={{
              display: "flex",
              alignItems: "end",
              justifyContent: "end",
              margin: "20px 20px",
              gap: "10px",
            }}
          >
            <Button
              style={{ height: "36px" }}
              onClick={() => {
                setRecorte("atendidos");
              }}
            >
              Atendidos
            </Button>
            <Button
              style={{ height: "36px" }}
              kind="primary"
              onClick={() => {
                setRecorte("cadastrados");
              }}
            >
              Cadastrados
            </Button>
          </div>
        }
      >
        {reportSections.map((chartList: any) => (
          <RenderChartGroup report={report} chartList={chartList} />
        ))}
        <center style={{ marginTop: "60px", marginBottom: "30px" }}>
          <h2>
            <b>Proporção referente a quantidade de pessoas atendidas na UBS:</b>
          </h2>
        </center>
        {reportSectionsSecond.map((chartList: any) => (
          <RenderChartGroup
            report={report}
            chartList={chartList}
            ChartFooter={FooterCommom}
          />
        ))}
      </ReportWrapper>
    </>
  );
};

export default memo(BucalV2);
