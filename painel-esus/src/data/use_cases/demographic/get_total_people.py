from typing import Optional

from src.data.interfaces.demographic_repository import TotalPeopleInterface
from src.domain.use_cases.demographic.demographic_use_case import (
    TotalPeopleUseCaseInterface,
)


class GetTotalPeopleUseCase(TotalPeopleUseCaseInterface):
    def __init__(self, _repository: TotalPeopleInterface):
        self._repository = _repository

    def get_total_people(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> int:
        return self._repository.get_total_people(cnes=cnes, equipe=equipe)
