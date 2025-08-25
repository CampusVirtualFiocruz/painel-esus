import json
from typing import Dict

import duckdb
from src.env.conf import getenv
from src.infra.db.repositories.utils.str_utils import mock_word
from src.infra.db.settings.connection_duckdb import DuckDbHandler

from .sqls.hipertension_diabetes_queries import (
    by_gender,
    by_location,
    by_race,
    complications,
    exams_table,
    get_base_sql,
    get_number_of_patients,
    get_sql_base_export,
    get_total,
    imc,
)


class HypertensionDiabetesRepository:

    def __init__(self, disease: str):
        self.disease = disease
        self.session = DuckDbHandler()
        self.mock_data = getenv("MOCK", False, False) == "True"

    def _validate(self, cnes: int, equipe: int):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")

        if equipe and not isinstance(cnes, int):
            raise InvalidArgument("Equipe must be int")

    def get_total(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        total_12 = self.session.fetchone(get_total(self.disease, cnes, equipe))
        total = self.session.fetchone(get_number_of_patients(self.disease, cnes, equipe))
        total_cid_ciap, total_auto = total[0], total[1]
        result = {
            "total-atendimentos-12-meses": {
                "data": total_12[0]
            },
            "total-pessoas-cid-ciap": {
                "data": total_cid_ciap
            },            
            "total-pessoas-auto": {
                "data": total_auto
            }        
        }
        return result

    def get_exams_count(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        cares_sql = exams_table(self.disease, cnes, equipe)
        result =  self.session.fetchall(cares_sql)
        if debug:
            print(self.session.columns)        
        return result

    def get_imc(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        sql = imc(self.disease, cnes, equipe)
        result = self.session.fetchall(sql)
        if debug:
            print(self.session.columns)
        return result

    def get_complications(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        sql = complications(self.disease, cnes, equipe)
        result = self.session.fetchall(sql)
        if debug:
            print(self.session.columns)
        return result

    def get_by_location(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        sql = by_location(self.disease, cnes, equipe)
        result = self.session.fetchall(sql)
        return result

    def get_by_race(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        sql = by_race(self.disease, cnes, equipe)
        result = self.session.fetchall(sql)
        return result

    def get_by_gender(self, cnes: int = None, equipe: int = None, debug=False):
        self._validate(cnes, equipe)
        sql = by_gender(self.disease, cnes, equipe)
        result = self.session.fetchall(sql)
        return result

    def get_nominal_list(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[],
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        con = duckdb.connect()
        pessoas_sql = get_base_sql(self.disease)
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

        order = ""
        order_list = []
        mapped_columns = {
            "name": "nome",
            "cpf": "cpf",
            "cns": "cns",
            "idade": "idade",
            "grupo_condicao": "autoreferido",
            "sexo": "sexo",
            "equipe": "nome_equipe",
            "micro_area": "micro_area",
        }
        if len(sort) > 0:
            for s in sort:
                filter = json.loads(s)
                if filter["field"] not in mapped_columns:
                    continue

                direction = filter["direction"] if "direction" in filter else "asc"
                columns = mapped_columns[filter["field"]]
                order_list.append(f"{columns} {direction}")
        else:
            order_list = ["nome asc"]

        if len(order_list) > 0:
            order = "order by "
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

    def get_nominal_list_download(self, cnes: int = None, equipe: int = None) -> Dict:
        con = duckdb.connect()
        pessoas_sql = get_sql_base_export(self.disease, cnes, equipe)
        result = con.sql(pessoas_sql).df()
        if self.mock_data:

            def parse(x):
                x["cpf"] = mock_word(x["cpf"], 2)
                x["cns"] = mock_word(x["cns"], 2)
                x["nome"] = mock_word(x["nome"], 3, True)
                x["telefone"] = mock_word(x["telefone"], 2)
                x["endereco"] = mock_word(x["endereco"], 2)
                x["numero"] = mock_word(x["numero"], 2)
                x["cep"] = mock_word(x["cep"], 2)
                x["complemento"] = mock_word(x["complemento"], 2)
                x["bairro"] = mock_word(x["bairro"], 2)
                x["nome_unidade_saude"] = mock_word(x["nome_unidade_saude"], 2)
                x["nome_equipe"] = mock_word(x["nome_equipe"], 2)
                return x

            result = result.apply(parse, axis=1)

        return result
