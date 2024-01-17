
export const ageGroupParser = (data: any) => {
    if (data === undefined) return [];


    let dataFake = {
        "Feminino": [
            {
                "Faixa etária 0 a 5 anos": {
                    "NaN": 3495,
                    "Rural": 50,
                    "Urbano": 300
                },
                "Faixa etária 6 a 12 anos": {
                    "NaN": 3495,
                    "Rural": 135,
                    "Urbano": 568
                },
                "Faixa etária 13 a 17 anos": {
                    "NaN": 3495,
                    "Rural": 578,
                    "Urbano": 2407
                },
                "Faixa etária 18 a 29 anos": {
                    "NaN": 4963,
                    "Rural": 897,
                    "Urbano": 3556
                },
                "Faixa etária 30 a 44 anos": {
                    "NaN": 4847,
                    "Rural": 1207,
                    "Urbano": 4363
                },
                "Faixa etária 45 a 59 anos": {
                    "NaN": 3910,
                    "Rural": 1048,
                    "Urbano": 4109
                },
                "Faixa etária 60 + anos": {
                    "NaN": 4016,
                    "Rural": 1170,
                    "Urbano": 4102
                }
            }
        ],
        "Masculino": [
            {
                "Faixa etária 0 a 5 anos": {
                    "NaN": 3495,
                    "Rural": 178,
                    "Urbano": 407
                },
                "Faixa etária 6 a 12 anos": {
                    "NaN": 3495,
                    "Rural": 278,
                    "Urbano": 1207
                },
                "Faixa etária 13 a 17 anos": {
                    "NaN": 3495,
                    "Rural": 378,
                    "Urbano": 1407
                },
                "Faixa etária 18 a 29 anos": {
                    "NaN": 3741,
                    "Rural": 655,
                    "Urbano": 2665
                },
                "Faixa etária 30 a 44 anos": {
                    "NaN": 3904,
                    "Rural": 819,
                    "Urbano": 2943
                },
                "Faixa etária 45 a 59 anos": {
                    "NaN": 2966,
                    "Rural": 880,
                    "Urbano": 2861
                },
                "Faixa etária 60 + anos": {
                    "NaN": 2921,
                    "Rural": 1062,
                    "Urbano": 3054
                }
            }
        ]
    };

    data.ageGroups = dataFake;

    const ageGroups = data.ageGroups;
    const masculino = ageGroups.Masculino;
    const feminino = ageGroups.Feminino;

    const masculinoType = {
        type: 'Masculino',
        areaUrbana: {},
        areaRural: {}
    };

    const femininoType = {
        type: 'Feminino',
        areaUrbana: {},
        areaRural: {}
    };

    let ageGroupsKeys = [];

    if (masculino !== undefined) {
        ageGroupsKeys = Object.keys(masculino[0]);
        ageGroupsKeys.forEach((item: string) => {
            const newKey = item.replace('Faixa et\u00e1ria ', '')
            // @ts-ignore: Unreachable code error
            masculinoType.areaUrbana[newKey] = {
                value: masculino[0][item]['Urbano'],
                itemStyle: {
                    color: "#2775b0"
                }
            };
            // @ts-ignore: Unreachable code error
            masculinoType.areaRural[newKey] = { value: masculino[0][item]['Rural'], itemStyle: { color: '#78b4d0' } };
        });
    }

    if (feminino !== undefined) {
        ageGroupsKeys = Object.keys(feminino[0]);
        ageGroupsKeys.forEach((item: string) => {
            const newKey = item.replace('Faixa et\u00e1ria ', '')
            // @ts-ignore: Unreachable code error
            femininoType.areaUrbana[newKey] = {
                value: feminino[0][item]['Urbano'],
                itemStyle: {
                    color: "#2775b0"
                }
            };
            // @ts-ignore: Unreachable code error
            femininoType.areaRural[newKey] = { value: feminino[0][item]['Rural'], itemStyle: { color: '#78b4d0' } };
        });
    }

    return [masculinoType, femininoType];
}