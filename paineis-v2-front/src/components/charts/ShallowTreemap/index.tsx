import ReactECharts from "echarts-for-react";
import "./style.scss";
import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";

export function ShallowTreemap(props: DonutChart) {
  const options = {
    color: props?.config?.colors || ["#09406A", "#5CD2C8"],
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
        type: "treemap",
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
        breadcrumb: {
          show: false,
        },
        roam: false,
        data: props.data.reduce(
          (prev, curr) =>
            [
              ...prev,
              {
                value: Number(curr?.value ?? 0) * 100,
                name: content?.[curr?.tag] || curr?.tag,
                label: {
                  formatter: ["{b|{@2012}}%", "{a|{b}}"].join("\n"),
                  rich: {
                    a: {
                      color: "white",
                      fontSize: 14,
                      marginTop: 16,
                    },
                    b: {
                      color: "white",
                      fontSize: 26,
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
