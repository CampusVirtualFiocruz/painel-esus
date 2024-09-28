# pylint: disable=R0913
from typing import Dict

from src.infra.db.entities.diabetes_nominal import DiabetesNominal
from src.infra.db.settings.connection_local import DBConnectionHandler


class DiabetesNominalListRepository:

    def find_all(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session
                .query(DiabetesNominal)
                .filter(DiabetesNominal.co_dim_unidade_saude == cnes)
                .all()
            )
            return users

    def find_by_nome(self, nome: str):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session
                .query(DiabetesNominal)
                .filter(DiabetesNominal.no_cidadao.ilike(f"%{nome}%"))
                .all()
            )
            return users

    def find_filter(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session
                .query(DiabetesNominal)
            )
            users = users.filter(
                DiabetesNominal.co_dim_unidade_saude == cnes)
            if nome is not None:
                users = users.filter(
                    DiabetesNominal.no_cidadao.ilike(f"%{nome}%"))
            if cpf is not None:
                users = users.filter(
                    DiabetesNominal.nu_cpf.ilike(f"%{cpf}%"))
            users = users.offset(max(0, page-1)).limit(pagesize)
            return users
