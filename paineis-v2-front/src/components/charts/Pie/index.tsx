import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";

export function Pie(props: PieChart) {
  const options = {
    color: ["#84aaff", "#0069d0"],
    tooltip: {
      trigger: "item",
    },
    legend: {
      top: "5%",
      // left: "center",
    },
    series: [
      {
        name: "",
        type: "pie",
        radius: ["70%"],
        avoidLabelOverlap: false,
        label: {
          show: true,
          // position: "bottom",
          fontSize: "16",
          fontWeight: "bold",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 16,
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
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
        height: "216px",
      }}
      opts={{ renderer: "svg" }}
    />
  );
}
