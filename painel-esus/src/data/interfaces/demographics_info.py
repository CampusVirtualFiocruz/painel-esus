from abc import ABC, abstractmethod
from typing import Dict

class DemographicsInfoRepository(ABC):
    @abstractmethod
    def get_demographics_info(self, cnes: int = None) -> Dict: pass
