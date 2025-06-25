import { CSSProperties, memo } from "react";
import { useParams, useSearchParams } from "react-router-dom";

import People from "../../assets/images/people.svg";
import Medkit from "../../assets/images/medkit.png";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import { content } from "../../assets/content/content";
import { PainelParams } from "../Hipertensao";
import { reportCharts, reportSections } from "./Infantil.utils";
import { formataNumero } from "../../utils";
import { getChartDescription } from "../../utils/chartTitleUtils";
import { ReportViewTypeEnum } from "../../utils/viewTypeEnum";
import "../../styles/idosa.scss";
import useReportDataInfantil from "../../hooks/sections/infantil/useReportDataInfantil";

const RenderChartGroup = ({
  report,
  chartList,
  renderSmall,
  alignMiddle,
  reportViewType,
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

    const configWithYAxisName =
      chartConfigs && chartConfigs.yAxis
        ? {
            ...chartConfigs,
            yAxis: {
              ...chartConfigs.yAxis,
              name: getChartDescription(
                chartConfigs.yAxis.name,
                reportViewType,
                content
              ),
            },
          }
        : chartConfigs;

    if (isRow) {
      return (
        <div
          className="is-row"
          style={{
            gap: "60px",
            justifyContent: "center",
          }}
        >
          <RenderChartGroup
            report={report}
            chartList={chartList?.[chartKey]}
            renderSmall
            alignMiddle={true}
            reportViewType={reportViewType}
          />
        </div>
      );
    }

    const containerStyle: CSSProperties = {
      position: "relative",
      marginBottom: "40px",
      textAlign: "center",
    };

    containerStyle.maxWidth = "400px";

    return (
      <div style={containerStyle}>
        <center>
          <h5
            style={{
              fontWeight: "bold",
              textAlign: "center",
              paddingTop: renderSmall ? "30px" : "initial",
              maxWidth: "336px",
            }}
          >
            {content?.[chartConfigs?.overrideTitle] ||
              content?.[chartKey] ||
              chartKey}
          </h5>
        </center>
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
        <CustomChart data={data} config={configWithYAxisName} />
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

const Infantil = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  const { id } = useParams<PainelParams>();
  const reportData: any = useReportDataInfantil({ ubsId: id, equipe });

  const reportViewType = !!equipe
    ? ReportViewTypeEnum.EQUIPE
    : !!id
    ? ReportViewTypeEnum.UBS
    : ReportViewTypeEnum.MUNICIPIO;

  const report = reportData?.data;

  if (reportData?.isLoading) {
    return <center>Aguarde...</center>;
  }

  const footerNote = (
    <div>
      ¹ Crianças que ainda não atingiram idade mínima para inclusão no critério
      correspondente às diretrizes preconizadas pelo Ministério da Saúde
    </div>
  );

  return (
    <>
      <ReportWrapper
        title={"Desenvolvimento Infantil"}
        subtitle="Crianças de até 36 meses"
        footer={<ReportFooter chaveListaNominal="Infantil" equipe={equipe} />}
        footerNote={footerNote}
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
            }}
          >
            <div
              style={{
                flex: 1,
                padding: "20px",
                backgroundColor: "",
                border: "1px solid black",
                color: "black",
                textAlign: "center",
              }}
            >
              <span
                style={{
                  display: "block",
                  fontSize: "16px",
                  marginBottom: "8px",
                }}
              >
                Total de crianças
                <br />
                {getChartDescription("", reportViewType, [])}
              </span>
              <img
                src={People}
                alt="Icone de pessoas"
                width={"30px"}
                style={{
                  filter: "",
                  transform: "translate(-10px, -5px)",
                }}
              />
              <span style={{ fontSize: "26px" }}>
                {formataNumero(report?.total?.data)}
              </span>
            </div>
            <span>&nbsp;</span>
          </div>
          <div
            style={{
              flex: 1,
            }}
          >
            <div
              style={{
                flex: 1,
                padding: "20px",
                backgroundColor: "",
                border: "1px solid black",
                color: "black",
                textAlign: "center",
              }}
            >
              <span
                style={{
                  display: "block",
                  fontSize: "16px",
                  marginBottom: "8px",
                }}
              >
                Total de crianças atendidas nos últimos 12 meses
              </span>
              <img
                src={Medkit}
                alt="Icone de pessoas"
                width={"30px"}
                style={{
                  filter: "",
                  transform: "translate(-10px, -5px)",
                }}
              />
              <span style={{ fontSize: "26px" }}>
                {formataNumero(
                  (
                    report?.["infantil-uma-consulta-12-meses"]?.data ?? []
                  )?.find(({ tag }: any) => tag === "sim")?.value
                )}
              </span>
            </div>
          </div>
        </div>
        {reportSections().map((chartList: any) => (
          <RenderChartGroup
            report={report}
            chartList={chartList}
            reportViewType={reportViewType}
          />
        ))}
        <center style={{ marginTop: "60px", marginBottom: "30px" }}>
          <h2>
            <b>Proporção de crianças com:</b>
          </h2>
        </center>
        {reportCharts.map((chartList: any) => (
          <RenderChartGroup report={report} chartList={chartList} />
        ))}
      </ReportWrapper>
    </>
  );
};

export default memo(Infantil);
