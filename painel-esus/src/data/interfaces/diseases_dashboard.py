from abc import ABC
from abc import abstractmethod
from typing import Dict

from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.entities.disease_exams import DiseaseExams


class DiseasesDashboardRepositoryInterface(ABC):

    @abstractmethod
    def get_total(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> DiseaseDashboardTotal:
        pass

    @abstractmethod
    def get_age_groups_location(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_age_group_gender(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_complications(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_professionals_count(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_exams_count(
        self,
        cnes: int = None,
        equipe: int = None,
        exam_disease: DiseaseExams = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_individual_exams_count(
        self,
        cnes: int = None,
        equipe: int = None,
        exam_disease: DiseaseExams = None,
        page: int = 1,
    ) -> Dict:
        pass

    @abstractmethod
    def get_imc(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass
