import { BarChart, DonutChart, TreemapShallowChart, ValueChart } from "./charts.types";

type MockRelatorioInfantil = {
  "total-criancas-cadastradas-2-anos": ValueChart;
  "total-criancas-atendidas-2-anos": ValueChart;
  "total-cadastros-criancas-raca-cor": TreemapShallowChart,
  "total-extratificacao-por-profissional": TreemapShallowChart,
  "distribuicao-criancas-faixa-etaria": BarChart,
  "distribuicao-criancas-sexo": BarChart,
  "distribuicao-criancas-local": DonutChart
};

export const charts: MockRelatorioInfantil = {
  "total-criancas-cadastradas-2-anos": {
    data: 523,
  },
  "total-criancas-atendidas-2-anos": {
    data: 498,
  },
  "total-cadastros-criancas-raca-cor": { data: [
    {
      tag: 'parda',
      value: 45.3,
    },
    {
      tag: 'branca',
      value: 43.4,
    },
    {
      tag: 'preta',
      value: 10.1,
    },
    {
      tag: 'indigena',
      value: 0.8,
    },
    {
      tag: 'amarela',
      value: 0.4,
    },
  ]},
  "total-extratificacao-por-profissional": { data: [
    { tag: "Assistente Social", value: 0.10 },
    { tag: "Cirurgião Dentista", value: 2 },
    { tag: "Enfermeiro", value: 35 },
    { tag: "Farmacêutico", value: 0 },
    { tag: "Fisioterapeuta", value: 0 },
    { tag: "Fonoaudiólogo", value: 0 },
    { tag: "Médico", value: 68.42 },
    { tag: "Nutricionista", value: 12 },
    { tag: "Professor da Educação Física", value: 0 },
    { tag: "Psicólogo", value: 0 },
    { tag: "Terapeuta Ocupacional", value: 0 },
    { tag: "Outros", value: 5 },
  ]},
  "distribuicao-criancas-faixa-etaria": {
    data: [
      {
        tag: "1-meses",
        value: {
          "urbana": 10,
          "rural": 20,
          "nao-informado": 30,
        },
      },
      {
        tag: "2-meses",
        value: {
          "urbana": 20,
          "rural": 30,
          "nao-informado": 40,
        },
      },
      {
        tag: "9-meses",
        value: {
          "urbana": 60,
          "rural": 80,
          "nao-informado": 100,
        },
      },
    ],
  },
  "distribuicao-criancas-sexo": {
    data: [
      {
        tag: "1-meses",
        value: {
          "urbana": 10,
          "rural": 20,
          "nao-informado": 30,
        },
      },
      {
        tag: "2-meses",
        value: {
          "urbana": 20,
          "rural": 30,
          "nao-informado": 40,
        },
      },
      {
        tag: "9-meses",
        value: {
          "urbana": 60,
          "rural": 80,
          "nao-informado": 100,
        },
      },
    ],
  },
  "distribuicao-criancas-local": {
    data: [
      {
        tag: "urbano",
        value: 81,
      },
      {
        tag: "nao-informado",
        value: 20,
      },
      {
        tag: "rural",
        value: 19,
      },
    ],
  },  
};
