import pandas as pd

from ..settings.connection_local import DBConnectionHandler


class UpdateBasesRepository:

    def __init__(self):
        ...

    def update_bases(self, cares, base_table: str):

        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            cares = cares.drop_duplicates()
            cares.to_sql(name=base_table, con=engine, if_exists='replace')

    def check_bases(self, base_table: str):
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = f'SELECT * FROM {base_table};'
            return pd.read_sql_query(sql, con=engine)
