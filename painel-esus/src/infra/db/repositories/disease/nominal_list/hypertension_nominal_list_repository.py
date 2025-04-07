# pylint: disable=R0913
from typing import Dict
from venv import logger
import json
import duckdb
import pandas as pd
from sqlalchemy import or_
from src.domain.entities.hypertension import Hypertension
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.sqls.disease.auto_referidos import (
    get_hypertension_base_sql,
    get_hypertension_base_sql_filter,
    get_hypertension_base_export,
)
from src.infra.db.settings.connection_local import DBConnectionHandler
from src.env.conf import getenv
from src.main.adapters.nominal_list_adapter import mock_word
from src.errors.log import logger


class HypertensionNominalListRepository:
    def __init__(self):
         self.mock_data = getenv("MOCK", False, False) == 'True'
    def find_all(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal,)
                .join(Pessoas, Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,)\
                .join(Equipes, Equipes.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,)
                .filter(Equipes.codigo_unidade_saude == cnes).all()
            )
            return users

    def find_by_id(self, cidadao_pec):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
                )
                .filter(HipertensaoNominal.co_fat_cidadao_pec == cidadao_pec)
                .first()
            )
            return users

    def find_all_download(self, cnes: int = None, equipe:int = None) -> Dict:
        con = duckdb.connect()
        pessoas_sql = get_hypertension_base_export(cnes, equipe)
        result = con.sql(pessoas_sql).df()
        if self.mock_data:
            def parse(x):
                x['cpf'] = mock_word(x['cpf'], 2)
                x['cns'] = mock_word(x['cns'], 2)
                x['nome'] = mock_word(x['nome'], 3, True)
                x['telefone'] = mock_word(x['telefone'], 2)
                x['endereco'] = mock_word(x['endereco'], 2)
                x['numero'] = mock_word(x['numero'], 2)
                x['cep'] = mock_word(x['cep'], 2)
                x['complemento'] = mock_word(x['complemento'], 2)
                x['bairro'] = mock_word(x['bairro'], 2)
                x['nome_unidade_saude'] = mock_word(x['nome_unidade_saude'], 2)
                x['nome_equipe'] = mock_word(x['nome_equipe'], 2)
                return x            
            result=result.apply(parse, axis=1)
            
        return result


    def find_by_nome(self, nome: str):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
                    isouter=True,
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
        pessoas_sql = get_hypertension_base_sql()
        conditions = []
        or_conditions = []

        if cnes is not None and cnes:
            conditions += [f"codigo_unidade_saude = {cnes}"]

        if query is not None and query:
            or_conditions += [
                f"cpf ilike '%{query}%'",
                f"nome ilike '%{query}%'",
                f"cns ilike  '%{query}%'"
            ]
        if equipe is not None and equipe:
            conditions += [ f'codigo_equipe = {equipe}']

        
            
            
        where_clause = []
        sql_where, sql, sql_or = "", "", ""

        if len(conditions) > 0:
            sql += " AND ".join(conditions)
            where_clause += [f"({sql})"]

        if len(or_conditions) > 0:
            sql_or += " OR ".join(or_conditions)
            where_clause += [f"({sql_or})"]

        if len(where_clause)>0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"

        order = 'order by '
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
            
        order += ", ".join(order_list)
        users = con.sql(
            pessoas_sql + sql_where + f" {order} LIMIT {limit} OFFSET {offset} "
        ).df()

        users = users.to_dict(orient="records")
        total = len(con.sql(pessoas_sql + sql_where).fetchall())
        return {
                "itemsCount": total,
                "itemsPerPage": pagesize,
                "page": page,
                "pagesCount": round(total / pagesize),
                "items": users,
        }

        # with DBConnectionHandler() as db_con:
        #     users = (
        #         db_con.session.query(*columns)
        #         .distinct(HipertensaoNominal.co_fat_cidadao_pec)
        #         .join(
        #             Pessoas,
        #             Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
        #             isouter=True,
        #         )
        #         .join(
        #             Equipes,
        #             Equipes.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
        #             isouter=True,
        #         )
        #     )
        #     conditions, or_conditions = [], []
        #     if cnes is not None and cnes:
        #         conditions+=[Equipes.codigo_unidade_saude == cnes]

        #     if nome is not None and nome:
        #         conditions+=[Pessoas.nome.ilike(f"%{nome}%")]

        #     if query is not None and query:
        #         or_conditions += [
        #             Pessoas.cpf.ilike(f"%{query}%"),
        #             Pessoas.nome.ilike(f"%{query}%"),
        #             Pessoas.cns.ilike(f"%{query}%"),
        #         ]

        #     if equipe is not None and equipe:
        #         conditions+=[Equipes.codigo_equipe == equipe]

        #     if len(conditions)>0:
        #         users = users.filter(*conditions)
        #     if len(or_conditions)>0:
        #         users = users.filter(or_(*or_conditions))

        #     users = users.filter(Pessoas.cidadao_pec.is_not(None))

        #     users = users.group_by(HipertensaoNominal.co_fat_cidadao_pec)
        #     total = users.count()
        #     users = (
        #         users.order_by(Pessoas.nome)
        #         .offset(max(0, page - 1) * pagesize)
        #         .limit(pagesize)
        #     )
        #     return {
        #         "itemsCount": total,
        #         "itemsPerPage": pagesize,
        #         "page": page,
        #         "pagesCount": round(total / pagesize),
        #         "items": list(users),
        #     }
