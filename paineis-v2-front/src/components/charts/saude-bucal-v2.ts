import { BarChart, DonutChart, WaffleChart } from "./charts.types";

type MockRelatorioSaudeBucalV2 = {
  "pessoas-por-sexo": BarChart;
  "distribuicao-pessoas-raca-cor": WaffleChart;
  "primeira-consulta-odonto-realizada": DonutChart;
  "tratamento-odonto-concluico": DonutChart;
  "exodontia-realizada": DonutChart;
  "procedimentos-preventivos-realizados": DonutChart;
  "tra-realizado": DonutChart;
  "escovacao-supervisionada-realizada": DonutChart;
};

export const charts: MockRelatorioSaudeBucalV2 = {
  "pessoas-por-sexo": {
    data: [
      {
        tag: "menos-1-ano",
        value: {
          feminino: 20,
          masculino: 20,
          indeterminado: 2,
        },
      },
      {
        tag: "60-64-anos",
        value: {
          feminino: 20,
          masculino: 20,
          indeterminado: 2,
        },
      },
      {
        tag: "65-69-anos",
        value: {
          feminino: 20,
          masculino: 20,
          indeterminado: 4,
        },
      },
    ],
  },
  "distribuicao-pessoas-raca-cor": {
    data: [
      {
        tag: "branca",
        value: 43.4,
      },
      {
        tag: "preta",
        value: 10.2,
      },
      {
        tag: "amarela",
        value: 0.4,
      },
      {
        tag: "parda",
        value: 45.3,
      },
      {
        tag: "indigena",
        value: 0.6,
      },
      {
        tag: "nao-informado",
        value: 0.5,
      },
    ],
  },
  "primeira-consulta-odonto-realizada": {
    data: [
      {
        tag: "realizado",
        value: 27,
      },
      {
        tag: "nao-realizado",
        value: 73,
      },
    ],
  },
  "tratamento-odonto-concluico": {
    data: [
      {
        tag: "realizado",
        value: 27,
      },
      {
        tag: "nao-realizado",
        value: 73,
      },
    ],
  },
  "exodontia-realizada": {
    data: [
      {
        tag: "realizado",
        value: 27,
      },
      {
        tag: "nao-realizado",
        value: 73,
      },
    ],
  },
  "procedimentos-preventivos-realizados": {
    data: [
      {
        tag: "realizado",
        value: 27,
      },
      {
        tag: "nao-realizado",
        value: 73,
      },
    ],
  },
  "tra-realizado": {
    data: [
      {
        tag: "realizado",
        value: 27,
      },
      {
        tag: "nao-realizado",
        value: 73,
      },
    ],
  },
  "escovacao-supervisionada-realizada": {
    data: [
      {
        tag: "realizado",
        value: 27,
      },
      {
        tag: "nao-realizado",
        value: 73,
      },
    ],
  },
};
