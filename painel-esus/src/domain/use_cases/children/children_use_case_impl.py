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

    def children_high_weight_records(self, cnes=None, equipe=None):
        return self.repository.get_high_weight_records(cnes, equipe)

    def children_milestone(self, cnes=None, equipe=None):
        return self.repository.get_milestone(cnes, equipe)

    def children_evaluated_feeding(self, cnes=None, equipe=None):
        return self.repository.get_evaluated_feeding(cnes, equipe)

    def children_get_nominal_list(
        self,
        cnes=None,
        equipe=None,
        page=0,
        page_size=10,
        nome=None,
        cpf=None,
        nome_unidade_saude=None,
        sort=None,
    ):
        return self.repository.get_nominal_list(
            cnes, equipe, page, page_size, nome, cpf, nome_unidade_saude, sort
        )
