export const ageGroupParser = (data: any) => {
  if (data === undefined) return [];

  let dataFake = {
    Feminino: [
      {
        "Faixa etária 0 a 5 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 6 a 12 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 13 a 17 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 18 a 29 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 30 a 44 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 45 a 59 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 60 + anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
      },
    ],
    Masculino: [
      {
        "Faixa etária 0 a 5 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 6 a 12 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 13 a 17 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 18 a 29 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 30 a 44 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 45 a 59 anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
        "Faixa etária 60 + anos": {
          NaN: 0,
          Rural: 0,
          Urbano: 0,
        },
      },
    ],
  };

  // data.ageGroups = dataFake;

  const ageGroups = data.ageGroups;
  const masculino = ageGroups.Masculino;
  const feminino = ageGroups.Feminino;

  const masculinoType = {
    type: "Masculino",
    areaUrbana: {},
    areaRural: {},
  };

  const femininoType = {
    type: "Feminino",
    areaUrbana: {},
    areaRural: {},
  };

  let ageGroupsKeys = [];

  if (masculino !== undefined) {
    ageGroupsKeys = Object.keys(masculino);
    ageGroupsKeys.forEach((item: string) => {
      const newKey = item.replace("Faixa et\u00e1ria ", "");
      // @ts-ignore: Unreachable code error
      masculinoType.areaUrbana[newKey] = {
        value: masculino[item]["Urbano"],
        itemStyle: {
          color: "#0069d0",
        },
      };
      // @ts-ignore: Unreachable code error
      masculinoType.areaRural[newKey] = {
        value: masculino[item]["Rural"],
        itemStyle: { color: "#84aaff" },
      };
    });
  }

  if (feminino !== undefined) {
    ageGroupsKeys = Object.keys(feminino);
    ageGroupsKeys.forEach((item: string) => {
      const newKey = item.replace("Faixa et\u00e1ria ", "");
      // @ts-ignore: Unreachable code error
      femininoType.areaUrbana[newKey] = {
        value: feminino[item]["Urbano"],
        itemStyle: {
          color: "#0069d0",
        },
      };
      // @ts-ignore: Unreachable code error
      femininoType.areaRural[newKey] = {
        value: feminino[item]["Rural"],
        itemStyle: { color: "#84aaff" },
      };
    });
  }

  return [masculinoType, femininoType];
};
