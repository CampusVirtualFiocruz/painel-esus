from abc import ABC, abstractmethod
from typing import Dict

class DemographicsInfo(ABC):

    @abstractmethod
    def get_demographics_info(self, cnes: int = None) -> Dict: pass
