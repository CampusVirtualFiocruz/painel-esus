import os

import duckdb
import polars as pl
from duckdb import DuckDBPyConnection
from src.domain.dict_types.acceptance_term import AcceptanceTerm
from src.errors.types import HttpNotFoundError
from src.infra.db.settings.connection_duckdb import DuckDbHandler, duck_db_handler

from .sqls import find_all, find_by_username_ibge, find_by_username_ibge_version


class AcceptanceTermRepository:
    def __init__(self):
        self.db = DuckDbHandler()

    def save(self, acceptance_term: AcceptanceTerm):
        working_directory = os.getcwd()
        input_path = os.path.join(working_directory, "dados", "settings")
        file_path = input_path + os.sep + "acceptance_term.parquet"
        if os.path.exists(file_path):
            term_base = pl.read_parquet(file_path)
            try:
                self.db.fetch_one_dict(
                    find_by_username_ibge_version(),
                    {
                        "username": acceptance_term.get("username"),
                        "ibge": acceptance_term.get("cod_ibge"),
                        "version": acceptance_term.get("version", "1.0"),
                    },
                )
            except HttpNotFoundError:
                new_record = pl.DataFrame(acceptance_term)
                term_base = pl.concat([term_base, new_record])
                term_base.write_parquet(file_path)
        else:
            term_base = pl.DataFrame(acceptance_term)
            term_base.write_parquet(file_path)

    def find_all(self):
        con = duck_db_handler()
        return next(con).sql(find_all()).fetchall()

    def find_username_ibge(self, username: str, ibge: str):
        return self.db.fetch_all_dict(
            find_by_username_ibge(),
            {
                "username": username,
                "ibge": ibge,
            },
        )

    def find_username_ibge_version(self, username: str, ibge: str, version: str):
        return self.db.fetch_all_dict(
            find_by_username_ibge_version(),
            {
                "username": username,
                "ibge": ibge,
                "version": version
            },
        )
