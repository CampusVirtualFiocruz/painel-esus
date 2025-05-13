import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";

const formatters = {
  full: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join("\n"),
  undefined: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join("\n"),
  perc: ["{b|{d}%}", "{a|{b}}"].join("\n"),
};

export function Donut(props: DonutChart) {
  const f = String(props?.config?.formatterKind) as keyof typeof formatters;

  let donutData = props.data.reduce(
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
                fontSize: 10,
                marginBottom: 16,
                padding: [0, 20],
              },
              b: {
                color: "black",
                fontSize: 24,
                fontWeight: "bold",
                padding: [0, 20],
              },
            },
          },
        } as any,
      ] as any,
    []
  );

  if(props?.config?.sort){
    const suggestionOrder = props?.config?.sort;
    const sortedDataList = donutData?.sort((a: any, b: any) => {
      return (
        suggestionOrder?.findIndex((s: any) => s === a?.name) -
        suggestionOrder?.findIndex((s: any) => s === b?.name)
      );
    });
    donutData = sortedDataList;
  }

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
        radius: props?.config?.radius || [
          props?.config?.radiusStart || "40%",
          "70%",
        ],
        roseType: props?.config?.roseType,
        avoidLabelOverlap: true,
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
        data: donutData,
      },
    ],
  };

  if (props?.config?.halfDonut) {
    options.series[0] = {
      ...options?.series?.[0],
      startAngle: 180,
      endAngle: 360,
    } as any;
  }

  return (
    <ReactECharts
      option={options}
      style={{
        width: "100%",
        minWidth: "316px",
        height: "316px",
        ...(props?.config?.componentStyle || {}),
      }}
      opts={{ renderer: "svg" }}
    />
  );
}
