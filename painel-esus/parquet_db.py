import os
import time

import pandas as pd
from src.infra.db.settings.connection_local import DBConnectionHandler


def gerar_banco():
    current_dir = os.getcwd()
    # print(os.path.join(current_dir, "dados", "output", "crianca.parquet"))
    bases = [
        ("crianca", os.path.join(current_dir, "dados", "output", "crianca.parquet")),
        ("idoso", os.path.join(current_dir, "dados", "output", "idoso.parquet")),
        # ("equipes", "./dados/output/equipe.parquet"),
    ]

    def create_base(base):
        time.sleep(5)
        data = pd.read_parquet(base[1])

        with DBConnectionHandler() as con:
            engine = con.get_engine()
            data.to_sql(name=base[0], con=engine, if_exists="append")

    for base in bases:
        create_base(base)
