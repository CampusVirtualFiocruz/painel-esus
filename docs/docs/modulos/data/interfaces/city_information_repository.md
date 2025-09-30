Module interfaces.city_information_repository
=============================================
Interfaces de repositório para informações do município.

Define o contrato que os repositórios concretos de informações da cidade
devem implementar.

Classes
-------

`CityInformationRepository()`
:   Contrato para recuperação de informações municipais, unidades e equipes.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `get_city_info(self, cnes: int = None) ‑> Dict`
    :   Retorna informações gerais do município (IBGE, CEP, UF etc.), opcionalmente filtradas por CNES.

    `get_teams(self, cnes: int = None) ‑> Dict`
    :   Lista equipes de saúde, opcionalmente filtradas por CNES.

    `get_units(self) ‑> Dict`
    :   Lista unidades de saúde do município.

    `get_units_with_patients(self) ‑> Dict`
    :   Lista unidades com agregações de pacientes.