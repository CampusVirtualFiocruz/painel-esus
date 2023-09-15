from abc import ABC, abstractmethod
from typing import Dict
from pandas import DataFrame

class DemographicsInfo(ABC):

    @abstractmethod
    def get_demographics_info(self, data_frame: DataFrame) -> Dict: pass
