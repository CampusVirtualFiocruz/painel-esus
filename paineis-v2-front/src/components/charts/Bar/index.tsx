import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";

export function Bar(props: BarChart) {
  const series = new Set<string>();

  props.data.forEach(({ value }) => {
    Object.keys(value).forEach((opt) => {
      series.add(String(opt));
    });
  });

  const chartSeries = Array.from(series).map((s: string) => {
    return {
      name: content?.[s] || s,
      type: "bar",
      stack: "total",
      data: props.data.reduce(
        (prev, curr) =>
          [
            ...prev,
            {
              value: curr?.value?.[s],
              name: content?.[curr?.tag] || curr?.tag,
            } as any,
          ] as any,
        []
      ),
      ...props?.config,
    };
  });

  const options = {
    color: ["#77B4D0", "#2775B0"],
    tooltip: {
      trigger: "item",
    },
    legend: {
      bottom: "0%",
      borderRadius: 0,
    },
    // grid: {
    //   width: "auto",
    //   left: 50,
    //   bottom: 150,
    // },
    xAxis: {
      name: props?.config?.xAxis?.name ?? undefined,
      type: "category",
    },
    yAxis: [
      {
        type: "value",
        axisLabel: {
          formatter: "{value}",
        },
        name: props?.config?.yAxis?.name ?? undefined,
        nameLocation: "middle",
        nameGap: 24,
      },
    ],
    series: chartSeries,
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
