# pylint: disable=W0611
from collections.abc import Generator

import duckdb
from src.errors.types.http_not_found import HttpNotFoundError


class DuckDBConnectionHandler:

    def __init__(self) -> None:
        self.session = None

    def __enter__(self):
        self.session = duckdb.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def duck_db_handler() -> Generator[duckdb.DuckDBPyConnection]:
    with duckdb.connect() as con:
        yield con
    duckdb.close()


class DuckDbHandler:
    description = None

    def fetch_all_dict(self, sql: str, params: dict = None):
        con = duck_db_handler()
        statement = next(con).execute(
            sql,
            params,
        )
        columns = [col[0] for col in statement.description]
        result = statement.fetchall()
        items = [dict(zip(columns, row)) for row in result]
        return items

    def fetch_one_dict(self, sql: str, params: dict = None):
        con = duck_db_handler()
        statement = next(con).execute(
                sql,
                params,
            )
        columns = [col[0] for col in statement.description]
        result = statement.fetchone()
        if result is not None:
            items = dict(zip(columns, result))
            return items
        raise HttpNotFoundError("Record Not Found.")

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
