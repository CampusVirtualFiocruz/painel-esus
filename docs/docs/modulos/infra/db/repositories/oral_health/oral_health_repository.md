Module oral_health.oral_health_repository
=========================================
Saúde Bucal.

Distribuiçao por sexo/raça, primeiros atendimentos, extrações,
procedimentos preventivos, tratamentos atraumáticos e escovação supervisionada,
além de lista nominal com filtros/ordenação/exportação.

Classes
-------

`OralHealthRepository()`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * src.data.interfaces.oral_health_dashboard_repository.OralHealthDashboardRepositoryInterface
    * abc.ABC

    ### Methods

    `donwload_nominal_list(self, cnes: int = None, equipe: int = None, category=None)`
    :   Gera DataFrame para exportação com anonimização de dados.

    `find_filter_nominal(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None, equipe: int = None, query: str = None, sort=[], category: str = 'atendidas')`
    :   Retorna lista nominal (items e metadados de paginação).
        
        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.

    `get_oral_health_cares_by_gender(self, cnes=None, equipe=None, category: str = None)`
    :   Distribuiçao de atendimentos de Odontologia por sexo.

    `get_oral_health_cares_by_race(self, cnes=None, equipe=None, category: str = None)`
    :   Distribuiçao de atendimentos de Odontologia por raça/cor.

    `get_oral_health_conclued_treatment(self, cnes=None, equipe=None, category=None)`
    :   Tratamentos concluídos em Odontologia.

    `get_oral_health_extraction(self, cnes=None, equipe=None, category=None)`
    :   Procedimentos de extração dentária.

    `get_oral_health_first_appointment(self, cnes=None, equipe=None, category: str = None)`
    :   Primeiro atendimento odontológico.

    `get_oral_health_prevention_procedures(self, cnes=None, equipe=None, category=None)`
    :   Procedimentos preventivos em Odontologia.

    `oral_health_get_atraumatic_treatment(self, cnes=None, equipe=None, category=None)`
    :   Tratamento restaurador atraumático.

    `oral_health_get_supervised_brushing(self, cnes=None, equipe=None, category=None)`
    :   Escovação supervisionada.

    `total_card(self, cnes: int = None, equipe: int = None, category: str = 'atentidas')`
    :   Retorna totais de atendimentos para Odontologia.

    `total_ubs(self, cnes: int = None, equipe: int = None)`
    :   Retorna totais de atendimentos por UBS para Odontologia.