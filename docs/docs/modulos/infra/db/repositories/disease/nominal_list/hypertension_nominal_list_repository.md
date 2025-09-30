Module disease.nominal_list.hypertension_nominal_list_repository
================================================================
Lista nominal de Hipertensão.

Listas nominais, filtros, ordenação e exportações com
anonimização.

Classes
-------

`HypertensionNominalListRepository()`
:   Operações de leitura e exportação da base nominal de Hipertensão.

    ### Methods

    `find_all(self, cnes: int = None) ‑> Dict`
    :

    `find_all_download(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :   Retorna DataFrame para exportação anonimizando dados sensíveis.

    `find_by_id(self, cidadao_pec)`
    :

    `find_by_nome(self, nome: str)`
    :

    `find_filter(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None, equipe: int = None, query: str = None, sort=[])`
    :   Retorna lista nominal (items e metadados de paginação).
        
        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.