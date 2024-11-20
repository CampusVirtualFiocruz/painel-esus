import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";

const formatters = {
  full: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join(
    "\n"
  ),
  undefined: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join(
    "\n"
  ),
  perc: ["{b|{d}%}", "{a|{b}}"].join(
    "\n"
  )
}

export function Donut(props: DonutChart) {
  const f = String(props?.config?.formatterKind) as keyof typeof formatters;
  
  const options = {
    color: props?.config?.colors || ["#09406A", "#5CD2C8"],
    tooltip: {
      trigger: "item",
      label: {
        formatter: "testes",
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
        radius: [props?.config?.radiusStart || "40%", "70%"],
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
                  formatter: formatters[f && f !== "undefined" ? f : "full"],
                  
                  rich: {
                    a: {
                      color: "black",
                      fontSize: 12,
                      marginBottom: 16,
                    },
                    b: {
                      color: "black",
                      fontSize: 30,
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
