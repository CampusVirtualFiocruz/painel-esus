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
