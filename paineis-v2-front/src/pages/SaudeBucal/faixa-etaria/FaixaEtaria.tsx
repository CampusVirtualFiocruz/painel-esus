import ReactECharts from "echarts-for-react";
import * as React from "react";
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import { Api } from "../../../services/api";
import { STALE_TIME } from "../../../config/stale-time";
import "./style.scss";
import AsyncDataLoad from "../async-data-load";
import { Typography } from "../../../components/ui/Typography";

export type PainelParams = {
  id: string;
};

export type FaixaEtariaAxis = {
  label: number;
  value: number;
};
export type FaixaEtariaResponse = {
  label: string;
  x: FaixaEtariaAxis;
  y: FaixaEtariaAxis;
};

export type BarchartType = {
  titulo: string;
  data: any[];
  colors?: any[];
};

export const BarChart = ({ titulo, data, colors }: BarchartType) => {
  const xAxis = data?.map((item: any) => item.label);
  const series: any = [];
  const dict: any = {};
  for (let i of data) {
    if (i.axis) {
      for (let j of i.axis) {
        if (dict[j.label]) {
          dict[j.label].push(j.value);
        } else {
          dict[j.label] = [j.value];
        }
      }
    }
  }
  for (let i of Object.keys(dict)) {
    console.log("->", i, dict[i]);
    series.push({
      label: i == "-" ? "Não Informado" : i,
      data: dict[i],
    });
  }

  const chartColors = colors || ["#0069d0", "#84aaff", "#e9ecef"];
  const formatLabel = (val: number) => {
    if (val >= 1000) {
      return `${val / 1000}K`;
    }
    return val;
  };
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
      data: xAxis,
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
      type: "value",
      axisLabel: {
        show: true,
        fontSize: 14,
        margin: 6,
        formatter: (val: number) => formatLabel(val),
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
    series: series.map((i: any, index: number) => {
      return {
        name: i.label,
        type: "bar",
        stack: "one",
        barWidth: "50%",
        barMinHeihgt: 10,
        itemStyle: {
          color: chartColors[index],
        },
        data: i.data,
      };
    }),
  };
  console.log("data", data);
  return (
    <div className="bar">
      <div className="vertical ms-1 me-4">{titulo}</div>

      <ReactECharts
        option={options}
        style={{
          width: "70%",
          minWidth: "370px",
          height: "484px",
        }}
        opts={{ renderer: "svg" }}
      />
    </div>
  );
};
const FaixaEtaria = () => {
  const { id } = useParams<PainelParams>();
  const {
    data: faixaEtariaResponse,
    isLoading,
    error,
  } = useQuery(
    ["saude-bucal-faixa-etaria", id],
    async () => {
      const url = "oral-health/get-cares-by-age-range";
      const path = id ? `${url}/${id}` : url;
      const response = await Api.get<FaixaEtariaResponse[]>(path);
      console.log("faixa etaria", response.data);
      return response.data;
    },
    {
      staleTime: STALE_TIME,
    }
  );
  return (
    <AsyncDataLoad {...{ isLoading, error }}>
      <div className="col-12">
        <Typography.Subtitle>
          Atendimentos em Saúde Bucal por faixa etária
        </Typography.Subtitle>
        {!isLoading && faixaEtariaResponse && (
          <BarChart
            {...{ data: faixaEtariaResponse, titulo: "Total de atendimentos" }}
          />
        )}
      </div>
    </AsyncDataLoad>
  );
};

export default FaixaEtaria;
