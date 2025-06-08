from abc import ABC, abstractmethod


class InfantilUseCase(ABC):

    @abstractmethod
    def infantil_total(self, cnes: int = None, equipe: int = None):
        pass
