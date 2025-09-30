Module interfaces.demographic_repository
========================================
Interfaces de repositório para Demografia.

Define contratos para repositórios de pirâmide etária, distribuição por sexo,
agregações por tipo de localidade e total de pessoas.

Classes
-------

`AgeGroupsInterface()`
:   Contrato para obter dados de pirâmide etária.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `get_age_groups(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :

`GenderInterface()`
:   Contrato para obter distribuição por sexo.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `get_gender(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :

`LocationAreaInterface()`
:   Contrato para agregações por tipo de localidade e recortes específicos.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `get_child_by_location_area(self) ‑> Dict`
    :   Retorna indicadores de crianças por localidade.

    `get_diabetes_by_location_area(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :

    `get_elderly_by_location_area(self) ‑> Dict`
    :   Retorna indicadores de idosos por localidade.

    `get_hypertension_by_location_area(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :

    `get_location_area(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :

`TotalPeopleInterface()`
:   Contrato para contagem total de pessoas.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `get_total_people(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :