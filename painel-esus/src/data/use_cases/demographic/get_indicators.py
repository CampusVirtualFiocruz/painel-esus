from typing import Dict

from src.data.interfaces.demographic_repository import DemographicIndicatorsInterface
from src.domain.use_cases.demographic.demographic_use_case import (
    DemographicIndicatorsUseCaseInterface,
)


class GetDemographicIndicatorsUseCase(DemographicIndicatorsUseCaseInterface):
    def __init__(self, _repository: DemographicIndicatorsInterface):
        self._repository = _repository

    def execute(self, cnes: int = None, equipe: int = None) -> Dict:
        return self._repository.get_indicators(cnes, equipe)
