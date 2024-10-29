#pylint: disable=C0302
response = {
  "extensions": {
    "tracing": {
      "version": 1,
      "startTime": "2024-10-29T13:47:09.714Z",
      "endTime": "2024-10-29T13:47:09.904Z",
      "duration": 190611258,
      "parsing": {
        "startOffset": 10817201,
        "duration": 10603294
      },
      "validation": {
        "startOffset": 15230203,
        "duration": 4289948
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
            "startOffset": 20833277,
            "duration": 1198523
          },
          {
            "path": [
              "sessao",
              "id"
            ],
            "parentType": "Sessao",
            "returnType": "ID!",
            "fieldName": "id",
            "startOffset": 22308716,
            "duration": 80515
          },
          {
            "path": [
              "sessao",
              "recursos"
            ],
            "parentType": "Sessao",
            "returnType": "[String]",
            "fieldName": "recursos",
            "startOffset": 22559991,
            "duration": 29762
          },
          {
            "path": [
              "sessao",
              "profissional"
            ],
            "parentType": "Sessao",
            "returnType": "Profissional!",
            "fieldName": "profissional",
            "startOffset": 22760258,
            "duration": 12671646
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
            "startOffset": 36722343,
            "duration": 167220
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
            "startOffset": 37134070,
            "duration": 35916
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
            "startOffset": 37395594,
            "duration": 35717
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
            "startOffset": 37573351,
            "duration": 122926
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
            "startOffset": 38195796,
            "duration": 12549891
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
            "startOffset": 50940909,
            "duration": 64628
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
            "startOffset": 51075399,
            "duration": 38293
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
            "startOffset": 38418117,
            "duration": 19260589
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
            "startOffset": 57896387,
            "duration": 39905
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              0,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 57983073,
            "duration": 18125
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
            "startOffset": 58036507,
            "duration": 13243
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
            "startOffset": 58161644,
            "duration": 17675
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
            "startOffset": 58516546,
            "duration": 17282
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              1,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 58802281,
            "duration": 38721
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
            "startOffset": 58887112,
            "duration": 50490
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
            "startOffset": 59078869,
            "duration": 25733
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
            "startOffset": 59382795,
            "duration": 24486
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              2,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 59453124,
            "duration": 13269
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
            "startOffset": 59498061,
            "duration": 11820
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
            "startOffset": 59588638,
            "duration": 15035
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
            "startOffset": 60132694,
            "duration": 24061
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              3,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 60320310,
            "duration": 14980
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
            "startOffset": 60467079,
            "duration": 14742
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
            "startOffset": 60644638,
            "duration": 193305
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
            "startOffset": 61235838,
            "duration": 15439
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              4,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 61484302,
            "duration": 15452
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
            "startOffset": 61764672,
            "duration": 15388
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
            "startOffset": 62545395,
            "duration": 230171
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              5,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 62818396,
            "duration": 11795
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
            "startOffset": 62871038,
            "duration": 11403
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
            "startOffset": 63635051,
            "duration": 14403
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              6,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 63884170,
            "duration": 20409
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
            "startOffset": 63939581,
            "duration": 11040
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
            "startOffset": 64671549,
            "duration": 17666
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              7,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 64732103,
            "duration": 12053
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
            "startOffset": 64777416,
            "duration": 16686
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
            "startOffset": 65510794,
            "duration": 16725
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              8,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 65571631,
            "duration": 11489
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
            "startOffset": 65616394,
            "duration": 16862
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
            "startOffset": 66407501,
            "duration": 19243
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              9,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 66471580,
            "duration": 11241
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
            "startOffset": 66543149,
            "duration": 10892
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
            "startOffset": 67118910,
            "duration": 20453
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              10,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 67387221,
            "duration": 15345
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
            "startOffset": 67591387,
            "duration": 14918
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
            "startOffset": 68680379,
            "duration": 18251
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              11,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 68740499,
            "duration": 17738
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
            "startOffset": 68791522,
            "duration": 10657
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
            "startOffset": 69478178,
            "duration": 17409
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              12,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 69533172,
            "duration": 17278
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
            "startOffset": 69784469,
            "duration": 13791
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
            "startOffset": 70375027,
            "duration": 55396
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              13,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 70497201,
            "duration": 14625
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
            "startOffset": 70546540,
            "duration": 17313
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
            "startOffset": 71064419,
            "duration": 15894
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              14,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 71314889,
            "duration": 16971
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
            "startOffset": 71385670,
            "duration": 18627
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
            "startOffset": 71499776,
            "duration": 21858
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
            "startOffset": 71895945,
            "duration": 17498
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              15,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 71958172,
            "duration": 11872
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
            "startOffset": 72299939,
            "duration": 28431
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
            "startOffset": 72922736,
            "duration": 67040
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              16,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 73026617,
            "duration": 11860
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
            "startOffset": 73207530,
            "duration": 11844
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
            "startOffset": 74300501,
            "duration": 132721
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              17,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 74526473,
            "duration": 13438
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
            "startOffset": 74679850,
            "duration": 20135
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
            "startOffset": 75833805,
            "duration": 14166
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              18,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 75932617,
            "duration": 66379
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
            "startOffset": 76086055,
            "duration": 10798
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
            "startOffset": 76390948,
            "duration": 15244
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
            "startOffset": 76931692,
            "duration": 67615
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              19,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 77170429,
            "duration": 28359
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
            "startOffset": 77317996,
            "duration": 8345
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
            "startOffset": 79422168,
            "duration": 10488
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              20,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 79565680,
            "duration": 126439
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
            "startOffset": 79763212,
            "duration": 8322
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
            "startOffset": 80617636,
            "duration": 9549
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              21,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 80816639,
            "duration": 8744
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
            "startOffset": 80948249,
            "duration": 123839
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
            "startOffset": 81221093,
            "duration": 10600
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
            "startOffset": 82031252,
            "duration": 9660
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              22,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 82112095,
            "duration": 57708
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
            "startOffset": 37824267,
            "duration": 44387308
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
            "startOffset": 82290948,
            "duration": 6175
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
            "startOffset": 82478060,
            "duration": 17430
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
            "startOffset": 82594444,
            "duration": 13736
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
            "startOffset": 82923931,
            "duration": 14480
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
            "startOffset": 83053499,
            "duration": 12470
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
            "startOffset": 83150369,
            "duration": 8072
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              23,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 83333415,
            "duration": 7629
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
            "startOffset": 83319065,
            "duration": 59076
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
            "startOffset": 83465104,
            "duration": 52916
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
            "startOffset": 83537517,
            "duration": 16261
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
            "startOffset": 83883427,
            "duration": 73501
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
            "startOffset": 84026672,
            "duration": 65639
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
            "startOffset": 84260003,
            "duration": 10580
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
            "startOffset": 84427032,
            "duration": 13483
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              24,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 84438189,
            "duration": 8604
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
            "startOffset": 84525112,
            "duration": 44869
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
            "startOffset": 84568292,
            "duration": 7868
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
            "startOffset": 84863163,
            "duration": 13233
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
            "startOffset": 85042912,
            "duration": 12857
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
            "startOffset": 85291277,
            "duration": 14112
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
            "startOffset": 85245784,
            "duration": 116138
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
            "startOffset": 85414099,
            "duration": 12907
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              25,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 85479461,
            "duration": 7820
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
            "startOffset": 85702539,
            "duration": 7455
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
            "startOffset": 85718801,
            "duration": 44891
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
            "startOffset": 85843800,
            "duration": 12230
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
            "startOffset": 86181357,
            "duration": 13595
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
            "startOffset": 86281899,
            "duration": 7884
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
            "startOffset": 86343984,
            "duration": 115281
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              26,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 86431224,
            "duration": 114502
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
            "startOffset": 86688253,
            "duration": 13928
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
            "startOffset": 86923507,
            "duration": 12472
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
            "startOffset": 87051696,
            "duration": 9860
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
            "startOffset": 87062177,
            "duration": 16844
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
            "startOffset": 87400965,
            "duration": 7332
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
            "startOffset": 87566618,
            "duration": 6106
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
            "startOffset": 87852922,
            "duration": 11746
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
            "startOffset": 87819711,
            "duration": 49956
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
            "startOffset": 87968733,
            "duration": 5825
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              27,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 88004770,
            "duration": 58792
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
            "startOffset": 88132648,
            "duration": 9067
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
            "startOffset": 88275700,
            "duration": 77404
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
            "startOffset": 88417958,
            "duration": 105978
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
            "startOffset": 88807948,
            "duration": 7271
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
            "startOffset": 88872221,
            "duration": 52695
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
            "startOffset": 89055784,
            "duration": 12466
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
            "startOffset": 89165843,
            "duration": 6810
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              28,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 89189952,
            "duration": 9664
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
            "startOffset": 89319337,
            "duration": 6217
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
            "startOffset": 89272889,
            "duration": 102335
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
            "startOffset": 89563794,
            "duration": 6688
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
            "startOffset": 89674775,
            "duration": 7208
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
            "startOffset": 89988484,
            "duration": 118857
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
            "startOffset": 90053317,
            "duration": 7828
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              29,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 90178513,
            "duration": 10130
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
            "startOffset": 90167133,
            "duration": 5883
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
            "startOffset": 90253053,
            "duration": 110028
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
            "startOffset": 90471633,
            "duration": 7346
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
            "startOffset": 90515366,
            "duration": 57055
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
            "startOffset": 90590067,
            "duration": 118130
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
            "startOffset": 90903293,
            "duration": 6833
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
            "startOffset": 90988732,
            "duration": 9332
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
            "startOffset": 91010212,
            "duration": 6659
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              30,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 91167189,
            "duration": 10210
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
            "startOffset": 91313059,
            "duration": 55362
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
            "startOffset": 91266332,
            "duration": 6653
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
            "startOffset": 91487530,
            "duration": 7252
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
            "startOffset": 91776412,
            "duration": 91662
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
            "startOffset": 91924232,
            "duration": 6216
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
            "startOffset": 92051260,
            "duration": 9635
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              31,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 92176263,
            "duration": 7485
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
            "startOffset": 92221586,
            "duration": 6580
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
            "startOffset": 92282985,
            "duration": 47314
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
            "startOffset": 92361137,
            "duration": 11317
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
            "startOffset": 92580908,
            "duration": 6519
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
            "startOffset": 92642657,
            "duration": 46652
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
            "startOffset": 92899579,
            "duration": 47125
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              32,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 93007393,
            "duration": 5370
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
            "startOffset": 93106537,
            "duration": 5546
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
            "startOffset": 93092222,
            "duration": 6385
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
            "startOffset": 93329657,
            "duration": 6259
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
            "startOffset": 93504860,
            "duration": 48203
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
            "startOffset": 93605864,
            "duration": 5290
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
            "startOffset": 93784997,
            "duration": 6152
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              33,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 93846790,
            "duration": 46162
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
            "startOffset": 93860435,
            "duration": 47443
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
            "startOffset": 94000041,
            "duration": 5242
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
            "startOffset": 93961309,
            "duration": 5000
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
            "startOffset": 94163671,
            "duration": 6462
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
            "startOffset": 94241153,
            "duration": 5784
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
            "startOffset": 94301066,
            "duration": 48120
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
            "startOffset": 94518156,
            "duration": 6083
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
            "startOffset": 94569259,
            "duration": 46634
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
            "startOffset": 94618375,
            "duration": 5963
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              34,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 94669453,
            "duration": 48185
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
            "startOffset": 94773274,
            "duration": 5066
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
            "startOffset": 94890780,
            "duration": 6086
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
            "startOffset": 94990683,
            "duration": 5820
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
            "startOffset": 95165093,
            "duration": 98997
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
            "startOffset": 95314572,
            "duration": 5614
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
            "startOffset": 95321408,
            "duration": 5935
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              35,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 95439604,
            "duration": 47545
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
            "startOffset": 95540075,
            "duration": 4889
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
            "startOffset": 95591153,
            "duration": 6097
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
            "startOffset": 95658521,
            "duration": 284305
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
            "startOffset": 96471899,
            "duration": 5632
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
            "startOffset": 96627995,
            "duration": 5619
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
            "startOffset": 96896606,
            "duration": 5775
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
            "startOffset": 96970552,
            "duration": 5523
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
            "startOffset": 96997331,
            "duration": 5499
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              36,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 97105729,
            "duration": 5182
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
            "startOffset": 97228242,
            "duration": 25358
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
            "startOffset": 97236269,
            "duration": 88046
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
            "startOffset": 97431649,
            "duration": 4760
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
            "startOffset": 97407997,
            "duration": 5027
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
            "startOffset": 97633751,
            "duration": 5622
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
            "startOffset": 97757507,
            "duration": 46504
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
            "startOffset": 97924114,
            "duration": 4883
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              37,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 98128552,
            "duration": 4781
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
            "startOffset": 98197665,
            "duration": 5505
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
            "startOffset": 98258842,
            "duration": 107469
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
            "startOffset": 98326722,
            "duration": 107213
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
            "startOffset": 98791964,
            "duration": 5413
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
            "startOffset": 99087055,
            "duration": 4620
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
            "startOffset": 99296556,
            "duration": 5112
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              38,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 99528769,
            "duration": 4949
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
            "startOffset": 99483038,
            "duration": 4884
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
            "startOffset": 99708223,
            "duration": 4323
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
            "startOffset": 99650202,
            "duration": 96319
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
            "startOffset": 100070048,
            "duration": 135494
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
            "startOffset": 100255979,
            "duration": 4200
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
            "startOffset": 100424820,
            "duration": 5340
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
            "startOffset": 100485886,
            "duration": 87541
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
            "startOffset": 100484096,
            "duration": 5004
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              39,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 100635040,
            "duration": 4449
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
            "startOffset": 100822242,
            "duration": 4357
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
            "startOffset": 100885733,
            "duration": 4864
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
            "startOffset": 101035640,
            "duration": 5080
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
            "startOffset": 101197101,
            "duration": 5032
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
            "startOffset": 101242344,
            "duration": 44291
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
            "startOffset": 101363834,
            "duration": 4826
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              40,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 101338436,
            "duration": 4226
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
            "startOffset": 101488631,
            "duration": 4216
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
            "startOffset": 101647035,
            "duration": 49443
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
            "startOffset": 101746307,
            "duration": 4733
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
            "startOffset": 101982207,
            "duration": 44466
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
            "startOffset": 102055042,
            "duration": 5074
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
            "startOffset": 102076539,
            "duration": 45934
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              41,
              "tipo"
            ],
            "parentType": "Lotacao",
            "returnType": "TipoAcesso!",
            "fieldName": "tipo",
            "startOffset": 102110960,
            "duration": 44011
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
            "startOffset": 102204475,
            "duration": 3622
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
            "startOffset": 102347080,
            "duration": 4651
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
            "startOffset": 60885843,
            "duration": 47855041
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
            "startOffset": 108806874,
            "duration": 296197
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
            "startOffset": 109126869,
            "duration": 9630
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
            "startOffset": 109148344,
            "duration": 4792
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              3,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 109166595,
            "duration": 6109
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
            "startOffset": 59640256,
            "duration": 49591009
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
            "startOffset": 109261539,
            "duration": 6548
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
            "startOffset": 109278942,
            "duration": 49769
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
            "startOffset": 97370748,
            "duration": 11967013
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
            "startOffset": 109342499,
            "duration": 8911
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              2,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 109363669,
            "duration": 7345
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
            "startOffset": 109368890,
            "duration": 9683
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
            "startOffset": 109393728,
            "duration": 6384
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
            "startOffset": 59150827,
            "duration": 50266621
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              36,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 109408332,
            "duration": 10052
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
            "startOffset": 81139790,
            "duration": 28293493
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
            "startOffset": 109445967,
            "duration": 6169
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
            "startOffset": 109452255,
            "duration": 5539
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
            "startOffset": 109464750,
            "duration": 4623
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
            "startOffset": 109470135,
            "duration": 8315
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
            "startOffset": 109480629,
            "duration": 4772
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              21,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 109490368,
            "duration": 6783
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              1,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 109497785,
            "duration": 5058
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
            "startOffset": 65021443,
            "duration": 44488886
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
            "startOffset": 109528879,
            "duration": 9559
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
            "startOffset": 58248978,
            "duration": 51293977
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
            "startOffset": 109545760,
            "duration": 3760
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              7,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 109556242,
            "duration": 3983
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
            "startOffset": 58084132,
            "duration": 51486161
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
            "startOffset": 109569599,
            "duration": 6180
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
            "startOffset": 109587894,
            "duration": 5287
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
            "startOffset": 109590222,
            "duration": 4328
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
            "startOffset": 109605139,
            "duration": 5531
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
            "startOffset": 109607046,
            "duration": 5728
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              0,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 109622591,
            "duration": 4920
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              0,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 109626026,
            "duration": 7290
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
            "startOffset": 91433932,
            "duration": 18215849
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
            "startOffset": 69119671,
            "duration": 40547292
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
            "startOffset": 109673512,
            "duration": 6428
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
            "startOffset": 109691156,
            "duration": 5210
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
            "startOffset": 109695742,
            "duration": 6527
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              30,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 109708139,
            "duration": 7728
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
            "startOffset": 109715355,
            "duration": 5672
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
            "startOffset": 72364701,
            "duration": 37368059
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
            "startOffset": 109731626,
            "duration": 4485
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              11,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 109747321,
            "duration": 5376
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
            "startOffset": 109759539,
            "duration": 6513
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
            "startOffset": 68110392,
            "duration": 41916294
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
            "startOffset": 109776485,
            "duration": 266262
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              15,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110052668,
            "duration": 5930
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
            "startOffset": 110057389,
            "duration": 8019
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
            "startOffset": 58975916,
            "duration": 51094500
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
            "startOffset": 110078706,
            "duration": 5496
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
            "startOffset": 110091160,
            "duration": 155857
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
            "startOffset": 110254853,
            "duration": 7439
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
            "startOffset": 110258833,
            "duration": 6160
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              1,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110274515,
            "duration": 4768
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              10,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 110278202,
            "duration": 5503
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
            "startOffset": 92439367,
            "duration": 17851809
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
            "startOffset": 110309293,
            "duration": 4847
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
            "startOffset": 66685690,
            "duration": 43650165
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
            "startOffset": 110336949,
            "duration": 5131
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              31,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110351004,
            "duration": 4606
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
            "startOffset": 73434640,
            "duration": 36931129
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
            "startOffset": 110364666,
            "duration": 6664
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
            "startOffset": 110381318,
            "duration": 3595
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
            "startOffset": 110385398,
            "duration": 5436
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
            "startOffset": 110392805,
            "duration": 3686
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
            "startOffset": 110403596,
            "duration": 5844
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              16,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110405995,
            "duration": 5124
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
            "startOffset": 59538960,
            "duration": 50885787
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              9,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 110421847,
            "duration": 4977
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
            "startOffset": 110440221,
            "duration": 3877
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
            "startOffset": 110452896,
            "duration": 3362
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              2,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110462341,
            "duration": 4589
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
            "startOffset": 65984134,
            "duration": 44484411
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
            "startOffset": 93203610,
            "duration": 17274066
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
            "startOffset": 110495799,
            "duration": 4152
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
            "startOffset": 110494959,
            "duration": 6491
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
            "startOffset": 110506992,
            "duration": 3178
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
            "startOffset": 110515810,
            "duration": 5601
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              32,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110519535,
            "duration": 4654
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
            "startOffset": 74889256,
            "duration": 35645549
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
            "startOffset": 110533296,
            "duration": 4854
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              8,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 110549888,
            "duration": 5347
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
            "startOffset": 110551011,
            "duration": 4759
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
            "startOffset": 110562919,
            "duration": 3631
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              17,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 110575399,
            "duration": 3896
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
            "startOffset": 60584760,
            "duration": 50002687
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
            "startOffset": 65124634,
            "duration": 45472376
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
            "startOffset": 110621485,
            "duration": 5947
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
            "startOffset": 110637796,
            "duration": 4576
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
            "startOffset": 110653671,
            "duration": 4331
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              7,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 110667561,
            "duration": 4265
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
            "startOffset": 64289579,
            "duration": 46415940
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
            "startOffset": 66641564,
            "duration": 44479265
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
            "startOffset": 110729374,
            "duration": 398886
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
            "startOffset": 111145246,
            "duration": 7249
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
            "startOffset": 111159839,
            "duration": 2915
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              6,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111168779,
            "duration": 3016
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
            "startOffset": 63241954,
            "duration": 47962233
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
            "startOffset": 110725151,
            "duration": 482131
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
            "startOffset": 111231937,
            "duration": 6140
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
            "startOffset": 111249487,
            "duration": 4374
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
            "startOffset": 111262353,
            "duration": 4299
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              5,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111275497,
            "duration": 4049
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
            "startOffset": 111283036,
            "duration": 10674
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
            "startOffset": 62040046,
            "duration": 49276603
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
            "startOffset": 111313270,
            "duration": 7152
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
            "startOffset": 111343788,
            "duration": 5712
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
            "startOffset": 111359580,
            "duration": 4387
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
            "startOffset": 111372636,
            "duration": 3914
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              4,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111385476,
            "duration": 3822
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
            "startOffset": 87343904,
            "duration": 24080188
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
            "startOffset": 111340952,
            "duration": 5213
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
            "startOffset": 60935297,
            "duration": 50512946
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
            "startOffset": 111450722,
            "duration": 5919
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
            "startOffset": 65718041,
            "duration": 45623266
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
            "startOffset": 111468260,
            "duration": 6928
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
            "startOffset": 111483601,
            "duration": 3579
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              3,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 111493649,
            "duration": 7693
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              26,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111496462,
            "duration": 7002
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
            "startOffset": 111498643,
            "duration": 10506
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
            "startOffset": 111525197,
            "duration": 11174
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
            "startOffset": 111526474,
            "duration": 8272
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
            "startOffset": 86015787,
            "duration": 25530552
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
            "startOffset": 61992552,
            "duration": 49564825
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
            "startOffset": 111574780,
            "duration": 6466
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
            "startOffset": 111578586,
            "duration": 9007
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
            "startOffset": 111591307,
            "duration": 3689
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
            "startOffset": 111601919,
            "duration": 2656
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              25,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111609983,
            "duration": 2515
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
            "startOffset": 89497107,
            "duration": 22038145
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
            "startOffset": 84845990,
            "duration": 26789169
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
            "startOffset": 111652214,
            "duration": 4691
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
            "startOffset": 111665219,
            "duration": 2899
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
            "startOffset": 111673453,
            "duration": 2486
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              24,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111681580,
            "duration": 3604
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
            "startOffset": 111548464,
            "duration": 136260
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
            "startOffset": 59681881,
            "duration": 52017255
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
            "startOffset": 111719077,
            "duration": 13773
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
            "startOffset": 111747242,
            "duration": 6224
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
            "startOffset": 59201965,
            "duration": 52561918
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
            "startOffset": 111789876,
            "duration": 6165
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
            "startOffset": 65080252,
            "duration": 46733108
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
            "startOffset": 111821547,
            "duration": 5132
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
            "startOffset": 111830898,
            "duration": 5445
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
            "startOffset": 111844620,
            "duration": 2869
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
            "startOffset": 64235752,
            "duration": 47622514
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
            "startOffset": 83843671,
            "duration": 28051920
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
            "startOffset": 111910984,
            "duration": 3720
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
            "startOffset": 111920900,
            "duration": 2377
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
            "startOffset": 111928901,
            "duration": 2339
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              23,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 111936823,
            "duration": 2442
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
            "startOffset": 82614194,
            "duration": 29354657
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
            "startOffset": 111966597,
            "duration": 6217
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
            "startOffset": 111983173,
            "duration": 4911
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
            "startOffset": 58299262,
            "duration": 53699197
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
            "startOffset": 111994865,
            "duration": 5892
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
            "startOffset": 112013118,
            "duration": 5092
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
            "startOffset": 112015887,
            "duration": 6338
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
            "startOffset": 112030180,
            "duration": 4225
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
            "startOffset": 112033211,
            "duration": 3970
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
            "startOffset": 69161208,
            "duration": 42887530
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              22,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112044980,
            "duration": 5035
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
            "startOffset": 112064159,
            "duration": 3363
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
            "startOffset": 112075580,
            "duration": 2934
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
            "startOffset": 68274208,
            "duration": 43814162
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
            "startOffset": 81416229,
            "duration": 30679311
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
            "startOffset": 112102107,
            "duration": 3777
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
            "startOffset": 112112752,
            "duration": 2991
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
            "startOffset": 66963518,
            "duration": 45161519
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
            "startOffset": 112120955,
            "duration": 7030
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
            "startOffset": 112136765,
            "duration": 4021
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
            "startOffset": 112140120,
            "duration": 3839
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
            "startOffset": 112035436,
            "duration": 115436
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
            "startOffset": 112150506,
            "duration": 6807
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              28,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 112162950,
            "duration": 5391
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              21,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112167258,
            "duration": 4798
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
            "startOffset": 112164684,
            "duration": 12017
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
            "startOffset": 70596331,
            "duration": 41587270
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
            "startOffset": 80183603,
            "duration": 32014563
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
            "startOffset": 112197827,
            "duration": 6616
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
            "startOffset": 112214431,
            "duration": 3903
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
            "startOffset": 63197087,
            "duration": 49024768
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
            "startOffset": 112224822,
            "duration": 2758
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
            "startOffset": 112233841,
            "duration": 3098
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              20,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112244791,
            "duration": 2825
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
            "startOffset": 112247213,
            "duration": 7794
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
            "startOffset": 112253230,
            "duration": 5458
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
            "startOffset": 77604383,
            "duration": 34669602
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
            "startOffset": 112271401,
            "duration": 7771
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
            "startOffset": 112324683,
            "duration": 4151
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
            "startOffset": 112306613,
            "duration": 21145
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
            "startOffset": 112335322,
            "duration": 2327
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
            "startOffset": 112344521,
            "duration": 2717
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
            "startOffset": 66032151,
            "duration": 46320434
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              19,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112354703,
            "duration": 2744
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
            "startOffset": 76553565,
            "duration": 35823299
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
            "startOffset": 112374295,
            "duration": 3398
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
            "startOffset": 112412937,
            "duration": 5882
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
            "startOffset": 69061754,
            "duration": 43396459
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
            "startOffset": 112426116,
            "duration": 2420
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
            "startOffset": 112474281,
            "duration": 5440
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              13,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 112483195,
            "duration": 8049
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
            "startOffset": 112482858,
            "duration": 7734
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
            "startOffset": 112520239,
            "duration": 3791
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
            "startOffset": 112530594,
            "duration": 2804
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
            "startOffset": 65166836,
            "duration": 47367117
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              18,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112542854,
            "duration": 4652
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
            "startOffset": 61934176,
            "duration": 50646869
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
            "startOffset": 112577489,
            "duration": 6120
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
            "startOffset": 75218683,
            "duration": 37400094
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
            "startOffset": 112492790,
            "duration": 149452
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
            "startOffset": 112637766,
            "duration": 5211
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
            "startOffset": 112666477,
            "duration": 3849
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
            "startOffset": 67993056,
            "duration": 44680930
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
            "startOffset": 112677758,
            "duration": 2611
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              17,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112687120,
            "duration": 2436
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
            "startOffset": 112696020,
            "duration": 21275
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
            "startOffset": 73655379,
            "duration": 39074633
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
            "startOffset": 112727097,
            "duration": 6674
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
            "startOffset": 112748538,
            "duration": 4532
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
            "startOffset": 112759569,
            "duration": 2391
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
            "startOffset": 112767090,
            "duration": 2232
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              16,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112774514,
            "duration": 2318
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
            "startOffset": 112671600,
            "duration": 112952
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
            "startOffset": 64331385,
            "duration": 48466011
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
            "startOffset": 72473778,
            "duration": 40326691
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
            "startOffset": 112816227,
            "duration": 3534
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
            "startOffset": 112826339,
            "duration": 3726
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
            "startOffset": 112838409,
            "duration": 2708
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
            "startOffset": 112796389,
            "duration": 4863
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              15,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112846619,
            "duration": 2849
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
            "startOffset": 71589451,
            "duration": 41283376
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
            "startOffset": 112876322,
            "duration": 6865
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
            "startOffset": 112888968,
            "duration": 3421
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
            "startOffset": 112898632,
            "duration": 2411
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
            "startOffset": 112907379,
            "duration": 2859
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              14,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112915369,
            "duration": 3677
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
            "startOffset": 70813478,
            "duration": 42125184
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
            "startOffset": 112957077,
            "duration": 3789
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
            "startOffset": 112968693,
            "duration": 3819
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
            "startOffset": 112963938,
            "duration": 8112
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
            "startOffset": 112978377,
            "duration": 2582
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              13,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 112987979,
            "duration": 2624
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
            "startOffset": 69892686,
            "duration": 43099062
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
            "startOffset": 69937711,
            "duration": 43075406
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
            "startOffset": 113005610,
            "duration": 10195
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
            "startOffset": 113028362,
            "duration": 3780
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
            "startOffset": 63283671,
            "duration": 49750843
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
            "startOffset": 113038759,
            "duration": 2528
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
            "startOffset": 113046716,
            "duration": 2379
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              12,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 113054361,
            "duration": 2617
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
            "startOffset": 102498686,
            "duration": 10583820
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
            "startOffset": 113374629,
            "duration": 4534
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
            "startOffset": 113386013,
            "duration": 2374
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
            "startOffset": 113395795,
            "duration": 2461
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
            "startOffset": 113397067,
            "duration": 6930
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              41,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 113404262,
            "duration": 3237
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
            "startOffset": 101695525,
            "duration": 11753921
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              4,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 112902921,
            "duration": 635616
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
            "startOffset": 113542645,
            "duration": 9713
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
            "startOffset": 113419791,
            "duration": 188581
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
            "startOffset": 113611507,
            "duration": 6568
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
            "startOffset": 113619159,
            "duration": 6413
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
            "startOffset": 84707999,
            "duration": 28922109
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
            "startOffset": 113637438,
            "duration": 3620
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
            "startOffset": 113647797,
            "duration": 2781
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              40,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 113657430,
            "duration": 2742
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
            "startOffset": 94870170,
            "duration": 18789768
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
            "startOffset": 100982822,
            "duration": 12702537
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
            "startOffset": 113700938,
            "duration": 3560
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
            "startOffset": 113710327,
            "duration": 3664
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
            "startOffset": 113718898,
            "duration": 2265
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              39,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 113726700,
            "duration": 2912
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
            "startOffset": 100133354,
            "duration": 13614925
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
            "startOffset": 62120543,
            "duration": 51564076
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
            "startOffset": 113761133,
            "duration": 3437
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
            "startOffset": 113771318,
            "duration": 2257
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
            "startOffset": 113794876,
            "duration": 2082
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
            "startOffset": 113801889,
            "duration": 24013
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
            "startOffset": 113840145,
            "duration": 4116
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
            "startOffset": 83774600,
            "duration": 30079917
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              38,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 113803925,
            "duration": 152653
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
            "startOffset": 98708202,
            "duration": 15290754
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
            "startOffset": 113997031,
            "duration": 8588
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
            "startOffset": 114021337,
            "duration": 5772
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
            "startOffset": 114037939,
            "duration": 4414
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
            "startOffset": 114050519,
            "duration": 4321
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              37,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 114065935,
            "duration": 4291
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
            "startOffset": 58382227,
            "duration": 55697780
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
            "startOffset": 114063837,
            "duration": 50536
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
            "startOffset": 97489802,
            "duration": 16722555
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
            "startOffset": 114232263,
            "duration": 5968
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
            "startOffset": 114109665,
            "duration": 144588
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
            "startOffset": 87494047,
            "duration": 26776391
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
            "startOffset": 114248267,
            "duration": 12594
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
            "startOffset": 114334733,
            "duration": 7700
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
            "startOffset": 114425631,
            "duration": 11278
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
            "startOffset": 114458018,
            "duration": 6256
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
            "startOffset": 114370204,
            "duration": 8683
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              34,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 114545990,
            "duration": 19980
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
            "startOffset": 114561731,
            "duration": 6119
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
            "startOffset": 114490824,
            "duration": 102206
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
            "startOffset": 77446040,
            "duration": 37179401
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
            "startOffset": 114555367,
            "duration": 107029
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
            "startOffset": 114564341,
            "duration": 4902
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              36,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 114618895,
            "duration": 99171
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
            "startOffset": 82541033,
            "duration": 32177908
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
            "startOffset": 114772446,
            "duration": 5716
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
            "startOffset": 114778755,
            "duration": 10644
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
            "startOffset": 114823781,
            "duration": 4131
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
            "startOffset": 96484738,
            "duration": 18344533
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
            "startOffset": 114726333,
            "duration": 7807
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
            "startOffset": 114841229,
            "duration": 54276
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
            "startOffset": 114845376,
            "duration": 51281
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
            "startOffset": 77526313,
            "duration": 37386165
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
            "startOffset": 86036380,
            "duration": 28915511
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              19,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 114952615,
            "duration": 6532
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
            "startOffset": 59252636,
            "duration": 55775373
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
            "startOffset": 115077822,
            "duration": 4379
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
            "startOffset": 63134628,
            "duration": 51980053
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
            "startOffset": 115016517,
            "duration": 100995
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
            "startOffset": 115146031,
            "duration": 7261
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
            "startOffset": 115166153,
            "duration": 4303
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              5,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 115179789,
            "duration": 5521
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
            "startOffset": 95638828,
            "duration": 19561998
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
            "startOffset": 115203767,
            "duration": 7862
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
            "startOffset": 115225851,
            "duration": 6978
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
            "startOffset": 115245042,
            "duration": 3853
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
            "startOffset": 115215201,
            "duration": 42185
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              35,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 115261551,
            "duration": 4294
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
            "startOffset": 115277057,
            "duration": 3788
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
            "startOffset": 79965709,
            "duration": 35314939
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
            "startOffset": 115279117,
            "duration": 9353
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
            "startOffset": 115306225,
            "duration": 4718
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
            "startOffset": 70652145,
            "duration": 44704639
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
            "startOffset": 115320941,
            "duration": 95502
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
            "startOffset": 115304262,
            "duration": 118267
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
            "startOffset": 115385002,
            "duration": 42705
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
            "startOffset": 115432811,
            "duration": 6864
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
            "startOffset": 115480621,
            "duration": 9013
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
            "startOffset": 115489484,
            "duration": 5384
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
            "startOffset": 85028413,
            "duration": 30470666
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              35,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 115476813,
            "duration": 3553
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              20,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 115524768,
            "duration": 7531
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
            "startOffset": 115593725,
            "duration": 41039
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
            "startOffset": 95045516,
            "duration": 20589393
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
            "startOffset": 115618304,
            "duration": 47955
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
            "startOffset": 75057343,
            "duration": 40628048
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
            "startOffset": 63987760,
            "duration": 51707378
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
            "startOffset": 115706224,
            "duration": 9026
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
            "startOffset": 115717813,
            "duration": 4654
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
            "startOffset": 115775447,
            "duration": 10805
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
            "startOffset": 115805900,
            "duration": 10602
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
            "startOffset": 83910758,
            "duration": 31911625
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
            "startOffset": 115828413,
            "duration": 6337
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
            "startOffset": 115794365,
            "duration": 42051
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
            "startOffset": 73616908,
            "duration": 42267910
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
            "startOffset": 115901800,
            "duration": 3768
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
            "startOffset": 115950483,
            "duration": 8599
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              6,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 115952407,
            "duration": 41980
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
            "startOffset": 116022948,
            "duration": 3897
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
            "startOffset": 115978395,
            "duration": 7516
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
            "startOffset": 116084883,
            "duration": 6026
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
            "startOffset": 98484948,
            "duration": 17615123
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
            "startOffset": 116070060,
            "duration": 50917
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
            "startOffset": 115966610,
            "duration": 160346
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
            "startOffset": 82734201,
            "duration": 33406923
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
            "startOffset": 116123509,
            "duration": 41657
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
            "startOffset": 116230899,
            "duration": 8362
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
            "startOffset": 116280910,
            "duration": 7014
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
            "startOffset": 116278617,
            "duration": 41352
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
            "startOffset": 116330242,
            "duration": 3348
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
            "startOffset": 72428790,
            "duration": 43908569
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              37,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 116342179,
            "duration": 2365
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
            "startOffset": 82468528,
            "duration": 33929908
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
            "startOffset": 116423337,
            "duration": 3498
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
            "startOffset": 116291593,
            "duration": 3871
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
            "startOffset": 116397131,
            "duration": 44932
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
            "startOffset": 81551502,
            "duration": 34903731
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
            "startOffset": 116450673,
            "duration": 8203
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
            "startOffset": 116517554,
            "duration": 3363
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              34,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 116529712,
            "duration": 3592
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
            "startOffset": 80049846,
            "duration": 36518850
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
            "startOffset": 116606176,
            "duration": 4421
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
            "startOffset": 59718707,
            "duration": 56924834
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
            "startOffset": 116714393,
            "duration": 3777
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
            "startOffset": 94225440,
            "duration": 22505106
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
            "startOffset": 116723981,
            "duration": 42758
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
            "startOffset": 116587278,
            "duration": 6130
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
            "startOffset": 116801533,
            "duration": 3703
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
            "startOffset": 116824743,
            "duration": 42140
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
            "startOffset": 116844638,
            "duration": 4562
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
            "startOffset": 85945283,
            "duration": 30959054
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              22,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 116920176,
            "duration": 3725
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
            "startOffset": 65665626,
            "duration": 51268769
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
            "startOffset": 80332936,
            "duration": 36603008
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
            "startOffset": 116817312,
            "duration": 7081
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
            "startOffset": 116950212,
            "duration": 3302
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
            "startOffset": 116918992,
            "duration": 3519
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
            "startOffset": 116962000,
            "duration": 2558
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              8,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 116972298,
            "duration": 3424
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
            "startOffset": 99848005,
            "duration": 17137226
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
            "startOffset": 117000298,
            "duration": 5826
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
            "startOffset": 117007924,
            "duration": 3665
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
            "startOffset": 117015017,
            "duration": 3191
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
            "startOffset": 116993131,
            "duration": 3982
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
            "startOffset": 117047179,
            "duration": 8915
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
            "startOffset": 117080087,
            "duration": 3168
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
            "startOffset": 117028369,
            "duration": 4055
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
            "startOffset": 88415834,
            "duration": 28713978
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              38,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 117152874,
            "duration": 3320
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
            "startOffset": 117185410,
            "duration": 3314
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              33,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 117101844,
            "duration": 108228
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
            "startOffset": 117215055,
            "duration": 3712
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
            "startOffset": 117239024,
            "duration": 8673
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
            "startOffset": 83632355,
            "duration": 33636479
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
            "startOffset": 77681461,
            "duration": 39566611
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
            "startOffset": 117349377,
            "duration": 3571
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
            "startOffset": 117318193,
            "duration": 106672
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
            "startOffset": 117437641,
            "duration": 3904
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
            "startOffset": 117487480,
            "duration": 42296
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
            "startOffset": 100929932,
            "duration": 16471073
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
            "startOffset": 76648412,
            "duration": 40927074
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
            "startOffset": 93388532,
            "duration": 24209276
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
            "startOffset": 117587270,
            "duration": 7340
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
            "startOffset": 117651393,
            "duration": 3652
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
            "startOffset": 117689464,
            "duration": 8052
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
            "startOffset": 117663323,
            "duration": 3634
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
            "startOffset": 117793695,
            "duration": 7416
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
            "startOffset": 117803482,
            "duration": 3143
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
            "startOffset": 117710920,
            "duration": 170786
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
            "startOffset": 75372699,
            "duration": 42480977
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
            "startOffset": 117928184,
            "duration": 47416
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
            "startOffset": 117823525,
            "duration": 162508
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
            "startOffset": 118034944,
            "duration": 3705
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
            "startOffset": 118043554,
            "duration": 3087
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
            "startOffset": 117933187,
            "duration": 3730
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
            "startOffset": 60979373,
            "duration": 57125412
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
            "startOffset": 118082768,
            "duration": 42342
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
            "startOffset": 73803655,
            "duration": 44368287
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
            "startOffset": 118268342,
            "duration": 3396
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              23,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 118154872,
            "duration": 3392
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
            "startOffset": 118385374,
            "duration": 8214
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
            "startOffset": 99989562,
            "duration": 18225382
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
            "startOffset": 118452246,
            "duration": 120472
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
            "startOffset": 66585982,
            "duration": 51996199
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
            "startOffset": 118532916,
            "duration": 49426
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
            "startOffset": 118471911,
            "duration": 190035
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
            "startOffset": 118669465,
            "duration": 2697
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
            "startOffset": 98601881,
            "duration": 20079970
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
            "startOffset": 118690754,
            "duration": 4077
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
            "startOffset": 118700211,
            "duration": 2118
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
            "startOffset": 94984568,
            "duration": 23725258
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
            "startOffset": 118672599,
            "duration": 3509
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
            "startOffset": 118719868,
            "duration": 2938
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
            "startOffset": 118743049,
            "duration": 3644
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
            "startOffset": 118533539,
            "duration": 219712
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
            "startOffset": 89581792,
            "duration": 29174341
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
            "startOffset": 72513693,
            "duration": 46301519
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
            "startOffset": 118750902,
            "duration": 7403
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
            "startOffset": 118908553,
            "duration": 3900
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
            "startOffset": 118924695,
            "duration": 3856
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
            "startOffset": 118964051,
            "duration": 3618
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              32,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 118862086,
            "duration": 3274
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
            "startOffset": 119012301,
            "duration": 40492
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
            "startOffset": 119062687,
            "duration": 7181
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
            "startOffset": 119090384,
            "duration": 4607
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
            "startOffset": 93321911,
            "duration": 25779256
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
            "startOffset": 119105927,
            "duration": 4937
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
            "startOffset": 119118647,
            "duration": 4591
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
            "startOffset": 119135176,
            "duration": 3234
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
            "startOffset": 119146551,
            "duration": 4936
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
            "startOffset": 62435362,
            "duration": 56733527
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
            "startOffset": 71634563,
            "duration": 47550606
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
            "startOffset": 119186251,
            "duration": 3440
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
            "startOffset": 119187346,
            "duration": 5923
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
            "startOffset": 119189142,
            "duration": 4654
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
            "startOffset": 119203598,
            "duration": 4998
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
            "startOffset": 119215890,
            "duration": 4016
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
            "startOffset": 119240024,
            "duration": 4338
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              9,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 119198113,
            "duration": 121668
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
            "startOffset": 119279930,
            "duration": 41395
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
            "startOffset": 119273788,
            "duration": 50445
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
            "startOffset": 63521178,
            "duration": 55850940
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
            "startOffset": 92563457,
            "duration": 26700696
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
            "startOffset": 119371082,
            "duration": 2956
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
            "startOffset": 92504271,
            "duration": 26920639
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
            "startOffset": 100875099,
            "duration": 18559804
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
            "startOffset": 70909818,
            "duration": 48549330
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
            "startOffset": 119632604,
            "duration": 3700
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
            "startOffset": 119631229,
            "duration": 7544
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
            "startOffset": 119644337,
            "duration": 2665
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
            "startOffset": 91564680,
            "duration": 28090023
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
            "startOffset": 119663646,
            "duration": 2748
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
            "startOffset": 119673501,
            "duration": 2163
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
            "startOffset": 95702211,
            "duration": 23981227
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
            "startOffset": 119613835,
            "duration": 3630
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
            "startOffset": 119743594,
            "duration": 3826
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
            "startOffset": 119771006,
            "duration": 3374
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
            "startOffset": 119837938,
            "duration": 3576
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
            "startOffset": 69978719,
            "duration": 49909896
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
            "startOffset": 119798753,
            "duration": 157954
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
            "startOffset": 119824508,
            "duration": 140200
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
            "startOffset": 119982580,
            "duration": 3124
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
            "startOffset": 101636275,
            "duration": 18394719
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
            "startOffset": 120028827,
            "duration": 3720
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
            "startOffset": 120012995,
            "duration": 7620
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
            "startOffset": 120082420,
            "duration": 3868
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
            "startOffset": 120097053,
            "duration": 3243
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
            "startOffset": 120118440,
            "duration": 3782
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
            "startOffset": 120130486,
            "duration": 41782
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
            "startOffset": 120179665,
            "duration": 6835
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
            "startOffset": 120208879,
            "duration": 4244
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
            "startOffset": 102593850,
            "duration": 17625959
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
            "startOffset": 120166403,
            "duration": 3101
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              39,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 120409655,
            "duration": 3256
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
            "startOffset": 120377525,
            "duration": 3639
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
            "startOffset": 64371115,
            "duration": 56067044
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              31,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 120477429,
            "duration": 3325
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
            "startOffset": 120531364,
            "duration": 3396
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
            "startOffset": 84638539,
            "duration": 35960228
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
            "startOffset": 101751570,
            "duration": 18829308
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
            "startOffset": 120639516,
            "duration": 4501
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
            "startOffset": 120727690,
            "duration": 4312
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
            "startOffset": 120761857,
            "duration": 3551
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
            "startOffset": 120777763,
            "duration": 4304
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
            "startOffset": 120808403,
            "duration": 40532
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
            "startOffset": 101037970,
            "duration": 19856813
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
            "startOffset": 120909487,
            "duration": 4348
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
            "startOffset": 120877871,
            "duration": 42812
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
            "startOffset": 91644832,
            "duration": 29306282
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
            "startOffset": 121030771,
            "duration": 4094
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
            "startOffset": 120958692,
            "duration": 3106
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
            "startOffset": 121030000,
            "duration": 4123
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
            "startOffset": 100273600,
            "duration": 20823877
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
            "startOffset": 121186861,
            "duration": 3751
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
            "startOffset": 121192542,
            "duration": 4483
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
            "startOffset": 121568172,
            "duration": 3402
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
            "startOffset": 121623587,
            "duration": 3956
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
            "startOffset": 121732919,
            "duration": 46270
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
            "startOffset": 65207085,
            "duration": 56690380
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
            "startOffset": 122032297,
            "duration": 4250
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
            "startOffset": 122089677,
            "duration": 48346
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
            "startOffset": 121196070,
            "duration": 944291
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
            "startOffset": 122206064,
            "duration": 4387
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
            "startOffset": 122204287,
            "duration": 3803
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
            "startOffset": 122545270,
            "duration": 3947
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
            "startOffset": 66073073,
            "duration": 56566658
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
            "startOffset": 122725853,
            "duration": 4117
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
            "startOffset": 122868837,
            "duration": 3949
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              24,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 122891061,
            "duration": 3485
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
            "startOffset": 98767372,
            "duration": 24184716
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
            "startOffset": 122993791,
            "duration": 7120
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
            "startOffset": 123029625,
            "duration": 41313
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
            "startOffset": 122962387,
            "duration": 155269
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
            "startOffset": 67638523,
            "duration": 55545343
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
            "startOffset": 123163896,
            "duration": 50205
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
            "startOffset": 67009405,
            "duration": 56217179
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
            "startOffset": 123097546,
            "duration": 2916
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
            "startOffset": 97600878,
            "duration": 25663146
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
            "startOffset": 123304222,
            "duration": 2962
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
            "startOffset": 123344050,
            "duration": 3628
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
            "startOffset": 123355904,
            "duration": 2251
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              10,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 123363788,
            "duration": 3262
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
            "startOffset": 123368904,
            "duration": 4930
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
            "startOffset": 102293611,
            "duration": 21083105
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
            "startOffset": 123392337,
            "duration": 4194
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
            "startOffset": 123402472,
            "duration": 2140
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              41,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 123415763,
            "duration": 2692
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
            "startOffset": 101581703,
            "duration": 21849800
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
            "startOffset": 123419938,
            "duration": 40926
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
            "startOffset": 123387466,
            "duration": 3800
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
            "startOffset": 123508489,
            "duration": 3214
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              30,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 123519807,
            "duration": 3412
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
            "startOffset": 96723314,
            "duration": 26836083
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
            "startOffset": 123505354,
            "duration": 3643
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
            "startOffset": 123627260,
            "duration": 3670
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
            "startOffset": 90645486,
            "duration": 33018844
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
            "startOffset": 123691794,
            "duration": 4041
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
            "startOffset": 123703420,
            "duration": 3885
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
            "startOffset": 123677955,
            "duration": 83991
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
            "startOffset": 123755690,
            "duration": 23294
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
            "startOffset": 123757287,
            "duration": 90083
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
            "startOffset": 95102449,
            "duration": 28763817
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
            "startOffset": 68325132,
            "duration": 55569074
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
            "startOffset": 123948970,
            "duration": 3486
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              40,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 123900669,
            "duration": 2920
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
            "startOffset": 123990102,
            "duration": 3658
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
            "startOffset": 124292005,
            "duration": 2957
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
            "startOffset": 94333254,
            "duration": 29970257
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
            "startOffset": 124330642,
            "duration": 4230
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
            "startOffset": 88257336,
            "duration": 36321944
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
            "startOffset": 124591056,
            "duration": 4000
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
            "startOffset": 124628964,
            "duration": 3298
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
            "startOffset": 124745072,
            "duration": 4128
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
            "startOffset": 124892906,
            "duration": 108038
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
            "startOffset": 69202304,
            "duration": 55849228
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
            "startOffset": 125082167,
            "duration": 13940
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
            "startOffset": 125233533,
            "duration": 4190
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
            "startOffset": 125245285,
            "duration": 5009
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
            "startOffset": 125257797,
            "duration": 3644
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
            "startOffset": 125274881,
            "duration": 2700
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
            "startOffset": 70018754,
            "duration": 55267057
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
            "startOffset": 125295924,
            "duration": 3165
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
            "startOffset": 125304220,
            "duration": 2790
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
            "startOffset": 125311577,
            "duration": 2943
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
            "startOffset": 125314556,
            "duration": 3951
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
            "startOffset": 125329684,
            "duration": 2878
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
            "startOffset": 125342101,
            "duration": 2604
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
            "startOffset": 125349537,
            "duration": 2660
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
            "startOffset": 125356815,
            "duration": 2769
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
            "startOffset": 125373290,
            "duration": 2858
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
            "startOffset": 70952927,
            "duration": 54429372
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
            "startOffset": 125391289,
            "duration": 3008
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
            "startOffset": 125399122,
            "duration": 2765
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
            "startOffset": 125428640,
            "duration": 4147
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              27,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 125369619,
            "duration": 112323
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
            "startOffset": 125460449,
            "duration": 23300
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
            "startOffset": 86958849,
            "duration": 38533573
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
            "startOffset": 125505360,
            "duration": 4108
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              29,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 125478353,
            "duration": 97007
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
            "startOffset": 93558592,
            "duration": 32063394
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
            "startOffset": 125584729,
            "duration": 41030
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
            "startOffset": 125680880,
            "duration": 24913
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
            "startOffset": 125734582,
            "duration": 3592
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
            "startOffset": 125735854,
            "duration": 3493
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
            "startOffset": 125733102,
            "duration": 43299
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
            "startOffset": 92622090,
            "duration": 33164309
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
            "startOffset": 89660637,
            "duration": 36156588
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              26,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 125892325,
            "duration": 3099
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
            "startOffset": 125916410,
            "duration": 3929
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
            "startOffset": 125922448,
            "duration": 3863
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
            "startOffset": 85869415,
            "duration": 40085426
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
            "startOffset": 125994257,
            "duration": 3380
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
            "startOffset": 91721975,
            "duration": 34303682
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
            "startOffset": 125975555,
            "duration": 80853
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
            "startOffset": 126101384,
            "duration": 3113
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
            "startOffset": 126170628,
            "duration": 4124
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
            "startOffset": 126099025,
            "duration": 104356
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
            "startOffset": 126203159,
            "duration": 42685
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
            "startOffset": 126264619,
            "duration": 3698
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
            "startOffset": 126327536,
            "duration": 4257
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              28,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 126290862,
            "duration": 3292
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
            "startOffset": 126231609,
            "duration": 182323
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
            "startOffset": 90719680,
            "duration": 35725341
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
            "startOffset": 126407872,
            "duration": 41292
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
            "startOffset": 88496266,
            "duration": 37958982
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
            "startOffset": 126534263,
            "duration": 89618
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
            "startOffset": 126576309,
            "duration": 4311
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              25,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 126611430,
            "duration": 3164
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
            "startOffset": 126713643,
            "duration": 3310
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
            "startOffset": 71676389,
            "duration": 55064796
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
            "startOffset": 126755590,
            "duration": 8224
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
            "startOffset": 89734067,
            "duration": 37035063
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
            "startOffset": 69838104,
            "duration": 56959468
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
            "startOffset": 126864092,
            "duration": 4131
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
            "startOffset": 126894339,
            "duration": 3446
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
            "startOffset": 126934843,
            "duration": 4679
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
            "startOffset": 126864098,
            "duration": 83004
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
            "startOffset": 126983535,
            "duration": 3180
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
            "startOffset": 126956104,
            "duration": 67036
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
            "startOffset": 126984356,
            "duration": 41267
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
            "startOffset": 127010340,
            "duration": 3811
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              27,
              "unidadeSaude",
              "endereco"
            ],
            "parentType": "UnidadeSaude",
            "returnType": "Endereco",
            "fieldName": "endereco",
            "startOffset": 127409642,
            "duration": 3665
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
            "startOffset": 88630325,
            "duration": 38790890
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
            "startOffset": 127352914,
            "duration": 3678
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              12,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 127031228,
            "duration": 512947
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
            "startOffset": 127670701,
            "duration": 3750
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
            "startOffset": 68840190,
            "duration": 58908243
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
            "startOffset": 127731766,
            "duration": 25261
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
            "startOffset": 72703704,
            "duration": 55070316
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
            "startOffset": 127858289,
            "duration": 3319
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
            "startOffset": 127902512,
            "duration": 3962
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
            "startOffset": 127978759,
            "duration": 3673
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
            "startOffset": 128090684,
            "duration": 4475
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
            "startOffset": 128082290,
            "duration": 40184
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              11,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 128166383,
            "duration": 3034
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
            "startOffset": 128194809,
            "duration": 95685
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
            "startOffset": 90433004,
            "duration": 37880282
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
            "startOffset": 128383756,
            "duration": 3683
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
            "startOffset": 128448206,
            "duration": 3735
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
            "startOffset": 128589444,
            "duration": 2910
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              29,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 128672807,
            "duration": 2849
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
            "startOffset": 71444210,
            "duration": 57239884
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
            "startOffset": 128691309,
            "duration": 3927
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
            "startOffset": 128698598,
            "duration": 4123
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
            "startOffset": 128708710,
            "duration": 2900
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              14,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 128716881,
            "duration": 2099
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
            "startOffset": 94101881,
            "duration": 34630096
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
            "startOffset": 128744203,
            "duration": 2818
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
            "startOffset": 128758056,
            "duration": 2286
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              33,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 128767950,
            "duration": 2070
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
            "startOffset": 76231442,
            "duration": 52553260
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
            "startOffset": 128832641,
            "duration": 3922
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
            "startOffset": 128879834,
            "duration": 40721
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
            "startOffset": 129013652,
            "duration": 42210
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
            "startOffset": 129016373,
            "duration": 4376
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
            "startOffset": 73840705,
            "duration": 55274328
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
            "startOffset": 129102179,
            "duration": 2860
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              18,
              "cbo",
              "cbo2002"
            ],
            "parentType": "Cbo",
            "returnType": "String!",
            "fieldName": "cbo2002",
            "startOffset": 129187174,
            "duration": 2799
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
            "startOffset": 129299244,
            "duration": 41555
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
            "startOffset": 129384314,
            "duration": 3881
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
            "startOffset": 129470340,
            "duration": 3707
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
            "startOffset": 129643301,
            "duration": 3756
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
            "startOffset": 129824147,
            "duration": 3767
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
            "startOffset": 129871882,
            "duration": 92825
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
            "startOffset": 130008037,
            "duration": 3524
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
            "startOffset": 130205404,
            "duration": 3730
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
            "startOffset": 75524224,
            "duration": 54894272
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
            "startOffset": 130544926,
            "duration": 4489
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
            "startOffset": 130593186,
            "duration": 40574
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
            "startOffset": 130676858,
            "duration": 3627
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
            "startOffset": 130863839,
            "duration": 3796
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
            "startOffset": 130992605,
            "duration": 3770
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
            "startOffset": 131043786,
            "duration": 40852
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
            "startOffset": 131128581,
            "duration": 3661
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
            "startOffset": 131474248,
            "duration": 9595
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
            "startOffset": 76741455,
            "duration": 54963964
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
            "startOffset": 131871101,
            "duration": 7895
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
            "startOffset": 132016711,
            "duration": 5194
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
            "startOffset": 132104446,
            "duration": 4101
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
            "startOffset": 132201845,
            "duration": 42047
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
            "startOffset": 78269734,
            "duration": 54034316
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
            "startOffset": 132489768,
            "duration": 4945
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
            "startOffset": 132538908,
            "duration": 41374
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
            "startOffset": 132623507,
            "duration": 3602
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
            "startOffset": 132756334,
            "duration": 3836
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
            "startOffset": 132940554,
            "duration": 3819
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
            "startOffset": 132987594,
            "duration": 5459
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
            "startOffset": 133036548,
            "duration": 3577
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
            "startOffset": 133169490,
            "duration": 3711
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
            "startOffset": 80408261,
            "duration": 52907485
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
            "startOffset": 133401703,
            "duration": 41708
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
            "startOffset": 133486929,
            "duration": 3832
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
            "startOffset": 133570361,
            "duration": 5580
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
            "startOffset": 133721587,
            "duration": 42359
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
            "startOffset": 133918508,
            "duration": 42603
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
            "startOffset": 134004310,
            "duration": 3694
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
            "startOffset": 134622029,
            "duration": 4371
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
            "startOffset": 134642154,
            "duration": 99672
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
            "startOffset": 81696935,
            "duration": 53080592
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
            "startOffset": 134886645,
            "duration": 4116
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
            "startOffset": 134915925,
            "duration": 41346
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
            "startOffset": 134982023,
            "duration": 3540
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
            "startOffset": 135314137,
            "duration": 9614
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
            "startOffset": 82854400,
            "duration": 52601458
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
            "startOffset": 135764538,
            "duration": 30576
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
            "startOffset": 135842976,
            "duration": 5484
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
            "startOffset": 136012873,
            "duration": 5409
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
            "startOffset": 136095012,
            "duration": 24006
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
            "startOffset": 136327326,
            "duration": 93594
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
            "startOffset": 136531064,
            "duration": 3844
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
            "startOffset": 136617631,
            "duration": 3819
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
            "startOffset": 136764241,
            "duration": 42172
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
            "startOffset": 83977597,
            "duration": 52880012
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
            "startOffset": 136983453,
            "duration": 4425
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
            "startOffset": 137031550,
            "duration": 93298
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
            "startOffset": 137168174,
            "duration": 3561
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
            "startOffset": 137302845,
            "duration": 3851
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
            "startOffset": 137432958,
            "duration": 3848
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
            "startOffset": 137610703,
            "duration": 3944
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
            "startOffset": 137658610,
            "duration": 41357
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
            "startOffset": 137789894,
            "duration": 3626
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
            "startOffset": 85096492,
            "duration": 52783689
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
            "startOffset": 138019349,
            "duration": 41713
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
            "startOffset": 138104380,
            "duration": 3761
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
            "startOffset": 138189794,
            "duration": 3698
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
            "startOffset": 138283409,
            "duration": 96930
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
            "startOffset": 139455015,
            "duration": 99400
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
            "startOffset": 139584407,
            "duration": 3807
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
            "startOffset": 139653318,
            "duration": 3590
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
            "startOffset": 139825137,
            "duration": 3684
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
            "startOffset": 86101633,
            "duration": 53758464
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
            "startOffset": 140065341,
            "duration": 4075
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
            "startOffset": 140137444,
            "duration": 3868
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
            "startOffset": 140166008,
            "duration": 96415
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
            "startOffset": 140336408,
            "duration": 3672
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
            "startOffset": 87574827,
            "duration": 52886363
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
            "startOffset": 140586685,
            "duration": 42730
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
            "startOffset": 140655920,
            "duration": 4047
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
            "startOffset": 140762945,
            "duration": 4221
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
            "startOffset": 140783976,
            "duration": 3124
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
            "startOffset": 140800914,
            "duration": 3732
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
            "startOffset": 140810499,
            "duration": 2841
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
            "startOffset": 140819828,
            "duration": 2685
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
            "startOffset": 141065673,
            "duration": 3831
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
            "startOffset": 88785769,
            "duration": 52375718
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
            "startOffset": 141395600,
            "duration": 4165
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
            "startOffset": 141524464,
            "duration": 3937
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
            "startOffset": 141627226,
            "duration": 41018
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
            "startOffset": 141814867,
            "duration": 3822
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
            "startOffset": 141990325,
            "duration": 3657
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
            "startOffset": 142130345,
            "duration": 3913
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
            "startOffset": 142233637,
            "duration": 42280
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
            "startOffset": 142504604,
            "duration": 4120
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
            "startOffset": 89806249,
            "duration": 52788876
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
            "startOffset": 142680509,
            "duration": 108225
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
            "startOffset": 142832101,
            "duration": 3807
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
            "startOffset": 142917951,
            "duration": 3699
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
            "startOffset": 143012636,
            "duration": 3170
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
            "startOffset": 143133169,
            "duration": 41538
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
            "startOffset": 143218758,
            "duration": 3822
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
            "startOffset": 143304628,
            "duration": 3674
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
            "startOffset": 143551620,
            "duration": 3818
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
            "startOffset": 90790669,
            "duration": 52887805
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
            "startOffset": 143802748,
            "duration": 4198
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
            "startOffset": 143889032,
            "duration": 3975
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
            "startOffset": 143936253,
            "duration": 40833
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
            "startOffset": 144135336,
            "duration": 3754
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
            "startOffset": 91850521,
            "duration": 52385366
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
            "startOffset": 144323983,
            "duration": 41037
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
            "startOffset": 144408849,
            "duration": 3861
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
            "startOffset": 144546442,
            "duration": 4757
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
            "startOffset": 144679755,
            "duration": 3854
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
            "startOffset": 144769026,
            "duration": 978110
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
            "startOffset": 145812389,
            "duration": 3786
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
            "startOffset": 146506108,
            "duration": 4315
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
            "startOffset": 146583979,
            "duration": 3739
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
            "startOffset": 92680594,
            "duration": 53937452
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
            "startOffset": 146729152,
            "duration": 8547
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
            "startOffset": 147034839,
            "duration": 9864
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
            "startOffset": 147075439,
            "duration": 23542
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
            "startOffset": 147197239,
            "duration": 5522
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
            "startOffset": 147418987,
            "duration": 8469
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
            "startOffset": 147517820,
            "duration": 6626
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
            "startOffset": 147584321,
            "duration": 65579
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
            "startOffset": 147788485,
            "duration": 6102
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
            "startOffset": 93616679,
            "duration": 54269348
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
            "startOffset": 147940588,
            "duration": 24244
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
            "startOffset": 147991153,
            "duration": 11187
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
            "startOffset": 148114579,
            "duration": 5799
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
            "startOffset": 148273929,
            "duration": 6370
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
            "startOffset": 148337037,
            "duration": 24554
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
            "startOffset": 148395354,
            "duration": 14732
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
            "startOffset": 148461341,
            "duration": 8173
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
            "startOffset": 148547337,
            "duration": 4160
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
            "startOffset": 94449928,
            "duration": 54134597
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
            "startOffset": 148654032,
            "duration": 4222
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
            "startOffset": 148702713,
            "duration": 3675
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
            "startOffset": 148730775,
            "duration": 23009
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
            "startOffset": 148831317,
            "duration": 7340
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
            "startOffset": 95159460,
            "duration": 53732784
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
            "startOffset": 148942262,
            "duration": 23487
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
            "startOffset": 148990954,
            "duration": 3424
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
            "startOffset": 149038029,
            "duration": 3360
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
            "startOffset": 149245988,
            "duration": 3414
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
            "startOffset": 149300280,
            "duration": 24578
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
            "startOffset": 149349924,
            "duration": 3335
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
            "startOffset": 149402409,
            "duration": 3414
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
            "startOffset": 149484087,
            "duration": 3415
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
            "startOffset": 96848466,
            "duration": 52668931
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
            "startOffset": 149588626,
            "duration": 4027
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
            "startOffset": 149637736,
            "duration": 3452
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
            "startOffset": 149666696,
            "duration": 21917
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
            "startOffset": 149741954,
            "duration": 3324
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
            "startOffset": 149814904,
            "duration": 3649
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
            "startOffset": 149862099,
            "duration": 3360
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
            "startOffset": 149889887,
            "duration": 22302
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
            "startOffset": 149964116,
            "duration": 3222
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
            "startOffset": 97636731,
            "duration": 52379399
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
            "startOffset": 150186413,
            "duration": 23265
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
            "startOffset": 150236518,
            "duration": 3270
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
            "startOffset": 150286133,
            "duration": 3365
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
            "startOffset": 150434929,
            "duration": 28060
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
            "startOffset": 98872452,
            "duration": 51651393
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
            "startOffset": 150592445,
            "duration": 4206
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
            "startOffset": 150640854,
            "duration": 3492
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
            "startOffset": 150669334,
            "duration": 21983
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
            "startOffset": 150744822,
            "duration": 3446
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
            "startOffset": 150819685,
            "duration": 3572
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
            "startOffset": 150867205,
            "duration": 3455
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
            "startOffset": 150895524,
            "duration": 22028
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
            "startOffset": 150970214,
            "duration": 3325
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
            "startOffset": 100327163,
            "duration": 50695032
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
            "startOffset": 151071139,
            "duration": 89573
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
            "startOffset": 151254371,
            "duration": 3289
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
            "startOffset": 151378682,
            "duration": 3379
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
            "startOffset": 151456629,
            "duration": 3418
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
            "startOffset": 151511903,
            "duration": 22346
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
            "startOffset": 151560658,
            "duration": 24598
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
            "startOffset": 151610100,
            "duration": 3267
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
            "startOffset": 151686398,
            "duration": 3412
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
            "startOffset": 101133064,
            "duration": 50586001
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
            "startOffset": 151790115,
            "duration": 4018
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
            "startOffset": 151840149,
            "duration": 3464
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
            "startOffset": 151868330,
            "duration": 22295
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
            "startOffset": 151942946,
            "duration": 3377
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
            "startOffset": 152014240,
            "duration": 3551
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
            "startOffset": 152061839,
            "duration": 3424
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
            "startOffset": 152089648,
            "duration": 23759
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
            "startOffset": 152214416,
            "duration": 3157
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
            "startOffset": 101848124,
            "duration": 50418538
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
            "startOffset": 152321433,
            "duration": 27338
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
            "startOffset": 152375329,
            "duration": 25311
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
            "startOffset": 152425176,
            "duration": 3287
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
            "startOffset": 152500230,
            "duration": 3322
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
            "startOffset": 102699083,
            "duration": 49833617
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
            "startOffset": 152603633,
            "duration": 4002
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
            "startOffset": 152652577,
            "duration": 3505
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
            "startOffset": 152680646,
            "duration": 21739
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
            "startOffset": 152755381,
            "duration": 3314
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
            "startOffset": 152826844,
            "duration": 9586
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
            "startOffset": 152881518,
            "duration": 6245
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
            "startOffset": 152913260,
            "duration": 26520
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
            "startOffset": 152999082,
            "duration": 4426
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              27,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 127888865,
            "duration": 26978244
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              27,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 154935128,
            "duration": 28430
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              27,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 154991777,
            "duration": 4077
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              28,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 126402328,
            "duration": 28662913
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              28,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 155177702,
            "duration": 13299
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              28,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 155273344,
            "duration": 68806
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              29,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 125624981,
            "duration": 29836602
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              29,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 155611519,
            "duration": 27189
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              29,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 155749336,
            "duration": 3531
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              30,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 123612189,
            "duration": 32332466
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              30,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 156072524,
            "duration": 3469
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              30,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 156102359,
            "duration": 85860
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              31,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 120788773,
            "duration": 35430905
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              31,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 156344411,
            "duration": 42633
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              31,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 156412394,
            "duration": 2879
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              32,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 119124854,
            "duration": 37361753
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              32,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 156610750,
            "duration": 3374
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              32,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 156659529,
            "duration": 21795
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              33,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 117429029,
            "duration": 39303457
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              33,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 156873778,
            "duration": 22159
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              33,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 156994974,
            "duration": 2809
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              34,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 116620695,
            "duration": 40515752
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              34,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 157204355,
            "duration": 3260
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              34,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 157238508,
            "duration": 42638
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              35,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 115576887,
            "duration": 41735590
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              35,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 157447654,
            "duration": 41968
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              35,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 157515118,
            "duration": 2964
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              36,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 114769756,
            "duration": 42885158
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              36,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 157791210,
            "duration": 3579
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              36,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 157843851,
            "duration": 29578
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              37,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 114093217,
            "duration": 43843300
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              37,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 158020587,
            "duration": 29832
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              37,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 158104511,
            "duration": 6927
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              38,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 113982816,
            "duration": 44285244
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              38,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 158341584,
            "duration": 5261
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              38,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 158397055,
            "duration": 84614
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              39,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 113736738,
            "duration": 44794241
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              39,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 158682335,
            "duration": 74242
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              39,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 158845781,
            "duration": 8017
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              40,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 113669208,
            "duration": 45363710
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              40,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 159254816,
            "duration": 8248
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              40,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 159342858,
            "duration": 44746
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              41,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 113417763,
            "duration": 46025765
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              41,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 159534747,
            "duration": 45051
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              41,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 159679309,
            "duration": 3427
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              12,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 113066869,
            "duration": 46710415
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              12,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 159865052,
            "duration": 3618
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              12,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 159914305,
            "duration": 41414
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              13,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112999328,
            "duration": 47007467
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              13,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 160148127,
            "duration": 42267
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              13,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 160236014,
            "duration": 3058
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              14,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112926454,
            "duration": 47402954
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              14,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 160415814,
            "duration": 6329
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              14,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 160520505,
            "duration": 50687
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              15,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112859248,
            "duration": 47764064
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              15,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 160711053,
            "duration": 43382
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              15,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 160797630,
            "duration": 3032
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              16,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112784976,
            "duration": 48149427
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
            "startOffset": 114719821,
            "duration": 46253385
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              16,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 161075602,
            "duration": 3463
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              16,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 161270210,
            "duration": 655796
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              17,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112715935,
            "duration": 49318357
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              17,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 162105353,
            "duration": 22600
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              17,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 162216673,
            "duration": 2957
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              18,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112579235,
            "duration": 49768170
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
            "startOffset": 152967392,
            "duration": 9359534
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              18,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 162447276,
            "duration": 5076
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
            "startOffset": 151915363,
            "duration": 10651584
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              18,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 162478726,
            "duration": 99760
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
            "startOffset": 151658464,
            "duration": 10963291
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
            "startOffset": 150942337,
            "duration": 11694754
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
            "startOffset": 149936742,
            "duration": 12712599
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              19,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112365304,
            "duration": 50246587
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
            "startOffset": 149455303,
            "duration": 13207265
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
            "startOffset": 148515694,
            "duration": 14161140
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
            "startOffset": 147721895,
            "duration": 14973003
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
            "startOffset": 146554842,
            "duration": 16152320
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              19,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 162729161,
            "duration": 100761
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              19,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 162856235,
            "duration": 3167
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
            "startOffset": 143390023,
            "duration": 19476056
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
            "startOffset": 142398371,
            "duration": 20593357
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              20,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112257376,
            "duration": 50794557
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
            "startOffset": 141016172,
            "duration": 22103299
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              20,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 163131315,
            "duration": 4616
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              20,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 163245567,
            "duration": 22786
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
            "startOffset": 138236660,
            "duration": 25040406
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              21,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112182233,
            "duration": 51183083
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
            "startOffset": 137743223,
            "duration": 25676421
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              21,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 163490207,
            "duration": 24533
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              21,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 163560035,
            "duration": 3029
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
            "startOffset": 136717019,
            "duration": 26953383
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              22,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 112069305,
            "duration": 51678920
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
            "startOffset": 134632166,
            "duration": 29168308
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              22,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 163871932,
            "duration": 3527
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
            "startOffset": 133121939,
            "duration": 30767280
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
            "startOffset": 131365016,
            "duration": 32538779
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
            "startOffset": 130159249,
            "duration": 33758187
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
            "startOffset": 128966041,
            "duration": 34965007
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              22,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 163902230,
            "duration": 204737
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
            "startOffset": 126431838,
            "duration": 37767539
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              23,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111949808,
            "duration": 52189539
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
            "startOffset": 125364171,
            "duration": 38921847
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              23,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 164276100,
            "duration": 110207
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              23,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 164411836,
            "duration": 3032
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
            "startOffset": 121678374,
            "duration": 42771771
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              24,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111880392,
            "duration": 52607081
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              24,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 164557158,
            "duration": 3533
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
            "startOffset": 119001844,
            "duration": 45625826
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              24,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 164606371,
            "duration": 22638
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              25,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111620327,
            "duration": 53117693
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
            "startOffset": 117856349,
            "duration": 46900774
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              25,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 164876637,
            "duration": 23118
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
            "startOffset": 115640909,
            "duration": 49257707
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              25,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 164946505,
            "duration": 3039
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              26,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111520299,
            "duration": 53502701
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
            "startOffset": 116383041,
            "duration": 48645086
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              26,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 165163380,
            "duration": 3576
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              26,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 165279237,
            "duration": 40583
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
            "startOffset": 117259275,
            "duration": 48070870
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              4,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111401110,
            "duration": 53971988
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
            "startOffset": 119132229,
            "duration": 46775781
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              4,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 165511811,
            "duration": 532486
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
            "startOffset": 119227249,
            "duration": 47082865
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              4,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 166633257,
            "duration": 5263
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
            "startOffset": 123055439,
            "duration": 43708130
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              5,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111294094,
            "duration": 55475948
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              5,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 166839558,
            "duration": 3539
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              5,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 166964715,
            "duration": 3110
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              6,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 111182995,
            "duration": 55857403
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
            "startOffset": 120116744,
            "duration": 47035155
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              6,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 167131508,
            "duration": 25071
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              6,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 167256829,
            "duration": 3136
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              7,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 110684737,
            "duration": 56647723
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              7,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 167451942,
            "duration": 3474
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              7,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 167519919,
            "duration": 3089
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
            "startOffset": 149713318,
            "duration": 17882942
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              8,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 110573432,
            "duration": 57069733
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              8,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 167671525,
            "duration": 93256
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              8,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 167794309,
            "duration": 2995
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              9,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 110445164,
            "duration": 57369736
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              9,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 167846244,
            "duration": 3507
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              9,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 167916297,
            "duration": 3028
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              10,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 110300268,
            "duration": 57732750
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              10,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 168154977,
            "duration": 3587
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              10,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 168273914,
            "duration": 23754
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
            "startOffset": 133674490,
            "duration": 34608772
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              11,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 109768000,
            "duration": 58622422
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              11,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 168742556,
            "duration": 3476
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              11,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 168883937,
            "duration": 3099
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
            "startOffset": 120827536,
            "duration": 48059262
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              0,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 109643116,
            "duration": 59376901
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              0,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 169158575,
            "duration": 3545
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              0,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 169207328,
            "duration": 40723
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              1,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 109517897,
            "duration": 59782219
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
            "startOffset": 122442888,
            "duration": 47033704
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              1,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 169445622,
            "duration": 3472
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              1,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 169631758,
            "duration": 3037
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              2,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 109387688,
            "duration": 60338163
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              2,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 169811146,
            "duration": 3525
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              2,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 169960690,
            "duration": 3070
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
            "startOffset": 123643373,
            "duration": 46469296
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              3,
              "unidadeSaude",
              "endereco",
              "uf"
            ],
            "parentType": "Endereco",
            "returnType": "UF",
            "fieldName": "uf",
            "startOffset": 109190172,
            "duration": 60971830
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              3,
              "unidadeSaude",
              "endereco",
              "uf",
              "sigla"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "sigla",
            "startOffset": 170248649,
            "duration": 3664
          },
          {
            "path": [
              "sessao",
              "profissional",
              "lotacoes",
              3,
              "unidadeSaude",
              "endereco",
              "uf",
              "nome"
            ],
            "parentType": "UF",
            "returnType": "String!",
            "fieldName": "nome",
            "startOffset": 170296403,
            "duration": 41100
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
            "startOffset": 124793344,
            "duration": 45798947
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
            "startOffset": 152472489,
            "duration": 18547252
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
            "startOffset": 140287762,
            "duration": 31208638
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
            "startOffset": 125266602,
            "duration": 46511934
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
            "startOffset": 152727448,
            "duration": 19598319
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
            "startOffset": 141767142,
            "duration": 31325840
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
            "startOffset": 140773327,
            "duration": 33083375
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
            "startOffset": 125320287,
            "duration": 49424670
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
            "startOffset": 143001990,
            "duration": 32311162
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
            "startOffset": 125609704,
            "duration": 50196425
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
            "startOffset": 144088015,
            "duration": 32301339
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
            "startOffset": 127570745,
            "duration": 48984299
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
            "startOffset": 144632496,
            "duration": 32181690
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
            "startOffset": 128335417,
            "duration": 48730593
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
            "startOffset": 147125127,
            "duration": 30402459
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
            "startOffset": 129554087,
            "duration": 48492320
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
            "startOffset": 148235512,
            "duration": 30363608
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
            "startOffset": 130814190,
            "duration": 48414840
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
            "startOffset": 148778352,
            "duration": 31057051
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
            "startOffset": 132152352,
            "duration": 48019892
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
            "startOffset": 150716623,
            "duration": 31357260
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
            "startOffset": 149149367,
            "duration": 33258103
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
            "startOffset": 136044106,
            "duration": 47204931
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
            "startOffset": 132708076,
            "duration": 50864308
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
            "startOffset": 150389221,
            "duration": 33784738
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
            "startOffset": 135199060,
            "duration": 50506951
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
            "startOffset": 151427497,
            "duration": 35431862
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
            "startOffset": 137253600,
            "duration": 50390334
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
            "startOffset": 152182578,
            "duration": 36059345
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
            "startOffset": 139755069,
            "duration": 49180823
          }
        ]
      }
    }
  },
  "data": {
    "sessao": {
      "id": "962ab9e4-07bd-461c-b0ab-39c589ae6464",
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "112",
              "nome": "GERENTE DE SERVIÇOS DE SAÚDE",
              "cbo2002": "131210"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "5",
              "nome": "Ceo",
              "cnes": "5444433",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "958",
              "nome": "TÉCNICO EM SAÚDE BUCAL",
              "cbo2002": "322405"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "5",
              "nome": "Ceo",
              "cnes": "5444433",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "960",
              "nome": "AUXILIAR EM SAÚDE BUCAL",
              "cbo2002": "322415"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "5",
              "nome": "Ceo",
              "cnes": "5444433",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "364",
              "nome": "CIRURGIÃO DENTISTA - CLÍNICO GERAL",
              "cbo2002": "223208"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "5",
              "nome": "Ceo",
              "cnes": "5444433",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "411",
              "nome": "TÉCNICO EM ORIENTAÇÃO E MOBILIDADE DE CEGOS E DEFICIENTES VISUAIS",
              "cbo2002": "2236I1"
            },
            "equipe": {
              "id": "14",
              "nome": "EMAD2"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "412",
              "nome": "FISIOTERAPEUTA GERAL",
              "cbo2002": "223605"
            },
            "equipe": {
              "id": "15",
              "nome": "EMAP"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1341",
              "nome": "AGENTE COMUNITÁRIO DE SAÚDE",
              "cbo2002": "515105"
            },
            "equipe": {
              "id": "15",
              "nome": "EMAP"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "112",
              "nome": "GERENTE DE SERVIÇOS DE SAÚDE",
              "cbo2002": "131210"
            },
            "equipe": {
              "id": "15",
              "nome": "EMAP"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "678",
              "nome": "PSICÓLOGO CLÍNICO",
              "cbo2002": "251510"
            },
            "equipe": {
              "id": "14",
              "nome": "EMAD2"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "947",
              "nome": "TÉCNICO DE ENFERMAGEM",
              "cbo2002": "322205"
            },
            "equipe": {
              "id": "14",
              "nome": "EMAD2"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "397",
              "nome": "ENFERMEIRO",
              "cbo2002": "223505"
            },
            "equipe": {
              "id": "13",
              "nome": "EMAD1"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": {
              "id": "13",
              "nome": "EMAD1"
            },
            "unidadeSaude": {
              "id": "4",
              "nome": "Unidade de Atendimento AD",
              "cnes": "5444428",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": {
              "id": "12",
              "nome": "NASF I"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "411",
              "nome": "TÉCNICO EM ORIENTAÇÃO E MOBILIDADE DE CEGOS E DEFICIENTES VISUAIS",
              "cbo2002": "2236I1"
            },
            "equipe": {
              "id": "10",
              "nome": "EAB2"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1262",
              "nome": "RECEPCIONISTA DE CONSULTÓRIO MÉDICO OU DENTÁRIO",
              "cbo2002": "422110"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "958",
              "nome": "TÉCNICO EM SAÚDE BUCAL",
              "cbo2002": "322405"
            },
            "equipe": {
              "id": "9",
              "nome": "ESB M2 ESUS"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "960",
              "nome": "AUXILIAR EM SAÚDE BUCAL",
              "cbo2002": "322415"
            },
            "equipe": {
              "id": "9",
              "nome": "ESB M2 ESUS"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "364",
              "nome": "CIRURGIÃO DENTISTA - CLÍNICO GERAL",
              "cbo2002": "223208"
            },
            "equipe": {
              "id": "9",
              "nome": "ESB M2 ESUS"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1218",
              "nome": "DIGITADOR",
              "cbo2002": "412110"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "412",
              "nome": "FISIOTERAPEUTA GERAL",
              "cbo2002": "223605"
            },
            "equipe": {
              "id": "10",
              "nome": "EAB2"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1341",
              "nome": "AGENTE COMUNITÁRIO DE SAÚDE",
              "cbo2002": "515105"
            },
            "equipe": {
              "id": "8",
              "nome": "EACS"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "112",
              "nome": "GERENTE DE SERVIÇOS DE SAÚDE",
              "cbo2002": "131210"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "678",
              "nome": "PSICÓLOGO CLÍNICO",
              "cbo2002": "251510"
            },
            "equipe": {
              "id": "10",
              "nome": "EAB2"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "947",
              "nome": "TÉCNICO DE ENFERMAGEM",
              "cbo2002": "322205"
            },
            "equipe": {
              "id": "10",
              "nome": "EAB2"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "397",
              "nome": "ENFERMEIRO",
              "cbo2002": "223505"
            },
            "equipe": {
              "id": "10",
              "nome": "EAB2"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": {
              "id": "11",
              "nome": "EMAD2"
            },
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "3",
              "nome": "Unidade Basica de Saude Agronomica",
              "cnes": "5444430",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": {
              "id": "6",
              "nome": "NASF I"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "411",
              "nome": "TÉCNICO EM ORIENTAÇÃO E MOBILIDADE DE CEGOS E DEFICIENTES VISUAIS",
              "cbo2002": "2236I1"
            },
            "equipe": {
              "id": "4",
              "nome": "EAB1"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1262",
              "nome": "RECEPCIONISTA DE CONSULTÓRIO MÉDICO OU DENTÁRIO",
              "cbo2002": "422110"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "958",
              "nome": "TÉCNICO EM SAÚDE BUCAL",
              "cbo2002": "322405"
            },
            "equipe": {
              "id": "3",
              "nome": "ESB M1 ESUS"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "960",
              "nome": "AUXILIAR EM SAÚDE BUCAL",
              "cbo2002": "322415"
            },
            "equipe": {
              "id": "3",
              "nome": "ESB M1 ESUS"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "364",
              "nome": "CIRURGIÃO DENTISTA - CLÍNICO GERAL",
              "cbo2002": "223208"
            },
            "equipe": {
              "id": "3",
              "nome": "ESB M1 ESUS"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1218",
              "nome": "DIGITADOR",
              "cbo2002": "412110"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "412",
              "nome": "FISIOTERAPEUTA GERAL",
              "cbo2002": "223605"
            },
            "equipe": {
              "id": "4",
              "nome": "EAB1"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "1341",
              "nome": "AGENTE COMUNITÁRIO DE SAÚDE",
              "cbo2002": "515105"
            },
            "equipe": {
              "id": "2",
              "nome": "EACS"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "112",
              "nome": "GERENTE DE SERVIÇOS DE SAÚDE",
              "cbo2002": "131210"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "678",
              "nome": "PSICÓLOGO CLÍNICO",
              "cbo2002": "251510"
            },
            "equipe": {
              "id": "4",
              "nome": "EAB1"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "947",
              "nome": "TÉCNICO DE ENFERMAGEM",
              "cbo2002": "322205"
            },
            "equipe": {
              "id": "4",
              "nome": "EAB1"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "397",
              "nome": "ENFERMEIRO",
              "cbo2002": "223505"
            },
            "equipe": {
              "id": "4",
              "nome": "EAB1"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": {
              "id": "5",
              "nome": "EMAD1"
            },
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
            "tipo": "LOTACAO",
            "ativo": True,
            "cbo": {
              "id": "461",
              "nome": "MÉDICO DA ESTRATÉGIA DE SAÚDE DA FAMÍLIA",
              "cbo2002": "225142"
            },
            "equipe": None,
            "unidadeSaude": {
              "id": "2",
              "nome": "Unidade Basica de Saude Centro",
              "cnes": "8007535",
              "endereco": {
                "uf": {
                  "sigla": "SC",
                  "nome": "SANTA CATARINA"
                }
              }
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
