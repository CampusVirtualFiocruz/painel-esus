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
    };
  });

  const options = {
    color: ["#84aaff", "#0069d0"],
    tooltip: {
      trigger: "item",
    },
    legend: {
      bottom: "0%",
    },
    // grid: {
    //   width: "auto",
    //   left: 50,
    //   bottom: 150,
    // },
    xAxis: {
      type: "category",
    },
    yAxis: {
      type: "value",
    },
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
