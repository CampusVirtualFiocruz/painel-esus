from src.infra.db.repositories.elderly.sqls import get_elderly_total_influenza
from src.infra.db.repositories.elderly.sqls import get_elderly_total_odonto
from src.infra.db.repositories.elderly.sqls import get_elderly_total_on_ubs_and_team
from src.infra.db.repositories.elderly.sqls import group_by_age_gender
from src.infra.db.repositories.elderly.sqls import group_by_age_location
from src.infra.db.repositories.elderly.sqls import group_by_race
from src.infra.db.repositories.elderly.sqls import total_hipertension_diabetes
from src.infra.db.settings.connection_local import DBConnectionHandler


class ElderlyRepository:

    def find_total(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_elderly_total_on_ubs_and_team(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_age_location(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_age_location(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_race(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_race(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_age_gender(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_age_gender(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_influenza_rate(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_elderly_total_influenza(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_odonto_rate(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_elderly_total_odonto(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_total_hipertension_diabetes(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = total_hipertension_diabetes(cnes, equipe)
            result = con.execute(sql)
            return list(result)
