import { MdInfoOutline } from "react-icons/md";
import { useParams, useSearchParams } from "react-router-dom";
import { content } from "../assets/content/content";
import { Donut, ValueCard } from "../components/charts";
import { ErrorMessage, LoadingSpinner } from "../components/ui";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "../components/ui/Tooltip";
import useReportDataQualidade from "../hooks/sections/qualidade/useReportDataQualidade";
import { ReportBasicParams } from "../utils";

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
        radius: [50, 90],
        formatterKind: "perc",
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
        colors: ["#b9b9b9", "#09406a"],
      },
    },
    "total-cidadaos-conforme-situação-cadastral": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "350px",
          },

        radius: [0, 90],
        colors: ["#0069d0", "#84aaff", "#e4e4e4", "#5c7ea0"],
      },
    },
    "localizacao-imoveis-cadastrados": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "350px",
          },

        radius: [0, 90],
        colors: ["#e4e4e4", "#84aaff", "#0069d0", "#5c7ea0"],
      },
    },
  },
  {
    "total-cidadaos-acompanhados": {
      Chart: Donut,
      config: {
        radius: [50, 90],
        formatterKind: "perc",
          componentStyle: {
            width: "400px",
            minWidth: "400px",
          },
        colors: ["#e4e4e4", "#84aaff", "#0069d0", "#5c7ea0"],
      },
    },
    "total-cadastros-pessoas-raca-cor": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "350px",
          },

        radius: [0, 90],
        colors: ["#e4e4e4", "#84aaff", "#0069d0", "#5c7ea0"],
      },
    },
  },
];

const footer = `O número de pessoas cuja Qualidade do Cadastro foi avaliada equivale ao total de indivíduos registrados por meio das Fichas de Cadastro Individual (FCI), Módulo Cidadão PEC (Prontuário Eletrônico do Cidadão) e da Recusa de Cadastro.`;

const Qualidade = () => {
  const { id } = useParams<ReportBasicParams>();
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  if (id === undefined) {
    reportHeader[0]["total-cadastros-ubs"].config.description =
      "Total de Cadastros no Município";
  } else {
    delete reportSections[0]["total-cidadaos-acompanhados"];
  }

  const { data, loadings, errors } = useReportDataQualidade({ ubsId: id, squadId: equipe });

  // Mapeamento de chaves para os novos nomes do hook
  const keyMapping = {
    "total-cadastros-cidadaos-por-tipo-identificacao": "cpfCnsRate",
    "total-cidadaos-conforme-situação-cadastral": "groupByStatus",
    "localizacao-imoveis-cadastrados": "groupByLocation",
    "total-cidadaos-acompanhados": "peopleWhoGetCare",
    "total-cadastros-pessoas-raca-cor": "groupByRace",
  };

  // Função para renderizar componente baseado no estado
  const renderComponent = (chartKey: string, CustomChart: any, chartConfigs: any, data: any) => {
    const mappedKey = keyMapping[chartKey as keyof typeof keyMapping];
    const isLoading = mappedKey ? loadings[mappedKey as keyof typeof loadings] : loadings.indicadores;
    const error = mappedKey ? errors[mappedKey as keyof typeof errors] : errors.indicadores;

    if (isLoading) {
      return <LoadingSpinner />;
    }

    if (error) {
      return <ErrorMessage error={error} />;
    }

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
  };

  return (
    <ReportWrapper
      title="Qualidade de Cadastro"
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
                const chartData = data?.[chartKey];

                if (loadings.indicadores) {
                  return <LoadingSpinner key={chartKey} />;
                }

                if (errors.indicadores) {
                  return <ErrorMessage key={chartKey} error={errors.indicadores} />;
                }

                return <CustomChart key={chartKey} data={chartData.data} config={chartConfigs} />;
              })
            )}
          </div>
        </div>
      }
      footer={<ReportFooter chaveListaNominal="Qualidade" equipe={equipe} />}
    >
      {reportSections.map((chartList: any, sectionIndex: number) => (
        <div key={sectionIndex} className="col-12 col-md-6">
          {Object.keys(chartList).map((chartKey) => {
            const CustomChart = chartList?.[chartKey]?.Chart;
            const chartConfigs = chartList?.[chartKey]?.config;
            const mappedKey = keyMapping[chartKey as keyof typeof keyMapping];
            const chartData = mappedKey ? data?.[mappedKey] : data?.[chartKey];

            return (
              <div key={chartKey}>
                {renderComponent(chartKey, CustomChart, chartConfigs, chartData)}
              </div>
            );
          })}
        </div>
      ))}
    </ReportWrapper>
  );
};

export default Qualidade;
