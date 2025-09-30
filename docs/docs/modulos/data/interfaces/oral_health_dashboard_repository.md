Module interfaces.oral_health_dashboard_repository
==================================================
Interface do repositório de Saúde Bucal para o dashboard.

Define o contrato para consultas agregadas e
listas nominais, incluindo paginação e exportação.

Opcionalmente filtradas por CNES, equipe e categoria.

Classes
-------

`OralHealthDashboardRepositoryInterface()`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `donwload_nominal_list(self, cnes: int = None, equipe: int = None, category: str = 'atendidas') ‑> ast.Dict`
    :

    `find_filter_nominal(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None, equipe: int = None, query: str = None, sort=[], category: str = 'atendidas') ‑> pandas.core.frame.DataFrame`
    :   Busca lista nominal com filtros e paginação.
        
        Aplica filtros por nome, CPF, equipe e consulta; permite ordenação
        e segmentação por categoria.

    `get_oral_health_cares_by_gender(self, cnes: int = None, equipe: int = None, category: str = None)`
    :   Agregados de atendimento por sexo.

    `get_oral_health_cares_by_race(self, cnes=None, equipe=None, category: str = None) ‑> pandas.core.frame.DataFrame`
    :   Agregados de atendimento por raça/cor.

    `get_oral_health_conclued_treatment(self, cnes=None, equipe=None, category: str = None) ‑> pandas.core.frame.DataFrame`
    :   Totais de tratamentos odontológicos concluídos.

    `get_oral_health_extraction(self, cnes: int = None, equipe: int = None, category: str = None)`
    :   Retorna dados brutos para extração.

    `get_oral_health_first_appointment(self, cnes=None, equipe=None, category: str = None) ‑> pandas.core.frame.DataFrame`
    :   Quantidade/percentual de primeira consulta odontológica.

    `get_oral_health_prevention_procedures(self, cnes=None, equipe=None, category: str = None) ‑> pandas.core.frame.DataFrame`
    :   Totais de procedimentos preventivos realizados.

    `oral_health_get_atraumatic_treatment(self, cnes=None, equipe=None, category: str = None) ‑> pandas.core.frame.DataFrame`
    :   Ocorrências de tratamento restaurador atraumático (TRA).

    `oral_health_get_supervised_brushing(self, cnes=None, equipe=None, category: str = None) ‑> pandas.core.frame.DataFrame`
    :   Indicadores de escovação supervisionada.

    `total_ubs(self, cnes: int = None, equipe: int = None) ‑> ast.Dict`
    :