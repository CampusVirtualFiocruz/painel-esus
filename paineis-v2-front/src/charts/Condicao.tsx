import ReactECharts from "echarts-for-react";
import { getPorcentagemIndicador } from "../utils";

export function Condicao({ data }: any) {
  let options = {};

  if (data !== undefined) {
    let total = data.urbano + data.rural;
    const entries = Object.entries(data).map((item) => {
      return {
        value: item[1],
        name: getPorcentagemIndicador(item[0], total, item[1]),
      };
    });

    options = {
      color: ["#84aaff", "#0069d0"],
      tooltip: {
        trigger: "item",
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
