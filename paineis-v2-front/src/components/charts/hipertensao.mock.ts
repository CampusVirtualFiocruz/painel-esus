import {
  BarChart,
  DonutGroupChart,
  ProgressListChart,
  ValueChart,
} from "./charts.types";

type MockRelatorioHipertensao = {
  "pessoas-por-faixa-etaria": BarChart;
  "pessoas-por-sexo": BarChart;
  "situacao-exames-12-meses": BarChart;
  "total-atendimentos-12-meses": ValueChart;
  "total-pessoas-cid-ciap": ValueChart;
  "total-pessoas-auto": ValueChart;
  "frequencia-complicacoes": DonutGroupChart;
  "adultos-por-imc": DonutGroupChart;
  "atendimentos-por-profissional": ProgressListChart;
};

export const charts: MockRelatorioHipertensao = {
  "pessoas-por-faixa-etaria": {
    data: [
      {
        tag: "0-19",
        value: {
          urbana: 10,
          rural: 12,
          "nao-informado": 6,
        },
      },
      {
        tag: "20-29",
        value: {
          urbana: 10,
          rural: 12,
          "nao-informado": 6,
        },
      },
      {
        tag: "30-39",
        value: {
          urbana: 10,
          rural: 12,
          "nao-informado": 6,
        },
      },
    ],
  },
  "pessoas-por-sexo": {
    data: [
      {
        tag: "0-19",
        value: {
          urbana: 10,
          rural: 12,
          "nao-informado": 6,
        },
      },
      {
        tag: "20-29",
        value: {
          urbana: 10,
          rural: 12,
          "nao-informado": 6,
        },
      },
      {
        tag: "30-39",
        value: {
          urbana: 10,
          rural: 12,
          "nao-informado": 6,
        },
      },
    ],
  },
  "situacao-exames-12-meses": {
    data: [
      {
        tag: "glicemia",
        value: {
          "sem-solicitacao": 214,
          "aguardando-resultado": 12,
          "resultado-registrado": 6,
        },
      },
      {
        tag: "creatinina",
        value: {
          "sem-solicitacao": 214,
          "aguardando-resultado": 12,
          "resultado-registrado": 6,
        },
      },
      {
        tag: "eas-equ",
        value: {
          "sem-solicitacao": 214,
          "aguardando-resultado": 12,
          "resultado-registrado": 6,
        },
      },
      {
        tag: "sodio",
        value: {
          "sem-solicitacao": 214,
          "aguardando-resultado": 12,
          "resultado-registrado": 6,
        },
      },
    ],
  },
  "total-atendimentos-12-meses": {
    data: 813,
  },
  "total-pessoas-cid-ciap": {
    data: 813,
  },
  "total-pessoas-auto": {
    data: 813,
  },
  "frequencia-complicacoes": {
    data: [
      {
        tag: "infarto-agudo-miocardio",
        value: 0,
        data: [
          {
            tag: "possui",
            value: 0,
          },
          {
            tag: "nao-possui",
            value: 0,
          },
        ],
      },
      {
        tag: "acidente-vascular-encefalico",
        value: 0.1,
        data: [
          {
            tag: "possui",
            value: 0,
          },
          {
            tag: "nao-possui",
            value: 0.1,
          },
        ],
      },
    ],
  },
  "adultos-por-imc": {
    data: [
      {
        tag: "baixo-peso",
        value: 0,
        data: [
          {
            tag: "possui",
            value: 0,
          },
          {
            tag: "nao-possui",
            value: 0,
          },
        ],
      },
      {
        tag: "peso-adequado",
        value: 0.4,
        data: [
          {
            tag: "possui",
            value: 0.4,
          },
          {
            tag: "nao-possui",
            value: 0.96,
          },
        ],
      },
    ],
  },
  "atendimentos-por-profissional": {
    data: [
      {
        value: 0.0012, // 0.12%
        tag: "assistente-social",
      },
      {
        value: 0.1796, // 17.96%
        tag: "enfermeiro",
      },
      {
        value: 0.8106, // 81.06%
        tag: "medico",
      },
    ],
  },
};
