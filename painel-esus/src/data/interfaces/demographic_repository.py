"""Interfaces de repositório para Demografia.

Define contratos para repositórios de pirâmide etária, distribuição por sexo,
agregações por tipo de localidade e total de pessoas.
"""
from abc import ABC, abstractmethod
from typing import Dict


class AgeGroupsInterface(ABC):
    """Contrato para obter dados de pirâmide etária."""
    @abstractmethod
    def get_age_groups(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass


class GenderInterface(ABC):
    """Contrato para obter distribuição por sexo."""
    @abstractmethod
    def get_gender(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass


class LocationAreaInterface(ABC):
    """Contrato para agregações por tipo de localidade e recortes específicos."""
    @abstractmethod
    def get_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_diabetes_by_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_hypertension_by_location_area(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass

    @abstractmethod
    def get_child_by_location_area(self) -> Dict:
        """Retorna indicadores de crianças por localidade."""
        pass

    @abstractmethod
    def get_elderly_by_location_area(self) -> Dict:
        """Retorna indicadores de idosos por localidade."""
        pass


class TotalPeopleInterface(ABC):
    """Contrato para contagem total de pessoas."""
    @abstractmethod
    def get_total_people(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        pass
