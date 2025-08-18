import json
import logging
import os
from pathlib import Path

from src.env.conf import env


def get_ibge_total():
    path = os.getcwd()
    path = Path(path)
    path = os.path.join(path, "ibge.json")
    with open(path, "r") as file:
        ibge_json = json.load(file)

    ibge = int(env.get("CIDADE_IBGE", 0))

    if ibge == "-":
        ibge_population = 0
    else:
        filtered = list(filter(lambda x: x["IBGE"] == ibge, ibge_json))
        if len(filtered) > 0:
            ibge_population = filtered[0]["POPULACAO"]
        else:
            ibge_population = 0     
    return ibge_population
