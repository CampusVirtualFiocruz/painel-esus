import { CSSProperties, memo, useState } from "react";
import { Button } from "bold-ui";
import { useParams, useSearchParams } from "react-router-dom";

import People from "../../assets/images/people.svg";
import Medkit from "../../assets/images/medkit.png";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import { content } from "../../assets/content/content";
import useReportDataBucal from "../../hooks/sections/bucal/useReportDataBucal";
import { PainelParams } from "../Hipertensao";
import { fixedLegend, getColorizedCharts, reportSections } from "./Bucal.utils";
import "../../styles/idosa.scss";


const RenderChartGroup = ({
  report,
  chartList,
  renderSmall,
  ChartFooter,
  alignMiddle,
}: any) => {
  return Object.keys(chartList).map((chartKey) => {
    const CustomChart = chartList?.[chartKey]?.Chart;
    const chartConfigs = chartList?.[chartKey]?.config;
    const data = (report as any)?.[chartKey]?.data;
    const isRow = chartKey === "row" || chartKey.indexOf("Row") !== -1;
    const isSecondRow = chartKey === "secondRow";

    if (chartConfigs) {
      const xAxisNames = data?.map((d: any) => content?.[d?.tag] ?? d?.tag);
      chartConfigs.xAxis = { data: [], ...chartConfigs.xAxis };
      chartConfigs.xAxis.data = xAxisNames;
    }

    if (isRow) {
      return (
        <div
          className="is-row"
          style={{
            gap: "60px",
            justifyContent: isSecondRow ? "center" : "initial",
          }}
        >
          <RenderChartGroup
            report={report}
            chartList={chartList?.[chartKey]}
            renderSmall
            ChartFooter={ChartFooter}
            alignMiddle={isSecondRow}
          />
        </div>
      );
    }

    const containerStyle: CSSProperties = {
      position: "relative",
      marginBottom: "40px",
    };

    if (alignMiddle) {
      containerStyle.maxWidth = "400px";
    }

    return (
      <div style={containerStyle}>
        <h5
          style={{
            fontWeight: "bold",
            textAlign: "center",
            padding: renderSmall ? "30px" : "initial",
            minHeight: "110px",
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
        {ChartFooter && <ChartFooter data={data} />}
      </div>
    );
  });
};

const ClassificationFooter = ({ data }: any) => {
  let percentage: any = undefined;
  let hasHighlightConfig =
    data && Array.isArray(data) && data?.[1]?.tag === "realizado";

  if (hasHighlightConfig) {
    const mainValue = data?.[1]?.value;
    const total = mainValue + data?.[0]?.value;
    percentage = (mainValue / total) * 100;
  }

  return (
    <div>
      {fixedLegend.map(({ color, title, text, min, max }) => {
        const shouldHighlight = percentage >= min && percentage < max;

        return (
          <div
            style={{
              padding: "3px",
              border: shouldHighlight ? "1px gray solid" : "",
            }}
          >
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
        );
      })}
    </div>
  );
};

const Bucal = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;
  const [recorte, setRecorte] = useState<"atendidos" | "cadastrados">(
    "atendidos"
  );

  const { id } = useParams<PainelParams>();
  const reportData: any = useReportDataBucal({ ubsId: id, equipe, recorte });

  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  const charts = getColorizedCharts(reportData);

  return (
    <>
      <ReportWrapper
        title={"Saúde Bucal"}
        footer={<ReportFooter chaveListaNominal="Bucal" equipe={equipe} />}
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
              kind={recorte === "atendidos" ? "primary" : "normal"}
              onClick={() => {
                setRecorte("atendidos");
              }}
            >
              Atendidas
            </Button>
            <Button
              style={{ height: "36px" }}
              kind={recorte === "cadastrados" ? "primary" : "normal"}
              onClick={() => {
                setRecorte("cadastrados");
              }}
            >
              Cadastradas
            </Button>
          </div>
        }
      >
        <div
          style={{
            display: "flex",
            width: "100%",
            maxWidth: "600px",
            marginTop: "60px",
            marginBottom: "30px",
            gap: "40px",
            fontWeight: "bold",
          }}
        >
          <div
            style={{
              flex: 1,
              padding: "20px",
              backgroundColor: recorte === "atendidos" ? "#0069D0" : "",
              border: recorte === "atendidos" ? "white" : "1px solid black",
              color: recorte === "atendidos" ? "white" : "black",
              textAlign: "center",
            }}
          >
            <span style={{ display: "block", fontSize: "16px", marginBottom: "8px" }}>
              Total de pessoas
              <br />
              atendidas na UBS
            </span>
            <img
              src={People}
              alt="Icone de pessoas"
              width={"30px"}
              style={{ filter: recorte === "atendidos" ? "brightness(10)" : "", transform: "translate(-10px, -5px)"}}
            />
            <span style={{ fontSize: "26px" }}>{report?.total?.data?.atendidas}</span>
          </div>
          <div
            style={{
              flex: 1,
              padding: "20px",
              backgroundColor: recorte !== "atendidos" ? "#0069D0" : "",
              border: recorte !== "atendidos" ? "white" : "1px solid black",
              color: recorte !== "atendidos" ? "white" : "black",
              textAlign: "center",
            }}
          >
            <span style={{ display: "block", fontSize: "16px", marginBottom: "8px" }}>
              Total de pessoas
              <br />
              cadastradas na UBS
            </span>
            <img
              src={People}
              alt="Icone de pessoas"
              width={"30px"}
              style={{ filter: recorte !== "atendidos" ? "brightness(10)" : "", transform: "translate(-10px, -5px)"}}
            />
            <span style={{ fontSize: "26px" }}>{report?.total?.data?.cadastradas}</span>
          </div>
        </div>
        {reportSections.map((chartList: any) => (
          <RenderChartGroup report={report} chartList={chartList} />
        ))}
        <center style={{ marginTop: "60px", marginBottom: "30px" }}>
          <h2>
            <b>Proporção referente a quantidade de pessoas atendidas na UBS:</b>
          </h2>
          <p>(Dados referentes aos últimos 24 meses)</p>
        </center>
        {charts.map((chartList: any) => (
          <RenderChartGroup
            report={report}
            chartList={chartList}
            ChartFooter={ClassificationFooter}
          />
        ))}
      </ReportWrapper>
    </>
  );
};

export default memo(Bucal);
