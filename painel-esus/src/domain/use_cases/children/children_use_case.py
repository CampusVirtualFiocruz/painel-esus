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
    def children_high_weight_records(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_milestone(self, cnes: int = None, equipe: int = None):
        pass

    @abstractmethod
    def children_evaluated_feeding(self, cnes: int = None, equipe: int = None):
        pass
