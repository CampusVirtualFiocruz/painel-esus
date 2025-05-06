from .sqls.oral_health_queries import by_gender, by_race, first_appointment, conclued_treatment, extraction, prevention_procedures, atraumatic_treatment, supervised_brushing
from src.data.interfaces.oral_health_dashboard_repository import OralHealthDashboardRepositoryInterface


class OralHealthRepository(OralHealthDashboardRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def get_oral_health_cares_by_gender(self, cnes=None, equipe=None, category: str = None):
        sql = by_gender(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_cares_by_race(self, cnes=None, equipe=None, category: str = None):
        sql = by_race(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_first_appointment(self, cnes=None, equipe=None, category='atendidas'):
        sql = first_appointment(cnes, equipe, category)
        return self.session.execute(sql).mappings().all()

    def get_conclued_treatment(self, cnes=None, equipe=None, category='atendidas'):
        sql = conclued_treatment(cnes, equipe, category)
        return self.session.execute(sql).mappings().all()

    def get_extraction_procedures_proportion(self, cnes=None, equipe=None, category='atendidas'):
        sql = extraction(cnes, equipe, category)
        return self.session.execute(sql).mappings().all()

    def get_prevention_procedures(self, cnes=None, equipe=None, category='atendidas'):
        sql = prevention_procedures(cnes, equipe, category)
        return self.session.execute(sql).mappings().all()

    def get_atraumatic_treatment(self, cnes=None, equipe=None, category='atendidas'):
        sql = atraumatic_treatment(cnes, equipe, category)
        return self.session.execute(sql).mappings().all()

    def get_supervised_brushing(self, cnes=None, equipe=None, category='atendidas'):
        sql = supervised_brushing(cnes, equipe, category)
        return self.session.execute(sql).mappings().all()

    def get_total(self, cnes=None):
        return []

    def get_cares_by_line_of_services(self, cnes=None):
        return []

    def get_cares_by_type_of_services(self, cnes=None):
        return []

    def get_oral_health_all_cares_by_place(self, cnes=None):
        return []

    def get_oral_health_cares_by_age_range(self, cnes=None):
        return []

    def get_oral_health_cares_by_outcome(self, cnes=None):
        return []

    def get_oral_health_cares_by_place(self, cnes=None):
        return []
