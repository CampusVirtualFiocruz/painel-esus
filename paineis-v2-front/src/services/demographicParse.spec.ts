import { ageGroupParser } from './demographicParser';
describe('Demographic parser', () => { 

    test('testing conversion', () => {



        const data = {
            ageGroups: {
                "Feminino": [
                {
                    "Faixa et\u00e1ria 0 a 17 anos": {
                    "Rural": 357,
                    "Urbano": 3099
                    },
                    "Faixa et\u00e1ria 18 a 29 anos": {
                    "Rural": 363,
                    "Urbano": 3137
                    },
                    "Faixa et\u00e1ria 30 a 44 anos": {
                    "Rural": 450,
                    "Urbano": 3909
                    },
                    "Faixa et\u00e1ria 45 a 59 anos": {
                    "Rural": 401,
                    "Urbano": 3346
                    },
                    "Faixa et\u00e1ria 60 + anos": {
                    "Rural": 392,
                    "Urbano": 2809
                    }
                }
                ],
                "Masculino": [
                    {
                        "Faixa et\u00e1ria 0 a 17 anos": {
                        "Rural": 357,
                        "Urbano": 3099
                        },
                        "Faixa et\u00e1ria 18 a 29 anos": {
                        "Rural": 363,
                        "Urbano": 3137
                        },
                        "Faixa et\u00e1ria 30 a 44 anos": {
                        "Rural": 450,
                        "Urbano": 3909
                        },
                        "Faixa et\u00e1ria 45 a 59 anos": {
                        "Rural": 401,
                        "Urbano": 3346
                        },
                        "Faixa et\u00e1ria 60 + anos": {
                        "Rural": 392,
                        "Urbano": 2809
                        }
                    }
                ]
            }
        };
        const response = ageGroupParser( data )
        const expec =  [
            {
                type: 'Masculino',
                areaUrbana: {
                    '0 a 17 anos': { value: 3099, itemStyle: { color: '#2775b0' } },
                    '18 a 29 anos': { value: 3137, itemStyle: { color: '#2775b0' } },
                    '30 a 44 anos': { value: 3909, itemStyle: { color: '#2775b0' } },
                    '45 a 59 anos': { value: 3346, itemStyle: { color: '#2775b0' } },
                    '60 + anos': { value: 2809, itemStyle: { color: '#2775b0' } }
                },
                areaRural: {
                    '0 a 17 anos': { value: 357, itemStyle: { color: '#78b4d0' } },
                    '18 a 29 anos': { value: 363, itemStyle: { color: '#78b4d0' } },
                    '30 a 44 anos': { value: 450, itemStyle: { color: '#78b4d0' } },
                    '45 a 59 anos': { value: 401, itemStyle: { color: '#78b4d0' } },
                    '60 + anos': { value: 392, itemStyle: { color: '#78b4d0' } }
                }
            },
            {
                type: 'Feminino',
                areaUrbana: {
                    '0 a 17 anos': { value: 3099, itemStyle: { color: '#2775b0' } },
                    '18 a 29 anos': { value: 3137, itemStyle: { color: '#2775b0' } },
                    '30 a 44 anos': { value: 3909, itemStyle: { color: '#2775b0' } },
                    '45 a 59 anos': { value: 3346, itemStyle: { color: '#2775b0' } },
                    '60 + anos': { value: 2809, itemStyle: { color: '#2775b0' } }
                },
                areaRural: {
                    '0 a 17 anos': { value: 357, itemStyle: { color: '#78b4d0' } },
                    '18 a 29 anos': { value: 363, itemStyle: { color: '#78b4d0' } },
                    '30 a 44 anos': { value: 450, itemStyle: { color: '#78b4d0' } },
                    '45 a 59 anos': { value: 401, itemStyle: { color: '#78b4d0' } },
                    '60 + anos': { value: 392, itemStyle: { color: '#78b4d0' } }
                }
            }
        ]; 

        expect(response).toEqual(expec)
     });
 })