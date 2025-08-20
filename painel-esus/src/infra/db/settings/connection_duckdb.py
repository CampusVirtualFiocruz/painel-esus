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
    description = None

    def _parse_columns(self, description):
        return [desc[0] for desc in description]

    def fetchall(self, sql):
        with DuckDBConnectionHandler() as conn:
            resp = conn.session.execute(sql).fetchall()
            self.description = conn.session.description
            self.columns = self._parse_columns(self.description)
            return resp

    def fetchone(self, sql):
        with DuckDBConnectionHandler() as conn:
            resp = conn.session.execute(sql).fetchone()
            self.description = conn.session.description
            self.columns = self._parse_columns(self.description)
            return resp

    def fetch_df(self, sql):
        with DuckDBConnectionHandler() as conn:
            resp = conn.session.execute(sql).df()
            self.description = conn.session.description
            self.columns = self._parse_columns(self.description)
            return resp

    def get_description(self):
        return self.description
    
    def get_columns(self):
        return self.columns
