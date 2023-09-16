#pylint:disable=invalid-name

from typing import Dict

from src.domain.use_cases.demographics_info import DemographicsInfo as DemographicsInfoInterface
from src.data.interfaces.demographics_info import DemographicsInfoRepository
from src.errors import InvalidArgument


class DemographicsInfo(DemographicsInfoInterface):

    def __init__(self, repository: DemographicsInfoRepository):
        self._repository = repository

    def get_demographics_info(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_demographics_info(cnes)
        return response
