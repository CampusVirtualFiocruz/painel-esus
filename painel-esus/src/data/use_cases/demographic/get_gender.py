from typing import Dict, Optional

from src.data.interfaces.demographic_repository import GenderInterface
from src.domain.use_cases.demographic.demographic_use_case import GenderUseCaseInterface


class GetGenderUseCase(GenderUseCaseInterface):
    def __init__(self, _repository: GenderInterface):
        self._repository = _repository

    def get_gender(
        self, cnes: Optional[int] = None, equipe: Optional[int] = None
    ) -> Dict:
        return self._repository.get_gender(cnes=cnes, equipe=equipe)
