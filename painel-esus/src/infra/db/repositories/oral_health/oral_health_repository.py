import json

import duckdb
from src.data.interfaces.oral_health_dashboard_repository import (
    OralHealthDashboardRepositoryInterface,
)
from src.env.conf import getenv
from src.infra.db.repositories.utils.str_utils import anonymize_data_frame

from .sqls.oral_health_queries import (
    atraumatic_treatment,
    by_gender,
    by_race,
    conclued_treatment,
    donwload_nominal_list,
    extraction,
    first_appointment,
    get_total_card,
    get_total_ubs,
    oral_healt_base_sql,
    prevention_procedures,
    supervised_brushing,
)


class OralHealthRepository(OralHealthDashboardRepositoryInterface):
    def __init__(self,):
        self.session = duckdb.connect()
        self.mock_data = getenv("MOCK", False, False) == "True"

    def total_card(self, cnes: int = None, equipe: int = None, category: str = 'atentidas'):
        sql = get_total_card(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def total_ubs(self, cnes: int = None, equipe: int = None):

        cadastradas = self.session.execute(get_total_ubs(cnes,equipe,'cadastradas')).fetchall()
        atendidas = self.session.execute(
            get_total_ubs(cnes, equipe, "atendidas")
        ).fetchall()
        return {
            "atendidas": (
                atendidas[0][0] if len(atendidas) > 0 and len(atendidas[0]) > 0 else 0
            ),
            "cadastradas": (
                cadastradas[0][0] if len(cadastradas) > 0 and len(cadastradas[0]) > 0 else 0
            ),
        }

    def get_oral_health_cares_by_gender(
        self, cnes=None, equipe=None, category: str = None
    ):
        sql = by_gender(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_cares_by_race(
        self, cnes=None, equipe=None, category: str = None
    ):
        sql = by_race(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_first_appointment(
        self, cnes=None, equipe=None, category: str = None
    ):
        sql = first_appointment(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_conclued_treatment(self, cnes=None, equipe=None, category=None):
        sql = conclued_treatment(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_extraction(self, cnes=None, equipe=None, category=None):
        sql = extraction(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_prevention_procedures(
        self, cnes=None, equipe=None, category=None
    ):
        sql = prevention_procedures(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def oral_health_get_atraumatic_treatment(
        self, cnes=None, equipe=None, category=None
    ):
        sql = atraumatic_treatment(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def oral_health_get_supervised_brushing(
        self, cnes=None, equipe=None, category=None
    ):
        sql = supervised_brushing(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[],
        category: str = 'atendidas'
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        con = duckdb.connect()
        oral_health = oral_healt_base_sql()
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

        if category is not None and category == 'atendidas':
            conditions += [f"atendimento_odonto = 1"]
        elif category is not None and category == 'cadastradas':
            conditions += [f"cadastradas_odonto = 1"]

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
        if len(where_clause)>0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"

        order = ''
        order_list = []
        mapped_columns = {
            "name": "nome",
            "cpf": "cpf",
            "cns": "cns",
            "idade": "idade",
            "sexo": "sexo",
            "gestante": "gestante",
            "equipe": "nome_equipe",
            "micro_area": "micro_area",
            "identidadeGenero": "tp_identidade_genero_cidadao",
            "necessidadesEspeciais": "st_paciente_necessidades_espec",
            "povosComunidades": "st_comunidade_tradicional",
        }
        if len(sort) > 0:
            for s in sort:
                filter = json.loads(s)
                if filter["field"] not in mapped_columns: continue

                direction = filter['direction'] if 'direction' in filter else'asc'
                columns = mapped_columns[filter["field"]]
                order_list.append( f'{columns} {direction}')
        else:
            order_list = ['nome asc']

        if len(order_list)>0:
            order = 'order by '
            order += ", ".join(order_list)

        users = con.sql(
            oral_health
            + sql_where
            + f"  {order} LIMIT {limit} OFFSET {offset} "
        ).df()

        users = users.to_dict(orient="records")
        total = len(con.sql(oral_health + sql_where).fetchall())
        return {
            "itemsCount": total,
            "itemsPerPage": pagesize,
            "page": page,
            "pagesCount": round(total / pagesize),
            "items": users,
        }

    def donwload_nominal_list(
        self, cnes: int = None, equipe: int = None, category=None
    ):

        sql = donwload_nominal_list(cnes, equipe, category)
        con = duckdb.connect()
        response = con.sql(sql).df()
        response = response.apply(anonymize_data_frame, axis=1)
        return response
