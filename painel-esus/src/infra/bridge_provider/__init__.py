# pylint: disable=line-too-long, C0302
import pytest


@pytest.fixture
def login_response():
    return {
        "extensions": {
            "tracing": {
                "version": 1,
                "startTime": "2024-09-30T20:57:59.604Z",
                "endTime": "2024-09-30T20:57:59.744Z",
                "duration": 140342580,
                "parsing": {
                    "startOffset": 6888722,
                    "duration": 6714721
                },
                "validation": {
                    "startOffset": 10143979,
                    "duration": 3217972
                },
                "execution": {
                    "resolvers": [
                        {
                            "path": [
                                "sessao"
                            ],
                            "parentType": "Query",
                            "returnType": "Sessao",
                            "fieldName": "sessao",
                            "startOffset": 13225342,
                            "duration": 1511822
                        },
                        {
                            "path": [
                                "sessao",
                                "id"
                            ],
                            "parentType": "Sessao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 14988397,
                            "duration": 29779
                        },
                        {
                            "path": [
                                "sessao",
                                "recursos"
                            ],
                            "parentType": "Sessao",
                            "returnType": "[String]",
                            "fieldName": "recursos",
                            "startOffset": 15214100,
                            "duration": 122332
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional"
                            ],
                            "parentType": "Sessao",
                            "returnType": "Profissional!",
                            "fieldName": "profissional",
                            "startOffset": 15432992,
                            "duration": 12792993
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "id"
                            ],
                            "parentType": "Profissional",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 29134637,
                            "duration": 58454
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "cpf"
                            ],
                            "parentType": "Profissional",
                            "returnType": "String!",
                            "fieldName": "cpf",
                            "startOffset": 29265275,
                            "duration": 15565
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "cns"
                            ],
                            "parentType": "Profissional",
                            "returnType": "String",
                            "fieldName": "cns",
                            "startOffset": 29302370,
                            "duration": 9417
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "nome"
                            ],
                            "parentType": "Profissional",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 29328429,
                            "duration": 8949
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "usuario"
                            ],
                            "parentType": "Profissional",
                            "returnType": "Usuario!",
                            "fieldName": "usuario",
                            "startOffset": 29547245,
                            "duration": 13484723
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "usuario",
                                "id"
                            ],
                            "parentType": "Usuario",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 43275273,
                            "duration": 34845
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "usuario",
                                "bloqueado"
                            ],
                            "parentType": "Usuario",
                            "returnType": "Boolean!",
                            "fieldName": "bloqueado",
                            "startOffset": 43532673,
                            "duration": 29760
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes"
                            ],
                            "parentType": "Profissional",
                            "returnType": "[Lotacao!]!",
                            "fieldName": "lotacoes",
                            "startOffset": 29591070,
                            "duration": 15152012
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 45353369,
                            "duration": 100787
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 45583671,
                            "duration": 24257
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 46017404,
                            "duration": 24216
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 46884882,
                            "duration": 15440
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 46934740,
                            "duration": 14217
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 47019738,
                            "duration": 14154
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 47228654,
                            "duration": 12809
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 47270365,
                            "duration": 12944
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 47492874,
                            "duration": 13429
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 47878880,
                            "duration": 14906
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 48090046,
                            "duration": 18888
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 48384815,
                            "duration": 149482
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 49223588,
                            "duration": 18930
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 49360630,
                            "duration": 16228
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 50122179,
                            "duration": 13952
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 50167172,
                            "duration": 13770
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 50433006,
                            "duration": 13041
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 50474095,
                            "duration": 12884
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 51127518,
                            "duration": 16125
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 51328435,
                            "duration": 18198
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 52349690,
                            "duration": 16204
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 52531019,
                            "duration": 97869
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 53582599,
                            "duration": 16902
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 53712597,
                            "duration": 149880
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 54736590,
                            "duration": 106350
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 54955264,
                            "duration": 16910
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 56105789,
                            "duration": 157667
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 56378034,
                            "duration": 15743
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 57512832,
                            "duration": 16058
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 57640972,
                            "duration": 15242
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 58798670,
                            "duration": 94191
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 59001590,
                            "duration": 19875
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 60069832,
                            "duration": 15462
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 60266474,
                            "duration": 17037
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 60559468,
                            "duration": 92555
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 61505111,
                            "duration": 15398
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 61622567,
                            "duration": 82681
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 62086192,
                            "duration": 10682
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 62123795,
                            "duration": 10834
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 62344133,
                            "duration": 11318
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 62380141,
                            "duration": 11228
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 62595511,
                            "duration": 10487
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 62631665,
                            "duration": 10398
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 62696188,
                            "duration": 13345
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 62875154,
                            "duration": 10576
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 62910833,
                            "duration": 14993
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 63129204,
                            "duration": 152412
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 63310533,
                            "duration": 11168
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 63801142,
                            "duration": 87338
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 63985666,
                            "duration": 13750
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 64128908,
                            "duration": 144354
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 65202820,
                            "duration": 15074
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 65313022,
                            "duration": 117295
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 66535564,
                            "duration": 8177
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 66681350,
                            "duration": 129716
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 67732174,
                            "duration": 145855
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 68067442,
                            "duration": 19629
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 69594741,
                            "duration": 60256
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 69732029,
                            "duration": 8914
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 70680622,
                            "duration": 5140
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 70845860,
                            "duration": 5711
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 71073564,
                            "duration": 108736
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 71822889,
                            "duration": 5429
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 71940491,
                            "duration": 5306
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 72650464,
                            "duration": 54309
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 72761694,
                            "duration": 5207
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 73315277,
                            "duration": 51659
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 73425000,
                            "duration": 5580
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 73654214,
                            "duration": 5684
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 74143415,
                            "duration": 5343
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 74205452,
                            "duration": 51551
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos"
                            ],
                            "parentType": "Profissional",
                            "returnType": "[Acesso!]",
                            "fieldName": "acessos",
                            "startOffset": 29356769,
                            "duration": 45339029
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 74863348,
                            "duration": 5396
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 74949091,
                            "duration": 47608
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                0,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 75073556,
                            "duration": 10484
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                0,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 75143206,
                            "duration": 84811
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                1,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 75502476,
                            "duration": 5635
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                1,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 75562334,
                            "duration": 46734
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 75526215,
                            "duration": 115137
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 75693372,
                            "duration": 4243
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                2,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 75778591,
                            "duration": 4552
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                2,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 75902552,
                            "duration": 153564
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 76405782,
                            "duration": 51306
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                3,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 76479438,
                            "duration": 4185
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 76577313,
                            "duration": 4315
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                3,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 76659041,
                            "duration": 48167
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 76864949,
                            "duration": 4942
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                4,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 76880741,
                            "duration": 4508
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                4,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 76937500,
                            "duration": 47401
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                5,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 77220210,
                            "duration": 4856
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 77285500,
                            "duration": 4750
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 77342360,
                            "duration": 117821
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                5,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 77348043,
                            "duration": 115603
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                6,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 77819634,
                            "duration": 4710
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 78026166,
                            "duration": 4295
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                6,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 77943582,
                            "duration": 116109
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 78082653,
                            "duration": 47537
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                7,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 78405018,
                            "duration": 4510
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                7,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 78464048,
                            "duration": 164971
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 78568995,
                            "duration": 99735
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 78788206,
                            "duration": 4196
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                8,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 78969238,
                            "duration": 4374
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 79080247,
                            "duration": 4761
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                8,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 79079814,
                            "duration": 101326
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 79472848,
                            "duration": 4027
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                9,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 79505311,
                            "duration": 4387
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 79680128,
                            "duration": 4413
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                9,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 79604994,
                            "duration": 127771
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                10,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 80072462,
                            "duration": 4630
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                10,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 80182846,
                            "duration": 47505
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                11,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 80557174,
                            "duration": 5493
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 80568194,
                            "duration": 5258
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                11,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 80671574,
                            "duration": 101839
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 80693603,
                            "duration": 147005
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                12,
                                "id"
                            ],
                            "parentType": "GestorEstadual",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 80943859,
                            "duration": 36334
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                12,
                                "tipo"
                            ],
                            "parentType": "GestorEstadual",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 81039122,
                            "duration": 69748
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 81329196,
                            "duration": 13593
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                13,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 81342089,
                            "duration": 5585
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                13,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 81401255,
                            "duration": 100278
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 81466072,
                            "duration": 13844
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                14,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 81679235,
                            "duration": 4833
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                14,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 81736806,
                            "duration": 4011
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                15,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 82009079,
                            "duration": 4954
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                15,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 82118793,
                            "duration": 3662
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 82161738,
                            "duration": 49850
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 82319491,
                            "duration": 5224
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                16,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 82497979,
                            "duration": 5020
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                16,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 82609358,
                            "duration": 4103
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 82876487,
                            "duration": 49248
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "ativo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 82978558,
                            "duration": 4475
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                17,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 83054877,
                            "duration": 4981
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 83157416,
                            "duration": 50585
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                17,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 83153896,
                            "duration": 4107
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                18,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 83529878,
                            "duration": 4898
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                18,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 83586670,
                            "duration": 3753
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                19,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 83855863,
                            "duration": 4920
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                19,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 83967780,
                            "duration": 3784
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                20,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 84255872,
                            "duration": 49619
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                20,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 84380252,
                            "duration": 4594
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                21,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 84556670,
                            "duration": 48167
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                21,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 84725273,
                            "duration": 3790
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                22,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 84952016,
                            "duration": 103561
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                22,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 85171955,
                            "duration": 4186
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                23,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 85398467,
                            "duration": 49077
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                23,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 85500558,
                            "duration": 3732
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                24,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 85777377,
                            "duration": 103889
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                24,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 85987468,
                            "duration": 3721
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                25,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 86338108,
                            "duration": 50526
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                25,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 86495990,
                            "duration": 3884
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                26,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 86840451,
                            "duration": 108171
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                26,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 87057592,
                            "duration": 3829
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                27,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 87367987,
                            "duration": 92811
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                27,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 87568185,
                            "duration": 3824
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                28,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 87907549,
                            "duration": 48903
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                28,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88008899,
                            "duration": 3893
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                29,
                                "id"
                            ],
                            "parentType": "GestorMunicipal",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88089984,
                            "duration": 4430
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                29,
                                "tipo"
                            ],
                            "parentType": "GestorMunicipal",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88102120,
                            "duration": 2833
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                30,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88130298,
                            "duration": 3559
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                30,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88141218,
                            "duration": 2434
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                31,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88168134,
                            "duration": 3447
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                31,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88178686,
                            "duration": 2599
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                32,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88205696,
                            "duration": 3531
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                32,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88216310,
                            "duration": 2582
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                33,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88243336,
                            "duration": 3627
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                33,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88254012,
                            "duration": 2480
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                34,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88280877,
                            "duration": 3578
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                34,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88291560,
                            "duration": 2478
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                35,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88318437,
                            "duration": 3432
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                35,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88328954,
                            "duration": 2578
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                36,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88355788,
                            "duration": 3753
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                36,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88366555,
                            "duration": 2462
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                37,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88393812,
                            "duration": 3644
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                37,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88404489,
                            "duration": 2364
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                38,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88431012,
                            "duration": 3652
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                38,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88548583,
                            "duration": 3759
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                39,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 88770079,
                            "duration": 48034
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                39,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 88869946,
                            "duration": 3772
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                40,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 89060533,
                            "duration": 4314
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                40,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 89226709,
                            "duration": 4147
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                41,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 89579696,
                            "duration": 4590
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                41,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 89679157,
                            "duration": 3759
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                42,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 89756684,
                            "duration": 3827
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                42,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 89913382,
                            "duration": 3892
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                43,
                                "id"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 89989554,
                            "duration": 3929
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "acessos",
                                43,
                                "tipo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipo",
                            "startOffset": 90000408,
                            "duration": 2568
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 54096423,
                            "duration": 42666429
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 78956545,
                            "duration": 17848563
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 96836094,
                            "duration": 27462
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 96877713,
                            "duration": 7349
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 52788491,
                            "duration": 44123264
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 96925962,
                            "duration": 3784
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 96936537,
                            "duration": 2701
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 49752470,
                            "duration": 47196709
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 96959866,
                            "duration": 3255
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 96969317,
                            "duration": 2341
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 51576859,
                            "duration": 45403203
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 96947980,
                            "duration": 12439
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 97105789,
                            "duration": 5443
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 97195522,
                            "duration": 10250
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 64096916,
                            "duration": 33241340
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 97289012,
                            "duration": 68026
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 50547851,
                            "duration": 46878769
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 97463210,
                            "duration": 49479
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 97589637,
                            "duration": 6455
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 97622926,
                            "duration": 4057
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 97695985,
                            "duration": 10984
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 51455996,
                            "duration": 46228001
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 50244962,
                            "duration": 47644572
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 98012295,
                            "duration": 4366
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 97956408,
                            "duration": 105628
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 98184457,
                            "duration": 4248
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 98140759,
                            "duration": 3730
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 56655049,
                            "duration": 41592430
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 45875225,
                            "duration": 52490889
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 98474856,
                            "duration": 3964
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 98399741,
                            "duration": 10428
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 98531050,
                            "duration": 47151
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 98584603,
                            "duration": 7968
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 55349164,
                            "duration": 43320564
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 74314908,
                            "duration": 24387324
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 98793420,
                            "duration": 8430
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 98808908,
                            "duration": 4414
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 98908764,
                            "duration": 3528
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 98925355,
                            "duration": 8207
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 61803915,
                            "duration": 37163559
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 57952552,
                            "duration": 41055462
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 99071760,
                            "duration": 4219
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 99133782,
                            "duration": 9529
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 99247955,
                            "duration": 4733
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 46977296,
                            "duration": 52393890
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 99276019,
                            "duration": 170795
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 69050626,
                            "duration": 30489871
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 100162854,
                            "duration": 62359
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 100222756,
                            "duration": 7283
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 100287356,
                            "duration": 3744
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 100360593,
                            "duration": 6235
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 75050852,
                            "duration": 25443117
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 67078028,
                            "duration": 33460062
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 100629458,
                            "duration": 6252
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 100598964,
                            "duration": 119047
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 100843208,
                            "duration": 5586
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 100857140,
                            "duration": 83097
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 65689267,
                            "duration": 35285318
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 62160098,
                            "duration": 39628224
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 101846318,
                            "duration": 5332
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 48681755,
                            "duration": 53226842
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 101944424,
                            "duration": 9107
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 101944345,
                            "duration": 11111
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 101969463,
                            "duration": 6449
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 47590162,
                            "duration": 54401254
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102014237,
                            "duration": 4132
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102015163,
                            "duration": 6740
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102032342,
                            "duration": 4798
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 47095715,
                            "duration": 54953035
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 62978175,
                            "duration": 39097030
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102080815,
                            "duration": 7058
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 47451457,
                            "duration": 54759155
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102248100,
                            "duration": 3879
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102304111,
                            "duration": 3227
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102190540,
                            "duration": 133544
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102391340,
                            "duration": 7875
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 59335419,
                            "duration": 43086695
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 48566643,
                            "duration": 53874546
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102526392,
                            "duration": 4496
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102467642,
                            "duration": 6849
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102535013,
                            "duration": 10920
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 102559399,
                            "duration": 4822
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 102571930,
                            "duration": 7061
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 47534257,
                            "duration": 55062032
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102606898,
                            "duration": 6058
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102614834,
                            "duration": 3822
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 102626494,
                            "duration": 2282
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102584599,
                            "duration": 47593
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 102635428,
                            "duration": 3515
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 47061939,
                            "duration": 55588302
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 46283136,
                            "duration": 56258615
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102666403,
                            "duration": 3119
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 102677272,
                            "duration": 2265
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 75793144,
                            "duration": 26890040
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 102685916,
                            "duration": 2892
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 62444416,
                            "duration": 40244844
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 46156791,
                            "duration": 56543808
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102715685,
                            "duration": 2885
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 102725244,
                            "duration": 5237
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 102737141,
                            "duration": 3393
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 56832202,
                            "duration": 45919313
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102769341,
                            "duration": 2962
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 102778893,
                            "duration": 3145
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 102788076,
                            "duration": 2978
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102788603,
                            "duration": 9612
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 55470194,
                            "duration": 47331989
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102850698,
                            "duration": 4696
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 102881005,
                            "duration": 56844
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102988454,
                            "duration": 50014
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 102929376,
                            "duration": 9491
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103057113,
                            "duration": 7611
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 62189509,
                            "duration": 40910243
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 57014015,
                            "duration": 46104234
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103126048,
                            "duration": 4654
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 103184478,
                            "duration": 46811
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 103281805,
                            "duration": 4637
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 62416416,
                            "duration": 40718859
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103300068,
                            "duration": 9687
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103213385,
                            "duration": 103883
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103324052,
                            "duration": 4918
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 55582909,
                            "duration": 47762029
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103365445,
                            "duration": 3712
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103377338,
                            "duration": 3560
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 54337039,
                            "duration": 49053320
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103405152,
                            "duration": 3854
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103416431,
                            "duration": 4336
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103371619,
                            "duration": 4015
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 53047466,
                            "duration": 50389485
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 54216007,
                            "duration": 49126081
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103461809,
                            "duration": 5175
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103474794,
                            "duration": 2723
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 51815621,
                            "duration": 51672920
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103499501,
                            "duration": 8836
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103511564,
                            "duration": 6012
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103529387,
                            "duration": 4184
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 50609048,
                            "duration": 52935518
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103563672,
                            "duration": 6112
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103579998,
                            "duration": 4696
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 61908295,
                            "duration": 41676854
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 50306905,
                            "duration": 53294028
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103623374,
                            "duration": 4860
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103619966,
                            "duration": 10066
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103638146,
                            "duration": 4715
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 49981630,
                            "duration": 53670179
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103667516,
                            "duration": 3631
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103678118,
                            "duration": 3875
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103577215,
                            "duration": 6882
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 48214745,
                            "duration": 55552418
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 71367527,
                            "duration": 32438523
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103696957,
                            "duration": 117492
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 103771216,
                            "duration": 4077
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 103874871,
                            "duration": 4942
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 103937169,
                            "duration": 4407
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 52915430,
                            "duration": 51028236
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 103947428,
                            "duration": 8740
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 63377605,
                            "duration": 40621687
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104048632,
                            "duration": 7866
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104101470,
                            "duration": 4122
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104160848,
                            "duration": 4994
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104201891,
                            "duration": 4000
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104086345,
                            "duration": 161856
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 70087606,
                            "duration": 34173870
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104290294,
                            "duration": 7991
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 104274145,
                            "duration": 3990
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 72873262,
                            "duration": 31512557
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 70327491,
                            "duration": 34106937
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 104432340,
                            "duration": 5471
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104434429,
                            "duration": 4730
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 51696833,
                            "duration": 52798883
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104537395,
                            "duration": 4093
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104567377,
                            "duration": 9007
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 72284375,
                            "duration": 32314054
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104690006,
                            "duration": 7824
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104602294,
                            "duration": 116635
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104773007,
                            "duration": 4574
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 104775243,
                            "duration": 4220
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104694057,
                            "duration": 6612
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 59214133,
                            "duration": 45641645
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104830674,
                            "duration": 49874
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 104883827,
                            "duration": 6833
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 104920916,
                            "duration": 10362
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 81799590,
                            "duration": 23137478
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 104995230,
                            "duration": 54126
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 69203318,
                            "duration": 35858722
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 50579101,
                            "duration": 54495676
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 105113275,
                            "duration": 6715
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105138209,
                            "duration": 6430
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105232373,
                            "duration": 53636
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 105203313,
                            "duration": 4979
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 105344637,
                            "duration": 5516
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 49566322,
                            "duration": 55681738
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105323197,
                            "duration": 63241
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 80958731,
                            "duration": 24497473
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 105509392,
                            "duration": 7204
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 105518206,
                            "duration": 6779
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 50276130,
                            "duration": 55299013
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105595649,
                            "duration": 59460
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105489797,
                            "duration": 172213
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 67345347,
                            "duration": 38345817
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 105776184,
                            "duration": 4039
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 105726503,
                            "duration": 5838
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105740743,
                            "duration": 51220
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 105845764,
                            "duration": 4112
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 105888616,
                            "duration": 8071
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 77583134,
                            "duration": 28371661
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 79896512,
                            "duration": 26007605
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 105969688,
                            "duration": 48137
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 49940613,
                            "duration": 56090327
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106095532,
                            "duration": 4084
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106016753,
                            "duration": 123155
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106164908,
                            "duration": 8138
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106072485,
                            "duration": 3946
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 106220066,
                            "duration": 3905
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106241916,
                            "duration": 4118
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 65975007,
                            "duration": 40304512
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 77638513,
                            "duration": 28664288
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 106282269,
                            "duration": 48933
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106232502,
                            "duration": 132263
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 71307800,
                            "duration": 35081810
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106479143,
                            "duration": 4597
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 62949634,
                            "duration": 43542994
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106543867,
                            "duration": 9653
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106498795,
                            "duration": 4102
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106622361,
                            "duration": 6908
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106647680,
                            "duration": 4407
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 106654156,
                            "duration": 4011
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 72988447,
                            "duration": 33730789
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106763397,
                            "duration": 12140
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 106720162,
                            "duration": 65683
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106784309,
                            "duration": 8732
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 50208573,
                            "duration": 56640264
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 70213699,
                            "duration": 36667714
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 106904743,
                            "duration": 7212
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 64626880,
                            "duration": 42286891
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 106978639,
                            "duration": 113060
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107092090,
                            "duration": 9038
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107147505,
                            "duration": 50618
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 75847571,
                            "duration": 31365216
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 107224627,
                            "duration": 8798
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107126435,
                            "duration": 6840
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107251205,
                            "duration": 4567
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107284253,
                            "duration": 5617
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107299142,
                            "duration": 3580
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107359336,
                            "duration": 6896
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 78181210,
                            "duration": 29201720
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107406489,
                            "duration": 4436
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107418379,
                            "duration": 3055
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 107299791,
                            "duration": 125272
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 63346204,
                            "duration": 44088823
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 75104792,
                            "duration": 32348039
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107461652,
                            "duration": 6282
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107479477,
                            "duration": 3892
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 50513198,
                            "duration": 56981891
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 63432341,
                            "duration": 43951713
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 69075815,
                            "duration": 38431568
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107512818,
                            "duration": 3391
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107524224,
                            "duration": 2651
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 79739680,
                            "duration": 27798021
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107552869,
                            "duration": 3153
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107596591,
                            "duration": 55716
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107673964,
                            "duration": 6584
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107716268,
                            "duration": 6360
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107761044,
                            "duration": 10420
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107769119,
                            "duration": 13169
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 65555994,
                            "duration": 42255192
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 74441152,
                            "duration": 33400401
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107829297,
                            "duration": 5741
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 63030259,
                            "duration": 44865598
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107915943,
                            "duration": 5071
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107928271,
                            "duration": 3503
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 62761771,
                            "duration": 45179888
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107959008,
                            "duration": 3503
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107963933,
                            "duration": 6593
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 107970458,
                            "duration": 3548
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 62494475,
                            "duration": 45489376
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 107998714,
                            "duration": 3590
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108009110,
                            "duration": 2821
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 62243283,
                            "duration": 45778417
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 108014797,
                            "duration": 8104
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108037513,
                            "duration": 3428
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108101090,
                            "duration": 6293
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 108082193,
                            "duration": 8643
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108015253,
                            "duration": 136412
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108047430,
                            "duration": 107703
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 67204824,
                            "duration": 41016135
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108214878,
                            "duration": 7315
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 61970450,
                            "duration": 46294866
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 52661222,
                            "duration": 55572056
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108400449,
                            "duration": 5932
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 78236119,
                            "duration": 30061177
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108483052,
                            "duration": 7083
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108502592,
                            "duration": 5067
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 108509956,
                            "duration": 5618
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108476555,
                            "duration": 7861
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108656650,
                            "duration": 5027
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108655952,
                            "duration": 8768
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 108555231,
                            "duration": 7789
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 108624866,
                            "duration": 6208
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "equipe"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Equipe",
                            "fieldName": "equipe",
                            "startOffset": 82534976,
                            "duration": 26200615
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 80902976,
                            "duration": 27835600
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 60930665,
                            "duration": 47841395
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 65833225,
                            "duration": 42965143
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "equipe",
                                "id"
                            ],
                            "parentType": "Equipe",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108970203,
                            "duration": 8101
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108971823,
                            "duration": 8239
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108990704,
                            "duration": 8126
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 108985211,
                            "duration": 4730
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 109083948,
                            "duration": 7488
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 109009355,
                            "duration": 122990
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 109148044,
                            "duration": 8522
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "equipe",
                                "nome"
                            ],
                            "parentType": "Equipe",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 109151022,
                            "duration": 49252
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 59621450,
                            "duration": 49613631
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 66948736,
                            "duration": 42316348
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 109155167,
                            "duration": 47220
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 64436041,
                            "duration": 44943276
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 109447351,
                            "duration": 8642
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 109553231,
                            "duration": 7581
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 109566002,
                            "duration": 6612
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 109473867,
                            "duration": 152476
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 53975783,
                            "duration": 55660824
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 109618488,
                            "duration": 52808
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 109726804,
                            "duration": 5259
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 109692702,
                            "duration": 8280
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 58321731,
                            "duration": 51550125
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 63406446,
                            "duration": 46385912
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 109886530,
                            "duration": 118093
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 110116828,
                            "duration": 6974
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110115519,
                            "duration": 9930
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110127467,
                            "duration": 8176
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 46489156,
                            "duration": 63818872
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 81724650,
                            "duration": 28524328
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 110254511,
                            "duration": 112695
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 110241741,
                            "duration": 129542
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 110429071,
                            "duration": 7422
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 83324202,
                            "duration": 27166888
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110495750,
                            "duration": 9155
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 63004671,
                            "duration": 47508746
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110562154,
                            "duration": 21901
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 110566780,
                            "duration": 5123
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110680013,
                            "duration": 5763
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 110741326,
                            "duration": 52140
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 68937101,
                            "duration": 41876889
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 110821726,
                            "duration": 10889
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110729273,
                            "duration": 7808
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 110907130,
                            "duration": 7903
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 110910911,
                            "duration": 7367
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 110946226,
                            "duration": 7318
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 62735391,
                            "duration": 48250988
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 82646350,
                            "duration": 28390148
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 110943245,
                            "duration": 11689
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 111069817,
                            "duration": 59709
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111165144,
                            "duration": 7167
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 55218223,
                            "duration": 55990133
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111167163,
                            "duration": 60818
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 111247075,
                            "duration": 9244
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 111289396,
                            "duration": 6965
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 111288759,
                            "duration": 100741
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 81914299,
                            "duration": 29452467
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 47133976,
                            "duration": 64263992
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 111506957,
                            "duration": 7871
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111543489,
                            "duration": 7268
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111399173,
                            "duration": 7572
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 62469612,
                            "duration": 49116547
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 111612601,
                            "duration": 6307
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 111669529,
                            "duration": 9210
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111672859,
                            "duration": 10071
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111763193,
                            "duration": 7236
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 81067933,
                            "duration": 30720601
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 83145435,
                            "duration": 28663454
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 111835161,
                            "duration": 7053
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 111832675,
                            "duration": 7337
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 111898288,
                            "duration": 6552
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 112011658,
                            "duration": 7803
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112034424,
                            "duration": 8168
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 62215950,
                            "duration": 49870640
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 111991622,
                            "duration": 108624
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 112097897,
                            "duration": 7533
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 112166851,
                            "duration": 6255
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 112108826,
                            "duration": 113882
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112209760,
                            "duration": 55967
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112221161,
                            "duration": 52599
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 80133400,
                            "duration": 32158736
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 82425354,
                            "duration": 29867644
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 112328820,
                            "duration": 6735
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 112325834,
                            "duration": 6041
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 112438251,
                            "duration": 6811
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112415948,
                            "duration": 113265
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 112540188,
                            "duration": 4635
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 112567053,
                            "duration": 8560
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 61941938,
                            "duration": 50699514
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 72156922,
                            "duration": 40511926
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112563585,
                            "duration": 9091
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 112754181,
                            "duration": 7198
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 79191779,
                            "duration": 33639992
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112853267,
                            "duration": 7768
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 112681802,
                            "duration": 181815
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112764843,
                            "duration": 125442
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 112954873,
                            "duration": 5972
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 47629582,
                            "duration": 65418652
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 112957272,
                            "duration": 91757
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 112981247,
                            "duration": 70155
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 113137261,
                            "duration": 7878
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 70959708,
                            "duration": 42234380
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 60763719,
                            "duration": 52453406
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 113251424,
                            "duration": 55499
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 113226323,
                            "duration": 8052
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 113366765,
                            "duration": 7005
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 113453031,
                            "duration": 7362
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 113472522,
                            "duration": 6802
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 78342904,
                            "duration": 35077852
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 113423603,
                            "duration": 120415
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 113647909,
                            "duration": 102480
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 113728213,
                            "duration": 35630
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 113677723,
                            "duration": 96216
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 69969241,
                            "duration": 43919341
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 113886243,
                            "duration": 10545
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 113921054,
                            "duration": 7489
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 113982999,
                            "duration": 6772
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 113964741,
                            "duration": 58682
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114021491,
                            "duration": 6546
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 114095661,
                            "duration": 7008
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 59443828,
                            "duration": 54672300
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 77745711,
                            "duration": 36399040
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 114193650,
                            "duration": 6439
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 114210457,
                            "duration": 52875
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 57835382,
                            "duration": 56437639
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114272890,
                            "duration": 51019
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 114376840,
                            "duration": 3955
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114387039,
                            "duration": 9045
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114299402,
                            "duration": 115694
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 114491650,
                            "duration": 6498
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 114474478,
                            "duration": 4277
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 56611265,
                            "duration": 57975413
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 114486017,
                            "duration": 102831
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 58136616,
                            "duration": 56464255
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 114679072,
                            "duration": 8127
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 48810268,
                            "duration": 65954600
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114760007,
                            "duration": 6883
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 114777726,
                            "duration": 3045
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 73589065,
                            "duration": 41207747
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 77044124,
                            "duration": 37791382
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114851094,
                            "duration": 3815
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 115003642,
                            "duration": 3877
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 114999817,
                            "duration": 9442
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115030555,
                            "duration": 7526
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115147232,
                            "duration": 7310
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115058479,
                            "duration": 99206
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 115111260,
                            "duration": 49404
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115161751,
                            "duration": 7805
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 83269461,
                            "duration": 31948670
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115242958,
                            "duration": 4013
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 115253943,
                            "duration": 3197
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 115263572,
                            "duration": 3505
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 82591132,
                            "duration": 32687627
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 60443550,
                            "duration": 54836714
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115278459,
                            "duration": 9596
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115294864,
                            "duration": 3393
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 115304681,
                            "duration": 3177
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 115313735,
                            "duration": 2961
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 81858572,
                            "duration": 33467137
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115341159,
                            "duration": 3040
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 115351085,
                            "duration": 3338
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 115276972,
                            "duration": 7390
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 76094218,
                            "duration": 39261937
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 115473473,
                            "duration": 4558
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115551810,
                            "duration": 6854
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 81013270,
                            "duration": 34572839
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115468653,
                            "duration": 128595
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 115634595,
                            "duration": 6356
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115567545,
                            "duration": 2951
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 75212316,
                            "duration": 40612974
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115717684,
                            "duration": 5585
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115859214,
                            "duration": 8673
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115876582,
                            "duration": 3581
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 74561534,
                            "duration": 41330230
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115896074,
                            "duration": 4556
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 76743167,
                            "duration": 39166147
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115915535,
                            "duration": 6791
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115934279,
                            "duration": 3695
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 73902924,
                            "duration": 42046412
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115830214,
                            "duration": 119494
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 115967164,
                            "duration": 4172
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 115978254,
                            "duration": 2707
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 73106814,
                            "duration": 42882793
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116004539,
                            "duration": 3721
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 116006623,
                            "duration": 7052
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 116015991,
                            "duration": 5482
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 116021337,
                            "duration": 5014
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "municipio"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Municipio!",
                            "fieldName": "municipio",
                            "startOffset": 72459808,
                            "duration": 43576545
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 115951970,
                            "duration": 3937
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "municipio",
                                "id"
                            ],
                            "parentType": "Municipio",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116059201,
                            "duration": 5635
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "municipio",
                                "nome"
                            ],
                            "parentType": "Municipio",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 116073460,
                            "duration": 2949
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 116095409,
                            "duration": 52692
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116159938,
                            "duration": 7942
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 116162120,
                            "duration": 6911
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 50023983,
                            "duration": 66188142
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 80011934,
                            "duration": 36268365
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 116226951,
                            "duration": 112967
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "cbo"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "Cbo!",
                            "fieldName": "cbo",
                            "startOffset": 62665102,
                            "duration": 53732670
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "cbo",
                                "id"
                            ],
                            "parentType": "Cbo",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116506718,
                            "duration": 4951
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116379243,
                            "duration": 139450
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116440640,
                            "duration": 103212
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 116573035,
                            "duration": 6641
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "cbo",
                                "nome"
                            ],
                            "parentType": "Cbo",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 116662404,
                            "duration": 4437
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 116685141,
                            "duration": 6810
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 116595494,
                            "duration": 3842
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 116750851,
                            "duration": 5080
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 79136600,
                            "duration": 37727510
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 116873596,
                            "duration": 51346
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 50343976,
                            "duration": 66643716
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 116968304,
                            "duration": 47447
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117154854,
                            "duration": 67675
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117137462,
                            "duration": 3690
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117294785,
                            "duration": 5889
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 78289755,
                            "duration": 39022949
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 117277960,
                            "duration": 6724
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117330288,
                            "duration": 3857
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117341505,
                            "duration": 2552
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117350422,
                            "duration": 3038
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 77691991,
                            "duration": 39670041
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117376202,
                            "duration": 3269
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117385766,
                            "duration": 2537
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117394444,
                            "duration": 2905
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 76989384,
                            "duration": 40416695
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117420306,
                            "duration": 3263
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117429806,
                            "duration": 2441
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117438175,
                            "duration": 3897
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 117435969,
                            "duration": 7770
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 75974866,
                            "duration": 41475959
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117465303,
                            "duration": 2887
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117475067,
                            "duration": 2514
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117483405,
                            "duration": 3325
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 75158938,
                            "duration": 42336584
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117510129,
                            "duration": 2900
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117519961,
                            "duration": 2460
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117528286,
                            "duration": 3237
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 74501283,
                            "duration": 43038797
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117554132,
                            "duration": 3401
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117564964,
                            "duration": 2974
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117573799,
                            "duration": 3512
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 73788819,
                            "duration": 43797041
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117599697,
                            "duration": 3037
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 117560858,
                            "duration": 5859
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117609812,
                            "duration": 2586
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117618937,
                            "duration": 3020
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 73048394,
                            "duration": 44582800
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117645005,
                            "duration": 2935
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117654961,
                            "duration": 2508
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117663355,
                            "duration": 3124
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 50645375,
                            "duration": 67029281
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "unidadeSaude"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "UnidadeSaude!",
                            "fieldName": "unidadeSaude",
                            "startOffset": 72401066,
                            "duration": 45276292
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "unidadeSaude",
                                "id"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117692010,
                            "duration": 2981
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "unidadeSaude",
                                "nome"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String",
                            "fieldName": "nome",
                            "startOffset": 117701884,
                            "duration": 2469
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "unidadeSaude",
                                "cnes"
                            ],
                            "parentType": "UnidadeSaude",
                            "returnType": "String!",
                            "fieldName": "cnes",
                            "startOffset": 117710232,
                            "duration": 3015
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 117790089,
                            "duration": 118876
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 117964438,
                            "duration": 6046
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 118121513,
                            "duration": 6358
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 118241329,
                            "duration": 5234
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 118504166,
                            "duration": 7372
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 118520411,
                            "duration": 4330
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 118531225,
                            "duration": 4094
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 118554759,
                            "duration": 4288
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 51996513,
                            "duration": 66579830
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 118597830,
                            "duration": 5653
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 118611139,
                            "duration": 4792
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 118622586,
                            "duration": 4181
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 118645476,
                            "duration": 4199
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 53238080,
                            "duration": 65426325
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 118683078,
                            "duration": 5313
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 118695638,
                            "duration": 4576
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 118706770,
                            "duration": 4157
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 118729644,
                            "duration": 4299
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 54465721,
                            "duration": 64283058
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 118766853,
                            "duration": 5321
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 118779498,
                            "duration": 4779
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 118790839,
                            "duration": 4190
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 118813713,
                            "duration": 4206
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 55707964,
                            "duration": 63123958
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 118850238,
                            "duration": 5385
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 118862897,
                            "duration": 4872
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 118874325,
                            "duration": 4156
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119113265,
                            "duration": 6454
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 57056645,
                            "duration": 62178133
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119304313,
                            "duration": 7066
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119319340,
                            "duration": 4936
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119331059,
                            "duration": 4374
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119354894,
                            "duration": 4685
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 58441077,
                            "duration": 60933906
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119394036,
                            "duration": 5458
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119406904,
                            "duration": 4346
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119418201,
                            "duration": 4312
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119441512,
                            "duration": 4573
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119460518,
                            "duration": 4696
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119473201,
                            "duration": 4263
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119484131,
                            "duration": 4584
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119509356,
                            "duration": 4199
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 59811770,
                            "duration": 59716906
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119546461,
                            "duration": 5617
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119559823,
                            "duration": 4298
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119570733,
                            "duration": 4552
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119593497,
                            "duration": 4116
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119612096,
                            "duration": 4592
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119623676,
                            "duration": 4650
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119634811,
                            "duration": 4072
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119657588,
                            "duration": 4710
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 61110873,
                            "duration": 58565748
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119695483,
                            "duration": 5361
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119708094,
                            "duration": 4774
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119719608,
                            "duration": 4278
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119741808,
                            "duration": 4555
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 62004592,
                            "duration": 57755988
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119779035,
                            "duration": 5216
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119791486,
                            "duration": 4401
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119802928,
                            "duration": 4195
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119825017,
                            "duration": 4491
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119843621,
                            "duration": 4557
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119855685,
                            "duration": 4258
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119866211,
                            "duration": 4532
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 119888046,
                            "duration": 4226
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 62274119,
                            "duration": 57649707
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 119944875,
                            "duration": 6417
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 119960371,
                            "duration": 5077
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 119973189,
                            "duration": 5400
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120000037,
                            "duration": 5014
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120022212,
                            "duration": 5561
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120035773,
                            "duration": 5335
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120048635,
                            "duration": 5061
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120074115,
                            "duration": 5559
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 62525254,
                            "duration": 57571094
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120118194,
                            "duration": 6360
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120133144,
                            "duration": 5499
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120146598,
                            "duration": 5106
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120172951,
                            "duration": 5398
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120194974,
                            "duration": 5554
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120209279,
                            "duration": 4941
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120221918,
                            "duration": 5219
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120247758,
                            "duration": 4946
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 62791571,
                            "duration": 57478349
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120290787,
                            "duration": 6166
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120306166,
                            "duration": 4986
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120318860,
                            "duration": 5458
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120345449,
                            "duration": 4933
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 63060021,
                            "duration": 57307345
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120387929,
                            "duration": 6384
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120403464,
                            "duration": 5335
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120416618,
                            "duration": 5469
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120443411,
                            "duration": 4932
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120466174,
                            "duration": 5446
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120479757,
                            "duration": 5595
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120493307,
                            "duration": 5074
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120518956,
                            "duration": 5680
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 63463313,
                            "duration": 57077790
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120562693,
                            "duration": 6325
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120577402,
                            "duration": 4899
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120590452,
                            "duration": 4875
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120616448,
                            "duration": 5395
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120638468,
                            "duration": 5452
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120652537,
                            "duration": 4987
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120665048,
                            "duration": 5195
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120690860,
                            "duration": 5105
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 64854217,
                            "duration": 55859135
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120734435,
                            "duration": 6619
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120750539,
                            "duration": 5141
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120763315,
                            "duration": 5392
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120790032,
                            "duration": 5188
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 66120115,
                            "duration": 54692763
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120855529,
                            "duration": 7615
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120873157,
                            "duration": 5236
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120886444,
                            "duration": 5566
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120913637,
                            "duration": 5157
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 120936660,
                            "duration": 5535
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 120950206,
                            "duration": 5055
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 120963478,
                            "duration": 4937
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 120988752,
                            "duration": 5423
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 67487934,
                            "duration": 53524126
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121035888,
                            "duration": 7155
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121052402,
                            "duration": 5250
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121066077,
                            "duration": 4976
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121092518,
                            "duration": 5325
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121115139,
                            "duration": 5469
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121129370,
                            "duration": 4942
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121141822,
                            "duration": 5236
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121196656,
                            "duration": 5938
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 69354821,
                            "duration": 51868141
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121254610,
                            "duration": 7292
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121272008,
                            "duration": 5115
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121285266,
                            "duration": 5477
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121316507,
                            "duration": 5616
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121340884,
                            "duration": 5664
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121354792,
                            "duration": 5520
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121368999,
                            "duration": 5045
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121395658,
                            "duration": 5829
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 70342610,
                            "duration": 51082155
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121448973,
                            "duration": 7128
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121464985,
                            "duration": 5109
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121478733,
                            "duration": 4982
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121508204,
                            "duration": 5603
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 71481542,
                            "duration": 50050462
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121554160,
                            "duration": 6948
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121570028,
                            "duration": 5052
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121583327,
                            "duration": 4942
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121609156,
                            "duration": 5375
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121631936,
                            "duration": 5632
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121646391,
                            "duration": 5023
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121659520,
                            "duration": 5776
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121686837,
                            "duration": 5312
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 72521910,
                            "duration": 49188898
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121744546,
                            "duration": 7002
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121761268,
                            "duration": 12942
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121783079,
                            "duration": 5998
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121811497,
                            "duration": 5197
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121836048,
                            "duration": 5649
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121850246,
                            "duration": 4894
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121864030,
                            "duration": 5032
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121890136,
                            "duration": 5444
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 73182358,
                            "duration": 48732082
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 121936460,
                            "duration": 7488
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 121952608,
                            "duration": 5037
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 121966252,
                            "duration": 4943
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 121994694,
                            "duration": 6124
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122018881,
                            "duration": 5817
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122033565,
                            "duration": 5083
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122046768,
                            "duration": 5572
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122072735,
                            "duration": 5251
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 73965223,
                            "duration": 48130517
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122116687,
                            "duration": 6383
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122132235,
                            "duration": 5048
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122145068,
                            "duration": 5112
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122171382,
                            "duration": 5013
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 74624997,
                            "duration": 47568355
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122235652,
                            "duration": 7710
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122253360,
                            "duration": 5263
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122266416,
                            "duration": 5036
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122294154,
                            "duration": 5056
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122317157,
                            "duration": 6212
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122331669,
                            "duration": 4975
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122345146,
                            "duration": 5056
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122370395,
                            "duration": 5340
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 75269085,
                            "duration": 47124261
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122413635,
                            "duration": 6911
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122428637,
                            "duration": 5128
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122441936,
                            "duration": 4809
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122467684,
                            "duration": 5118
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122491253,
                            "duration": 5492
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122505919,
                            "duration": 5350
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122519060,
                            "duration": 4977
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122545004,
                            "duration": 5119
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 76217547,
                            "duration": 46349744
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122588669,
                            "duration": 174864
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122787560,
                            "duration": 11671
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122809846,
                            "duration": 7014
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122849771,
                            "duration": 5648
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 122886349,
                            "duration": 6966
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 122902211,
                            "duration": 5070
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 122916231,
                            "duration": 5027
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 122944060,
                            "duration": 5394
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 77100741,
                            "duration": 45880696
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123011696,
                            "duration": 8908
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123030328,
                            "duration": 5014
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123043760,
                            "duration": 5117
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123075759,
                            "duration": 5110
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 77801909,
                            "duration": 45299035
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123124448,
                            "duration": 7246
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123140419,
                            "duration": 5075
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123153857,
                            "duration": 4892
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123182175,
                            "duration": 5158
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123205963,
                            "duration": 5595
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123220140,
                            "duration": 5913
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123233719,
                            "duration": 4854
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123259708,
                            "duration": 4852
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 78397950,
                            "duration": 44884287
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123304178,
                            "duration": 6163
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123318852,
                            "duration": 5475
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123331782,
                            "duration": 5228
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123359245,
                            "duration": 5085
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123381994,
                            "duration": 5986
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123396482,
                            "duration": 4955
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123409539,
                            "duration": 4795
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123435473,
                            "duration": 5025
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 79247446,
                            "duration": 44210087
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123478457,
                            "duration": 20815
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123509229,
                            "duration": 12708
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123531327,
                            "duration": 5380
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123558483,
                            "duration": 5040
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 80247952,
                            "duration": 43334483
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123604392,
                            "duration": 21821
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123637135,
                            "duration": 5684
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123650911,
                            "duration": 11293
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123687877,
                            "duration": 8834
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123717059,
                            "duration": 6104
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123731511,
                            "duration": 5560
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123748819,
                            "duration": 5439
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123776327,
                            "duration": 5047
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 81123813,
                            "duration": 42675239
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123822135,
                            "duration": 6478
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123837272,
                            "duration": 5214
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123850369,
                            "duration": 5088
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123877490,
                            "duration": 4967
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123900186,
                            "duration": 6037
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 123914475,
                            "duration": 4694
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 123927178,
                            "duration": 4879
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 123953254,
                            "duration": 4932
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 81974644,
                            "duration": 42000267
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 123996863,
                            "duration": 89702
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 124099702,
                            "duration": 7186
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 124115077,
                            "duration": 6069
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 124145617,
                            "duration": 5394
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 124171473,
                            "duration": 5260
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 124185065,
                            "duration": 5522
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 124198428,
                            "duration": 5277
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 124225673,
                            "duration": 4974
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 82702827,
                            "duration": 41546336
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 124272765,
                            "duration": 6493
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 124288280,
                            "duration": 5933
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 124301996,
                            "duration": 5487
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 124329455,
                            "duration": 5531
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis"
                            ],
                            "parentType": "Lotacao",
                            "returnType": "[Perfil]",
                            "fieldName": "perfis",
                            "startOffset": 83432490,
                            "duration": 40919488
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                0,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 124373257,
                            "duration": 5802
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                0,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 124387543,
                            "duration": 5715
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                0,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 124401361,
                            "duration": 4996
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                0,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 124427230,
                            "duration": 5390
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                1,
                                "id"
                            ],
                            "parentType": "Perfil",
                            "returnType": "ID!",
                            "fieldName": "id",
                            "startOffset": 124449877,
                            "duration": 5218
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                1,
                                "nome"
                            ],
                            "parentType": "Perfil",
                            "returnType": "String!",
                            "fieldName": "nome",
                            "startOffset": 124463752,
                            "duration": 5123
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                1,
                                "ativo"
                            ],
                            "parentType": "Perfil",
                            "returnType": "Boolean!",
                            "fieldName": "ativo",
                            "startOffset": 124476769,
                            "duration": 5491
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                1,
                                "tipoPerfil"
                            ],
                            "parentType": "Perfil",
                            "returnType": "TipoAcesso!",
                            "fieldName": "tipoPerfil",
                            "startOffset": 124502139,
                            "duration": 5132
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                0,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 111111250,
                            "duration": 26992119
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 124490095,
                            "duration": 13805769
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 124129650,
                            "duration": 14193475
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123940394,
                            "duration": 14394933
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123763327,
                            "duration": 14582011
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123422633,
                            "duration": 14933317
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123247058,
                            "duration": 15119076
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122929771,
                            "duration": 15446683
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122532694,
                            "duration": 15854862
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122358204,
                            "duration": 16039527
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122060482,
                            "duration": 16347377
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121877728,
                            "duration": 16540483
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121673469,
                            "duration": 16754817
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121299252,
                            "duration": 17138569
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121155215,
                            "duration": 17292324
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120976468,
                            "duration": 17480782
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120678344,
                            "duration": 17788794
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120506868,
                            "duration": 17970602
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120235126,
                            "duration": 18251919
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120062030,
                            "duration": 18434966
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119877591,
                            "duration": 18629717
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119646287,
                            "duration": 18870684
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119495444,
                            "duration": 19031502
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 118542560,
                            "duration": 20002076
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 115520696,
                            "duration": 23035065
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 114370797,
                            "duration": 24194892
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 112029387,
                            "duration": 26561926
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                1,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 112553038,
                            "duration": 26061862
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                2,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 113533003,
                            "duration": 25128809
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                3,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 116033714,
                            "duration": 22673470
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                4,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 116747772,
                            "duration": 22012749
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                8,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 118718478,
                            "duration": 20095784
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                5,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 117498520,
                            "duration": 21385480
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                35,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123346038,
                            "duration": 15561697
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                20,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120603316,
                            "duration": 18337417
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                6,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 118180729,
                            "duration": 20792091
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                7,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 118634277,
                            "duration": 20369242
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                9,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 118802650,
                            "duration": 20246343
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                10,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119052474,
                            "duration": 20023039
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                40,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 124316508,
                            "duration": 14782427
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                25,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121494721,
                            "duration": 17626565
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                11,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119342435,
                            "duration": 19804685
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                41,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 124414311,
                            "duration": 14755886
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                27,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121798002,
                            "duration": 17414156
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                26,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121596337,
                            "duration": 17655019
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                12,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119429349,
                            "duration": 19861377
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                28,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121979462,
                            "duration": 17351309
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                13,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119582504,
                            "duration": 19778496
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                29,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122158760,
                            "duration": 17232422
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                14,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119730733,
                            "duration": 19677727
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                30,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122280444,
                            "duration": 17144601
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                15,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119814206,
                            "duration": 19657753
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                31,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122454813,
                            "duration": 17064086
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                16,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 119986656,
                            "duration": 19562440
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                32,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 122827490,
                            "duration": 16750771
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                17,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120160160,
                            "duration": 19524167
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                33,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123057407,
                            "duration": 16664762
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                18,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120332503,
                            "duration": 19412069
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                37,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123671546,
                            "duration": 16094902
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                34,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123167119,
                            "duration": 16668457
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                22,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120900123,
                            "duration": 18979617
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                19,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120430162,
                            "duration": 19488006
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                36,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123545102,
                            "duration": 16411393
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                21,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 120776777,
                            "duration": 19253454
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                38,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 123864261,
                            "duration": 16234821
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                23,
                                "perfis",
                                0,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121079352,
                            "duration": 19057051
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                39,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 124212738,
                            "duration": 15958525
                        },
                        {
                            "path": [
                                "sessao",
                                "profissional",
                                "lotacoes",
                                24,
                                "perfis",
                                1,
                                "recursos"
                            ],
                            "parentType": "Perfil",
                            "returnType": "[String]!",
                            "fieldName": "recursos",
                            "startOffset": 121382372,
                            "duration": 18830505
                        }
                    ]
                }
            }
        },
        "data": {
            "sessao": {
                "id": "9c212a60-de5d-43f6-b40e-df97f7c49203",
                "recursos": [],
                "profissional": {
                    "id": "314",
                    "cpf": "10288507860",
                    "cns": "138530625640003",
                    "nome": "Usuario Paineis Fiocruz",
                    "acessos": [
                        {
                            "id": "14507",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14493",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14444",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14463",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14447",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14481",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14491",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14500",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14453",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14445",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14451",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14487",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "15202",
                            "tipo": "GESTOR_ESTADUAL"
                        },
                        {
                            "id": "14489",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14449",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14508",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14471",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14497",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14503",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14499",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14450",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14448",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14477",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14495",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14483",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14457",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14485",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14504",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14461",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "15201",
                            "tipo": "GESTOR_MUNICIPAL"
                        },
                        {
                            "id": "14446",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14443",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14502",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14501",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14469",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14506",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14455",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14465",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14479",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14505",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14459",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14475",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14467",
                            "tipo": "LOTACAO"
                        },
                        {
                            "id": "14473",
                            "tipo": "LOTACAO"
                        }
                    ],
                    "usuario": {
                        "id": "314",
                        "bloqueado": False
                    },
                    "lotacoes": [
                        {
                            "id": "14508",
                            "ativo": True,
                            "cbo": {
                                "id": "112",
                                "nome": "GERENTE DE SERVIÇOS DE SAÚDE"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "5",
                                "nome": "Ceo",
                                "cnes": "5444433"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "49",
                                    "nome": "COORDENADOR DO CEO",
                                    "ativo": True,
                                    "recursos": [
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Unificação de bases",
                                        "Gestão de cadastros de cidadão/Unificação de cadastros",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Inativar",
                                        "Relatórios",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Absenteísmo/Todos os profissionais",
                                        "Relatórios/Gerenciais/Absenteísmo/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Resumo de produção/Todos os profissionais",
                                        "Relatórios/Produção/Resumo de produção/Todos os profissionais/Categoria profissional",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Agendar/Todas as equipes",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Cancelar/Todas as equipes",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar perfis",
                                        "Visualizar profissionais",
                                        "Visualizar profissionais/Cadastrar, editar e excluir",
                                        "Visualizar profissionais/Redefinir senha",
                                        "Visualizar profissionais/Visualizar acessos",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda online",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda online/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda/Todas as unidades",
                                        "Visualizar unidades de saúde",
                                        "Visualizar unidades de saúde/Ativar ou inativar tipo de serviço",
                                        "Visualizar unidades de saúde/Ativar ou inativar tipo de serviço/Todas as unidades",
                                        "Visualizar unidades de saúde/Configurar consulta no Hórus",
                                        "Visualizar unidades de saúde/Configurar consulta no Hórus/Todas as unidades"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14507",
                            "ativo": True,
                            "cbo": {
                                "id": "958",
                                "nome": "TÉCNICO EM SAÚDE BUCAL"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "5",
                                "nome": "Ceo",
                                "cnes": "5444433"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "50",
                                    "nome": "TSB CEO - TÉCNICO DE SAÚDE BUCAL CEO",
                                    "ativo": True,
                                    "recursos": [
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14506",
                            "ativo": True,
                            "cbo": {
                                "id": "960",
                                "nome": "AUXILIAR EM SAÚDE BUCAL"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "5",
                                "nome": "Ceo",
                                "cnes": "5444433"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "47",
                                    "nome": "ASB CEO - AUXILIAR DE SAÚDE BUCAL CEO",
                                    "ativo": True,
                                    "recursos": [
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14505",
                            "ativo": True,
                            "cbo": {
                                "id": "364",
                                "nome": "CIRURGIÃO DENTISTA - CLÍNICO GERAL"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "5",
                                "nome": "Ceo",
                                "cnes": "5444433"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "48",
                                    "nome": "CIRURGIÃO DENTISTA CEO",
                                    "ativo": True,
                                    "recursos": [
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Agendar/Todas as equipes",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Cancelar/Todas as equipes",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14504",
                            "ativo": True,
                            "cbo": {
                                "id": "411",
                                "nome": "TÉCNICO EM ORIENTAÇÃO E MOBILIDADE DE CEGOS E DEFICIENTES VISUAIS"
                            },
                            "equipe": {
                                "id": "14",
                                "nome": "EMAD2"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "40",
                                    "nome": "OUTRO PROF. NÍVEL MÉDIO/TÉCNICO AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14503",
                            "ativo": True,
                            "cbo": {
                                "id": "412",
                                "nome": "FISIOTERAPEUTA GERAL"
                            },
                            "equipe": {
                                "id": "15",
                                "nome": "EMAP"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "42",
                                    "nome": "OUTRO PROF. NÍVEL SUPERIOR AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14502",
                            "ativo": True,
                            "cbo": {
                                "id": "1341",
                                "nome": "AGENTE COMUNITÁRIO DE SAÚDE"
                            },
                            "equipe": {
                                "id": "15",
                                "nome": "EMAP"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "25",
                                    "nome": "ACS - AGENTE COMUNITÁRIO DE SAÚDE",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Território",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de visita domiciliar",
                                        "CDS/Ficha de visita domiciliar/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14501",
                            "ativo": True,
                            "cbo": {
                                "id": "112",
                                "nome": "GERENTE DE SERVIÇOS DE SAÚDE"
                            },
                            "equipe": {
                                "id": "15",
                                "nome": "EMAP"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "30",
                                    "nome": "COORDENADOR AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe/Gerar relatório de AD do município",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Visualizar agenda de AD do município",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Visualizar agenda de AD do município/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Visualizar agenda de AD do município/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Visualizar lista de AD do município",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Visualizar lista de AD do município/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Visualizar lista de AD do município/Excluir",
                                        "Configurar atenção domiciliar",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Inativar",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial/Todas as equipes",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial/Todos os profissionais",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Cadastro individual/Todas as equipes",
                                        "Relatórios/Consolidados/Cadastro individual/Todos os profissionais",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Consolidados/Situação do território/Todas as equipes",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento domiciliar/Todas as equipes",
                                        "Relatórios/Produção/Atendimento domiciliar/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento domiciliar/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todas as equipes",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todos os profissionais",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todos os profissionais/Categoria profissional",
                                        "Visualizar perfis",
                                        "Visualizar profissionais",
                                        "Visualizar profissionais/Cadastrar, editar e excluir",
                                        "Visualizar profissionais/Redefinir senha",
                                        "Visualizar profissionais/Visualizar acessos",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda/Todas as unidades"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14500",
                            "ativo": True,
                            "cbo": {
                                "id": "678",
                                "nome": "PSICÓLOGO CLÍNICO"
                            },
                            "equipe": {
                                "id": "14",
                                "nome": "EMAD2"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "42",
                                    "nome": "OUTRO PROF. NÍVEL SUPERIOR AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14499",
                            "ativo": True,
                            "cbo": {
                                "id": "947",
                                "nome": "TÉCNICO DE ENFERMAGEM"
                            },
                            "equipe": {
                                "id": "14",
                                "nome": "EMAD2"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "27",
                                    "nome": "AUXILIAR OU TÉCNICO DE ENFERMAGEM AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14497",
                            "ativo": True,
                            "cbo": {
                                "id": "397",
                                "nome": "ENFERMEIRO"
                            },
                            "equipe": {
                                "id": "13",
                                "nome": "EMAD1"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "33",
                                    "nome": "ENFERMEIRO AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14495",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": {
                                "id": "13",
                                "nome": "EMAD1"
                            },
                            "unidadeSaude": {
                                "id": "4",
                                "nome": "Unidade de Atendimento AD",
                                "cnes": "5444428"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "38",
                                    "nome": "MÉDICO AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14493",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": {
                                "id": "12",
                                "nome": "NASF I"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "39",
                                    "nome": "MÉDICO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14491",
                            "ativo": True,
                            "cbo": {
                                "id": "411",
                                "nome": "TÉCNICO EM ORIENTAÇÃO E MOBILIDADE DE CEGOS E DEFICIENTES VISUAIS"
                            },
                            "equipe": {
                                "id": "10",
                                "nome": "EAB2"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "41",
                                    "nome": "OUTRO PROF. NÍVEL MÉDIO/TÉCNICO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14489",
                            "ativo": True,
                            "cbo": {
                                "id": "1262",
                                "nome": "RECEPCIONISTA DE CONSULTÓRIO MÉDICO OU DENTÁRIO"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "45",
                                    "nome": "RECEPÇÃO",
                                    "ativo": True,
                                    "recursos": [
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Agendar/Todas as equipes",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Cancelar/Todas as equipes",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14487",
                            "ativo": True,
                            "cbo": {
                                "id": "958",
                                "nome": "TÉCNICO EM SAÚDE BUCAL"
                            },
                            "equipe": {
                                "id": "9",
                                "nome": "ESB M2 ESUS"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "46",
                                    "nome": "TSB - TÉCNICO DE SAÚDE BUCAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14485",
                            "ativo": True,
                            "cbo": {
                                "id": "960",
                                "nome": "AUXILIAR EM SAÚDE BUCAL"
                            },
                            "equipe": {
                                "id": "9",
                                "nome": "ESB M2 ESUS"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "26",
                                    "nome": "ASB - AUXILIAR DE SAÚDE BUCAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14483",
                            "ativo": True,
                            "cbo": {
                                "id": "364",
                                "nome": "CIRURGIÃO DENTISTA - CLÍNICO GERAL"
                            },
                            "equipe": {
                                "id": "9",
                                "nome": "ESB M2 ESUS"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "29",
                                    "nome": "CIRURGIÃO DENTISTA",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14481",
                            "ativo": True,
                            "cbo": {
                                "id": "1218",
                                "nome": "DIGITADOR"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "32",
                                    "nome": "DIGITADOR",
                                    "ativo": True,
                                    "recursos": [
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "CDS/Ficha de visita domiciliar",
                                        "CDS/Ficha de visita domiciliar/Cadastrar, editar e excluir"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14479",
                            "ativo": True,
                            "cbo": {
                                "id": "412",
                                "nome": "FISIOTERAPEUTA GERAL"
                            },
                            "equipe": {
                                "id": "10",
                                "nome": "EAB2"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "43",
                                    "nome": "OUTRO PROF. NÍVEL SUPERIOR",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14477",
                            "ativo": True,
                            "cbo": {
                                "id": "1341",
                                "nome": "AGENTE COMUNITÁRIO DE SAÚDE"
                            },
                            "equipe": {
                                "id": "8",
                                "nome": "EACS"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "25",
                                    "nome": "ACS - AGENTE COMUNITÁRIO DE SAÚDE",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Território",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de visita domiciliar",
                                        "CDS/Ficha de visita domiciliar/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14475",
                            "ativo": True,
                            "cbo": {
                                "id": "112",
                                "nome": "GERENTE DE SERVIÇOS DE SAÚDE"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "31",
                                    "nome": "COORDENADOR DA UBS",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Cidadãos vinculados/Todas as equipes",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Acompanhamentos/Condições de saúde/Todas as equipes",
                                        "Busca ativa de vacinação",
                                        "Busca ativa de vacinação/Todas as equipes",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Reterritorialização",
                                        "Gestão de cadastros de cidadão/Unificação de bases",
                                        "Gestão de cadastros de cidadão/Unificação de cadastros",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Inativar",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial/Todas as equipes",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial/Todos os profissionais",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Cadastro individual/Todas as equipes",
                                        "Relatórios/Consolidados/Cadastro individual/Todos os profissionais",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Consolidados/Situação do território/Todas as equipes",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Absenteísmo/CBO",
                                        "Relatórios/Gerenciais/Absenteísmo/Todas as equipes",
                                        "Relatórios/Gerenciais/Absenteísmo/Todos os profissionais",
                                        "Relatórios/Gerenciais/Absenteísmo/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Atendimentos/CBO",
                                        "Relatórios/Gerenciais/Atendimentos/Todas as equipes",
                                        "Relatórios/Gerenciais/Atendimentos/Todos os profissionais",
                                        "Relatórios/Gerenciais/Atendimentos/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Gerenciais/Vacinação/CBO",
                                        "Relatórios/Gerenciais/Vacinação/Todas as equipes",
                                        "Relatórios/Gerenciais/Vacinação/Todos os profissionais",
                                        "Relatórios/Gerenciais/Vacinação/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Cadastro do território/Todas as equipes",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Criança/Todas as equipes",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Gestante/Todas as equipes",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Operacional/Risco cardiovascular/Todas as equipes",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento domiciliar/Todas as equipes",
                                        "Relatórios/Produção/Atendimento domiciliar/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento domiciliar/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento individual/Todas as equipes",
                                        "Relatórios/Produção/Atendimento individual/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento individual/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todas as equipes",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Atividade coletiva/Todas as equipes",
                                        "Relatórios/Produção/Atividade coletiva/Todos os profissionais",
                                        "Relatórios/Produção/Atividade coletiva/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todas as equipes",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todos os profissionais",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Marcadores de consumo alimentar/Todas as equipes",
                                        "Relatórios/Produção/Marcadores de consumo alimentar/Todos os profissionais",
                                        "Relatórios/Produção/Marcadores de consumo alimentar/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Procedimentos consolidados/Todas as equipes",
                                        "Relatórios/Produção/Procedimentos consolidados/Todos os profissionais",
                                        "Relatórios/Produção/Procedimentos consolidados/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Procedimentos/Todas as equipes",
                                        "Relatórios/Produção/Procedimentos/Todos os profissionais",
                                        "Relatórios/Produção/Procedimentos/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Resumo de produção/Todas as equipes",
                                        "Relatórios/Produção/Resumo de produção/Todos os profissionais",
                                        "Relatórios/Produção/Resumo de produção/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia/Todas as equipes",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia/Todos os profissionais",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Vacinação/Todas as equipes",
                                        "Relatórios/Produção/Vacinação/Todos os profissionais",
                                        "Relatórios/Produção/Vacinação/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Relatórios/Produção/Visita domiciliar/Todas as equipes",
                                        "Relatórios/Produção/Visita domiciliar/Todos os profissionais",
                                        "Relatórios/Produção/Visita domiciliar/Todos os profissionais/Categoria profissional",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Agendar/Todas as equipes",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Cancelar/Todas as equipes",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar perfis",
                                        "Visualizar profissionais",
                                        "Visualizar profissionais/Cadastrar, editar e excluir",
                                        "Visualizar profissionais/Redefinir senha",
                                        "Visualizar profissionais/Visualizar acessos",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda online",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda online/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda/Todas as unidades",
                                        "Visualizar unidades de saúde",
                                        "Visualizar unidades de saúde/Ativar ou inativar tipo de serviço",
                                        "Visualizar unidades de saúde/Ativar ou inativar tipo de serviço/Todas as unidades",
                                        "Visualizar unidades de saúde/Configurar consulta no Hórus",
                                        "Visualizar unidades de saúde/Configurar consulta no Hórus/Todas as unidades"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14473",
                            "ativo": True,
                            "cbo": {
                                "id": "678",
                                "nome": "PSICÓLOGO CLÍNICO"
                            },
                            "equipe": {
                                "id": "10",
                                "nome": "EAB2"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "43",
                                    "nome": "OUTRO PROF. NÍVEL SUPERIOR",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14471",
                            "ativo": True,
                            "cbo": {
                                "id": "947",
                                "nome": "TÉCNICO DE ENFERMAGEM"
                            },
                            "equipe": {
                                "id": "10",
                                "nome": "EAB2"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "28",
                                    "nome": "AUXILIAR OU TÉCNICO DE ENFERMAGEM",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14469",
                            "ativo": True,
                            "cbo": {
                                "id": "397",
                                "nome": "ENFERMEIRO"
                            },
                            "equipe": {
                                "id": "10",
                                "nome": "EAB2"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "34",
                                    "nome": "ENFERMEIRO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14467",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": {
                                "id": "11",
                                "nome": "EMAD2"
                            },
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "38",
                                    "nome": "MÉDICO AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14465",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "3",
                                "nome": "Unidade Basica de Saude Agronomica",
                                "cnes": "5444430"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "39",
                                    "nome": "MÉDICO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14463",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": {
                                "id": "6",
                                "nome": "NASF I"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "39",
                                    "nome": "MÉDICO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14461",
                            "ativo": True,
                            "cbo": {
                                "id": "411",
                                "nome": "TÉCNICO EM ORIENTAÇÃO E MOBILIDADE DE CEGOS E DEFICIENTES VISUAIS"
                            },
                            "equipe": {
                                "id": "4",
                                "nome": "EAB1"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "41",
                                    "nome": "OUTRO PROF. NÍVEL MÉDIO/TÉCNICO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14459",
                            "ativo": True,
                            "cbo": {
                                "id": "1262",
                                "nome": "RECEPCIONISTA DE CONSULTÓRIO MÉDICO OU DENTÁRIO"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "45",
                                    "nome": "RECEPÇÃO",
                                    "ativo": True,
                                    "recursos": [
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Agendar/Todas as equipes",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Cancelar/Todas as equipes",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14457",
                            "ativo": True,
                            "cbo": {
                                "id": "958",
                                "nome": "TÉCNICO EM SAÚDE BUCAL"
                            },
                            "equipe": {
                                "id": "3",
                                "nome": "ESB M1 ESUS"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "46",
                                    "nome": "TSB - TÉCNICO DE SAÚDE BUCAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14455",
                            "ativo": True,
                            "cbo": {
                                "id": "960",
                                "nome": "AUXILIAR EM SAÚDE BUCAL"
                            },
                            "equipe": {
                                "id": "3",
                                "nome": "ESB M1 ESUS"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "26",
                                    "nome": "ASB - AUXILIAR DE SAÚDE BUCAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14453",
                            "ativo": True,
                            "cbo": {
                                "id": "364",
                                "nome": "CIRURGIÃO DENTISTA - CLÍNICO GERAL"
                            },
                            "equipe": {
                                "id": "3",
                                "nome": "ESB M1 ESUS"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "29",
                                    "nome": "CIRURGIÃO DENTISTA",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14451",
                            "ativo": True,
                            "cbo": {
                                "id": "1218",
                                "nome": "DIGITADOR"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "32",
                                    "nome": "DIGITADOR",
                                    "ativo": True,
                                    "recursos": [
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento odontológico",
                                        "CDS/Ficha de atendimento odontológico/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "CDS/Ficha de visita domiciliar",
                                        "CDS/Ficha de visita domiciliar/Cadastrar, editar e excluir"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14450",
                            "ativo": True,
                            "cbo": {
                                "id": "412",
                                "nome": "FISIOTERAPEUTA GERAL"
                            },
                            "equipe": {
                                "id": "4",
                                "nome": "EAB1"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "43",
                                    "nome": "OUTRO PROF. NÍVEL SUPERIOR",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14449",
                            "ativo": True,
                            "cbo": {
                                "id": "1341",
                                "nome": "AGENTE COMUNITÁRIO DE SAÚDE"
                            },
                            "equipe": {
                                "id": "2",
                                "nome": "EACS"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "25",
                                    "nome": "ACS - AGENTE COMUNITÁRIO DE SAÚDE",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Território",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de visita domiciliar",
                                        "CDS/Ficha de visita domiciliar/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14448",
                            "ativo": True,
                            "cbo": {
                                "id": "112",
                                "nome": "GERENTE DE SERVIÇOS DE SAÚDE"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "31",
                                    "nome": "COORDENADOR DA UBS",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Cidadãos vinculados/Todas as equipes",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Acompanhamentos/Condições de saúde/Todas as equipes",
                                        "Busca ativa de vacinação",
                                        "Busca ativa de vacinação/Todas as equipes",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Reterritorialização",
                                        "Gestão de cadastros de cidadão/Unificação de bases",
                                        "Gestão de cadastros de cidadão/Unificação de cadastros",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Inativar",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial/Todas as equipes",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial/Todos os profissionais",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Cadastro individual/Todas as equipes",
                                        "Relatórios/Consolidados/Cadastro individual/Todos os profissionais",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Consolidados/Situação do território/Todas as equipes",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Absenteísmo/CBO",
                                        "Relatórios/Gerenciais/Absenteísmo/Todas as equipes",
                                        "Relatórios/Gerenciais/Absenteísmo/Todos os profissionais",
                                        "Relatórios/Gerenciais/Absenteísmo/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Atendimentos/CBO",
                                        "Relatórios/Gerenciais/Atendimentos/Todas as equipes",
                                        "Relatórios/Gerenciais/Atendimentos/Todos os profissionais",
                                        "Relatórios/Gerenciais/Atendimentos/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Gerenciais/Vacinação/CBO",
                                        "Relatórios/Gerenciais/Vacinação/Todas as equipes",
                                        "Relatórios/Gerenciais/Vacinação/Todos os profissionais",
                                        "Relatórios/Gerenciais/Vacinação/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Cadastro do território/Todas as equipes",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Criança/Todas as equipes",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Gestante/Todas as equipes",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Operacional/Risco cardiovascular/Todas as equipes",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento domiciliar/Todas as equipes",
                                        "Relatórios/Produção/Atendimento domiciliar/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento domiciliar/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento individual/Todas as equipes",
                                        "Relatórios/Produção/Atendimento individual/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento individual/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todas as equipes",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todos os profissionais",
                                        "Relatórios/Produção/Atendimento odontológico individual/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Atividade coletiva/Todas as equipes",
                                        "Relatórios/Produção/Atividade coletiva/Todos os profissionais",
                                        "Relatórios/Produção/Atividade coletiva/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todas as equipes",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todos os profissionais",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Marcadores de consumo alimentar/Todas as equipes",
                                        "Relatórios/Produção/Marcadores de consumo alimentar/Todos os profissionais",
                                        "Relatórios/Produção/Marcadores de consumo alimentar/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Procedimentos consolidados/Todas as equipes",
                                        "Relatórios/Produção/Procedimentos consolidados/Todos os profissionais",
                                        "Relatórios/Produção/Procedimentos consolidados/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Procedimentos/Todas as equipes",
                                        "Relatórios/Produção/Procedimentos/Todos os profissionais",
                                        "Relatórios/Produção/Procedimentos/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Resumo de produção/Todas as equipes",
                                        "Relatórios/Produção/Resumo de produção/Todos os profissionais",
                                        "Relatórios/Produção/Resumo de produção/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia/Todas as equipes",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia/Todos os profissionais",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Vacinação/Todas as equipes",
                                        "Relatórios/Produção/Vacinação/Todos os profissionais",
                                        "Relatórios/Produção/Vacinação/Todos os profissionais/Categoria profissional",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Relatórios/Produção/Visita domiciliar/Todas as equipes",
                                        "Relatórios/Produção/Visita domiciliar/Todos os profissionais",
                                        "Relatórios/Produção/Visita domiciliar/Todos os profissionais/Categoria profissional",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Agendar/Todas as equipes",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Cancelar/Todas as equipes",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar perfis",
                                        "Visualizar profissionais",
                                        "Visualizar profissionais/Cadastrar, editar e excluir",
                                        "Visualizar profissionais/Redefinir senha",
                                        "Visualizar profissionais/Visualizar acessos",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação",
                                        "Visualizar profissionais/Visualizar acessos/Cadastrar, editar e excluir lotação/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda online",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda online/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Configurar agenda/Todas as unidades",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda",
                                        "Visualizar profissionais/Visualizar acessos/Fechar agenda/Todas as unidades",
                                        "Visualizar unidades de saúde",
                                        "Visualizar unidades de saúde/Ativar ou inativar tipo de serviço",
                                        "Visualizar unidades de saúde/Ativar ou inativar tipo de serviço/Todas as unidades",
                                        "Visualizar unidades de saúde/Configurar consulta no Hórus",
                                        "Visualizar unidades de saúde/Configurar consulta no Hórus/Todas as unidades"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14447",
                            "ativo": True,
                            "cbo": {
                                "id": "678",
                                "nome": "PSICÓLOGO CLÍNICO"
                            },
                            "equipe": {
                                "id": "4",
                                "nome": "EAB1"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "43",
                                    "nome": "OUTRO PROF. NÍVEL SUPERIOR",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14446",
                            "ativo": True,
                            "cbo": {
                                "id": "947",
                                "nome": "TÉCNICO DE ENFERMAGEM"
                            },
                            "equipe": {
                                "id": "4",
                                "nome": "EAB1"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "28",
                                    "nome": "AUXILIAR OU TÉCNICO DE ENFERMAGEM",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Visualizar agenda",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14445",
                            "ativo": True,
                            "cbo": {
                                "id": "397",
                                "nome": "ENFERMEIRO"
                            },
                            "equipe": {
                                "id": "4",
                                "nome": "EAB1"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "34",
                                    "nome": "ENFERMEIRO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14444",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": {
                                "id": "5",
                                "nome": "EMAD1"
                            },
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "38",
                                    "nome": "MÉDICO AD",
                                    "ativo": True,
                                    "recursos": [
                                        "Atenção Domiciliar",
                                        "Atenção Domiciliar/Gerar relatório de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Agendar",
                                        "Atenção Domiciliar/Visualizar agenda de AD da equipe/Cancelar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Cadastrar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Editar",
                                        "Atenção Domiciliar/Visualizar lista de AD da equipe/Excluir",
                                        "CDS",
                                        "CDS/Ficha de atendimento domiciliar",
                                        "CDS/Ficha de atendimento domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de avaliação de elegibilidade",
                                        "CDS/Ficha de avaliação de elegibilidade/Cadastrar, editar e excluir",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        },
                        {
                            "id": "14443",
                            "ativo": True,
                            "cbo": {
                                "id": "461",
                                "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA"
                            },
                            "equipe": None,
                            "unidadeSaude": {
                                "id": "2",
                                "nome": "Unidade Basica de Saude Centro",
                                "cnes": "8007535"
                            },
                            "municipio": {
                                "id": "8866",
                                "nome": "FLORIANÓPOLIS"
                            },
                            "perfis": [
                                {
                                    "id": "39",
                                    "nome": "MÉDICO",
                                    "ativo": True,
                                    "recursos": [
                                        "Acompanhamentos",
                                        "Acompanhamentos/Cidadãos vinculados",
                                        "Acompanhamentos/Condições de saúde",
                                        "Acompanhamentos/Condições de saúde/Problemas e condições",
                                        "Busca ativa de vacinação",
                                        "CDS",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia",
                                        "CDS/Ficha complementar - Síndrome neurológica por Zika ou Microcefalia/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atendimento individual",
                                        "CDS/Ficha de atendimento individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de atividade coletiva",
                                        "CDS/Ficha de atividade coletiva/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro domiciliar",
                                        "CDS/Ficha de cadastro domiciliar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de cadastro individual",
                                        "CDS/Ficha de cadastro individual/Cadastrar, editar e excluir",
                                        "CDS/Ficha de consumo alimentar",
                                        "CDS/Ficha de consumo alimentar/Cadastrar, editar e excluir",
                                        "CDS/Ficha de procedimentos",
                                        "CDS/Ficha de procedimentos/Cadastrar, editar e excluir",
                                        "CDS/Ficha de vacinação",
                                        "CDS/Ficha de vacinação/Cadastrar, editar e excluir",
                                        "Cadastrar, editar e excluir lotes de imunobiológico",
                                        "Gestão de cadastros de cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Cadastrar e editar",
                                        "Gestão de cadastros de cidadão/Visualizar cidadão/Excluir",
                                        "Relatórios",
                                        "Relatórios/Consolidados",
                                        "Relatórios/Consolidados/Cadastro domiciliar e territorial",
                                        "Relatórios/Consolidados/Cadastro individual",
                                        "Relatórios/Consolidados/Situação do território",
                                        "Relatórios/Gerenciais",
                                        "Relatórios/Gerenciais/Absenteísmo",
                                        "Relatórios/Gerenciais/Atendimentos",
                                        "Relatórios/Gerenciais/Vacinação",
                                        "Relatórios/Operacional",
                                        "Relatórios/Operacional/Cadastro do território",
                                        "Relatórios/Operacional/Criança",
                                        "Relatórios/Operacional/Gestante",
                                        "Relatórios/Operacional/Risco cardiovascular",
                                        "Relatórios/Produção",
                                        "Relatórios/Produção/Atendimento domiciliar",
                                        "Relatórios/Produção/Atendimento individual",
                                        "Relatórios/Produção/Atendimento odontológico individual",
                                        "Relatórios/Produção/Atividade coletiva",
                                        "Relatórios/Produção/Avaliação de elegibilidade e admissão",
                                        "Relatórios/Produção/Marcadores de consumo alimentar",
                                        "Relatórios/Produção/Procedimentos",
                                        "Relatórios/Produção/Procedimentos consolidados",
                                        "Relatórios/Produção/Resumo de produção",
                                        "Relatórios/Produção/Síndrome neurológica por Zika ou Microcefalia",
                                        "Relatórios/Produção/Vacinação",
                                        "Relatórios/Produção/Visita domiciliar",
                                        "Videochamada",
                                        "Videochamada/Realizar videochamada",
                                        "Visualizar agenda",
                                        "Visualizar agenda/Agendar",
                                        "Visualizar agenda/Cancelar",
                                        "Visualizar agenda/Informar falta do cidadão",
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Registrar atendimento",
                                        "Visualizar lista de atendimento/Registrar atendimento/Registrar atendimento de vacinação",
                                        "Visualizar prontuário"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                },
                                {
                                    "id": "35",
                                    "nome": "ESCUTA INICIAL",
                                    "ativo": True,
                                    "recursos": [
                                        "Visualizar lista de atendimento",
                                        "Visualizar lista de atendimento/Cadastrar, editar e excluir",
                                        "Visualizar lista de atendimento/Gerar declaração de comparecimento",
                                        "Visualizar lista de atendimento/Informar que cidadão não aguardou",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial",
                                        "Visualizar lista de atendimento/Visualizar escuta inicial/Registrar escuta inicial"
                                    ],
                                    "tipoPerfil": "LOTACAO"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
