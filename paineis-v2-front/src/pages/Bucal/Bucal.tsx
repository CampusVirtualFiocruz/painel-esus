import { Button } from "bold-ui";
import { CSSProperties, memo, useState } from "react";
import { useParams, useSearchParams } from "react-router-dom";

import { content } from "../../assets/content/content";
import People from "../../assets/images/people.svg";
import ErrorMessage from "../../components/ui/ErrorMessage";
import LoadingSpinner from "../../components/ui/LoadingSpinner";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import useReportDataBucal from "../../hooks/sections/bucal/useReportDataBucal";
import "../../styles/idosa.scss";
import { formataNumero } from "../../utils";
import { getChartDescription } from "../../utils/chartTitleUtils";
import { ReportViewTypeEnum } from "../../utils/viewTypeEnum";
import { PainelParams } from "../Hipertensao";
import { reportCharts, reportSections } from "./Bucal.utils";

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
    const data = (report as any)?.[chartKey]?.data;
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
            gap: "60px",
            justifyContent: isSecondRow ? "space-evenly" : "initial",
          }}
        >
          <RenderChartGroup
            report={report}
            chartList={chartList?.[chartKey]}
            renderSmall
            alignMiddle={isSecondRow}
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
    };

    if (alignMiddle) {
      containerStyle.maxWidth = "400px";
    }

    return (
      <div key={chartKey} style={containerStyle}>
        <h5
          style={{
            fontWeight: "bold",
            textAlign: "center",
            paddingTop: renderSmall ? "30px" : "initial",
          }}
        >
          {content?.[chartConfigs?.overrideTitle] ||
            content?.[chartKey] ||
            chartKey}
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

const Bucal = () => {
  const [params] = useSearchParams();
  const equipe = params.get("equipe") as any;
  const [recorte, setRecorte] = useState<"atendidas" | "cadastradas">(
    "atendidas"
  );

  const { id } = useParams<PainelParams>();
  const { data, loadings, errors, refetchAll } = useReportDataBucal({ ubsId: id, equipe, recorte });

  const reportViewType = !!equipe
    ? ReportViewTypeEnum.EQUIPE
    : !!id
    ? ReportViewTypeEnum.UBS
    : ReportViewTypeEnum.MUNICIPIO;

  const footerNote =
    recorte === "atendidas" ? (
      <>
        A <b>População Atendida</b> se refere à todas as pessoas vinculadas à
        uma equipe que tenham realizado algum atendimento odontológico nos
        últimos 2 anos. Para fins deste relatório serão considerados todos os
        atendimentos odontológicos da pessoa, ainda que tenham sido realizados
        em outra Unidade de Saúde, conforme a regra de cálculo preconizada. Não
        serão incluídas na População Atendida as pessoas que realizaram
        atendimento odontológico, porém, não possuem Ficha da Cadastro
        Individual.
      </>
    ) : (
      <>
        A <b>População Cadastrada</b> se refere à todas as pessoas vinculadas à
        uma equipe que tenham a Ficha de Cadastro Individual atualizada nos
        últimos 2 anos. Para fins deste relatório serão considerados todos os
        atendimentos odontológicos da pessoa, ainda que tenham sido realizados
        em outra Unidade de Saúde, conforme a regra de cálculo preconizada.
      </>
    );

  return (
    <>
      <ReportWrapper
        title={"Saúde Bucal"}
        footer={<ReportFooter chaveListaNominal="Bucal" equipe={equipe} />}
        footerNote={footerNote}
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
              kind={recorte === "atendidas" ? "primary" : "normal"}
              onClick={() => {
                setRecorte("atendidas");
              }}
            >
              Atendidas
            </Button>
            <Button
              style={{ height: "36px" }}
              kind={recorte === "cadastradas" ? "primary" : "normal"}
              onClick={() => {
                setRecorte("cadastradas");
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
            }}
          >
            <div
              style={{
                flex: 1,
                padding: "20px",
                backgroundColor: recorte === "atendidas" ? "#0069D0" : "",
                border: recorte === "atendidas" ? "white" : "1px solid black",
                color: recorte === "atendidas" ? "white" : "black",
                textAlign: "center",
              }}
            >
              {loadings.total ? (
                <LoadingSpinner size="sm" text="Carregando total..." />
              ) : errors.total ? (
                <ErrorMessage
                  error={errors.total}
                  title="Erro ao carregar total de atendidas"
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
                    Total de pessoas
                    <br />
                    atendidas {getChartDescription("", reportViewType, [])}
                  </span>
                  <img
                    src={People}
                    alt="Icone de pessoas"
                    width={"30px"}
                    style={{
                      filter: recorte === "atendidas" ? "brightness(10)" : "",
                      transform: "translate(-10px, -5px)",
                    }}
                  />
                  <span style={{ fontSize: "26px" }}>
                    {formataNumero(data?.total?.data?.atendidas)}
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
                backgroundColor: recorte !== "atendidas" ? "#0069D0" : "",
                border: recorte !== "atendidas" ? "white" : "1px solid black",
                color: recorte !== "atendidas" ? "white" : "black",
                textAlign: "center",
              }}
            >
              {loadings.total ? (
                <LoadingSpinner size="sm" text="Carregando total..." />
              ) : errors.total ? (
                <ErrorMessage
                  error={errors.total}
                  title="Erro ao carregar total de cadastradas"
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
                    Total de pessoas
                    <br />
                    cadastradas {getChartDescription("", reportViewType, [])}*
                  </span>
                  <img
                    src={People}
                    alt="Icone de pessoas"
                    width={"30px"}
                    style={{
                      filter: recorte !== "atendidas" ? "brightness(10)" : "",
                      transform: "translate(-10px, -5px)",
                    }}
                  />
                  <span style={{ fontSize: "26px" }}>
                    {formataNumero(data?.total?.data?.cadastradas)}
                  </span>
                </>
              )}
            </div>
            <div
              style={{
                marginTop: "2px",
                width: "100%",
                textAlign: "right",
                fontWeight: "initial",
                fontSize: "14px",
              }}
            >
              *nos últimos 24 meses
            </div>
          </div>
        </div>
        <center style={{ marginTop: "60px", marginBottom: "30px" }}>
          <h2>
            <b>
              Proporção referente a quantidade de pessoas{" "}
              {recorte === "atendidas" ? "atendidas" : "cadastradas"}{" "}
              {getChartDescription("", reportViewType, [])}:
            </b>
          </h2>
          <p>(Dados referentes aos últimos 24 meses)</p>
        </center>
        {reportCharts.map((chartList: any) => (
          <RenderChartGroup
            key={JSON.stringify(chartList)}
            report={data}
            chartList={chartList}
            loadings={loadings}
            errors={errors}
            refetchAll={refetchAll}
          />
        ))}
        {reportSections(recorte).map((chartList: any, index: number) => (
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
      </ReportWrapper>
    </>
  );
};

export default memo(Bucal);
