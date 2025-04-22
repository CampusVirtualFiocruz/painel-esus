import { BarChart, DonutChart, ValueChart, WaffleChart } from "./charts.types";

type MockRelatorioIdosoV2 = {
  "total-ubs": ValueChart;
  "total-atendidas": ValueChart;
  "pessoas-por-sexo": BarChart;
  "distribuicao-pessoas-raca-cor": WaffleChart;
  "duas-consultas-medicas-enfermagem": DonutChart;
  "dois-registros-peso-altura": DonutChart;
  "duas-visitas-domiciliares-acs-tacs": DonutChart;
  "avalicao-creatina": DonutChart;
  "registro-vacina-influenza": DonutChart;
  "consulta-com-dentista-aps": DonutChart;
  "ivcf-20": DonutChart;
};

export const charts: MockRelatorioIdosoV2 = {
  "total-ubs": {
    data: 724,
  },
  "total-atendidas": {
    data: 643,
  },
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
  "duas-consultas-medicas-enfermagem": {
    data: [
      {
        tag: "duas-mais-consultas",
        value: 87,
      },
      {
        tag: "uma-nenhuma-consulta",
        value: 13,
      },
    ],
  },
  "dois-registros-peso-altura": {
    data: [
      {
        tag: "dois-mais-registros",
        value: 82,
      },
      {
        tag: "um-nenhum-registro",
        value: 18,
      },
    ],
  },
  "duas-visitas-domiciliares-acs-tacs": {
    data: [
      {
        tag: "duas-mais-visitas",
        value: 87,
      },
      {
        tag: "uma-nenhuma-visita",
        value: 13,
      },
    ],
  },
  "avalicao-creatina": {
    data: [
      {
        tag: "avaliadas",
        value: 87,
      },
      {
        tag: "sem-avaliacao",
        value: 13,
      },
    ],
  },
  "registro-vacina-influenza": {
    data: [
      {
        tag: "vacinadas",
        value: 87,
      },
      {
        tag: "nao-vacinadas",
        value: 13,
      },
    ],
  },
  "consulta-com-dentista-aps": {
    data: [
      {
        tag: "consultadas",
        value: 87,
      },
      {
        tag: "sem-consulta",
        value: 13,
      },
    ],
  },
  "ivcf-20": {
    data: [
      {
        tag: "avaliadas",
        value: 87,
      },
      {
        tag: "sem-avaliacao",
        value: 13,
      },
    ],
  },
};
