from typing import Dict

from src.data.interfaces.hypertension_dashboard import \
    HypertensionDashboardRepositoryInterface
from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.use_cases.diabetes_hypertension.hypertension_use_case import \
    HypertensionDasboardUseCaseInterface
from src.errors import InvalidArgument


class HypertensionUseCase(HypertensionDasboardUseCaseInterface):

    def __init__(self, repository: HypertensionDashboardRepositoryInterface):
        self.__repository = repository

    def get_total(self, cnes: int = None) -> DiseaseDashboardTotal:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self.__repository.get_total(cnes)
        return response

    def get_age_group_gender(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        return self.__repository.get_age_group_gender(cnes)

    def get_age_groups_location(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        return self.__repository.get_age_groups_location(cnes)

    def get_complications(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        return self.__repository.get_complications(cnes)

    def get_exams_count(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        return self.__repository.get_exams_count(cnes)

    def get_professionals_count(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        return self.__repository.get_professionals_count(cnes)

    def get_imc(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        return self.__repository.get_imc(cnes)
