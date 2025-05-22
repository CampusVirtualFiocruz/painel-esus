import ReactECharts from "echarts-for-react";
import { BarChart } from "../charts.types";
import { content } from "../../../assets/content/content";
import "./style.scss";
import { getChartDescription } from "../../../utils/chartTitleUtils";

export function Bar(props: BarChart) {
  const series = new Set<string>();
  let inputData = props.data;

  inputData.forEach(({ value }) => {
    Object.keys(value).forEach((opt) => {
      series.add(String(opt));
    });
  });

  if (props?.config?.xAxis?.sort) {
    const suggestionOrder = props?.config?.xAxis?.sort;
    const sortedList = inputData?.sort((a: any, b: any) => {
      return (
        suggestionOrder?.findIndex((s: any) => s === content[a?.tag]) -
        suggestionOrder?.findIndex((s: any) => s === content[b?.tag])
      );
    });
    inputData = sortedList;
  }

  const chartSeries = Array.from(series).map((s: string) => {
    const chartSeriesData = inputData.reduce(
      (prev, curr) =>
        [
          ...prev,
          {
            value: curr?.value?.[s],
            name: content?.[curr?.tag] || curr?.tag,
          } as any,
        ] as any,
      []
    );

    const barChartResult: any = {
      name: content?.[s] || s,
      type: "bar",
      stack: "total",
      data: chartSeriesData,
      ...props?.config,
    };

    if (props?.config?.xAxis?.sort) {
      const suggestionOrder = props?.config?.xAxis?.sort;
      const sortedAxisList = barChartResult.xAxis.data?.sort(
        (a: any, b: any) => {
          return (
            suggestionOrder?.findIndex((s: any) => s === a) -
            suggestionOrder?.findIndex((s: any) => s === b)
          );
        }
      );
      barChartResult.xAxis.data = sortedAxisList;
    }

    return barChartResult;
  });

  const options: any = {
    color: props?.config?.colors || ["#77B4D0", "#2775B0"],
    tooltip: {
      trigger: "item",
    },
    legend: {
      bottom: "0%",
      data: props?.config?.hideLegend ? [] : undefined,
      borderRadius: 0,
      icon: "rect",
    },
    grid: {
      width: "auto",
      left: 70,
      bottom: 140,
    },
    xAxis: {
      type: "category",
      axisLabel: {
        formatter: "{value}",
        rotate: 90,
        nameTextStyle: { overflow: "break" },
        margin: 10,
        fontSize: 14,
        weight: "bold",
      },
      ...{
        ...(props?.config?.xAxis ?? {}),
        rotate: 45,
        nameTextStyle: { overflow: "break" },
      },
    },
    yAxis: [
      {
        type: "value",
        axisLabel: {
          formatter: "{value}",
          fontSize: 12,
        },
        name: getChartDescription(props?.config?.yAxis?.name, props.config?.reportViewType, content),
        nameLocation: "middle",
        nameGap: 40,
      },
    ],
    series: chartSeries,
  };

  if (props?.config?.invertAxis) {
    const aux = JSON.parse(JSON.stringify(options?.yAxis));
    options.yAxis = options?.xAxis;
    options.xAxis = aux;
  }

  return (
    <ReactECharts
      option={options}
      style={{
        width: "100%",
        minWidth: "316px",
        height: "600px",
        ...(props?.config?.componentStyle || {}),
      }}
      opts={{ renderer: "svg" }}
    />
  );
}
