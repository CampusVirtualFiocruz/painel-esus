from abc import ABC, abstractmethod


class OralHealthDashboardUseCaseInterface(ABC):

    @abstractmethod
    def get_total(self, cnes: int = None): pass

    @abstractmethod
    def get_cares_by_line_of_services(self,  cnes: int = None): pass

    @abstractmethod
    def get_cares_by_type_of_services(self,  cnes: int = None): pass

    @abstractmethod
    def get_extraction_procedures_proportion(self,  cnes: int = None): pass

    @abstractmethod
    def get_oral_health_cares_by_age_range(self,  cnes: int = None): pass

    @abstractmethod
    def get_oral_health_cares_by_gender(self,  cnes: int = None): pass

    @abstractmethod
    def get_oral_health_cares_by_outcome(self,  cnes: int = None): pass

    @abstractmethod
    def get_oral_health_cares_by_place(self,  cnes: int = None): pass

    @abstractmethod
    def get_oral_health_all_cares_by_place(self,  cnes: int = None): pass
