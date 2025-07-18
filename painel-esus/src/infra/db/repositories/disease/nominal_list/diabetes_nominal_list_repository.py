# pylint: disable=R0913
import json
from typing import Dict

import duckdb
import pandas as pd
from sqlalchemy import or_
from src.domain.entities.diabetes import Diabetes
from src.env.conf import getenv
from src.infra.db.entities.diabetes_nominal import DiabetesNominal
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.sqls.disease.auto_referidos import (
    get_diabetes_base_export,
    get_diabetes_base_sql,
    get_diabetes_base_sql_filter,
)
from src.infra.db.repositories.utils.str_utils import anonymize_data_frame
from src.infra.db.settings.connection_local import DBConnectionHandler


class DiabetesNominalListRepository:
    def __init__(self):
        self.mock_data = getenv("MOCK", False, False) == 'True'
    def find_all(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(DiabetesNominal)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == DiabetesNominal.co_fat_cidadao_pec,
                    isouter=True,
                )
                .join(
                    Equipes,
                    Equipes.cidadao_pec == DiabetesNominal.co_fat_cidadao_pec,
                    isouter=True,
                )
                .filter(Equipes.codigo_unidade_saude == cnes)
                .all()
            )
            return users

    def find_all_download(self, cnes: int = None, equipe:int=None) -> Dict:
        con = duckdb.connect()
        pessoas_sql = get_diabetes_base_export(cnes, equipe)

        result= con.sql(pessoas_sql).df()
        result = result.apply(anonymize_data_frame, axis=1)
        return result

    def find_by_nome(self, nome: str):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(DiabetesNominal)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == DiabetesNominal.co_fat_cidadao_pec,
                )
                .filter(Pessoas.nome.ilike(f"%{nome}%"))
                .all()
            )
            return users

    def find_filter(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[]
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        con = duckdb.connect()
        pessoas_sql = get_diabetes_base_sql()
        conditions = []
        or_conditions = []

        if cnes is not None and cnes:
            conditions += [f"codigo_unidade_saude = {cnes}"]

        if query is not None and query:
            or_conditions += [
                f"cpf ilike '%{query}%'",
                f"nome ilike '%{query}%'",
                f"cns ilike  '%{query}%'",
            ]
        if equipe is not None and equipe:
            conditions += [f"codigo_equipe = {equipe}"]

        where_clause = []
        sql_where, sql, sql_or = "", "", ""
        # where_clause += [f"( n_atendimentos_12_meses != 0)"]
        if len(conditions) > 0:
            sql += " AND ".join(conditions)
            where_clause += [f"({sql})"]

        if len(or_conditions) > 0:
            sql_or += " OR ".join(or_conditions)
            where_clause += [f"({sql_or})"]

        if len(where_clause) > 0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"
        if len(where_clause)>0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"

        order = ''
        order_list = []
        mapped_columns = {
            'name': 'no_cidadao',
            'cpf':'cpf',
            'cns': 'cns',
            'idade': 'idade',
            'grupo_condicao': 'autoreferido',
            'sexo': 'sexo',
            'equipe': 'nome_equipe',
            'micro_area': 'micro_area'
        }
        if len(sort) > 0:
            for s in sort:
                filter = json.loads(s)
                if filter["field"] not in mapped_columns: continue

                direction = filter['direction'] if 'direction' in filter else'asc'
                columns = mapped_columns[filter["field"]]
                order_list.append( f'{columns} {direction}')
        else:
            order_list = 'no_cidadao asc'

        if len(order_list)>0:
            order = 'order by '
            order += ", ".join(order_list)

        users = con.sql(
            pessoas_sql
            + sql_where
            + f"  {order} LIMIT {limit} OFFSET {offset} "
        ).df()

        users = users.to_dict(orient="records")
        total = len(con.sql(pessoas_sql + sql_where).fetchall())
        return {
            "itemsCount": total,
            "itemsPerPage": pagesize,
            "page": page,
            "pagesCount": round(total / pagesize),
            "items": list(users),
        }
