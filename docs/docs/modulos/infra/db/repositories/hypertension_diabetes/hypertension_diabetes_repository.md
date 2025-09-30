Module hypertension_diabetes.hypertension_diabetes_repository
=============================================================
Indicadores de Hipertensão/Diabetes.

Recebe a condição-alvo ("disease") e expõe métodos para
indicadores (totais, exames, IMC, complicações, distribuição por localidade/raça/
sexo) e listas nominais com filtros/ordenação/exportação.

Observações:
- Quando a variável de ambiente ``MOCK=True`` estiver definida, alguns
  fluxos podem retornar dados simulados.

Classes
-------

`HypertensionDiabetesRepository(disease: str)`
:   Inicializa o repositório com a condição-alvo ("hipertensão"/"diabetes").

    ### Methods

    `get_by_gender(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Distribuição por sexo.

    `get_by_location(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Distribuição por localidade.

    `get_by_race(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Distribuição por raça/cor.

    `get_complications(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Complicações associadas à condição (retorna agregações).

    `get_exams_count(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Exames por condição (colunas dinâmicas).

    `get_imc(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Distribuição de IMC para a população-alvo.

    `get_nominal_list(self, cnes: int, page: int = 0, pagesize: int = 10, nome: str = None, cpf: str = None, equipe: int = None, query: str = None, sort=[])`
    :   Retorna lista nominal (items e metadados de paginação).
        
        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.

    `get_nominal_list_download(self, cnes: int = None, equipe: int = None) ‑> Dict`
    :   Gera DataFrame para exportação com anonimização de dados.

    `get_total(self, cnes: int = None, equipe: int = None, debug=False)`
    :   Retorna totais: atendimentos 12 meses, pessoas por CID/CIAP e autoreferidos.