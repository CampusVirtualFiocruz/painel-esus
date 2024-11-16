import { BarChart, DonutChart, TreemapShallowChart, ValueChart } from "./charts.types";

type MockRelatorioTabagismo = {
  "total-ubs": ValueChart;
  "total-atendidas": ValueChart;
  "total-raca-cor": TreemapShallowChart;
  "total-imc": DonutChart;
  "total-proporcao-vacina-influenza": DonutChart;
  "total-proporcao-atendimento-odonto": DonutChart;
  "pessoas-por-faixa-etaria": BarChart,
  "pessoas-por-sexo": BarChart,
  "pessoas-por-diagnostico": BarChart,
};

export const charts: MockRelatorioTabagismo = {
  "total-ubs": {
    data: 768,
  },
  "total-atendidas": {
    data: 83,
  },
  "total-raca-cor": {
    data: [
      {
        tag: "parda",
        value: 40,
      },
      {
        tag: "amarela",
        value: 60,
      },
    ],
  },
  "total-imc": {
    data: [
      {
        tag: "baixo-peso",
        value: 40,
      },
      {
        tag: "normal",
        value: 60,
      },
    ],
  },
  "total-proporcao-vacina-influenza": {
    data: [
      {
        tag: "vacinadas",
        value: 40,
      },
      {
        tag: "nao-vacinadas",
        value: 60,
      },
    ],
  },
  "total-proporcao-atendimento-odonto": {
    data: [
      {
        tag: "atendidas",
        value: 40,
      },
      {
        tag: "nao-atendidas",
        value: 60,
      },
    ],
  },
  "pessoas-por-faixa-etaria": {
    data: [
      {
        tag: "60-64-anos",
        value: {
          "urbana": 260,
          "rural": 260,
          "nao-informado": 260,
        },
      },
      {
        tag: "65-69-anos",
        value: {
          "urbana": 260,
          "rural": 260,
          "nao-informado": 260,
        },
      },
    ],
  },
  "pessoas-por-sexo": {
    data: [
      {
        tag: "60-64-anos",
        value: {
          "feminino": 20,
          "masculino": 20,
        },
      },
      {
        tag: "65-69-anos",
        value: {
          "feminino": 20,
          "masculino": 20,
        },
      },
    ],
  },
  "pessoas-por-diagnostico": {
    data: [
      {
        tag: "hipertensao",
        value: {
          "total": 219,
        },
      },
      {
        tag: "diabetes",
        value: {
          "total": 154,
        },
      },
      {
        tag: "hipertensao-diabetes-associadas",
        value: {
          "total": 281,
        },
      },
    ],
  },
};
