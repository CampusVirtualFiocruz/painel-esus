Module cadastro.records_repository
==================================
Cadastro Individual.

Consultas relacionadas ao cadastro de pessoas (equipe,
localidade, raça/cor, status e outras agregações).

Responsabilidades principais:
- Agregar totais e indicadores do cadastro.
- Agrupar cadastros por localidade, raça/cor, origem e status.
- Fornecer listas nominais paginadas e exportação anonimizadas.

Observações:
- Quando a variável de ambiente ``MOCK=True`` estiver definida, alguns
  fluxos podem retornar dados simulados.

Classes
-------

`RecordsRepository()`
:   Implementa operações de leitura de dados cadastrais.

    ### Methods

    `find_all_download(self, cnes: int = None, equipe: int = None)`
    :   Gera DataFrame para exportação da lista nominal.
        
        Os dados sensíveis são anonimizados.

    `find_filter_nominal(self, cnes: int = None, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None, equipe: int = None, query: str = None, sort=[])`
    :   Retorna lista nominal (items e metadados de paginação).
        
        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - nome, cpf, query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.

    `get_cpf_cns_rate(self, cnes: int = None, equipe: int = None)`
    :   Retorna taxa de preenchimento de CPF/CNS entre os cadastrados.

    `get_total_group(self, cnes: int = None, equipe: int = None)`
    :   Retorna total de pessoas cadastradas por agrupamento padrão.
        
        Parâmetros opcionais cnes e equipe permitem filtrar por
        unidade e equipe.

    `group_localidade(self, cnes: int = None, equipe: int = None)`
    :   Agrupa cadastros por tipo de localidade.

    `group_raca_cor(self, cnes: int = None, equipe: int = None)`
    :   Agrupa cadastros por raça/cor.

    `group_records_by_origin(self, cnes: int = None, equipe: int = None)`
    :   Agrupa registros pela origem (ex.: e-SUS, importações).

    `group_records_status(self, cnes: int = None, equipe: int = None)`
    :   Agrupa cadastros por status (ativo, atualizado, desatualizado etc.).

    `nominal_list(self, cnes: int = None, equipe: int = None)`
    :   Lista nominal baseada na origem dos registros.

    `people_who_get_care(self, cnes: int = None, equipe: int = None)`
    :   Retorna agregações de pessoas que recebem atendimento.