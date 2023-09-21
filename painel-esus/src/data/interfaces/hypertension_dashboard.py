from abc import ABC, abstractmethod

from src.domain.dict_types import DiseaseDashboardTotal


class HypertensionDashboardRepositoryInterface(ABC):

    @abstractmethod
    def get_total(self, cnes: int = None) -> DiseaseDashboardTotal: pass
