from src.main.adapters.base.base_dashboard_adapter import BaseDashboardAdapter


class OralHealthAdapter(BaseDashboardAdapter):

    def by_gender(self, response):
        return self.group_gender_age(response)

    def by_race(self, response):
        return self.group_race(response)

    def first_appointment(self, response):
        return self.group_count_binary(response, "nao-realizado", "realizado")

    def conclued_treatment(self, response):
        return self.group_count_binary(response, "nao-realizado", "realizado")

    def extraction(self, response):
        return self.group_count_binary(response, "nao-realizado", "realizado")

    def prevention_procedures(self, response):
        return self.group_count_binary(response, "nao-realizado", "realizado")

    def atraumatic_treatment(self, response):
        return self.group_count_binary(response, "nao-realizado", "realizado")

    def supervised_brushing(self, response):
        return self.group_count_binary(response, "nao-realizado", "realizado")
