import { useParams, useSearchParams } from "react-router-dom";
import { content } from "../assets/content/content";
import { useQuery } from "react-query";

import { Bar, Donut, ShallowTreemap, ValueCard } from "../components/charts";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import useReportDataIdosas from "../hooks/sections/idosas/useReportDataIdosas";
import { Api } from "../services/api";
import { useInfo } from "../context/infoProvider/useInfo";
import "../styles/idosa.scss";
import { ReportBasicParams } from "../utils";

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
            minWidth: "150px",
            height: "150px",
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
            width: "110%",
            minWidth: "150px",
            height: "150px",
          },
        },
      },
    },
    "pessoas-por-faixa-etaria": {
      Chart: Bar,
      config: {
        colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-idosas-ubs"],
        },
      },
    },
  },
  {
    "pessoas-por-sexo": {
      Chart: Bar,
      config: {
        colors: ["rgba(57,150,193,255)", "rgba(92,210,200,255)", "#dddddd"],
        yAxis: {
          name: content?.["total-idosas-ubs"],
        },
      },
    },
    "pessoas-por-diagnostico": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["#0069d0", "#49e8db", "#84aaff"],
        invertAxis: true,
      },
    },
  },
];

const RenderChartGroup = ({ report, chartList, renderSmall }: any) => {
  return Object.keys(chartList).map((chartKey) => {
    const CustomChart = chartList?.[chartKey]?.Chart;
    const chartConfigs = chartList?.[chartKey]?.config;
    const data = (report as any)?.[chartKey]?.data;
    const isRow = chartKey === "row";

    if (chartConfigs) {
      const xAxisNames = data?.map((d: any) => content?.[d?.tag] ?? d?.tag);
      chartConfigs.xAxis = {};
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
      <div style={{ marginBottom: "40px" }}>
        <h5
          style={{
            fontWeight: "bold",
            textAlign: "center",
            padding: renderSmall ? "30px" : "initial",
          }}
        >
          {content?.[chartKey] || chartKey}
        </h5>
        <CustomChart data={data} config={chartConfigs} />
      </div>
    );
  });
};

const Idosa = () => {
  const { id } = useParams<ReportBasicParams>();
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

  const reportData = useReportDataIdosas({ ubsId: id, squadId: equipe });
  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  return (
    <ReportWrapper
      title={"Cuidado da Pessoa Idosa"}
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
                      // chartConfigs.reportViewType = !!equipe ? ReportViewTypeEnum.EQUIPE : !!id ? ReportViewTypeEnum.UBS : ReportViewTypeEnum.MUNICIPIO;
                      const data = (report as any)?.[chartKey]?.data;

                      // "100+ anos" como item final dos gráficos
                      const pessoasPorFaixaEtaria =
                        report["pessoas-por-faixa-etaria"].data;
                      const pessoasPorSexo = report["pessoas-por-sexo"].data;

                      if (pessoasPorFaixaEtaria[0]?.tag === "100-ou-mais") {
                        const cemOuMaisItem = pessoasPorFaixaEtaria.shift();
                        pessoasPorFaixaEtaria.push(cemOuMaisItem);
                      }

                      if (pessoasPorSexo[0]?.tag === "100-ou-mais") {
                        const cemOuMaisItem = pessoasPorSexo.shift();
                        pessoasPorSexo.push(cemOuMaisItem);
                      }

                      return <CustomChart data={data} config={chartConfigs}  />;
                    })
                  )}
                </div>
              </div>
            </>
          )}
          {colIndex === 1 && (
            <div style={{ paddingTop: "60px", content: " " }} />
          )}
          <RenderChartGroup report={report} chartList={chartList} />
        </div>
      ))}
    </ReportWrapper>
  );
};

export default Idosa;
