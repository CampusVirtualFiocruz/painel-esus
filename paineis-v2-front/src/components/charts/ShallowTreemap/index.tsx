import ReactECharts from "echarts-for-react";
import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";
import "./style.scss";

export function ShallowTreemap(props: DonutChart) {
  const options = {
    color: props?.config?.colors || ["#09406A", "#5CD2C8"],
    tooltip: {
      trigger: "item",
      formatter: (val: any) => {
              return [
                `<strong>${val.data.name} (${val.data.percent}%)</strong>`,
                `${val.data.value}`,
              ].join("<br/>");
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
                value: Number(curr?.value ?? 0) ,
                name: content?.[curr?.tag] || curr?.tag,
                percent: Number(curr?.percent ?? 0)*100,

                label: {
                  formatter: (val:any) => {
                    return [
                      `{b|${val.data.percent}%}`,
                      `{a|${val.data.name}}`,
                    ].join("\n")
                      },
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
