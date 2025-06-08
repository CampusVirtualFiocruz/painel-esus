from src.domain.use_cases.infantil.infantil_use_case import InfantilUseCase


class InfantilUseCaseImpl(InfantilUseCase):
    def __init__(self, repository):
        self.repository = repository

    def infantil_total(self, cnes=None, equipe=None):
        return self.repository.get_total_infantil(cnes, equipe)

    def infantil_by_age(self, cnes=None, equipe=None):
        return self.repository.get_by_age(cnes, equipe)
