Module elderly.elderly_repository
=================================
Idosos.

Consultas e listas do acompanhamento de idosos: totais por UBS,
atendimentos, distribuição por sexo/raça, exames e listas nominais com
paginação/exportação e anonimização de dados sensíveis.

Classes
-------

`ElderlyRepository()`
:   Leitura para indicadores e listas de idosos.

    ### Methods

    `acs_visits(self, cnes: int = None, equipe: int = None)`
    :   Visitas de ACS a idosos.

    `by_gender(self, cnes: int = None, equipe: int = None)`
    :   Distribuição por sexo entre idosos.

    `by_race(self, cnes: int = None, equipe: int = None)`
    :   Distribuição por raça/cor entre idosos.

    `creatinine(self, cnes: int = None, equipe: int = None)`
    :   Exames de creatinina e datas relacionadas para idosos.

    `dentist_appointment(self, cnes: int = None, equipe: int = None)`
    :   Atendimentos odontológicos com idosos.

    `find_all_download(self, cnes: int = None, equipe: int = None)`
    :   Gera DataFrame para exportação com anonimização de dados.

    `find_filter_nominal(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None, equipe: int = None, query: str = None, sort=[])`
    :   Retorna lista nominal (items e metadados de paginação).
        
        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.

    `height_records(self, cnes: int = None, equipe: int = None)`
    :   Registros de altura no acompanhamento do idoso.

    `influenza_vaccines(self, cnes: int = None, equipe: int = None)`
    :   Vacinação contra influenza em idosos.

    `ivcf_20(self, cnes: int = None, equipe: int = None)`
    :   Indicador IVCF-20 (fragilidade) para idosos.

    `medical_appointment(self, cnes: int = None, equipe: int = None)`
    :   Consultas médicas realizadas com idosos.

    `total_card(self, cnes: int = None, equipe: int = None)`
    :   Retorna totais agrupado por localização.

    `total_medical_cares(self, cnes: int = None, equipe: int = None)`
    :   Total de atendimentos médicos a idosos.

    `total_ubs(self, cnes: int = None, equipe: int = None)`
    :   Retorna totais por UBS para idosos.