import os
from pathlib import Path

import pandas as pd
from src.env.conf import env
from src.errors.logging import logging


class IBGEPopulationRepository:

    def __init__(self, csv_path: str = None):
        self.csv_path = csv_path or os.path.join(Path(os.getcwd()), "ibge.csv")

    def get_ibge_population(self):
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
