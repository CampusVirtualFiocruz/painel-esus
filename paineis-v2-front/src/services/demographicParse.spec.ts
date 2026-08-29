import { ageGroupParser } from "./demographicParser";

describe("Demographic parser", () => {
  test("handles undefined data", () => {
    expect(ageGroupParser(undefined)).toEqual([]);
  });

  test("testing conversion with full data", () => {
    const data = {
      ageGroups: {
        Feminino: {
          "Faixa et\u00e1ria 0 a 17 anos": {
            Rural: 357,
            Urbano: 3099,
            "Nao Informado": 10,
          },
          "Faixa et\u00e1ria 18 a 29 anos": {
            Rural: 363,
            Urbano: 3137,
            "Nao Informado": 20,
          },
        },
        Masculino: {
          "Faixa et\u00e1ria 0 a 17 anos": {
            Rural: 357,
            Urbano: 3099,
            "Nao Informado": 15,
          },
          "Faixa et\u00e1ria 18 a 29 anos": {
            Rural: 363,
            Urbano: 3137,
            "Nao Informado": 25,
          },
        },
      },
    };

    const response = ageGroupParser(data);
    const expec = [
      {
        type: "Masculino",
        areaUrbana: {
          "0 a 17 anos": { value: 3099, label: "Urbano", itemStyle: { color: "#0069d0" } },
          "18 a 29 anos": { value: 3137, label: "Urbano", itemStyle: { color: "#0069d0" } },
        },
        areaRural: {
          "0 a 17 anos": { value: 357, label: "Rural", itemStyle: { color: "#84aaff" } },
          "18 a 29 anos": { value: 363, label: "Rural", itemStyle: { color: "#84aaff" } },
        },
        nao_informado: {
          "0 a 17 anos": { value: 15, label: "Não Informado", itemStyle: { color: "#e9ecef" } },
          "18 a 29 anos": { value: 25, label: "Não Informado", itemStyle: { color: "#e9ecef" } },
        },
      },
      {
        type: "Feminino",
        areaUrbana: {
          "0 a 17 anos": { value: 3099, label: "Urbano", itemStyle: { color: "#0069d0" } },
          "18 a 29 anos": { value: 3137, label: "Urbano", itemStyle: { color: "#0069d0" } },
        },
        areaRural: {
          "0 a 17 anos": { value: 357, label: "Rural", itemStyle: { color: "#84aaff" } },
          "18 a 29 anos": { value: 363, label: "Rural", itemStyle: { color: "#84aaff" } },
        },
        nao_informado: {
          "0 a 17 anos": { value: 10, label: "Não Informado", itemStyle: { color: "#e9ecef" } },
          "18 a 29 anos": { value: 20, label: "Não Informado", itemStyle: { color: "#e9ecef" } },
        },
      },
    ];

    expect(response).toEqual(expec);
  });

  test("testing conversion with partial data (only Masculino)", () => {
    const data = {
      ageGroups: {
        Masculino: {
          "Faixa et\u00e1ria 0 a 17 anos": {
            Rural: 100,
            Urbano: 200,
            "Nao Informado": 5,
          },
        },
      },
    };

    const response = ageGroupParser(data);
    const expec = [
      {
        type: "Masculino",
        areaUrbana: {
          "0 a 17 anos": { value: 200, label: "Urbano", itemStyle: { color: "#0069d0" } },
        },
        areaRural: {
          "0 a 17 anos": { value: 100, label: "Rural", itemStyle: { color: "#84aaff" } },
        },
        nao_informado: {
          "0 a 17 anos": { value: 5, label: "Não Informado", itemStyle: { color: "#e9ecef" } },
        },
      },
      {
        type: "Feminino",
        areaUrbana: {},
        areaRural: {},
        nao_informado: {},
      },
    ];

    expect(response).toEqual(expec);
  });

  test("testing conversion with partial data (only Feminino)", () => {
    const data = {
      ageGroups: {
        Feminino: {
          "Faixa et\u00e1ria 0 a 17 anos": {
            Rural: 100,
            Urbano: 200,
            "Nao Informado": 5,
          },
        },
      },
    };

    const response = ageGroupParser(data);
    const expec = [
      {
        type: "Masculino",
        areaUrbana: {},
        areaRural: {},
        nao_informado: {},
      },
      {
        type: "Feminino",
        areaUrbana: {
          "0 a 17 anos": { value: 200, label: "Urbano", itemStyle: { color: "#0069d0" } },
        },
        areaRural: {
          "0 a 17 anos": { value: 100, label: "Rural", itemStyle: { color: "#84aaff" } },
        },
        nao_informado: {
          "0 a 17 anos": { value: 5, label: "Não Informado", itemStyle: { color: "#e9ecef" } },
        },
      },
    ];

    expect(response).toEqual(expec);
  });
});
