"""Demografia: Distribuição por localidade.

Agregações por tipo de localidade (urbana/rural) e integra
indicadores por localidade para condições específicas (diabetes, hipertensão),
além de crianças e idosos.
"""

import duckdb
from src.data.interfaces.demographic_repository import LocationAreaInterface
from src.infra.db.repositories.children.sqls.children_queries import (
    get_total_card as get_children_total_card,
)
from src.infra.db.repositories.elderly.sqls.total import (
    get_total_card as get_elderly_total_card,
)
from src.infra.db.repositories.sqls.demographics import filter_by_localidade
from src.infra.db.repositories.sqls.disease.auto_referidos import (
    filter_diabetes_by_localidade,
    filter_hypertension_by_localidade,
)
from src.infra.db.settings.connection_duckdb import DuckDbHandler


class LocationAreaRepository(LocationAreaInterface):

    def __init__(self, db_connection=DuckDbHandler()):
        """Inicializa a conexão."""
        self.db = db_connection

    def get_location_area(self, cnes: int = None, equipe: int = None):
        """Retorna agregações por tipo de localidade geral."""
        location_area_sql = filter_by_localidade(cnes, equipe)
        result_location_area_sql = self.db.fetchall(location_area_sql)
        return result_location_area_sql

    def get_diabetes_by_location_area(self, cnes: int = None, equipe: int = None):
        """Retorna agregações por localidade para população com diabetes."""
        location_area_sql = filter_diabetes_by_localidade(cnes, equipe)
        result_location_area_sql = self.db.fetchall(location_area_sql)
        return result_location_area_sql

    def get_hypertension_by_location_area(self, cnes: int = None, equipe: int = None):
        """Retorna agregações por localidade para população com hipertensão."""
        location_area_sql = filter_hypertension_by_localidade(cnes, equipe)
        result_location_area_sql = self.db.fetchall(location_area_sql)
        return result_location_area_sql

    def get_child_by_location_area(self, cnes: int = None, equipe: int = None):
        """Retorna total de crianças por localidade."""
        location_area_sql = get_children_total_card(cnes, equipe)
        result_location_area_sql = self.db.fetchall(location_area_sql)
        return result_location_area_sql

    def get_elderly_by_location_area(self, cnes: int = None, equipe: int = None):
        """Retorna total de idosos por localidade."""
        location_area_sql = get_elderly_total_card(cnes, equipe)
        result_location_area_sql = self.db.fetchall(location_area_sql)
        return result_location_area_sql
