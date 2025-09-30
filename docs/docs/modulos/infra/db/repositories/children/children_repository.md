Module children.children_repository
===================================
Crianças.

Consultas relacionadas ao acompanhamento de crianças
(consultas, visitas de Agente Comunitário de Saúde (ACS), odontologia, marcos do desenvolvimento
etc.).

Responsabilidades principais:
- Totais (crianças atendidas/cadastradas) e séries de 12 meses.
- Distribuiçao por faixa etária e por raça/cor.
- Indicadores específicos (primeira consulta em 8 dias, consultas até 2 anos,
  visitas de Agente Comunitário de Saúde (ACS) em 30 dias/6 meses, registros de peso e altura, marcos, alimentação
  avaliada, procedimentos odontológicos).
- Listas nominais com paginação e exportação anonimizadas.

Classes
-------

`ChildrenRepository()`
:   Implementa operações de leitura de dados de Crianças.

    ### Methods

    `get_acs_visit_until_30d(self, cnes: int = None, equipe: int = None)`
    :   Visitas de ACS até 30 dias do nascimento.

    `get_acs_visit_until_6m(self, cnes: int = None, equipe: int = None)`
    :   Visitas de ACS até 6 meses de vida.

    `get_appointments_until_2_years(self, cnes: int = None, equipe: int = None)`
    :   Atendimentos até os 2 anos de idade.

    `get_by_age(self, cnes: int = None, equipe: int = None)`
    :   Indicadores por faixa etária.

    `get_by_race(self, cnes: int = None, equipe: int = None)`
    :   Indicadores por raça/cor.

    `get_dental_appointments_until_12m(self, cnes: int = None, equipe: int = None)`
    :   Consultas odontológicas até 12 meses.

    `get_dental_appointments_until_24m(self, cnes: int = None, equipe: int = None)`
    :   Consultas odontológicas até 24 meses.

    `get_evaluated_feeding(self, cnes: int = None, equipe: int = None)`
    :   Avaliação de alimentação em consultas/visitas.

    `get_first_consult_8d(self, cnes: int = None, equipe: int = None)`
    :   Total de primeira consulta em até 8 dias de vida.

    `get_high_weight_records(self, cnes: int = None, equipe: int = None)`
    :   Registros de peso e altura no acompanhamento infantil.

    `get_milestone(self, cnes: int = None, equipe: int = None)`
    :   Indicadores de marco do desenvolvimento.

    `get_nominal_list(self, cnes: int = None, equipe: int = None, page: int = 0, page_size: int = 10, nome: str = None, cpf: str = None, nome_unidade_saude: int = None, q: str = None, sort: list[dict] = None) ‑> list[dict]`
    :   Retorna lista nominal (items e metadados de paginação).
        
        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - nome, cpf, query (q): filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.

    `get_nominal_list_download(self, cnes: int = None, equipe: int = None)`
    :   Gera DataFrame para exportação da lista nominal.
        
        Os dados sensíveis são anonimizados.

    `get_total_children(self, cnes: int = None, equipe: int = None)`
    :   Retorna total de crianças por UBS/equipe.

    `get_total_twelve_months_children(self, cnes: int = None, equipe: int = None)`
    :   Retorna acumulado e último 12 meses de crianças atendidas.

    `total_card(self, cnes: int = None, equipe: int = None, category: str = 'atentidas')`
    :   Retorna totais agrupado por localização.

    `total_medical_cares(self, cnes: int = None, equipe: int = None)`
    :   Total de atendimentos médicos para o público infantil.