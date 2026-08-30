"""Idosos.

Consultas e listas do acompanhamento de idosos: totais por UBS,
atendimentos, distribuição por sexo/raça, exames e listas nominais com
paginação/exportação e anonimização de dados sensíveis.
"""

import json

import duckdb
import pandas as pd
from src.env.conf import getenv
from src.infra.db.repositories.elderly.sqls import (
    acs_visits,
    by_gender,
    by_race,
    creatinine,
    dentist_appointment,
    get_elderly_base,
    get_medical_cares,
    get_total_card,
    get_total_ubs,
    height_records,
    influenza_vaccines,
    ivcf_20,
    medical_appointments,
    nominal_download,
)
from src.infra.db.repositories.utils.str_utils import anonymize_data_frame
from src.infra.db.settings.connection_local import DBConnectionHandler


class ElderlyRepository:
    """Leitura para indicadores e listas de idosos."""
    def __init__(self):
        self.mock_data = getenv("MOCK", False, False) == 'True'

    def total_ubs(self, cnes: int = None, equipe: int = None):
        """Retorna totais por UBS para idosos."""
        sql = get_total_ubs(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def total_card(self, cnes: int = None, equipe: int = None):
            """Retorna totais agrupado por localização."""
            sql = get_total_card(cnes,equipe)
            con = duckdb.connect()
            result = con.sql(sql).fetchall()
            return result


    def total_medical_cares(self, cnes: int = None, equipe: int = None):
        """Total de atendimentos médicos a idosos."""
        sql = get_medical_cares(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def by_gender(self, cnes: int = None, equipe: int = None):
        """Distribuição por sexo entre idosos."""
        sql = by_gender(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        if len(result) > 0 and '100' in result[0][0]:
            result = [list(result[2:])+list(result[:2]) ][0]
        return result

    def by_race(self, cnes: int = None, equipe: int = None):
        """Distribuição por raça/cor entre idosos."""
        sql = by_race(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def medical_appointment(self, cnes: int = None, equipe: int = None):
        """Consultas médicas realizadas com idosos."""
        sql = medical_appointments(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def height_records(self, cnes: int = None, equipe: int = None):
        """Registros de altura no acompanhamento do idoso."""
        sql = height_records(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def acs_visits(self, cnes: int = None, equipe: int = None):
        """Visitas de ACS a idosos."""
        sql = acs_visits(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def creatinine(self, cnes: int = None, equipe: int = None):
        """Exames de creatinina e datas relacionadas para idosos."""
        sql = creatinine(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def dentist_appointment(self, cnes: int = None, equipe: int = None):
        """Atendimentos odontológicos com idosos."""
        sql = dentist_appointment(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def ivcf_20(self, cnes: int = None, equipe: int = None):
        """Indicador IVCF-20 (fragilidade) para idosos."""
        sql = ivcf_20(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def influenza_vaccines(self, cnes: int = None, equipe: int = None):
        """Vacinação contra influenza em idosos."""
        sql = influenza_vaccines(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result


    def _build_where_clause(self, cnes: int = None, query: str = None, equipe: int = None) -> str:
        """Constrói a cláusula WHERE para a lista nominal."""
        conditions = []
        or_conditions = []

        if cnes is not None and cnes:
            conditions.append(f"codigo_unidade_saude = {cnes}")

        if query is not None and query:
            or_conditions.extend([
                f"cpf ilike '%{query}%'",
                f"nome ilike '%{query}%'",
                f"cns ilike  '%{query}%'",
            ])
        if equipe is not None and equipe:
            conditions.append(f"codigo_equipe = {equipe}")

        where_clause = []

        if len(conditions) > 0:
            sql = " AND ".join(conditions)
            where_clause.append(f"({sql})")

        if len(or_conditions) > 0:
            sql_or = " OR ".join(or_conditions)
            where_clause.append(f"({sql_or})")

        if len(where_clause) > 0:
            return " WHERE " + " AND ".join(where_clause)

        return ""

    def _build_order_clause(self, sort: list | None) -> str:
        """Constrói a cláusula ORDER BY para a lista nominal."""
        mapped_columns = {
            'name': 'nome',
            'cpf': 'cpf',
            'cns': 'cns',
            'idade': 'idade',
            'sexo': 'sexo',
            'equipe': 'nome_equipe',
            'micro_area': 'micro_area'
        }
        order_list = []
        if sort:
            for s in sort:
                filter_obj = json.loads(s)
                if filter_obj["field"] not in mapped_columns:
                    continue

                direction = filter_obj.get('direction', 'asc').lower()
                if direction not in {"asc", "desc"}:
                    direction = "asc"
                column = mapped_columns[filter_obj["field"]]
                order_list.append(f"{column} {direction}")
        else:
            order_list = ['nome asc']

        if len(order_list) > 0:
            return " ORDER BY " + ", ".join(order_list)
        return ""

    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=None,
    ):
        """Retorna lista nominal (items e metadados de paginação).

        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.
        """
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        offset = max(0, page - 1) * pagesize
        limit = pagesize

        con = duckdb.connect()
        pessoas_sql = get_elderly_base()

        sql_where = self._build_where_clause(cnes, query, equipe)
        order = self._build_order_clause(sort)

        users = con.sql(
            pessoas_sql
            + sql_where
            + f" {order} LIMIT {limit} OFFSET {offset} "
        ).df()

        users = users.to_dict(orient="records")
        total = con.sql(
            f"SELECT COUNT(*) FROM ({pessoas_sql} {sql_where}) AS filtered_rows"
        ).fetchone()[0]
        return {
            "itemsCount": total,
            "itemsPerPage": pagesize,
            "page": page,
            "pagesCount": (total + pagesize - 1) // pagesize if pagesize > 0 else 0,
            "items": users,
        }

    def find_all_download(self, cnes: int = None, equipe: int = None):
        """Gera DataFrame para exportação com anonimização de dados."""
        sql = nominal_download(cnes,equipe)
        con = duckdb.connect()
        response = con.sql(sql).df()
        response=response.apply(anonymize_data_frame, axis=1)
        return response
