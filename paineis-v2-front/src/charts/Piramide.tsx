import ReactECharts from "echarts-for-react";
import { ageGroupParser } from "../services/demographicParser";

export default function Piramide({ data }: any) {
  const waterMarkText = "ECHARTS";
  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");

  canvas.width = canvas.height = 100;

  if (ctx) {
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.globalAlpha = 0.08;
    ctx.font = "20px Microsoft Yahei";
    ctx.translate(50, 50);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
  }

  const result: any = ageGroupParser({ ageGroups: data });
  const options = {
    tooltip: {
      trigger: "item",
      formatter: function (params: any) {
        return `${params.name}<br />${params.marker}${params.data.label}: ${params.value}`;
      },
    },
    legend: {
      // Try 'horizontal'
      orient: "horizontal",
      right: 10,
      top: "center",
    },
    grid: [
      {
        top: 0,
        width: "35%",
        bottom: 0,
        right: "51%",
        containLabel: false,
      },
      {
        top: 0,
        width: "35%",
        bottom: 0,
        left: "51%",
        containLabel: false,
      },
    ],
    xAxis: [
      {
        type: "value",
        //max: builderJson.all,
        splitLine: {
          show: false,
        },
        inverse: true,
      },
      {
        type: "value",
        //max: builderJson.all,
        gridIndex: 1,
        splitLine: {
          show: false,
        },
      },
    ],
    yAxis: [
      {
        gridIndex: 0,
        type: "category",
        data: Object.keys(result[0].areaUrbana),
        inverse: true,
        axisLabel: {
          show: true,
          fontSize: 16,
          margin: 8,
          width: "10%",
          //formatter: '        ',
        },
        axisLine: {
          show: false,
        },
        axisTick: {
          show: false,
        },
      },
      {
        gridIndex: 1,
        type: "category",
        data: Object.keys(result[0].areaUrbana),
        inverse: true,
        position: "right",
        offset: 0,
        axisLine: {
          show: false,
        },
        axisLabel: {
          margin: 10,
          fontSize: 16,
        },
        axisTick: {
          show: false,
        },
      },
    ],
    series: [
      {
        type: "bar",
        barWidth: "20px",
        stack: "masculino",
        z: 3,
        xAxisIndex: 0,
        yAxisIndex: 0,
        data: Object.keys(result[0].nao_informado).map(function (key) {
          return result[0].nao_informado[key];
        }),
      },
      {
        type: "bar",
        barWidth: "20px",
        stack: "masculino",
        z: 3,
        style: {
          font: "28px sans-serif",
        },
        xAxisIndex: 0,
        yAxisIndex: 0,
        data: Object.keys(result[0].areaUrbana).map(function (key: string) {
          return result[0].areaUrbana[key];
        }),
      },
      {
        type: "bar",
        barWidth: "20px",
        stack: "masculino",
        z: 3,
        xAxisIndex: 0,
        yAxisIndex: 0,
        data: Object.keys(result[0].areaRural).map(function (key) {
          return result[0].areaRural[key];
        }),
      },

      {
        type: "bar",
        barWidth: "20px",
        stack: "feminino",
        z: 3,
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: Object.keys(result[1].nao_informado).map(function (key) {
          return result[1].nao_informado[key];
        }),
      },
      {
        type: "bar",
        barWidth: "20px",
        stack: "feminino",
        z: 3,
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: Object.keys(result[1].areaUrbana).map(function (key) {
          return result[1].areaUrbana[key];
        }),
      },
      {
        type: "bar",
        barWidth: "20px",
        stack: "feminino",
        z: 3,
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: Object.keys(result[1].areaRural).map(function (key) {
          return result[1].areaRural[key];
        }),
      },
    ],
  };

  return (
    <>
      <ReactECharts
        option={options}
        style={{
          width: "100%",
          height: "400px",
        }}
        className="my-5"
        opts={{ renderer: "svg" }}
      />
    </>
  );
}
