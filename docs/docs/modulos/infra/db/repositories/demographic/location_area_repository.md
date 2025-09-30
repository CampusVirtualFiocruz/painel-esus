Module demographic.location_area_repository
===========================================
Demografia: Distribuição por localidade.

Agregações por tipo de localidade (urbana/rural) e integra
indicadores por localidade para condições específicas (diabetes, hipertensão),
além de crianças e idosos.

Classes
-------

`LocationAreaRepository(db_connection=<src.infra.db.settings.connection_duckdb.DuckDbHandler object>)`
:   Contrato para agregações por tipo de localidade e recortes específicos.
    
    Inicializa a conexão.

    ### Ancestors (in MRO)

    * src.data.interfaces.demographic_repository.LocationAreaInterface
    * abc.ABC

    ### Methods

    `get_child_by_location_area(self, cnes: int = None, equipe: int = None)`
    :   Retorna total de crianças por localidade.

    `get_diabetes_by_location_area(self, cnes: int = None, equipe: int = None)`
    :   Retorna agregações por localidade para população com diabetes.

    `get_elderly_by_location_area(self, cnes: int = None, equipe: int = None)`
    :   Retorna total de idosos por localidade.

    `get_hypertension_by_location_area(self, cnes: int = None, equipe: int = None)`
    :   Retorna agregações por localidade para população com hipertensão.

    `get_location_area(self, cnes: int = None, equipe: int = None)`
    :   Retorna agregações por tipo de localidade geral.