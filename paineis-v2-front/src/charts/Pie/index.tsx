import ReactECharts from "echarts-for-react";
import { formatAsPercent } from "../../utils";
import "./style.scss";

export interface TPieData {
  value: number;
}
export class TPieChart {
  constructor(
    public nome: string,
    public dataGraphic: TPieData[],
    public colorActive: string = "#0069d0"
  ) {
    this.nome = nome;
    this.dataGraphic = dataGraphic;
    this.colorActive = colorActive;
  }
}
export function PieChart({ dataGraphic, nome, colorActive }: TPieChart) {
  const total = dataGraphic[1].value;
  const ativo = (dataGraphic[0].value / total) * 100;

  const options = {
    color: ["#e4e4e4", "#0069d0", "#84aaff", "#5c7ea0"],
    tooltip: {
      trigger: "item",
      formatter: "{b0}: {c0}({d}%)",
    },
    title: {
      text: "",
      left: "center",
      top: "0",
      bottom: "auto",
      textStyle: {
        fontSize: 16,
        overflow: "break",
        width: 100,
      },
    },
    series: [
      {
        name: "",
        type: "pie",
        radius: "40%",
        center: ["50%", "50%"],
        animationDuration: 800,
        avoidLabelOverlap: false,
        label: {
          show: true,
          position: "outside",
          overflow: "break",
          fontSize: "16",
          fontWeight: "bold",
          width: 120,
          formatter: "{b|{d}%} \n\n{a|{b}}",
          rich: {
            a: {
              color: "#262729",
              fontWeight: "400",
              fontSize: 12,
              align: "center",
            },
            b: {
              color: "#262729",
              fontWeight: "bold",
              fontSize: 25,
              align: "center",
            },
          },
          distanceToLabelLine: -4,
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
    <div style={{ textAlign: "center" }}>
      <ReactECharts
        option={options}
        style={{
          minWidth: "300px",
          height: "186px",
        }}
        opts={{ renderer: "svg" }}
      />
    </div>
  );
}

export function Pie({ data }: any) {
  let nome = "obstetrics-factors";
  let comConsulta = data[1].com_consulta;
  let semConsulta = data[1].sem_consulta;
  let limite = data[1]?.limite;

  let dataGraphic = [{ value: comConsulta }, { value: semConsulta }];

  const options = {
    color: ["#e4e4e4", "#0069d0"],
    tooltip: {
      trigger: "item",
      formatter: "({d}%)",
    },
    legend: {
      bottom: 10,
      left: "center",
      data: ["CityA", "CityB"],
    },
    series: [
      {
        name: nome,
        type: "pie",
        radius: "80%",
        center: ["50%", "50%"],
        animationDuration: 1000,
        label: {
          show: true,
          position: "center",
          fontSize: "16",
          fontWeight: "bold",
        },
        itemStyle: {},
        labelLine: {
          show: false,
        },
        data: dataGraphic,
      },
    ],
  };

  return (
    <div className="pie">
      <ReactECharts
        option={options}
        style={{
          width: "126px",
          height: "126px",
        }}
        opts={{ renderer: "svg" }}
      />
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-around",
          alignItems: "center",
          width: "126px",
        }}
      >
        <span className="porcentagem">{formatAsPercent(comConsulta)}</span>
        <span className="nomeGrafico">{data[0]}</span>
        <span className="nomeGrafico">{limite}</span>
      </div>
    </div>
  );
}
