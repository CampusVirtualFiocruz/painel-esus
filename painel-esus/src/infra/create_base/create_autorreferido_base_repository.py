# pylint: disable= R1703, W0612,C0103
import pandas as pd
import polars as pl
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import ResourceClosedError
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.errors import InvalidArgument
from src.errors import NoSuchTableError
from src.errors.logging import logging
from src.infra.db.repositories.sqls.nominal_list.autoreferido import AUTORREFERIDO
from src.infra.db.repositories.update_bases import UpdateBasesRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


class CreateAutorreferidoBaseRepository(CreateBasesRepositoryInterface):
    _base = 'autorreferidos'
    schema = {
        "cidadao_pec": pl.UInt64(),
        "st_hipertensao_arterial": pl.String(),
        "st_diabete": pl.String(),
    }

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def destroy_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            update_base_repository = UpdateBasesRepository()
            update_base_repository.destroy_bases(self._base)
        except (OperationalError, ResourceClosedError) as exc:
            raise NoSuchTableError(
                f'No {self.get_base()} table found') from exc

    def create_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            self.destroy_base()
        except NoSuchTableError:
            logging.info(f'Base {self._base} already destroyed!')
        try:
            local_db = LocalDBConnectionHandler()
            local_engine = local_db.get_engine()
            _next = True
            offset = 0
            chunk_size = 1000
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    df = pd.read_sql_query(
                        text(f"{AUTORREFERIDO}  LIMIT {chunk_size} OFFSET {offset};"),
                        con=engine,
                    )

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                              if_exists='append')

        except NoSuchTableError:
            logging.info(f'Erro {self._base} already destroyed!')
