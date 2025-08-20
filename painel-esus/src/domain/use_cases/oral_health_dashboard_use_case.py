# pylint: disable=W0102,R0913
from abc import ABC, abstractmethod


class OralHealthDashboardUseCaseInterface(ABC):

    @abstractmethod
    def get_oral_health_extraction(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        pass

    @abstractmethod
    def get_oral_health_cares_by_gender(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        pass

    @abstractmethod
    def get_oral_health_cares_by_race(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        pass

    @abstractmethod
    def get_oral_health_first_appointment(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        pass

    @abstractmethod
    def get_oral_health_conclued_treatment(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        pass

    @abstractmethod
    def oral_health_get_supervised_brushing(
        self, cnes=None, equipe=None, category: str = None
    ):
        pass

    @abstractmethod
    def get_oral_health_prevention_procedures(
        self, cnes=None, equipe=None, category: str = None
    ):
        pass

    @abstractmethod
    def oral_health_get_atraumatic_treatment(
        self, cnes=None, equipe=None, category: str = None
    ):
        pass
    
    @abstractmethod
    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[],
        category: str = 'atendidas'
    ): pass
    
    @abstractmethod
    def get_oral_health_total(
        self, cnes: int = None, equipe: int = None
    ):
        pass

    @abstractmethod
    def donwload_nominal_list(
        self, cnes: int = None, equipe: int = None
    ):
        pass
