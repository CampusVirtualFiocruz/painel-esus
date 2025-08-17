from typing import Dict, Optional

from src.data.interfaces.demographic_repository import GenderInterface
from src.domain.use_cases.demographic.demographic_use_case import GenderUseCaseInterface
from src.main.adapters.adapters import DemographicAdapter


class GetGenderUseCase(GenderUseCaseInterface):
    def __init__(self, _repository: GenderInterface, _adapter=DemographicAdapter()):
        self._repository = _repository
        self._adapter = _adapter

    def get_gender(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> Dict:
        result = self._repository.get_gender(cnes=cnes, equipe=equipe)
        return self._adapter.gender_apadter(result)
