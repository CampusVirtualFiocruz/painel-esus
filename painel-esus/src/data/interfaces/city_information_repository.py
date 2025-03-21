from abc import ABC
from abc import abstractmethod
from typing import Dict


class CityInformationRepository(ABC):
    @abstractmethod
    def get_city_info(self, cnes: int = None) -> Dict: pass
    @abstractmethod
    def get_units(self) -> Dict: pass
    @abstractmethod
    def get_units_with_patients(self) -> Dict: pass
    @abstractmethod
    def get_teams(self, cnes:int = None) -> Dict: pass
