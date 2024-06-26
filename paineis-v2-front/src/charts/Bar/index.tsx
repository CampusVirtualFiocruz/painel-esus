import ReactECharts from "echarts-for-react";
import "./style.scss";

type Faixa = {
  NaN?: number;
  Rural?: string;
  Urbano?: number;
};

type BarData = {
  data: any;
  titulo: string;
};

export function Bar({ data, titulo }: BarData) {
  let faixaEtaria = Object.keys(data).map(function (key) {
    return String(key);
  });

  let arrData = Object.entries(data).map(function (obj: any) {
    let objFaixa = obj[1];

    if (
      !objFaixa.hasOwnProperty("Rural") ||
      !objFaixa.hasOwnProperty("Urbano")
    ) {
      return {
        NaN: objFaixa.NaN,
        Rural: 0,
        Urbano: 0,
      };
    }

    return objFaixa;
  });
  let dataRural = arrData.map((obj: Faixa) => {
    return obj.Rural;
  });
  let dataUrbano = arrData.map((obj: Faixa) => {
    return obj.Urbano;
  });

  const options = {
    legend: {
      bottom: "0%",
    },
    xAxis: {
      data: faixaEtaria,
      axisLine: { onZero: true },
      splitLine: { show: false },
      splitArea: { show: false },
      axisTick: {
        show: false,
      },
      axisLabel: {
        show: true,
        fontSize: 16,
        margin: 10,
        rotate: 90,
      },
    },
    yAxis: {
      axisLabel: {
        show: true,
        fontSize: 16,
        margin: 6,
      },
      splitLine: {
        show: false,
      },
      axisLine: {
        show: true,
      },
      axisTick: {
        show: true,
      },
    },
    grid: {
      width: "auto",
      left: 50,
      bottom: 150,
    },
    series: [
      {
        name: "Área Rural",
        type: "bar",
        stack: "one",
        barWidth: "50%",
        itemStyle: {
          color: "#84aaff",
        },
        data: dataRural,
      },
      {
        name: "Área Urbana",
        type: "bar",
        stack: "one",
        barWidth: "50%",
        itemStyle: {
          color: "#0069d0",
        },
        data: dataUrbano,
      },
    ],
  };

  return (
    <div className="bar">
      <div className="vertical ms-1 me-4">{titulo}</div>

      <ReactECharts
        option={options}
        style={{
          width: "100%",
          minWidth: "370px",
          height: "484px",
        }}
        opts={{ renderer: "svg" }}
      />
    </div>
  );
}
