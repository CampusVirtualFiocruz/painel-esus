from typing import Dict, Optional

from src.data.interfaces.demographic_repository import LocationAreaInterface
from src.domain.use_cases.demographic.demographic_use_case import (
    LocationAreaUseCaseInterface,
)


class GetLocationAreaUseCase(LocationAreaUseCaseInterface):
    def __init__(self, _repository: LocationAreaInterface):
        self._repository = _repository

    def get_location_area(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> Dict:
        return {
            "location_area": self._repository.get_location_area(cnes, equipe),
            "diabetes": self._repository.get_diabetes_by_location_area(cnes, equipe),
            "hypertension": self._repository.get_hypertension_by_location_area(
                cnes, equipe
            ),
            "child": self._repository.get_child_by_location_area(),
            "elderly": self._repository.get_elderly_by_location_area(),
        }

    def get_diabetes_by_location_area(self, cnes: int = None, equipe: int = None):
        return (self._repository.get_diabetes_by_location_area(cnes, equipe),)

    def get_hypertension_by_location_area(self, cnes: int = None, equipe: int = None):
        return self._repository.get_hypertension_by_location_area(cnes, equipe)

    def get_child_by_location_area(self):
        return self._repository.get_child_by_location_area()

    def get_elderly_by_location_area(self):
        return self._repository.get_elderly_by_location_area()
