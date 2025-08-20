from src.domain.use_cases.demographic.demographic_use_case import (
    IBGEPopulationUseCaseInterface,
)


class GetIBGEPopulationUseCase(IBGEPopulationUseCaseInterface):
    def __init__(self, _repository):
        self._repository = _repository

    def get_ibge_population(self) -> str:
        return self._repository.get_ibge_population()
