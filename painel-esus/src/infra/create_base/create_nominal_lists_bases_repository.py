# pylint: disable= R1703
import pandas as pd
import polars as pl
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import ResourceClosedError
from src.data.interfaces.create_bases.create_bases_repository import \
    CreateBasesRepositoryInterface
from src.errors import InvalidArgument
from src.errors import NoSuchTableError
from src.errors.logging import logging
from src.infra.db.repositories.sqls.nominal_list import LISTA_NOMINAL_DIABETES
from src.infra.db.repositories.sqls.nominal_list import LISTA_NOMINAL_HIPERTENSAO
from src.infra.db.repositories.update_bases import UpdateBasesRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import \
    DBConnectionHandler as LocalDBConnectionHandler


class CreateNominalListsBasesRepository(CreateBasesRepositoryInterface):
    _base = None
    schema = {
        "co_fat_cidadao_pec": pl.UInt64(),
        "no_cidadao": pl.String(),
        "nu_cns": pl.String(),
        "nu_cpf": pl.String(),
        "no_sexo": pl.String(),
        "no_raca_cor": pl.String(),
        "nu_micro_area": pl.String(),
        "nu_area": pl.String(),
        "dt_nascimento": pl.Date(),
        "ds_logradouro": pl.String(),
        "no_bairro": pl.String(),
        "nu_numero": pl.String(),
        "ds_cep": pl.String(),
        "no_localidade": pl.String(),
        "no_uf": pl.String(),
        "sg_uf": pl.String(),
        "no_tipo_logradouro": pl.String(),
        "co_dim_equipe": pl.UInt64(),
        "co_dim_unidade_saude": pl.UInt64(),
        "co_dim_tempo": pl.Date(),
        "data_ultima_visita_acs": pl.Date(),
        "alerta_visita_acs": pl.Boolean(),
        "total_consulta_individual_medico": pl.UInt64(),
        "alerta_total_de_consultas_medico": pl.Boolean(),
        "ultimo_atendimento_medico": pl.Date(),
        "alerta_ultima_consulta_medico": pl.Boolean(),
        "ultimo_atendimento_odonto": pl.Date(),
        "alerta_ultima_consulta_odontologica": pl.Boolean(),
        "ultima_data_afericao_pa": pl.Date(),
        "alerta_afericao_pa": pl.Boolean(),
        "ultima_data_creatinina": pl.Date(),
        "alerta_creatinina": pl.Boolean(),
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


class CreateHypertensionNominalListRepository(CreateNominalListsBasesRepository):
    _base = 'hipertensao_nominal'

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
                        text(f'{LISTA_NOMINAL_HIPERTENSAO}  LIMIT {chunk_size} OFFSET {offset};'), con=engine)

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                              if_exists='append')

        except NoSuchTableError:
            logging.info(f'Erro {self._base} already destroyed!')


class CreateDiabetesNominalListRepository(CreateNominalListsBasesRepository):
    _base = 'diabetes_nominal'

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
                        text(f'{LISTA_NOMINAL_DIABETES}  LIMIT {chunk_size} OFFSET {offset};'), con=engine)

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                              if_exists='append')

        except NoSuchTableError:
            logging.info(f'Erro {self._base} already destroyed!')
