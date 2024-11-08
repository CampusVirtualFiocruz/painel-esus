# pylint: disable= R1703, W0612,C0103
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.errors import InvalidArgument
from src.errors import NoSuchTableError
from src.errors.logging import logging
from src.infra.db.repositories.sqls.tabelas import TABELAS
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


class CreateStructureBaseRepository(CreateBasesRepositoryInterface):
    _base = 'estrutura'
    def get_base(self):
        return self._base

    def destroy_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')

    def create_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            with LocalDBConnectionHandler().get_engine().connect() as con:
                for tabela in TABELAS:
                    statement = text(f"{tabela}")
                    con.execute(
                        statement,
                    )
                    con.commit()

        except NoSuchTableError:
            logging.info(f'Erro {self._base} already destroyed!')
