from typing import Dict, Optional

from src.data.interfaces.demographic_repository import DemographicLocationAreaInterface
from src.domain.use_cases.demographic.demographic_use_case import (
    DemographicLocationAreaUseCaseInterface,
)


class GetLocationAreaReport(DemographicLocationAreaUseCaseInterface):
    def __init__(self, _repository: DemographicLocationAreaInterface):
        self._repository = _repository

    def get_location_area(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> Dict:
        return {
            "location_area": self._repository.get_location_area(cnes, equipe),
            "diabetes": self._repository.get_diabetes_location_area(cnes, equipe),
            "hypertension": self._repository.get_hypertension_location_area(
                cnes, equipe
            ),
            "child": self._repository.get_child_location_area(),
            "elderly": self._repository.get_elderly_location_area(),
        }
