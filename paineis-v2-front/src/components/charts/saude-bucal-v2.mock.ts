import { BarChart, DonutChart, WaffleChart } from "./charts.types";

type MockRelatorioIdosoV2 = {
  "pessoas-por-sexo": BarChart;
  "distribuicao-pessoas-raca-cor": WaffleChart;
  "primeira-consulta-odonto": DonutChart;
  "concluiu-tratamento-odonto": DonutChart;
  "realizou-exodontia": DonutChart;
  "realizou-preventivo-odonto": DonutChart;
  "realizou-tra-odonto": DonutChart;
  "realizou-escovacao-supervisionada": DonutChart;
};

export const charts: MockRelatorioIdosoV2 = {
  "pessoas-por-sexo": {
    data: [
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
  "primeira-consulta-odonto": {
    data: [
      {
        tag: "",
        value: 87,
      },
      {
        tag: "",
        value: 13,
      },
    ],
  },
  "concluiu-tratamento-odonto": {
    data: [
      {
        tag: "",
        value: 82,
      },
      {
        tag: "",
        value: 18,
      },
    ],
  },
  "realizou-exodontia": {
    data: [
      {
        tag: "",
        value: 87,
      },
      {
        tag: "",
        value: 13,
      },
    ],
  },
  "realizou-preventivo-odonto": {
    data: [
      {
        tag: "",
        value: 87,
      },
      {
        tag: "",
        value: 13,
      },
    ],
  },
  "realizou-tra-odonto": {
    data: [
      {
        tag: "",
        value: 87,
      },
      {
        tag: "",
        value: 13,
      },
    ],
  },
  "realizou-escovacao-supervisionada": {
    data: [
      {
        tag: "",
        value: 87,
      },
      {
        tag: "",
        value: 13,
      },
    ],
  },
};
