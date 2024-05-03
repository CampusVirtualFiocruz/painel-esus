# pylint: disable=E0401
from abc import ABC, abstractmethod
from pandas import DataFrame


class OralHealthAllCaresRepositoryInterface(ABC):

    @abstractmethod
    def get_total(self, cnes: int = None) -> DataFrame: pass
