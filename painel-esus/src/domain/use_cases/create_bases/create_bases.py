from abc import ABC, abstractmethod
from typing import Dict


class CreateBasesUsecasesInterface(ABC):

    @abstractmethod
    def create_bases(self) -> Dict: pass

    @abstractmethod
    def destroy_bases(self) -> Dict: pass
