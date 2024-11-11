from typing import Dict

from src.data.interfaces.diseases_dashboard import DiseasesDashboardRepositoryInterface
from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.entities.disease_exams import DiseaseExams
from src.domain.use_cases.diseases_dashboard.diseases_use_case import (
    DiseasesDashboardUseCase,
)
from src.errors import InvalidArgument


class DiseaseUseCase(DiseasesDashboardUseCase):

    def __init__(self, repository: DiseasesDashboardRepositoryInterface):
        self.__repository = repository

    def get_total(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> DiseaseDashboardTotal:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        response = self.__repository.get_total(cnes, equipe)
        return response

    def get_age_group_gender(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_age_group_gender(cnes, equipe)

    def get_age_groups_location(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_age_groups_location(cnes, equipe)

    def get_complications(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_complications(cnes, equipe)

    def get_exams_count(
        self,
        cnes: int = None,
        equipe: int = None,
        exam_disease: DiseaseExams = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_exams_count(
            cnes=cnes,
            equipe=equipe,
            exam_disease=exam_disease,
        )

    def get_professionals_count(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_professionals_count(cnes, equipe)

    def get_imc(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_imc(cnes, equipe)

    def get_individual_exams_count(
        self,
        cnes: int = None,
        equipe: int = None,
        exam_disease: DiseaseExams = None,
        page: int = 1,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        return self.__repository.get_individual_exams_count(
            cnes,
            equipe,
            exam_disease,
            page,
        )
