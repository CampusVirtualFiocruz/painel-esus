import duckdb
from src.infra.db.repositories.utils.str_utils import anonymize_data_frame
from src.infra.db.settings.connection_duckdb import DuckDbHandler

from .sqls.children_queries import (
    get_medical_cares,
    get_total_card,
    get_total_ubs,
    sql_acs_visit_until_6m,
    sql_acs_visit_until_30d,
    sql_appointments_until_2_years,
    sql_by_age_children,
    sql_by_race_children,
    sql_dental_appointments_until_12m,
    sql_dental_appointments_until_24m,
    sql_evaluated_feeding,
    sql_first_consult_8d,
    sql_get_nominal_list,
    sql_get_nominal_list_download,
    sql_high_weight_records,
    sql_milestone,
    sql_total_and_last_12_months,
)


class ChildrenRepository:
    def __init__(self):
        self.session = DuckDbHandler()

    def total_card(
        self, cnes: int = None, equipe: int = None, category: str = "atentidas"
    ):
        sql = get_total_card(cnes, equipe)
        return self.session.fetchall(sql)

    def get_total_children(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(get_total_ubs(cnes, equipe))

    def get_total_twelve_months_children(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_total_and_last_12_months(cnes, equipe))

    def get_by_age(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_by_age_children(cnes, equipe))

    def get_by_race(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_by_race_children(cnes, equipe))

    def total_medical_cares(self, cnes: int = None, equipe: int = None):
        sql = get_medical_cares(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def get_first_consult_8d(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_first_consult_8d(cnes, equipe))

    def get_appointments_until_2_years(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_appointments_until_2_years(cnes, equipe))

    def get_acs_visit_until_30d(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_acs_visit_until_30d(cnes, equipe))

    def get_acs_visit_until_6m(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_acs_visit_until_6m(cnes, equipe))

    def get_dental_appointments_until_12m(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_dental_appointments_until_12m(cnes, equipe))

    def get_dental_appointments_until_24m(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_dental_appointments_until_24m(cnes, equipe))

    def get_high_weight_records(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_high_weight_records(cnes, equipe))

    def get_milestone(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_milestone(cnes, equipe))

    def get_evaluated_feeding(self, cnes: int = None, equipe: int = None):
        return self.session.fetchall(sql_evaluated_feeding(cnes, equipe))

    def get_nominal_list(
        self,
        cnes: int = None,
        equipe: int = None,
        page: int = 0,
        page_size: int = 10,
        nome: str = None,
        cpf: str = None,
        nome_unidade_saude: int = None,
        q: str = None,
        sort: list[dict] = None,
    ) -> list[dict]:

        try:
            page = int(page)
        except (TypeError, ValueError):
            page = 0

        try:
            page_size = int(page_size)
        except (TypeError, ValueError):
            page_size = 10

        query = sql_get_nominal_list(
            cnes=cnes,
            equipe=equipe,
            page=page,
            page_size=page_size,
            nome=nome,
            cpf=cpf,
            nome_unidade_saude=nome_unidade_saude,
            q=q,
            sort=sort,
        )

        result = self.session.fetchall(query)
        columns = [col[0] for col in self.session.get_description()]
        items = [dict(zip(columns, row)) for row in result]

        count_query = (
            sql_get_nominal_list(
                cnes=cnes,
                equipe=equipe,
                page=page,
                page_size=page_size,
                nome=nome,
                cpf=cpf,
                nome_unidade_saude=nome_unidade_saude,
                sort=sort,
            )
            .replace("SELECT *", "SELECT COUNT(*) as total")
            .split("ORDER BY")[0]
        )

        total = self.session.fetchone(count_query)

        return {
            "items": items,
            "itemsCount": total,
            "itemsPerPage": page_size,
            "page": page,
            "pagesCount": (total + page_size - 1) // page_size,
        }

    def get_nominal_list_download(self, cnes: int = None, equipe: int = None):
        response = self.session.fetch_df(sql_get_nominal_list_download(cnes, equipe))
        response = response.apply(anonymize_data_frame, axis=1)
        return response
