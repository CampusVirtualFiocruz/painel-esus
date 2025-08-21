import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { ReportBasicParams } from "../../../utils";
import { Typography } from "../../ui/Typography";

import ReactECharts from "echarts-for-react";
import { content } from "../../../assets/content/content";
import bucal from "../../../assets/images/menu/bucal.png";
import children from "../../../assets/images/menu/children.png";
import diabetes from "../../../assets/images/menu/diabetes.png";
import hipertensao from "../../../assets/images/menu/hipertensao.png";
import old from "../../../assets/images/menu/old.png";
import quality from "../../../assets/images/menu/quality.png";
import { getPorcentagemIndicador } from "../../../utils";

const sumValues = (data: Array<{ value: number }>) =>
  data.reduce((acc, item) => acc + (item.value || 0), 0);

const CardDonutChart = ({ data }: { data: Array<{ tag: string, value: number }> }) => {
  let options = {};
  let total = sumValues(data);

  const entries = data.map(({ value, tag }) => ({
    value,
    name: getPorcentagemIndicador(tag, total, value),
    label: content?.[tag] ?? 'Não informado',
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
  const { id } = useParams<ReportBasicParams>();
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

  // Configuração dos cartões temáticos
  interface ThematicCardConfig {
    chartKey: string;
    routeKey: availableRoutesToThemedReport;
    title: string;
    icon: string;
    alt: string;
    width?: string;
  }

  const thematicCardsConfig: ThematicCardConfig[][] = [
    // Primeira linha
    [
      {
        chartKey: "tematico-diabetes",
        routeKey: "diabetes",
        title: "Diabetes",
        icon: diabetes,
        alt: "Diabetes"
      },
      {
        chartKey: "tematico-hipertensao",
        routeKey: "hipertensao",
        title: "Hipertensão",
        icon: hipertensao,
        alt: "Hipertensão"
      },
      {
        chartKey: "tematico-qualidade",
        routeKey: "qualidade",
        title: "Qualidade de Cadastros",
        icon: quality,
        alt: "Qualidade"
      }
    ],
    // Segunda linha
    [
      {
        chartKey: "tematico-idoso",
        routeKey: "idosaV2",
        title: "Cuidado da Pessoa Idosa",
        icon: old,
        alt: "Pessoa Idosa",
        width: "30%"
      },
      {
        chartKey: "tematico-bucal",
        routeKey: "saude-bucal",
        title: "Saúde Bucal",
        icon: bucal,
        alt: "Saude Bucal",
        width: "34%"
      },
      {
        chartKey: "tematico-infantil",
        routeKey: "infantil",
        title: "Desenvolvimento Infantil",
        icon: children,
        alt: "Desenvolvimento Infantil",
        width: "30%"
      }
    ]
  ];

  const renderThematicCard = (cardConfig: ThematicCardConfig) => {
    const { chartKey, routeKey, title, icon, alt, width } = cardConfig;
    const chartData = charts?.[chartKey]?.data;

    if (!Boolean(chartData)) return null;

    return (
      <div
        key={chartKey}
        className="card-condicao p-2"
        onClick={() => handleToThemedReport(routeKey)}
      >
        <span className="nome-condicao">{title}</span>
        <h4>{sumValues(chartData)}</h4>
        <div className="d-flex align-items-center">
          <img
            src={icon}
            alt={alt}
            className="mx-2"
            {...(width && { width })}
          />
          <CardDonutChart data={chartData} />
        </div>
      </div>
    );
  };

  return (
    <>
      {" "}
      <div style={{ marginTop: "60px", marginBottom: "20px" }}>
        <Typography.Subtitle>Relatórios Temáticos</Typography.Subtitle>
      </div>
      <div className="container">
        {thematicCardsConfig.map((cardRow, rowIndex) => (
          <div
            key={`thematic-row-${rowIndex}`}
            className="row container-cards-condicoes"
            style={rowIndex > 0 ? { marginTop: "20px" } : undefined}
          >
            {cardRow.map(renderThematicCard)}
          </div>
        ))}
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
