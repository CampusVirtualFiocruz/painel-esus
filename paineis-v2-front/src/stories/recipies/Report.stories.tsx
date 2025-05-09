import type { Meta, StoryObj } from "@storybook/react";
import { content } from "./../../assets/content/content";
import {
  Bar,
  Donut,
  ShallowTreemap,
  ValueCard,
  ProgressBar,
} from "./../../components/charts";
import { charts } from "../../components/charts/infantil.mock";
import { Footer } from "../../components/Footer";
import { Button, Link } from "bold-ui";
import { FaUser } from "react-icons/fa";

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

const ReportFooter = ({
  chaveListaNominal,
  equipe,
}: {
  chaveListaNominal?:
    | "Hipertensão"
    | "Diabetes"
    | "Idosa"
    | "Qualidade"
    | "Infantil";
  equipe?: any;
}) => {
  const handleToViewList = () => {};

  const handleToPainelMunicipio = () => {};

  const handleToPainelUBS = () => {};

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        gap: "20px",
        marginTop: "30px",
        marginBottom: "120px",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
          gap: "20px",
        }}
      >
        {chaveListaNominal && (
          <Button
            style={{
              backgroundColor: "#343131",
              color: "white",
              width: "250px",
            }}
            onClick={handleToViewList}
          >
            <FaUser style={{ marginRight: "10px" }} />
            {content.buttonViewList}
          </Button>
        )}
        <Button
          kind="primary"
          onClick={handleToPainelUBS}
          style={{
            width: "250px",
          }}
        >
          {content.buttonBackToUbs}
        </Button>
      </div>
      <Link onClick={handleToPainelMunicipio} style={{ color: "#343131" }}>
        {content.buttonBackToCity}
      </Link>
    </div>
  );
};

const ReportWrapper = ({
  title,
  subtitle,
  children,
  header,
  footer,
  footerNote,
  ...props
}: any) => {
  const prefix = "";
  const titleWithDetails = `${prefix ? prefix + "/" : ""} ${title}`;

  return (
    <div
      style={{
        display: "flex",
        flex: 1,
        flexDirection: "column",
        minHeight: "100vh",
      }}
      {...props}
    >
      {/* <Header /> */}
      <div
        style={{
          flex: 1,
          color: "#24252E",
          backgroundColor: "white",
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <div
            style={{
              marginTop: "50px",
              display: "block",
              width: "40px",
              height: "4px",
              backgroundColor: "black",
              content: " ",
            }}
          />
          <h1
            style={{
              display: "inline-block",
              textAlign: "center",
              marginTop: "20px",
              fontWeight: "bold",
              marginRight: "10px",
            }}
          >
            {titleWithDetails}
          </h1>
          {Boolean(subtitle) && (
            <p
              style={{
                display: "inline-block",
              }}
            >
              {subtitle}
            </p>
          )}
        </div>
        <div style={{ width: "100%" }}>{header}</div>
        <div className="container" style={{ marginTop: "20px" }}>
          <div className="row justify-content-center">{children}</div>
          {Boolean(footerNote) && (
            <div
              style={{
                backgroundColor: "#edf3f8",
                borderRadius: "10px",
                padding: "16px 20px",
                marginBottom: "26px",
              }}
            >
              {footerNote}
            </div>
          )}
        </div>
        {/*  {footer} */}
      </div>
      <Footer />
    </div>
  );
};

const Infantil = () => {
  const report = charts;

  return (
    <ReportWrapper
      title={"Documentação - Relatório Exemplo"}
      subtitle="(cuidado até o 2º ano de vida de acordo com a data da última atualização pelo município)"
      footer={<ReportFooter chaveListaNominal="Infantil" equipe={undefined} />}
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

const Report = () => {
  return <Infantil />;
};

const meta = {
  title: "Recipies/Report",
  component: Report,
  parameters: {
    //layout: 'centered',
  },
  tags: ["autodocs"],
  argTypes: {},
  args: {},
} satisfies Meta;

export default meta;
type Story = StoryObj<typeof meta>;

export const Basic: Story = {
  args: {},
};
