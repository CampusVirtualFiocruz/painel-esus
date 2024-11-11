from abc import ABC
from abc import abstractmethod
from typing import Dict


class DemographicsInfoRepository(ABC):
    @abstractmethod
    def get_demographics_info(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass
