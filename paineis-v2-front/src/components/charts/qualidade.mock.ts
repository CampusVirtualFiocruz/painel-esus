import {
  BarChart,
  DonutChart,
  TreemapShallowChart,
  ValueChart,
} from './charts.types';

type MockRelatorioTabagismo = {
  'total-cadastros-ubs': ValueChart;
  'porcentagem-cadastros-atualizados': ValueChart;
  'total-cadastros-cidadaos-por-tipo-identificacao': DonutChart;
  'status-cadastros-cidadaos': DonutChart;
  'localizacao-domicilios-cadastrados': DonutChart;
  'via-cadastros-cidadaos': BarChart;
  'total-cadastros-pessoas-raca-cor': TreemapShallowChart;
};

export const charts: MockRelatorioTabagismo = {
  'total-cadastros-ubs': {
    data: 768,
  },
  'porcentagem-cadastros-atualizados': {
    data: 83,
  },
  'total-cadastros-cidadaos-por-tipo-identificacao': {
    data: [
      {
        tag: 'sem-cpf-cnf',
        value: 32,
      },
      {
        tag: 'cadastros-identificados-por-cpf-cns',
        value: 68,
      },
    ],
  },
  'status-cadastros-cidadaos': {
    data: [
      {
        tag: 'ativo',
        value: 81,
      },
      {
        tag: 'inconsistente',
        value: 19,
      },
    ],
  },
  'localizacao-domicilios-cadastrados': {
    data: [
      {
        tag: 'urbana',
        value: 30,
      },
      {
        tag: 'nao-informado',
        value: 58,
      },
      {
        tag: 'rural',
        value: 12,
      },
    ],
  },
  'via-cadastros-cidadaos': {
    data: [
      {
        tag: 'fci',
        value: {
          fci: 260,
        },
      },
      {
        tag: 'pec',
        value: {
          pec: 210,
        },
      },
      {
        tag: 'recusa',
        value: {
          recusa: 10,
        },
      },
    ],
  },
  'total-cadastros-pessoas-raca-cor': {
    data: [
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
    ],
  },
};
