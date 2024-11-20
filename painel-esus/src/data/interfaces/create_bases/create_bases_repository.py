from abc import ABC
from abc import abstractmethod


class CreateBasesRepositoryInterface(ABC):

    @abstractmethod
    def create_base(self): pass

    # @abstractmethod
    # def destroy_base(self): pass
