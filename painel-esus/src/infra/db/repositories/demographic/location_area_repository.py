import duckdb
from src.data.interfaces.demographic_repository import LocationAreaInterface
from src.infra.db.repositories.sqls.demographics import filter_by_localidade
from src.infra.db.repositories.sqls.disease.auto_referidos import (
    filter_diabetes_by_localidade,
    filter_hypertension_by_localidade,
)


class LocationAreaRepository(LocationAreaInterface):

    def __init__(self, db_connection=duckdb):
        self.db = db_connection

    def get_location_area(self, cnes: int = None, equipe: int = None):
        location_area_sql = filter_by_localidade(cnes, equipe)
        result_location_area_sql = self.db.sql(location_area_sql).fetchall()

        location_area_body = {"rural": 0, "urbano": 0, "nao_definido": 0}

        for resp in result_location_area_sql:
            location_area_body[resp[0]] = int(resp[1])
        return location_area_body

    def get_diabetes_by_location_area(self, cnes: int = None, equipe: int = None):
        location_area_sql = filter_diabetes_by_localidade(cnes, equipe)
        result_location_area_sql = self.db.sql(location_area_sql).fetchall()

        diabetes_location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        for resp in result_location_area_sql:
            if resp[0] is None:
                diabetes_location_body["nao_informado"] = int(resp[1])
            else:
                diabetes_location_body[resp[0]] = int(resp[1])
        return diabetes_location_body

    def get_hypertension_by_location_area(self, cnes: int = None, equipe: int = None):
        location_area_sql = filter_hypertension_by_localidade(cnes, equipe)
        result_location_area_sql = self.db.sql(location_area_sql).fetchall()

        hypertension_location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        for resp in result_location_area_sql:
            if resp[0] is None:
                hypertension_location_body["nao_informado"] = int(resp[1])
            else:
                hypertension_location_body[resp[0]] = int(resp[1])
        return hypertension_location_body

    def get_child_by_location_area(self):
        child_location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}

        return child_location_body

    def get_elderly_by_location_area(self):
        elderly_location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}

        return elderly_location_body
