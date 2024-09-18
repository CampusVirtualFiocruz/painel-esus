from src.infra.create_base.local.create_base_atendimento_individual_filtro import (
    CreateLocalAtendimentoIndividualFiltroDatabase,
)
from src.infra.create_base.local.create_local_demographic_database import (
    CreateLocalDemographicDatabase,
)
from src.infra.create_base.local.create_local_units_bases_repository import (
    CreateLocalUnitsDatabase,
)
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


class CreateLocalDatabaseFactory:

    @staticmethod
    def demographics_factory():
        return CreateLocalDemographicDatabase(
            DBConnectionHandler(), LocalDBConnectionHandler()
        )

    @staticmethod
    def atendimento_individual_filtro_factory():
        return CreateLocalAtendimentoIndividualFiltroDatabase(
            DBConnectionHandler(), LocalDBConnectionHandler()
        )

    @staticmethod
    def units():
        return CreateLocalUnitsDatabase(
            DBConnectionHandler(),
            LocalDBConnectionHandler(),
        )
