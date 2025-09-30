Module demographic.age_groups_repository
========================================
Demografia: Pirâmide etária.

Contagens por faixas etárias e sexo.

Classes
-------

`AgeGroupsRepository(db_connection=<src.infra.db.settings.connection_duckdb.DuckDbHandler object>)`
:   Contrato para obter dados de pirâmide etária.
    
    Inicializa a conexão.

    ### Ancestors (in MRO)

    * src.data.interfaces.demographic_repository.AgeGroupsInterface
    * abc.ABC

    ### Methods

    `get_age_groups(self, cnes: int = None, equipe: int = None)`
    :   Obtém contagens por faixas etárias (pirâmide etária), opcionalmente filtradas por CNES e equipe.
        
        O resultado é adaptado pelo DemographicAdapter.