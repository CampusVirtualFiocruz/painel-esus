import { BarChart, DonutChart, ValueChart, WaffleChart } from './charts.types';

type MockRelatorioInfantilV2 = {
  'total-cadastros': ValueChart;
  'total-atendidas-12-meses': ValueChart;
  'criancas-por-sexo': BarChart;
  'distribuicao-criancas-raca-cor': WaffleChart;
  'primeira-consulta-ate-8-dia': DonutChart;
  'nove-consultas-puericultura-2-anos': DonutChart;
  'pesoa-altura-9-consultas-puericultura': DonutChart;
  'uma-visita-domiciliar-acs-tacs-30dias': DonutChart;
  'uma-visita-domiciliar-acs-tacs-31dias-a-6meses': DonutChart;
  'consulta-odonto-ate-12-meses': DonutChart;
  'consulta-odonto-12-24-meses': DonutChart;
  'marcos-desenvolvimento-avaliados': DonutChart;
  'consumo-alimentar-avaliado': DonutChart;
};

export const charts: MockRelatorioInfantilV2 = {
  'total-cadastros': {
    data: 724,
  },
  'total-atendidas-12-meses': {
    data: 643,
  },
  'criancas-por-sexo': {
    data: [
      {
        tag: '0-8-dias',
        value: {
          feminino: 20,
          masculino: 20,
          indeterminado: 2,
          'nao-informado': 2,
        },
      },
      {
        tag: '1-2-meses',
        value: {
          feminino: 20,
          masculino: 20,
          indeterminado: 4,
          'nao-informado': 2,
        },
      },
      {
        tag: '24-36-meses',
        value: {
          feminino: 20,
          masculino: 20,
          indeterminado: 4,
          'nao-informado': 2,
        },
      },
    ],
  },
  'distribuicao-criancas-raca-cor': {
    data: [
      {
        tag: 'branca',
        value: 43.4,
      },
      {
        tag: 'preta',
        value: 10.2,
      },
      {
        tag: 'amarela',
        value: 0.4,
      },
      {
        tag: 'parda',
        value: 45.3,
      },
      {
        tag: 'indigena',
        value: 0.6,
      },
      {
        tag: 'nao-informado',
        value: 0.5,
      },
    ],
  },
  'primeira-consulta-ate-8-dia': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'nove-consultas-puericultura-2-anos': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'pesoa-altura-9-consultas-puericultura': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'uma-visita-domiciliar-acs-tacs-30dias': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'uma-visita-domiciliar-acs-tacs-31dias-a-6meses': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'consulta-odonto-ate-12-meses': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'consulta-odonto-12-24-meses': {
    data: [
      {
        tag: 'sim',
        value: 82,
      },
      {
        tag: 'nao',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'marcos-desenvolvimento-avaliados': {
    data: [
      {
        tag: 'avaliados',
        value: 82,
      },
      {
        tag: 'nao-avaliados',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
  'consumo-alimentar-avaliado': {
    data: [
      {
        tag: 'avaliados',
        value: 82,
      },
      {
        tag: 'nao-avaliados',
        value: 10,
      },
      {
        tag: 'nao-se-aplica',
        value: 8,
      },
    ],
  },
};
