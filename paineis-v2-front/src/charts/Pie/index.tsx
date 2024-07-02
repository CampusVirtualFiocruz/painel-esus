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
    public colorActive: string = "#5cd2c8"
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
    color: [colorActive, "#e4e4e4"],
    tooltip: {
      trigger: "item",
      formatter: "({d}%)",
    },
    title: {
      text: nome,
      left: "center",
      top: "0",
      textStyle: {
        fontSize: 16,
        overflow: "break",
        width: 120,
      },
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
    <div
      className="pie-chart"
      style={{
        width: "100%",
      }}
    >
      <ReactECharts
        option={options}
        style={{
          width: "126px",
          height: "186px",
        }}
        opts={{ renderer: "svg" }}
      />
      <div className="data-info d-flex flex-column align-items-center">
        <span className="porcentagem">
          {dataGraphic[0].value + `(${formatAsPercent(ativo.toString())})`}
        </span>
      </div>
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
    color: ["#84aaff", "#0069d0"],
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
      <div className="data-info d-flex flex-column align-items-center">
        <span className="porcentagem">{formatAsPercent(comConsulta)}</span>
        <span className="nomeGrafico">{data[0]}</span>
        <span className="nomeGrafico">{limite}</span>
      </div>
    </div>
  );
}
