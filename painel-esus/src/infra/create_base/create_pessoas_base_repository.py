# pylint: disable= R1703, W0612,C0103
import os

import pandas as pd
import polars as pl
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, ResourceClosedError
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.env.conf import getenv
from src.errors import InvalidArgument, NoSuchTableError
from src.errors.logging import logging
from src.infra.db.repositories.sqls.pessoa.pessoas import (
    pessoas_tb_acompanhamento as PESSOAS,
)
from src.infra.db.repositories.sqls.pessoa.status_cadastro import status_cadastro
from src.infra.db.repositories.update_bases import UpdateBasesRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)

schema_overrides = {
    "id_cidadao_pec": pl.UInt64(),
    "co_cidadao": pl.String(),
    "nu_cns": pl.String(),
    "nu_cpf": pl.String(),
    "no_cidadao": pl.String(),
    "co_dim_tempo_nascimento": pl.Date(),
    "no_social_cidadao": pl.String(),
    "co_dim_unidade_saude": pl.UInt64(),
    "co_dim_sexo": pl.UInt64(),
    "sg_sexo": pl.String(),
    "co_dim_identidade_genero": pl.UInt64(),
    "ds_raca_cor": pl.String(),
    "co_dim_tipo_localizacao": pl.UInt64(),
    "no_mae_cidadao": pl.String(),
    "no_pai_cidadao": pl.String(),
    "no_profissional": pl.String(),
    "dt_obito": pl.Date(),
    "nu_declaracao_obito": pl.String(),
    "idade": pl.UInt64(),
    "total_meses": pl.UInt64(),
    "total_dias": pl.UInt64()
}

class CreatePessoasBaseRepository(CreateBasesRepositoryInterface):
    _base = 'pessoas'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def destroy_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            update_base_repository = UpdateBasesRepository()
            # update_base_repository.destroy_bases(self._base)
            try:
                os.remove("dados/input/pessoas.csv")
            except FileNotFoundError:
                ...
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
            chunk_size = getenv("CHUNK_SIZE", 1000)
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    df = pd.read_sql_query(
                        text(f'{PESSOAS}  LIMIT {chunk_size} OFFSET {offset};'), con=engine)

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                              if_exists='append')
                    df.to_csv("dados/input/pessoas.csv", mode='a', index=False,sep=";")

        except NoSuchTableError:
            logging.info(f'Erro {self._base} already destroyed!')

    # def create_base3(self):
    #     if self._base is None:
    #         raise InvalidArgument('Creation base not passed.')
    #     try:
    #         self.destroy_base()
    #     except NoSuchTableError:
    #         logging.info(f'Base {self._base} already destroyed!')
    #     try:
    #         chunk_size = getenv("CHUNK_SIZE", 1000)
    #         local_db = LocalDBConnectionHandler()
    #         local_engine = local_db.get_engine()
    #         working_directory  = os.getcwd()
    #         input_path = os.path.join(working_directory, "dados", "input") 
    #         parquet_file = 'pessoas.parquet'
    #         with DBConnectionHandler() as db:
    #             (
    #                 pl.read_database(
    #                     PESSOAS,
    #                     connection=db.get_engine(),
    #                     schema_overrides=schema_overrides,
    #                 )
    #                 .lazy()
    #                 .collect(streaming=True)
    #                 .with_columns(
    #                     pl.col(f"dt_obito").dt.strftime("%Y-%m-%d"),
    #                     pl.col(f"co_dim_tempo_nascimento").dt.strftime("%Y-%m-%d"),
    #                 )
    #                 .write_parquet(input_path + os.sep + parquet_file)
    #                 .write_database(
    #                     if_table_exists="append",
    #                     connection=local_engine,
    #                     table_name="pessoas",
    #                     engine="sqlalchemy",
    #                 )
    #             )

    #     except NoSuchTableError:
    #         logging.info(f'Erro {self._base} already destroyed!')


class CreateStatusRecordsRepository(CreateBasesRepositoryInterface):
    _base = "status_records"
    def destroy_base(self):
        if self._base is None:
            raise InvalidArgument("Creation base not passed.")

    def create_base(self):
        if self._base is None:
            raise InvalidArgument("Creation base not passed.")
        try:
            self.destroy_base()
        except NoSuchTableError:
            logging.info(f"Base {self._base} already destroyed!")
        try:
            local_db = LocalDBConnectionHandler()
            local_engine = local_db.get_engine()
            _next = True
            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 1000)
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    sql = status_cadastro()
                    df = pd.read_sql_query(
                        text(f"{sql}  LIMIT {chunk_size} OFFSET {offset};"),
                        con=engine,
                    )

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine, if_exists="append")

        except NoSuchTableError:
            logging.info(f"Erro {self._base} already destroyed!")
