import ReactECharts from "echarts-for-react";
import "./style.scss";

type Faixa = {
  NaN?: number;
  Rural?: string;
  Urbano?: number;
  "Nao Informado"?: number;
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
      !objFaixa.hasOwnProperty("Urbano") ||
      !objFaixa.hasOwnProperty("Nao Informado")
    ) {
      return {
        NaN: objFaixa.NaN,
        Rural: 0,
        Urbano: 0,
        "Nao Informado": 0,
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
  let dataNaoInformado = arrData.map((obj: Faixa) => {
    return obj["Nao Informado"];
  });

  const options = {
    legend: {
      bottom: "0%",
    },
    tooltip: {
      trigger: "axis",
      formatter: function (params: any) {
        let description = `${params[0].name}<hr>`;
        params.forEach((param: any) => {
          description += `${param.marker}${param.seriesName}: ${param.value}<br />`;
        });
        return description;
      },
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
        fontSize: 14,
        margin: 10,
        rotate: 90,
      },
    },
    yAxis: {
      type: "value",
      axisLabel: {
        show: true,
        fontSize: 14,
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
        barMinHeight: 10,
        barWidth: "33%",
        itemStyle: {
          color: "#84aaff",
        },
        data: dataRural,
      },
      {
        name: "Área Urbana",
        type: "bar",
        stack: "one",
        barMinHeight: 10,
        barWidth: "33%",
        itemStyle: {
          color: "#0069d0",
        },
        data: dataUrbano,
      },
      {
        name: "Não Informado",
        type: "bar",
        stack: "one",
        barMinHeight: 10,
        barWidth: "33%",
        itemStyle: {
          color: "#e9ecef",
        },
        data: dataNaoInformado,
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
