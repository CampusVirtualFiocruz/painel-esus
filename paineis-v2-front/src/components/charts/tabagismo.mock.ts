import { BarChart, DonutChart, PieChart } from "./charts.types";

type MockRelatorioTabagismo = {
  "proporcao-tabagistas-acompanhadas": DonutChart;
  "proporcao-fatores-riscos-por-dant": BarChart;
  "tabagistas-faixa-etaria": BarChart;
  "consulta-odontologica-tabagistas": PieChart;
  "pessoas-tabagistas-sexo": BarChart;
  "pessoas-tabagistas-escolaridade": BarChart;
};

export const tabagismoCharts: MockRelatorioTabagismo = {
  "proporcao-tabagistas-acompanhadas": {
    data: [
      {
        tag: "acompanhadas-ubs-nao-tabagistas",
        value: 5861,
      },
      {
        tag: "acompanhadas-ubs-tabagistas",
        value: 4451,
      },
    ],
  },
  "proporcao-fatores-riscos-por-dant": {
    data: [
      {
        tag: "doenca-cardiovascular",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "cancer",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "diabetes-melitus",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "doenca-respiratoria-cronica",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
    ],
  },
  "tabagistas-faixa-etaria": {
    data: [
      {
        tag: "ate-30",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "ate-40",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "ate-50",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      // etc
    ],
  },
  "consulta-odontologica-tabagistas": {
    data: [
      {
        tag: "sim",
        value: 71,
      },
      {
        tag: "nao",
        value: 39,
      },
    ],
  },
  "pessoas-tabagistas-sexo": {
    data: [
      {
        tag: "ate-30",
        value: {
          masc: 10,
          fem: 12,
        },
      },
      {
        tag: "ate-40",
        value: {
          masc: 10,
          fem: 12,
        },
      },
      {
        tag: "ate-50",
        value: {
          masc: 10,
          fem: 12,
        },
      },
      // etc
    ],
  },
  "pessoas-tabagistas-escolaridade": {
    data: [
      {
        tag: "analfabeto",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "primeiro-grau-completo",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      {
        tag: "primeiro-grau-incompleto",
        value: {
          urbana: 10,
          rural: 12,
        },
      },
      // etc
    ],
  },
};
