from src.data.interfaces.oral_health_dashboard_repository import (
    OralHealthDashboardRepositoryInterface,
)
from .sqls.oral_health_queries import (
    by_gender,
    by_race,
    first_appointment,
    conclued_treatment,
    extraction,
    prevention_procedures,
    atraumatic_treatment,
    supervised_brushing,
)


class OralHealthRepository(OralHealthDashboardRepositoryInterface):
    def __init__(self, session):
        self.session = session

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
