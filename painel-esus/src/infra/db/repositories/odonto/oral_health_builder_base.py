# pylint: disable=E0401

import pandas as pd
from src.infra.db.repositories.sqls.odonto import (ATENDIMENTO_ONDONTO,
                                                   MAX_DATE_ATENDIMENTO_ODONTO)
from src.infra.db.repositories.update_bases import UpdateBasesRepository
from src.infra.db.settings.connection import DBConnectionHandler


class OralHealthBuilderBaseRepository:

    def __init__(self):
        pass

    def _load_oral_cares(self):
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DATE_ATENDIMENTO_ODONTO, con=engine)

            max_date = str(max_date['max_date'].iloc[0])
            sql = ATENDIMENTO_ONDONTO
            sql += f"""
                where
                    dt_registro between '{max_date}'::DATE - interval '12 month' and '{max_date}';
            """
            atendimento_odonto = pd.read_sql_query(sql, con=engine)
            return atendimento_odonto

    def create_database(self):
        oral_cares = self._load_oral_cares()
        update_bases = UpdateBasesRepository()
        update_bases.update_bases(oral_cares, 'atendimento_odontologico')
