"""Demografia: População do IBGE.

Lê um CSV local com colunas "IBGE" e "POPULACAO" e retorna a população
formatada (ex.: 123.456) do município configurado via variável de ambiente
"CIDADE_IBGE".
"""

import os
from pathlib import Path

import pandas as pd
from src.env.conf import env
from src.errors.logging import logging


class IBGEPopulationRepository:

    def __init__(self, csv_path: str = None):
        """Define o caminho do CSV do IBGE. Usa "ibge.csv" no diretório atual
        por padrão."""
        self.csv_path = csv_path or os.path.join(Path(os.getcwd()), "ibge.csv")

    def get_ibge_population(self):
        """Retorna população do município (a partir de "CIDADE_IBGE").

        Em falhas ou IBGE não configurado, retorna 0.
        """
        df = pd.read_csv(self.csv_path, sep=";")

        ibge = int(env.get("CIDADE_IBGE", 0))
        if ibge == "-":
            ibge_population = 0
        else:
            try:
                df_ibge = df[df["IBGE"] == ibge]
                ibge_population = df_ibge["POPULACAO"].iloc[0]
                ibge_population = f"{ibge_population:_.0f}".replace("_", ".")
            except Exception as exc:
                logging.exception(exc)
                ibge_population = 0
        return ibge_population
