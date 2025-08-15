from abc import ABC, abstractmethod
from typing import Dict


class AgeGroupsUseCaseInterface(ABC):
    @abstractmethod
    def get_age_groups(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass


class GenderUseCaseInterface(ABC):
    @abstractmethod
    def get_gender(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass


class IBGEPopulationUseCaseInterface(ABC):
    @abstractmethod
    def get_ibge_population(self) -> str:
        pass


class LocationAreaUseCaseInterface(ABC):
    @abstractmethod
    def get_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_diabetes_by_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_hypertension_by_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_child_by_location_area(self) -> Dict:
        pass

    @abstractmethod
    def get_elderly_by_location_area(self) -> Dict:
        pass


class TotalPeopleUseCaseInterface(ABC):
    @abstractmethod
    def get_total_people(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass
