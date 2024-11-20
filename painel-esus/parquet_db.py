import pandas as pd
from src.infra.db.settings.connection_local import DBConnectionHandler

bases = [
    ("crianca", "./dados/output/crianca.parquet"),
    ("idoso", "./dados/output/idoso.parquet"),
    # ("equipes", "./dados/output/equipe.parquet"),
]

def create_base(base):
    data = pd.read_parquet(base[1])

    with DBConnectionHandler() as con:
        engine = con.get_engine()
        data.to_sql(name=base[0], con=engine, if_exists="append")

for base in bases:
    create_base(base)
