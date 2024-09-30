# pylint: disable=R0913
from typing import Dict

import pandas as pd
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.settings.connection_local import DBConnectionHandler


class HypertensionNominalListRepository:

    def find_all(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session
                .query(HipertensaoNominal)
                .filter(HipertensaoNominal.co_dim_unidade_saude == cnes)
                .all()
            )
            return users

    def find_all_download(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            response = pd.read_sql_query(con=db_con.get_engine(),
                                         sql=f"select * from hipertensao_nominal where co_dim_unidade_saude = {cnes} order by no_cidadao")
            return response

    def find_by_nome(self, nome: str):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session
                .query(HipertensaoNominal)
                .filter(HipertensaoNominal.no_cidadao.ilike(f"%{nome}%"))
                .all()
            )
            return users

    def find_filter(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None,):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session
                .query(HipertensaoNominal)
            )
            users = users.filter(
                HipertensaoNominal.co_dim_unidade_saude == cnes)
            if nome is not None:
                users = users.filter(
                    HipertensaoNominal.no_cidadao.ilike(f"%{nome}%"))
            if cpf is not None:
                users = users.filter(
                    HipertensaoNominal.nu_cpf.ilike(f"%{cpf}%"))
            users = users.offset(max(0, page-1)).limit(pagesize)
            return users
