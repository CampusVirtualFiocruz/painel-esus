import polars as pl
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import ResourceClosedError
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.errors import InvalidArgument
from src.errors import NoSuchTableError
from src.errors.logging import logging
from src.infra.create_base.create_local_database import CreateLocalDataBase
from src.infra.db.repositories.sqls.units_list import UNITS_LIST_GEN


class CreateLocalUnitsDatabase(CreateLocalDataBase, CreateBasesRepositoryInterface):
    table_name = "unidades"

    def get_base(self):
        return self.table_name

    def create_base(self):
        schema_overrides = {
            "co_seq_dim_unidade_saude": pl.UInt64(),
            "nu_cnes": pl.String(),
            "no_unidade_saude": pl.String(),
        }
        sql = UNITS_LIST_GEN
        self.create_table(self.table_name, sql, schema_overrides)
        logging.info(f"Creating Base {self.table_name}!")

    def destroy_base(self):
        if self.table_name is None:
            raise InvalidArgument("Creation base not passed.")
        try:
            self.drop_table(self.table_name)
        except (OperationalError, ResourceClosedError) as exc:
            raise NoSuchTableError(f"No {self.table_name} table found") from exc
