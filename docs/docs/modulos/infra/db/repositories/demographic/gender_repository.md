Module demographic.gender_repository
====================================
Demografia: Distribuição por sexo.

Consulta agregada por sexo (feminino/masculino) e retorna um dicionário
com a contagem normalizada.

Classes
-------

`GenderRepository(db_connection=<src.infra.db.settings.connection_duckdb.DuckDbHandler object>)`
:   Contrato para obter distribuição por sexo.
    
    Inicializa a conexão.

    ### Ancestors (in MRO)

    * src.data.interfaces.demographic_repository.GenderInterface
    * abc.ABC

    ### Methods

    `get_gender(self, cnes: int = None, equipe: int = None)`
    :   Retorna contagens por sexo em formato de dicionário, opcionalmente filtradas por CNES e equipe.