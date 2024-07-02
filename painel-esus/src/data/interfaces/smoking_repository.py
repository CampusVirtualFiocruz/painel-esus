from abc import ABC
from abc import abstractmethod


class SmokingRepository(ABC):
    @abstractmethod
    def followed_smoked_people_proportion(self, cnes: int = None): pass

    @abstractmethod
    def risk_factors_proportion_by_dant(self, cnes: int = None): pass

    @abstractmethod
    def smokers_by_age(self, cnes: int = None): pass

    @abstractmethod
    def proportion_of_dental_consultations_among_smokers(
        self, cnes: int = None): pass

    @abstractmethod
    def smokers_by_sex(self, cnes: int = None): pass

    @abstractmethod
    def smokers_by_education(self, cnes: int = None): pass
