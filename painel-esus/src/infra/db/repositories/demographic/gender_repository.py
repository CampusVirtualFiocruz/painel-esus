import duckdb
from src.data.interfaces.demographic_repository import DemographicGenderInterface
from src.infra.db.repositories.sqls.demographics import filter_by_sexo


class GenderRepository(DemographicGenderInterface):

    def __init__(self, db_connection=duckdb):
        self.db = db_connection

    def get_by_gender(self, cnes: int = None, equipe: int = None):
        gender = {"feminino": 0, "masculino": 0}
        gender_sql = filter_by_sexo(cnes, equipe)
        result_gender = self.db.sql(gender_sql).fetchall()

        for resp in result_gender:
            gender[str(resp[0]).lower()] = int(resp[1])
        return gender
