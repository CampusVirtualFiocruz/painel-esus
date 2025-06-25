# pylint: disable=W0611
import duckdb


class DuckDBConnectionHandler:

    def __init__(self) -> None:
        self.session = None

    def __enter__(self):
        self.session = duckdb.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


class DuckDbHandler:

    def fetchall(self, sql):
        with DuckDBConnectionHandler() as conn:
            resp = conn.session.execute(sql).fetchall()
            return resp

    def fetch_df(self, sql):
        with DuckDBConnectionHandler() as conn:
            resp = conn.session.execute(sql).df()
            return resp
