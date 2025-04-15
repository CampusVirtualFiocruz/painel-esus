from src.domain.use_cases.demographic.demographic_use_case import (
    DemographicIBGEPopulationUseCaseInterface,
)


class GetIBGEPopulationUseCase(DemographicIBGEPopulationUseCaseInterface):
    def __init__(self, _repository):
        self._repository = _repository

    def execute(self) -> str:
        return self._repository.get_ibge_population()
