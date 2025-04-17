import { useParams, useSearchParams } from "react-router-dom";
import { content } from "../assets/content/content";
import { Bar, Donut, ValueCard } from "../components/charts";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import Waffle from "../components/charts/Waffle";
import { memo } from "react";
import useReportDataIdosasV2 from "../hooks/sections/idosasV2/useReportDataIdosasV2";
import { PainelParams } from "./Hipertensao";
import "../styles/idosa.scss";

const reportHeader = [
  {
    "total-ubs": {
      Chart: ValueCard,
      config: {
        description: "total-idosas-ubs",
        icon: "paperdark",
      },
    },
    "total-atendidas": {
      Chart: ValueCard,
      config: {
        description: "total-idosas-atendidas",
        icon: "paper",
      },
    },
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
          xAxis: {
            sort: [
              "60 a 69 anos",
              "70 a 79 anos",
              "80 a 89 anos",
              "90 a 99 anos",
            ],
          },
          yAxis: {
            name: content?.["total-idosas-ubs"],
          },
        },
      },
      "distribuicao-pessoas-raca-cor": {
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
      },
    },
  },
];

const reportSectionsSecond: any = [
  {
    firstRow: {
      "duas-consultas-medicas-enfermagem": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          sort: ["Com duas ou\nmais visitas", "Com uma ou\nnenhuma visita"],
          componentStyle: {
            height: "250px",
          },
          colors: ["#E4E4E4","#0069D0",  "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "dois-registros-peso-altura": {
        Chart: Donut,
        footerNote: <>*Pelo menos 01 (um) registro</>,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          sort: ["Com dois ou\nmais registros", "Com um ou\nnenhum registro"],
          componentStyle: {
            height: "250px",
          },
          colors: ["#0A406A", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "duas-visitas-domiciliares-acs-tacs": {
        Chart: Donut,
        footerNote: (
          <>
            *com intervalo mínimo de
            <br /> 30 dias entre as visitas
          </>
        ),
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
    },
    secondRow: {
      "avalicao-creatina": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          //roseType: "radius",
          radius: [50, 80],
          sort: ["Avaliadas", "Sem avaliação"],
          colors: ["#6595FF", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "registro-vacina-influenza": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          //roseType: "radius",
          radius: [50, 80],
          sort: ["Vacinadas", "Não\nVacinadas"],
          colors: ["#49E8DB", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "consulta-com-dentista-aps": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          //roseType: "radius",
          radius: [50, 80],
          sort: ["Consultadas", "Sem consulta"],
          colors: ["#0069D0", "#E4E4E4", "#84aaff", "#5c7ea0"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
    "ivcf-20": {
      Chart: Donut,
      subtitle: "Índice disponibilizado para registro a partir de 2025",
      config: {
        formatterKind: "perc",
        radiusStart: "35%",
        sort: ["Avaliadas", "Sem avaliação"],
        componentStyle: {
          marginTop: "30px",
          marginBottom: "-150px",
          height: "360px",
        },
        colors: ["#0A406A", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
        halfDonut: true,
      },
    },
  },
];

const RenderChartGroup = ({ report, chartList, renderSmall }: any) => {
  return Object.keys(chartList).map((chartKey) => {
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
      </div>
    );
  });
};

const IdosaV2 = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  const { id } = useParams<PainelParams>();
  const reportData: any = useReportDataIdosasV2({ ubsId: id, squadId: equipe });
  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  return (
    <ReportWrapper
      title={"Cuidado da Pessoa Idosa"}
      footer={<ReportFooter chaveListaNominal="Idosa" equipe={equipe} />}
    >
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
                console.log("achou data", chartKey);
                const CustomChart = chartList?.[chartKey]?.Chart;
                const chartConfigs = chartList?.[chartKey]?.config;
                const data = (report as any)?.[chartKey]?.data;

                return <CustomChart data={data} config={chartConfigs} />;
              })
            )}
          </div>
        </div>
      </>
      {reportSections.map((chartList: any) => (
        <RenderChartGroup report={report} chartList={chartList} />
      ))}
      <center style={{ marginTop: "60px", marginBottom: "30px" }}>
        <h2>
          <b>Proporção de pessoas idosas com:</b>
        </h2>
        <p>(Referentes aos últimos 12 meses)</p>
      </center>
      {reportSectionsSecond.map((chartList: any) => (
        <RenderChartGroup report={report} chartList={chartList} />
      ))}
    </ReportWrapper>
  );
};

export default memo(IdosaV2);
