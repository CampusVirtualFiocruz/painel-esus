import { CSSProperties, memo } from "react";
import { useParams, useSearchParams } from "react-router-dom";
import { content } from "../../assets/content/content";
import ErrorMessage from "../../components/ui/ErrorMessage";
import LoadingSpinner from "../../components/ui/LoadingSpinner";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import useReportDataDiabetes from "../../hooks/sections/diabetes/useReportDataDiabetes";
import { formataNumero, ReportBasicParams } from "../../utils";
import { getChartDescription } from "../../utils/chartTitleUtils";
import { ReportViewTypeEnum } from "../../utils/viewTypeEnum";
import { Card, RenderSingleValue } from "../../components/ui";
import { reportLeftSections, reportRightSections } from "./Diabetes.utils";
import "../../styles/idosa.scss";
import "./Diabetes.scss";

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
          //className="is-row"
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
      marginBottom: "60px",
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
              paddingTop: 0,
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

const Diabetes = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;

  const { id } = useParams<ReportBasicParams>();
  const { data, loadings, errors, refetchAll } = useReportDataDiabetes({
    ubsId: id,
    equipe,
  });

  const reportViewType = !!equipe
    ? ReportViewTypeEnum.EQUIPE
    : !!id
    ? ReportViewTypeEnum.UBS
    : ReportViewTypeEnum.MUNICIPIO;

  const footerNote = (
    <div>
      ¹ O número de pessoas com diabetes equivale ao total de indivíduos que
      tiveram atendimentos individuais com registro do código CID e/ou CIAP
      correspondente à condiçãode saúde na Ficha de Atendimento Individual,
      somado ao conjunto de pessoas com registro autorreferido da condição de
      saúde na Ficha de Cadastro Individual.
    </div>
  );

  return (
    <>
      <ReportWrapper
        title={"Painel Diabetes"}
        footer={
          <ReportFooter chaveListaNominal="Diabetes" equipe={equipe} />
        }
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
          <div style={{ display: "flex", flexDirection: "row", gap: "6px" }}>
            <Card style={{ flex: 1 }}>
              <RenderSingleValue
                icon="medkit"
                title="Total de atendimentos nos últimos 12 meses"
                value={formataNumero(
                  data?.["total"]?.["total-atendimentos-12-meses"]?.data ?? []
                )}
              />
            </Card>
            <Card style={{ flex: 2 }}>
              <div
                style={{ display: "flex", flexDirection: "row", gap: "20px" }}
              >
                <RenderSingleValue
                  icon="people"
                  title="Nº de pessoas com diabetes (CID/CIAP)¹"
                  value={data?.["total"]?.[
                    "total-pessoas-cid-ciap"
                  ]?.data?.toLocaleString("pt-BR")}
                />
                <RenderSingleValue
                  icon="people"
                  title="Nº de pessoas com diabetes (autorreferida)¹"
                  value={data?.["total"]?.[
                    "total-pessoas-auto"
                  ]?.data?.toLocaleString("pt-BR")}
                />
              </div>
            </Card>
          </div>
        </div>
        <div style={{ display: "flex", flex: "row", gap: "80px" }}>
        <div>
          {reportLeftSections().map((chartList: any, index: number) => (
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
          </div>
          <div style={{ paddingTop: "0"}}>
          {reportRightSections().map((chartList: any, index: number) => (
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
          </div>
        </div>
      </ReportWrapper>
    </>
  );
};

export default memo(Diabetes);
