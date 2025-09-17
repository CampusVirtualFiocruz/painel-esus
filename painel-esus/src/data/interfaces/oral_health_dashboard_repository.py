"""Interface do repositório de Saúde Bucal para o dashboard.

Define o contrato para consultas agregadas e
listas nominais, incluindo paginação e exportação.

Opcionalmente filtradas por CNES, equipe e categoria.
"""

# pylint: disable=E0401,W0102,R0913
from abc import ABC, abstractmethod
from ast import Dict

from pandas import DataFrame


class OralHealthDashboardRepositoryInterface(ABC):

    @abstractmethod
    def get_oral_health_extraction(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        """Retorna dados brutos para extração."""
        pass

    @abstractmethod
    def get_oral_health_cares_by_gender(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        """Agregados de atendimento por sexo."""
        pass

    @abstractmethod
    def get_oral_health_cares_by_race(
        self, cnes=None, equipe=None, category: str = None
    ) -> DataFrame:
        """Agregados de atendimento por raça/cor."""
        pass

    @abstractmethod
    def get_oral_health_first_appointment(
        self, cnes=None, equipe=None, category: str = None
    ) -> DataFrame:
        """Quantidade/percentual de primeira consulta odontológica."""
        pass

    @abstractmethod
    def get_oral_health_conclued_treatment(
        self, cnes=None, equipe=None, category: str = None
    ) -> DataFrame:
        """Totais de tratamentos odontológicos concluídos."""
        pass

    @abstractmethod
    def oral_health_get_supervised_brushing(
        self, cnes=None, equipe=None, category: str = None
    ) -> DataFrame:
        """Indicadores de escovação supervisionada."""
        pass

    @abstractmethod
    def get_oral_health_prevention_procedures(
        self, cnes=None, equipe=None, category: str = None
    ) -> DataFrame:
        """Totais de procedimentos preventivos realizados."""
        pass

    @abstractmethod
    def oral_health_get_atraumatic_treatment(
        self, cnes=None, equipe=None, category: str = None
    ) -> DataFrame:
        """Ocorrências de tratamento restaurador atraumático (TRA)."""
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
    ) -> DataFrame:
        """Busca lista nominal com filtros e paginação.

        Aplica filtros por nome, CPF, equipe e consulta; permite ordenação
        e segmentação por categoria.
        """
        pass

    @abstractmethod
    def total_ubs(self, cnes: int = None, equipe: int = None) -> Dict: pass

    @abstractmethod
    def donwload_nominal_list(self, cnes: int = None, equipe: int = None, category: str = 'atendidas') -> Dict: pass
