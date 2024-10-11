import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";

export function Donut(props: DonutChart) {
  const options = {
    color: ["#09406A", "#5CD2C8"],
    tooltip: {
      trigger: "item",
      label: {
        formatter: "ai papai",
      },
    },
    legend: {
      icon: "rect",
      data: [],
    },
    series: [
      {
        name: "",
        type: "pie",
        radius: ["40%", "70%"],
        avoidLabelOverlap: false,
        labelLine: {
          show: false,
        },
        label: {
          show: true,
          fontSize: "10",
        },
        emphasis: {
          label: {
            fontWeight: "bold",
          },
        },
        data: props.data.reduce(
          (prev, curr) =>
            [
              ...prev,
              {
                value: curr?.value ?? 0,
                name: content?.[curr?.tag] || curr?.tag,
                label: {
                  formatter: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join(
                    "\n"
                  ),
                  rich: {
                    a: {
                      color: "black",
                      fontSize: 16,
                      marginBottom: 16,
                    },
                    b: {
                      color: "black",
                      fontSize: 24,
                      fontWeight: "bold",
                    },
                  },
                },
              } as any,
            ] as any,
          []
        ),
      },
    ],
  };

  return (
    <ReactECharts
      option={options}
      style={{
        width: "100%",
        minWidth: "316px",
        height: "316px",
      }}
      opts={{ renderer: "svg" }}
    />
  );
}
