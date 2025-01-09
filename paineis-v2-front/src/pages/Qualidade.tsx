import { useParams, useSearchParams } from "react-router-dom";
import { MdInfoOutline } from "react-icons/md";
import { content } from "../assets/content/content";
import { Bar, Donut, ShallowTreemap, ValueCard } from "../components/charts";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import useReportDataQualidade from "../hooks/sections/qualidade/useReportDataQualidade";
import { PainelParams } from "./Hipertensao";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "../components/ui/Tooltip";

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
        colors: ["#5CD2C8", "#b9b9b9", "#0069d0", "#5c7ea0"],
        info: (
          <>
            ”Cadastro Ativo” equivale a todas os cadastros cujas pessoas estão
            vivas e permanecem domiciliadas no território da UBS/ Equipe de
            Saúde.
            <br />
            ”Cadastro Inativo” equivale a todos os cadastros de pessoas que se
            mudaram do território da UBS/ Equipe de Saúde ou falecidas.
          </>
        ),
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
    "total-pessoas-acompanhadas": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        radiusStart: "0%",
        colors: ["#e4e4e4", "#84aaff", "#0069d0", "#5c7ea0"],
      },
    },
    "total-cadastros-pessoas-raca-cor": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        radiusStart: "0%",
        colors: ["#e4e4e4", "#84aaff", "#0069d0", "#5c7ea0"],
      },
    },
  },
];

const footer = `O número de pessoas cuja Qualidade do Cadastro foi avaliada equivale ao total de indivíduos registrados a partir do ano de 2019 por meio das Fichas de Cadastro Individual (FCI), Módulo Cidadão PEC (Prontuário Eletrônico do Cidadão) e da Recusa de Cadastro.`;

const Qualidade = () => {
  const { id } = useParams<PainelParams>();
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  if (id == undefined) {
    reportHeader[0]["total-cadastros-ubs"].config.description =
      "Total de Cadastros no Município";
  } else {
    delete reportSections[0]["total-pessoas-acompanhadas"];
  }

  const reportData = useReportDataQualidade({ ubsId: id, squadId: equipe });
  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  return (
    <ReportWrapper
      title="Qualidade de Cadastro"
      subtitle={"(Pessoas registradas a partir de 2019)"}
      footerNote={footer}
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

            const Title = () => {
              const TitleText = () => (
                <h5 style={{ fontWeight: "bold", textAlign: "center" }}>
                  {content?.[chartKey] || chartKey}{" "}
                  {Boolean(chartConfigs?.info) && (
                    <MdInfoOutline
                      style={{
                        cursor: "pointer",
                        color: "#222222",
                        height: 20,
                        width: 20,
                      }}
                    />
                  )}
                </h5>
              );

              return chartConfigs?.info ? (
                <Tooltip>
                  <TooltipTrigger>
                    <TitleText />
                  </TooltipTrigger>
                  <TooltipContent className="Tooltip">
                    {chartConfigs?.info}
                  </TooltipContent>
                </Tooltip>
              ) : (
                <TitleText />
              );
            };

            return (
              <div style={{ marginBottom: "70px" }}>
                <Title />
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
