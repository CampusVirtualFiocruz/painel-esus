import json

import pandas as pd

# Abrir o arquivo JSON
with open('painel-esus-logs.authlogs.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

ibge = pd.read_csv('ibge.csv', sep=';')

linhas = []

# Percorrer os objetos e imprimir os campos desejados
for item in dados:
    data = item.get("createdAt", {}).get("$date", "Data não encontrada")
    codigo_ibge = item.get("codigoIbge", "Código não encontrado")
    version = item.get("version", "Versão não encontrada")
    row = ibge[ibge['IBGE'].astype(str).str.contains(item['codigoIbge'])]
    if row.shape[0] > 0:
        uf = row["UF"].values[0]
        city = row["NOME DO MUNICIPIO"].values[0]
        linha = {
            "codigoIbge": item.get("codigoIbge"),
            "createdAt": item.get("createdAt", {}).get("$date"),
            "uf": uf,
            "cidade": city,
            "versão": version
        }
        linhas.append(linha)

df = pd.DataFrame(linhas)
df.to_csv("logs_exported.csv", sep=';', index=False)
