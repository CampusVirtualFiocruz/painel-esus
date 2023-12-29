from abc import ABC, abstractmethod
from typing import Dict


class CityInformations(ABC):

    @abstractmethod
    def get_city_info(self, cnes: int = None) -> Dict: pass
    @abstractmethod
    def get_units(self) -> Dict: pass
