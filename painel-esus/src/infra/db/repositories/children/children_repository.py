import duckdb

from .sqls.children_queries import (
    sql_total_children,
    sql_by_age_children,
    sql_by_race_children,
    sql_first_consult_8d,
    sql_appointments_until_2_years,
    sql_acs_visit_until_30d,
    sql_acs_visit_until_6m,
    sql_dental_appointments_until_12m,
    sql_dental_appointments_until_24m
)


class ChildrenRepository:
    def __init__(self):
        self.session = duckdb.connect()

    def get_total_children(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_total_children(cnes, equipe)).fetchall()

    def get_by_age(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_by_age_children(cnes, equipe)).fetchall()

    def get_by_race(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_by_race_children(cnes, equipe)).fetchall()

    def get_first_consult_8d(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_first_consult_8d(cnes, equipe)).fetchall()

    def get_appointments_until_2_years(self, cnes: int = None, equipe: int = None):
        return self.session.execute(
            sql_appointments_until_2_years(cnes, equipe)
        ).fetchall()
    
    def get_acs_visit_until_30d(self, cnes: int = None, equipe: int = None):
        return self.session.execute(
            sql_acs_visit_until_30d(cnes, equipe)
        ).fetchall()
    
    def get_acs_visit_until_6m(self, cnes: int = None, equipe: int = None):
        return self.session.execute(
            sql_acs_visit_until_6m(cnes, equipe)
        ).fetchall()
    
    def get_dental_appointments_until_12m(self, cnes: int = None, equipe: int = None):
        return self.session.execute(
                sql_dental_appointments_until_12m(cnes, equipe)
            ).fetchall()

    def get_dental_appointments_until_24m(self, cnes: int = None, equipe: int = None):
        return self.session.execute(
            sql_dental_appointments_until_24m(cnes, equipe)
        ).fetchall()
    
    

