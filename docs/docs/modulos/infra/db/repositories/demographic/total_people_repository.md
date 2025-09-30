Module demographic.total_people_repository
==========================================
Demografia: Total de pessoas.

Classes
-------

`TotalPeopleRepository(db_connection=<src.infra.db.settings.connection_duckdb.DuckDbHandler object>)`
:   Contrato para contagem total de pessoas.
    
    Inicializa a conexão.

    ### Ancestors (in MRO)

    * src.data.interfaces.demographic_repository.TotalPeopleInterface
    * abc.ABC

    ### Methods

    `get_total_people(self, cnes: int = None, equipe: int = None)`
    :   Retorna o total de pessoas, opcionalmente filtradas por CNES e equipe.