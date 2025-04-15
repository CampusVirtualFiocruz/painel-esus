from typing import Optional

from src.data.interfaces.demographic_repository import DemographicTotalPeopleInterface
from src.domain.use_cases.demographic.demographic_use_case import (
    DemographicTotalPeopleUseCaseInterface,
)


class GetTotalPeople(DemographicTotalPeopleUseCaseInterface):
    def __init__(self, _repository: DemographicTotalPeopleInterface):
        self._repository = _repository

    def get_total_people(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> int:
        return self._repository.get_total_people(cnes=cnes, equipe=equipe)
