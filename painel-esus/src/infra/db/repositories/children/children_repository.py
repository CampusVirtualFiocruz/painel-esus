import duckdb

from .sqls.children_queries import (
    sql_appointments_until_2_years,
    sql_by_age_children,
    sql_by_race_children,
    sql_evaluated_feeding,
    sql_first_consult_8d,
    sql_high_weight_records,
    sql_milestone,
    sql_total_children,
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

    def get_high_weight_records(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_high_weight_records(cnes, equipe)).fetchall()

    def get_milestone(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_milestone(cnes, equipe)).fetchall()

    def get_evaluated_feeding(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_evaluated_feeding(cnes, equipe)).fetchall()
