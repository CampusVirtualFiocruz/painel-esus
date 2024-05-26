import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";

export function Donut(props: DonutChart) {
  const options = {
    color: ["#84aaff", "#0069d0"],
    tooltip: {
      trigger: "item",
    },
    legend: {
      top: "5%",
      data: [],
      // data: ["Legend A", "Legend B", "Legend C"],
      // backgroundColor: "#ccc",
      // textStyle: {
      //   color: "#ccc",
      //   // ...
      // },
      // left: "center",
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
