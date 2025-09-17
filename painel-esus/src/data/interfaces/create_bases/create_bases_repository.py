"""Interface para criação/atualização de bases nominais derivadas.

Usada por processos que consolidam dados do e-SUS em tabelas auxiliares
para consumo rápido pelo Painel (ex.: bases nominais de hipertensão/diabetes).
"""

from abc import ABC
from abc import abstractmethod


class CreateBasesRepositoryInterface(ABC):

    @abstractmethod
    def create_base(self):
        """Gera ou atualiza a base nominal alvo, persistindo no banco local."""
        pass

    # @abstractmethod
    # def destroy_base(self): pass
