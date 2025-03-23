# pylint: disable=R0913
from typing import Dict

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

columns = [
    HipertensaoNominal.co_fat_cidadao_pec,
    HipertensaoNominal.diagnostico,
    HipertensaoNominal.cids,
    HipertensaoNominal.min_date,
    HipertensaoNominal.data_ultima_visita_acs,
    HipertensaoNominal.alerta_visita_acs,
    HipertensaoNominal.total_consulta_individual_medico,
    HipertensaoNominal.alerta_total_de_consultas_medico,
    HipertensaoNominal.ultimo_atendimento_medico,
    HipertensaoNominal.alerta_ultima_consulta_medico,
    HipertensaoNominal.ultimo_atendimento_odonto,
    HipertensaoNominal.alerta_ultima_consulta_odontologica,
    HipertensaoNominal.ultima_data_afericao_pa,
    HipertensaoNominal.alerta_afericao_pa,
    HipertensaoNominal.ultima_data_creatinina,
    HipertensaoNominal.alerta_creatinina,
    Pessoas.co_cidadao,
    Pessoas.raca_cor,
    Pessoas.cpf,
    Pessoas.cns,
    Pessoas.nome,
    Pessoas.nome_social,
    Pessoas.data_nascimento,
    Pessoas.idade,
    Pessoas.sexo,
    Pessoas.identidade_genero,
    Pessoas.telefone,
    Pessoas.ultima_atualizacao_cidadao,
    Pessoas.ultima_atualizacao_fcd,
    Pessoas.tipo_endereco,
    Pessoas.endereco,
    Pessoas.complemento,
    Pessoas.numero,
    Pessoas.bairro,
    Pessoas.cep,
    Pessoas.tipo_localidade,
    Equipes.nome_unidade_saude, Equipes.nome_equipe, Equipes.micro_area
]
class HypertensionNominalListRepository:

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
        return con.sql(pessoas_sql).df()


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

        users = con.sql(
            pessoas_sql + sql_where + f" order by no_cidadao asc LIMIT {limit} OFFSET {offset} "
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
