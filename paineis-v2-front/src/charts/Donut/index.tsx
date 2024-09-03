import ReactECharts from "echarts-for-react";
import { formatAsPercent } from "../../utils";
import "./style.scss";

export function Donut({ data }: any) {
  let nome = "prenatal-indicators";
  let comConsulta = data[1].com_consulta;
  let semConsulta = data[1].sem_consulta;

  let dataGraphic = [{ value: comConsulta }, { value: semConsulta }];

  const options = {
    color: ["#84aaff", "#0069d0"],
    tooltip: {
      trigger: "item",
      formatter: "({d}%)",
    },
    series: [
      {
        name: nome,
        type: "pie",
        radius: ["30", "52"],
        avoidLabelOverlap: false,
        label: {
          show: true,
          position: "center",
          fontSize: "16",
          fontWeight: "bold",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: "16",
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: dataGraphic,
      },
    ],
  };

  return (
    <div className="donut">
      <ReactECharts
        option={options}
        style={{
          width: "116px",
          height: "116px",
        }}
        opts={{ renderer: "svg" }}
      />
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          alignItems: "center",
          width: "116px",
        }}
      >
        <span className="porcentagem">{formatAsPercent(comConsulta)}</span>
        <span className="nomeGrafico">{data[0]}</span>
      </div>
    </div>
  );
}

export interface TPieData {
  value: number;
  name: string;
}
export class TDonutChart {
  constructor(
    public nome: string,
    public dataGraphic: TPieData[],
    public colorActive: string = "#5cd2c8"
  ) {
    this.nome = nome;
    this.dataGraphic = dataGraphic;
    this.colorActive = colorActive;
  }
}
export function DonutChart({ dataGraphic, nome, colorActive }: TDonutChart) {
  const total = dataGraphic[0].value + dataGraphic[1].value;
  const ativo = (dataGraphic[0].value / total) * 100;

  const options = {
    color: ["#84aaff", "#0069d0", "#e9ecef", "#08315b"],
    tooltip: {
      trigger: "item",
      formatter: "{b0}: {c0}({d}%)",
    },
    series: [
      {
        name: nome,
        type: "pie",
        radius: ["40%", "80%"],
        avoidLabelOverlap: true,
        label: {
          show: true,
          overflow: "break",
          width: 110,
          formatter: "{b|{d}%}\n\n{a|{b}}\n\n{c|({c})}",
          rich: {
            a: {
              color: "#262729",
              fontWeight: "400",
              fontSize: 10,
              align: "right",
            },
            b: {
              color: "#262729",
              fontWeight: "bold",
              fontSize: 22,
              align: "right",
            },
            c: {
              color: "#262729",
              fontWeight: "bold",
              fontSize: 10,
              align: "right",
            },
            distanceToLabelLine: 50,
          },
        },
        emphasis: {
          label: {
            show: true,
            fontSize: "14",
          },
        },
        labelLine: {
          show: false,
        },
        data: dataGraphic,
      },
    ],
  };

  return (
    <div
      className="donut"
      style={{
        width: "100%",
        margin: 10,
        padding: 10,
      }}
    >
      <ReactECharts
        option={options}
        style={{
          width: "100%",
          minWidth: "316px",
          height: "216px",
        }}
        opts={{ renderer: "svg" }}
      />
      <div className="w-50 d-flex flex-column justify-content-center align-items-center">
        {/* <span className='porcentagem'>{formatAsPercent(ativo.toString())}</span> */}
        {/* <span className='nomeGrafico'>{data[0]}</span> */}
      </div>
    </div>
  );
}
