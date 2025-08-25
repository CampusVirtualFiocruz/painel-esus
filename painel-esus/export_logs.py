import pandas as pd

logs = [
  {
    "codigoIbge": "2311108",
    "createdAt": "16/04/2025 10:38:44"
  },
  {
    "codigoIbge": "3158953",
    "createdAt": "16/04/2025 23:33:27"
  },
  {
    "codigoIbge": "2211407",
    "createdAt": "16/04/2025 09:27:30"
  },
  {
    "codigoIbge": "3141405",
    "createdAt": "08/04/2025 14:42:07"
  },
  {
    "codigoIbge": "5216007",
    "createdAt": "16/04/2025 08:24:39"
  },
  {
    "codigoIbge": "2403202",
    "createdAt": "16/04/2025 10:43:37"
  },
  {
    "codigoIbge": "2208106",
    "createdAt": "16/04/2025 13:42:26"
  },
  {
    "codigoIbge": "2307635",
    "createdAt": "16/04/2025 11:53:41"
  },
  {
    "codigoIbge": "3163805",
    "createdAt": "11/04/2025 11:55:11"
  },
  {
    "codigoIbge": "1302603",
    "createdAt": "14/04/2025 20:14:30"
  },
  {
    "codigoIbge": "314140",
    "createdAt": "27/03/2025 14:40:04"
  },
  {
    "codigoIbge": "2508505",
    "createdAt": "17/04/2025 10:33:55"
  },
  {
    "codigoIbge": "2210383",
    "createdAt": "16/04/2025 18:04:22"
  },
  {
    "codigoIbge": "3171303",
    "createdAt": "08/04/2025 15:04:27"
  },
  {
    "codigoIbge": "2311355",
    "createdAt": "15/04/2025 16:09:41"
  },
  {
    "codigoIbge": "3111705",
    "createdAt": "11/04/2025 11:56:52"
  },
  {
    "codigoIbge": "2609307",
    "createdAt": "15/04/2025 08:24:05"
  },
  {
    "codigoIbge": "2205599",
    "createdAt": "16/04/2025 17:11:11"
  },
  {
    "codigoIbge": "2303709",
    "createdAt": "16/04/2025 12:46:35"
  },
  {
    "codigoIbge": "2202752",
    "createdAt": "16/04/2025 13:40:05"
  }
]

ibge = pd.read_csv('ibge.csv', sep=';')

for log in logs:

    row = ibge[ibge['IBGE'].astype(str).str.contains(log['codigoIbge'])]
    if row.shape[0] > 0:
        uf = row["UF"].values[0]
        city = row["NOME DO MUNICIPIO"].values[0]
        log['uf'] = uf
        log['cidade'] = city
    
log_csv = pd.DataFrame(data=logs)
log_csv.to_csv("logs_exported.csv", sep=';', index=False)
