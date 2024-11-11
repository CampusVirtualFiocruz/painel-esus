# pylint:disable=invalid-name
from typing import Dict

from src.data.interfaces.demographics_info import DemographicsInfoRepository
from src.domain.use_cases.demographics_info import (
    DemographicsInfo as DemographicsInfoInterface,
)
from src.errors import InvalidArgument


class DemographicsInfo(DemographicsInfoInterface):

    def __init__(self, repository: DemographicsInfoRepository):
        self._repository = repository

    def get_demographics_info(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        response = self._repository.get_demographics_info(cnes, equipe)
        return response
