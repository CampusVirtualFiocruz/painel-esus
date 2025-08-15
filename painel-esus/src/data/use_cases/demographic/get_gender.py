from typing import Dict, Optional

from src.data.interfaces.demographic_repository import GenderInterface
from src.domain.use_cases.demographic.demographic_use_case import GenderUseCaseInterface
from src.main.adapters.adapters import DemographicAdapter


class GetGenderUseCase(GenderUseCaseInterface):
    def __init__(self, _repository: GenderInterface):
        self._repository = _repository

    def get_gender(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> Dict:
        result = self._repository.get_gender(cnes=cnes, equipe=equipe)
        return DemographicAdapter().gender_apadter(result)
