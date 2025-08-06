import { CSSProperties, memo } from "react";
import { useParams, useSearchParams } from "react-router-dom";

import { content } from "../../assets/content/content";
import Medkit from "../../assets/images/medkit.png";
import People from "../../assets/images/people.svg";
import ErrorMessage from "../../components/ui/ErrorMessage";
import LoadingSpinner from "../../components/ui/LoadingSpinner";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import useReportDataInfantil from "../../hooks/sections/infantil/useReportDataInfantil";
import "../../styles/idosa.scss";
import { formataNumero } from "../../utils";
import { getChartDescription } from "../../utils/chartTitleUtils";
import { ReportViewTypeEnum } from "../../utils/viewTypeEnum";
import { PainelParams } from "../Hipertensao";
import { reportCharts, reportSections } from "./Infantil.utils";

const RenderChartGroup = ({
  report,
  chartList,
  renderSmall,
  alignMiddle,
  reportViewType,
  loadings,
  errors,
  refetchAll,
}: any) => {
  return Object.keys(chartList).map((chartKey) => {
    const CustomChart = chartList?.[chartKey]?.Chart;
    const chartConfigs = chartList?.[chartKey]?.config;
    const data = (report as any)?.[chartKey];
    const isRow = chartKey === "row" || chartKey.indexOf("Row") !== -1;
    const isSecondRow = chartKey === "secondRow";

    // Verificar loading para esta seção
    if (loadings[chartKey as keyof typeof loadings]) {
      return <LoadingSpinner key={chartKey} />;
    }

    // Verificar erro para esta seção
    if (errors[chartKey as keyof typeof errors]) {
      return (
        <ErrorMessage
          key={chartKey}
          error={errors[chartKey as keyof typeof errors]}
          title={`Erro ao carregar ${content?.[chartKey] || chartKey}`}
          showRetry={true}
          onRetry={refetchAll}
        />
      );
    }

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
          key={chartKey}
          className="is-row"
          style={{
            gap: "10px",
            justifyContent: "center",
          }}
        >
          <RenderChartGroup
            report={report}
            chartList={chartList?.[chartKey]}
            renderSmall
            alignMiddle={true}
            reportViewType={reportViewType}
            loadings={loadings}
            errors={errors}
            refetchAll={refetchAll}
          />
        </div>
      );
    }

    const containerStyle: CSSProperties = {
      position: "relative",
      marginBottom: "40px",
      textAlign: "center",
    };

   // containerStyle.maxWidth = "400px";

    return (
      <div key={chartKey} style={containerStyle}>
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
  const { data, loadings, errors, refetchAll } = useReportDataInfantil({ ubsId: id, equipe });

  const reportViewType = !!equipe
    ? ReportViewTypeEnum.EQUIPE
    : !!id
    ? ReportViewTypeEnum.UBS
    : ReportViewTypeEnum.MUNICIPIO;

  const footerNote = (
    <div>
      ¹ Crianças que ainda não atingiram idade mínima para inclusão no critério
      correspondente às diretrizes preconizadas pelo Ministério da Saúde
    </div>
  );

  console.log({data})

  return (
    <>
      <ReportWrapper
        title={"Desenvolvimento Infantil"}
        subtitle="Crianças até 36 meses"
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
              {loadings.total ? (
                <LoadingSpinner size="sm" text="Carregando total..." />
              ) : errors.total ? (
                <ErrorMessage
                  error={errors.total}
                  title="Erro ao carregar total de crianças"
                  showRetry={true}
                  onRetry={refetchAll}
                />
              ) : (
                <>
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
                    {formataNumero(data?.total?.['total-cadastros']?.data ?? 0)}
                  </span>
                </>
              )}
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
              {loadings["total-atendimentos"] ? (
                <LoadingSpinner size="sm" text="Carregando atendimentos..." />
              ) : errors["total-atendimentos"] ? (
                <ErrorMessage
                  error={errors["total-atendimentos"]}
                  title="Erro ao carregar total de atendimentos"
                  showRetry={true}
                  onRetry={refetchAll}
                />
              ) : (
                <>
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
                    {formataNumero(data?.["total-atendimentos"] ?? [])}
                  </span>
                </>
              )}
            </div>
          </div>
        </div>
        {reportSections().map((chartList: any, index: number) => (
          <RenderChartGroup
            key={index}
            report={data}
            chartList={chartList}
            reportViewType={reportViewType}
            loadings={loadings}
            errors={errors}
            refetchAll={refetchAll}
          />
        ))}
        <center style={{ marginTop: "60px", marginBottom: "30px" }}>
          <h2>
            <b>Proporção de crianças com:</b>
          </h2>
        </center>
        {reportCharts.map((chartList: any, index: number) => (
          <RenderChartGroup
            key={index}
            report={data}
            chartList={chartList}
            loadings={loadings}
            errors={errors}
            refetchAll={refetchAll}
          />
        ))}
      </ReportWrapper>
    </>
  );
};

export default memo(Infantil);
