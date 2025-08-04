import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { Typography } from "../../ui/Typography";
import { PainelParams } from "../../ui/ReportFooter";

import diabetes from "../../../assets/images/menu/diabetes.png";
import hipertensao from "../../../assets/images/menu/hipertensao.png";
import bucal from "../../../assets/images/menu/bucal.png";
import children from "../../../assets/images/menu/children.png";
import old from "../../../assets/images/menu/old.png";
import quality from "../../../assets/images/menu/quality.png";
import ReactECharts from "echarts-for-react";
import { getPorcentagemIndicador } from "../../../utils";
import { content } from "../../../assets/content/content";

const sumValues = (data: Array<{ value: number }>) =>
  data.reduce((acc, item) => acc + (item.value || 0), 0);

const CardDonutChart = ({ data }: { data: Array<{ tag: string, value: number }> }) => {
  let options = {};
  let total = sumValues(data);

  const entries = data.map(({ value, tag }) => ({
    value,
    name: getPorcentagemIndicador(tag, total, value),
    label:content?.[tag],
  }));

  console.log("entries", entries);

  options = {
    color: ["#84aaff", "#0069d0", "#e9ecef"],
    tooltip: {
      trigger: "item",
      formatter: function (params: any) {
        return `${params.data.label}: ${params.data.value} (${params.name})`;
      },
    },
    series: [
      {
        name: "Grafico 1",
        type: "pie",
        radius: "38px",
        center: ["50%", "50%"],
        data: entries,
        label: {
          position: "top",
          show: true,
          formatter: ["{b}"].join("\n"),
          fontSize: 16,
          color: "#FFF",
          alignTo: "labelLine",
          distanceToLabelLine: -24,
        },
        emphasis: {
          itemStyle: {},
        },
      },
    ],
  };

  return (
    <ReactECharts
      option={options}
      style={{
        width: "174px",
        height: "122px",
      }}
      opts={{ renderer: "svg" }}
    />
  );
};

const ReportCardSelector = ({ charts }: any) => {
  let navigate = useNavigate();
  const { id } = useParams<PainelParams>();
  const [params] = useSearchParams();
  const equipe = params.get("equipe");

  type availableRoutesToThemedReport =
    | "diabetes"
    | "hipertensao"
    | "infantil"
    | "qualidade"
    | "idosaV2"
    | "saude-bucal";

  const handleToThemedReport = (key: availableRoutesToThemedReport) => {
    if (id) {
      navigate(`/${key}/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/${key}${equipe ? `?equipe=${equipe}` : ""}`);
    }
  };

  return (
    <>
      {" "}
      <div style={{ marginTop: "60px", marginBottom: "20px" }}>
        <Typography.Subtitle>Relatórios Temáticos</Typography.Subtitle>
      </div>
      <div className="container">
        <div className="row container-cards-condicoes">
          {Boolean(charts?.["tematico-diabetes"]?.data) && (
            <div
              className="card-condicao p-2"
              onClick={() => handleToThemedReport("diabetes")}
            >
              <span className="nome-condicao">Diabetes</span>
              <h4>{sumValues(charts?.["tematico-diabetes"]?.data)}</h4>
              <div className="d-flex align-items-center">
                <img src={diabetes} alt="Diabetes" className="mx-2" />
                <CardDonutChart data={charts?.["tematico-diabetes"]?.data} />
              </div>
            </div>
          )}
          {Boolean(charts?.["tematico-diabetes"]?.data) && (
            <div
              className="card-condicao p-2"
              onClick={() => handleToThemedReport("hipertensao")}
            >
              <span className="nome-condicao">Hipertensão</span>
              <h4>{sumValues(charts?.["tematico-diabetes"]?.data)}</h4>
              <div className="d-flex align-items-center">
                <img src={hipertensao} alt="Hipertensão" className="mx-2" />
                <CardDonutChart data={charts?.["tematico-diabetes"]?.data} />
              </div>
            </div>
          )}
          {Boolean(charts?.["tematico-diabetes"]?.data) && (
            <div
              className="card-condicao p-2"
              onClick={() => handleToThemedReport("qualidade")}
            >
              <span className="nome-condicao">Qualidade de Cadastros</span>
              <h4>{sumValues(charts?.["tematico-diabetes"]?.data)}</h4>
              <div className="d-flex align-items-center">
                <img src={quality} alt="Qualidade" className="mx-2" />
                <CardDonutChart data={charts?.["tematico-diabetes"]?.data} />
              </div>
            </div>
          )}
        </div>
        <div
          className="row container-cards-condicoes"
          style={{ marginTop: "20px" }}
        >
          {Boolean(charts?.["tematico-diabetes"]?.data) && (
            <div
              className="card-condicao p-2"
              onClick={() => handleToThemedReport("idosaV2")}
            >
              <span className="nome-condicao">Cuidado da Pessoa Idosa</span>
              <h4>{sumValues(charts?.["tematico-diabetes"]?.data)}</h4>
              <div className="d-flex align-items-center">
                <img
                  width={"30%"}
                  src={old}
                  alt="Pessoa Idosa"
                  className="mx-2"
                />
                <CardDonutChart data={charts?.["tematico-diabetes"]?.data} />
              </div>
            </div>
          )}
          {Boolean(charts?.["tematico-diabetes"]?.data) && (
            <div
              className="card-condicao p-2"
              onClick={() => handleToThemedReport("saude-bucal")}
            >
              <span className="nome-condicao">Saúde Bucal</span>
              <h4>{sumValues(charts?.["tematico-diabetes"]?.data)}</h4>
              <div className="d-flex align-items-center">
                <img
                  width={"34%"}
                  src={bucal}
                  alt="Saude Bucal"
                  className="mx-2"
                />
                <CardDonutChart data={charts?.["tematico-diabetes"]?.data} />
              </div>
            </div>
          )}
          {Boolean(charts?.["tematico-diabetes"]?.data) && (
            <div
              className="card-condicao p-2"
              onClick={() => handleToThemedReport("infantil")}
            >
              <span className="nome-condicao">Desenvolvimento Infantil</span>
              <h4>{sumValues(charts?.["tematico-diabetes"]?.data)}</h4>
              <div className="d-flex align-items-center">
                <img
                  width={"30%"}
                  src={children}
                  alt="Desenvolvimento Infantil"
                  className="mx-2"
                />
                <CardDonutChart data={charts?.["tematico-diabetes"]?.data} />
              </div>
            </div>
          )}
        </div>
        <div className="d-flex my-5 justify-content-center">
          <div className="container-areas d-flex align-items-center me-4">
            <div className="box-container-light me-2"></div>
            <h4>Zona Urbana</h4>
          </div>
          <div className="container-areas d-flex align-items-center ms-4">
            <div className="box-container-dark me-2"></div>
            <h4>Zona Rural</h4>
          </div>
          <div className="container-areas d-flex align-items-center ms-4">
            <div className="box-container-nonactive me-2"></div>
            <h4>Não Informado</h4>
          </div>
        </div>
      </div>
    </>
  );
};

export default ReportCardSelector;
