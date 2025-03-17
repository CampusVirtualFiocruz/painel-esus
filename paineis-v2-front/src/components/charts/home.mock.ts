import { DonutChart, ValueChart, PyramidChart } from "./charts.types";

type MockRelatorioHome = {
  "total-cidadaos-cadastrados": ValueChart;
  "total-populacao-apurada": ValueChart;
  "tipo-localizacao": DonutChart;
  "total-masculino": ValueChart;
  "total-feminino": ValueChart;
  "piramide-etaria": PyramidChart;
  "tematico-diabetes": DonutChart;
  "tematico-hipertensao": DonutChart;
  "tematico-qualidade": DonutChart;
};

export const charts: MockRelatorioHome = {
  "total-cidadaos-cadastrados": {
    data: 2592,
  },
  "total-populacao-apurada": {
    data: 44800,
  },
  "tipo-localizacao": {
    data: [
      {
        tag: "urbano",
        value: 1874,
      },
      {
        tag: "nao-informado",
        value: 104,
      },
      {
        tag: "rural",
        value: 614,
      },
    ],
  },
  "total-masculino": {
    data: 1232,
  },
  "total-feminino": {
    data: 1360,
  },
  "piramide-etaria": {
    data: {
      left: [
        {
          tag: "100-mais",
          value: {
            urbano: 0,
            rural: 0,
            "nao-informado": 0,
          },
        },
        {
          tag: "95-99",
          value: {
            urbano: 12,
            rural: 10,
            "nao-informado": 6,
          },
        },
        {
          tag: "90-94",
          value: {
            urbano: 22,
            rural: 16,
            "nao-informado": 19,
          },
        },
      ],
      right: [
        {
          tag: "100-mais",
          value: {
            urbano: 0,
            rural: 0,
            "nao-informado": 0,
          },
        },
        {
          tag: "95-99",
          value: {
            urbano: 14,
            rural: 8,
            "nao-informado": 8,
          },
        },
        {
          tag: "90-94",
          value: {
            urbano: 32,
            rural: 30,
            "nao-informado": 10,
          },
        },
      ],
    },
  },
  "tematico-diabetes": {
    data: [
      {
        tag: "urbano",
        value: 1874,
      },
      {
        tag: "nao-informado",
        value: 104,
      },
      {
        tag: "rural",
        value: 614,
      },
    ],
  },
  "tematico-hipertensao": {
    data: [
      {
        tag: "urbano",
        value: 1874,
      },
      {
        tag: "nao-informado",
        value: 104,
      },
      {
        tag: "rural",
        value: 614,
      },
    ],
  },
  "tematico-qualidade": {
    data: [
      {
        tag: "urbano",
        value: 1874,
      },
      {
        tag: "nao-informado",
        value: 104,
      },
      {
        tag: "rural",
        value: 614,
      },
    ],
  },
};
