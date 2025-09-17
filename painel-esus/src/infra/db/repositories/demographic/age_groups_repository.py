# pylint: disable=W1202

"""Demografia: Pirâmide etária.

Contagens por faixas etárias e sexo.
"""

from collections import OrderedDict
from typing import Dict

import duckdb
from src.data.interfaces.demographic_repository import AgeGroupsInterface
from src.errors.logging import logging
from src.infra.db.repositories.sqls.demographics import filter_by_gender_age
from src.infra.db.settings.connection_duckdb import DuckDbHandler
from src.main.adapters.adapters import DemographicAdapter


class AgeGroupsRepository(AgeGroupsInterface):

    def __init__(self, db_connection=DuckDbHandler()):
        """Inicializa a conexão."""
        self.db = db_connection
        self.indicators = None

    def get_age_groups(self, cnes: int = None, equipe: int = None):
        """Obtém contagens por faixas etárias (pirâmide etária), opcionalmente filtradas por CNES e equipe.

        O resultado é adaptado pelo DemographicAdapter.
        """
        age_gender = filter_by_gender_age(cnes, equipe)
        result_age_gender = self.db.fetchall(age_gender)
        # age_groups = self.__create_age_groups(result_age_gender)
        return DemographicAdapter().age_group_pyramid(result_age_gender)
