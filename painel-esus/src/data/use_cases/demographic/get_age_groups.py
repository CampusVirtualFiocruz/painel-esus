from typing import Dict, Optional

from src.data.interfaces.demographic_repository import AgeGroupsInterface
from src.domain.use_cases.demographic.demographic_use_case import (
    AgeGroupsUseCaseInterface,
)


class GetAgeGroupsUseCase(AgeGroupsUseCaseInterface):
    def __init__(self, _repository: AgeGroupsInterface):
        self._repository = _repository

    def get_age_groups(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> Dict:
        return self._repository.get_age_groups(cnes=cnes, equipe=equipe)
