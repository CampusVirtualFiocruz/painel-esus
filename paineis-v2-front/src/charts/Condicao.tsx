import ReactECharts from "echarts-for-react";
import { getPorcentagemIndicador } from "../utils";

const parse_label = (label: string) => {
  return {
    rural: "Rural",
    urbano: "Urbano",
    nao_informado: "Não Informado",
  }[label];
};
export function Condicao({ data }: any) {
  let options = {};

  if (data !== undefined) {
    let total = data.urbano + data.rural + (data.nao_informado || 0);
    const entries = Object.entries(data).map((item, index) => {
      return {
        value: item[1],
        name:
          getPorcentagemIndicador(item[0], total, item[1]) +
          "" +
          new Array(index).fill(" ").join(""),
        label: parse_label(item[0]),
      };
    });

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
  }

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
}
