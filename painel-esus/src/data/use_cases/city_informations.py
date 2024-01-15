# pylint:disable=invalid-name

from typing import Dict

from src.domain.use_cases.city_nformations import CityInformations
from src.data.interfaces.city_information_repository import CityInformationRepository
from src.errors import InvalidArgument


class CityInformationsUseCase(CityInformations):

    def __init__(self, repository: CityInformationRepository):
        self._repository = repository

    def get_city_info(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_city_info(cnes)
        return response

    def get_units(self):
        response = self._repository.get_units()
        return response
