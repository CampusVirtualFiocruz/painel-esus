import duckdb

from .sqls.infantil_queries import sql_total_infantil, sql_by_age_infantil


class InfantilRepository:
    def __init__(self):
        self.session = duckdb.connect()

    def get_total_infantil(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_total_infantil(cnes, equipe)).fetchall()

    def get_by_age(self, cnes: int = None, equipe: int = None):
        return self.session.execute(sql_by_age_infantil(cnes, equipe)).fetchall()
