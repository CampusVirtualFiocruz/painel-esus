import pandas as pd
from src.infra.db.settings.connection_local import DBConnectionHandler


class Disease:

    def __init__(self):
        self.target = []

    def filter_registers(self, data_frame: any) -> any:
        target_df = data_frame
        target_df = target_df.drop_duplicates()
        mask = target_df["codigo"].isin(self.target)
        return target_df.loc[mask]

    def filter_registers_sql(self, table: str) -> any:
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = f"""with table_lista as (select  distinct (co_fat_cidadao_pec) co_fat_cidadao_pec, co_dim_tipo_localizacao  from {table} h)
select co_dim_tipo_localizacao, count(*) valor from table_lista group by 1;
"""
            return pd.read_sql_query(sql, con=engine)
