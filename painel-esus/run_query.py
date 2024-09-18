import pandas as pd
from src.errors.logging import logging
from src.infra.db.settings.connection_local import DBConnectionHandler


def get_tables():
    with DBConnectionHandler() as conn:
        engine = conn.get_engine()
        return pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type='table';", con=engine
        )


logging.info("BEGIN TABLES")
logging.info(f"\n{get_tables()}")
logging.info("END TABLES")
