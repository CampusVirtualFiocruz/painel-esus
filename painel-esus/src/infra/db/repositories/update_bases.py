import pandas as pd
from sqlalchemy.exc import OperationalError
from src.errors import NoSuchTableError
from src.infra.db.settings.connection_local import DBConnectionHandler


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
            try:
                engine = db_con.get_engine()
                sql = f'SELECT * FROM {base_table};'
                return pd.read_sql_query(sql, con=engine)
            except OperationalError as exc:
                raise NoSuchTableError(
                    f'No {base_table} table found.') from exc

    def check_table_exists(self, base_table: str):
        with DBConnectionHandler() as db_con:
            try:
                sql = f"""
                    SELECT 
                        name
                    FROM 
                        sqlite_schema
                    WHERE 
                        type ='table' AND 
                        name NOT LIKE 'sqlite_%' AND name='{base_table}';"""
                engine = db_con.get_engine()
                return pd.read_sql_query(sql, con=engine)
            except OperationalError as exc:
                raise NoSuchTableError(
                    f'No {base_table} table found.') from exc

    def destroy_bases(self, base_table: str):
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = f'DROP TABLE {base_table};'
            return pd.read_sql_query(sql, con=engine)
