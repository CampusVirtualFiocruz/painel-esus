import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";

const formatters = {
  full: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join("\n"),
  undefined: ["{a|{b}}", "{b|{@2012}}", "{b|({d}%)}"].join("\n"),
  perc: ["{b|{d}%}", "{a|{b}}"].join("\n"),
};

const removeDuplicatesByKey = <T, K extends keyof T>(arr: T[], key: K): T[] =>
  Array.from(new Map(arr.map((item) => [item[key], item])).values());

const ClassificationFooter = ({ data, rangedLegend }: any) => {
  let percentage: any = undefined;
  let hasHighlightConfig =
    data && Array.isArray(data) && data?.[1]?.tag === "realizado";

  if (hasHighlightConfig) {
    const mainValue = data?.[1]?.value;
    const total = mainValue + data?.[0]?.value;
    percentage = (mainValue / total) * 100;
  }

  return (
    <div className="donut-footer">
      {removeDuplicatesByKey<typeof rangedLegend, string>(
        rangedLegend,
        "title"
      ).map(({ color, title, text, window }: any, index: number) => {
        const shouldHighlight = Boolean(window.find(({ min, max }: { min: number, max: number }) => percentage >= min && percentage < max));

        if(!shouldHighlight){
          return null;
        }

        return (
          <div key={index} className="legend-item">
            <span
              className="legend-color"
              style={{
                backgroundColor: color,
              }}
            />
            <span className="legend-text">Realizado</span>
          </div>
        );
      })}
      <div className="legend-item">
        <span
          className="legend-color"
          style={{
            backgroundColor: "#d6d6d6",
          }}
        />
        <span className="legend-text">Não Realizado</span>
      </div>
    </div>
  );
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
                padding: [0, 0],
              },
              b: {
                color: "black",
                fontSize: 20,
                fontWeight: "bold",
                padding: [0, 0],
              },
            },
          },
        } as any,
      ] as any,
    []
  );

  if (props?.config?.sort) {
    const suggestionOrder = props?.config?.sort;
    const sortedDataList = donutData?.sort((a: any, b: any) => {
      return (
        suggestionOrder?.findIndex((s: any) => s === a?.name) -
        suggestionOrder?.findIndex((s: any) => s === b?.name)
      );
    });
    donutData = sortedDataList;
  }

  let chartColor = props?.config?.colors || ["#09406A", "#5CD2C8"];

  if (props?.config?.rangedLegend) {
    let percentage: any = undefined;
    let hasHighlightConfig =
      props.data &&
      Array.isArray(props.data) &&
      props.data?.[1]?.tag === "realizado";

    if (hasHighlightConfig) {
      const data: any = props.data;
      const mainValue = data?.[1]?.value;
      const total = mainValue + data?.[0]?.value;
      percentage = (mainValue / total) * 100;
    }

    props?.config?.rangedLegend.forEach(({ color, window }) => {
      const shouldHighlight = Boolean(window.find(({ min, max }: { min: number, max: number }) => percentage >= min && percentage < max));
      if (shouldHighlight) {
        chartColor = [color, "#E4E4E4"];
      }
    });
  }

  const options = {
    color: chartColor,
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
    <div className="donut-chart-container">
      <ReactECharts
        option={options}
        style={{
          width: "316px",
          minWidth: "316px",
          height: "316px",
          maxWidth: "100%",
          ...(props?.config?.componentStyle || {}),
        }}
        opts={{ renderer: "svg" }}
      />
      {props?.config?.rangedLegend && (
        <ClassificationFooter
          data={props.data}
          rangedLegend={props?.config.rangedLegend}
        />
      )}
    </div>
  );
}
