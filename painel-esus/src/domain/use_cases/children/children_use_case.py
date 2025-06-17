from abc import ABC, abstractmethod


class ChildrenUseCase(ABC):

    @abstractmethod
    def children_total(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_by_age(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_by_race(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_first_consult_8d(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_appointments_until_2_years(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_acs_visit_until_30d(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_acs_visit_until_6m(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_dental_appointments_until_12m(
        self, cnes: int = None, equipe: int = None
    ):
        pass

    @abstractmethod
    def children_dental_appointments_until_24m(
        self, cnes: int = None, equipe: int = None
    ):
        pass

    def children_high_weight_records(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_milestone(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_evaluated_feeding(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_get_nominal_list(
        self,
        cnes: int = None,
        equipe: int = None,
        page: int = 0,
        page_size: int = 10,
        nome: str = None,
        cpf: str = None,
        nome_unidade_saude: int = None,
        sort: list[dict] = None,
    ):
        pass

    @abstractmethod
    def children_get_nominal_list_download(self, cnes: int = None, equipe: int = None):
        pass
