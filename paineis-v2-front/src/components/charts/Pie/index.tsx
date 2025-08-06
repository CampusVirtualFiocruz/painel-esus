import ReactECharts from "echarts-for-react";
import { content } from "../../../assets/content/content";
import { PieChart } from "../charts.types";
import "./style.scss";

export function Pie(props: PieChart) {
  const options = {
    color: props?.config?.colors || ["#5CD2C8", "#E4E4E4"],
    tooltip: {
      trigger: "item",
    },
    legend: {
      icon: "rect",
      top: "5%",
    },
    series: [
      {
        name: "",
        type: "pie",
        radius: ["0%", "70%"],
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
            show: true,
            fontSize: 16,
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
