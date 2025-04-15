from abc import ABC, abstractmethod
from typing import Dict


class DemographicAgeGroupsInterface(ABC):
    @abstractmethod
    def get_age_groups(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass


class DemographicGenderInterface(ABC):
    @abstractmethod
    def get_gender(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass


class DemographicLocationAreaInterface(ABC):
    @abstractmethod
    def get_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_diabetes_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_hypertension_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_child_location_area(self) -> Dict:
        pass

    @abstractmethod
    def get_elderly_location_area(self) -> Dict:
        pass


class DemographicTotalPeopleInterface(ABC):
    @abstractmethod
    def get_total_people(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass
