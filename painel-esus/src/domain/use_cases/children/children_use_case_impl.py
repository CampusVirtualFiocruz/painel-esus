from src.domain.use_cases.children.children_use_case import ChildrenUseCase


class ChildrenUseCaseImpl(ChildrenUseCase):
    def __init__(self, repository):
        self.repository = repository

    def children_total(self, cnes=None, equipe=None):
        return self.repository.get_total_children(cnes, equipe)

    def children_by_age(self, cnes=None, equipe=None):
        return self.repository.get_by_age(cnes, equipe)

    def children_by_race(self, cnes=None, equipe=None):
        return self.repository.get_by_race(cnes, equipe)

    def children_first_consult_8d(self, cnes=None, equipe=None):
        return self.repository.get_first_consult_8d(cnes, equipe)

    def children_appointments_until_2_years(self, cnes=None, equipe=None):
        return self.repository.get_appointments_until_2_years(cnes, equipe)
