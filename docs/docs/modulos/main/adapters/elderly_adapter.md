Module elderly_adapter
======================
Adapter para o módulo Idosos.

Formata respostas de repositórios em estruturas consumíveis pelo frontend:
estruturas prontas para o frontend e também adapta listas nominais.

Classes
-------

`ElderlyAdapter()`
:   Formata resultados do domínio Idosos para consumo na UI.

    ### Methods

    `by_gender(self, response)`
    :   Distribuição por sexo para faixas etárias padronizadas.

    `by_race(self, response)`
    :   Distribuição por raça/cor padronizada para o módulo Idosos.

    `creatinine(self, response)`
    :   Proporção com/sem avaliação de creatinina.

    `dentist_appointment(self, response)`
    :   Proporção com/sem consulta odontológica na APS.

    `influenza_vaccines(self, response)`
    :   Proporção de vacinação contra influenza.

    `ivcf_20(self, response)`
    :   Proporção com/sem avaliação IVCF-20.

    `nominal_list(self, response)`
    :   Adapter para lista nominal de idoso.

    `total_card(self, response)`
    :   Mapeia distribuição por localidade (urbana/rural/NI).

    `total_medical_cares(self, response)`
    :   Total de atendimentos médicos com idosos.

    `total_ubs(self, response)`
    :   Retorna total numérico de UBS aplicável ao módulo Idosos.

    `two_acs_visits(self, response)`
    :   Distribuição de pessoas com &lt;2 ou >=2 visitas ACS.

    `two_height_records(self, response)`
    :   Distribuição de pessoas com &lt;2 ou >=2 registros de peso/altura.

    `two_medical_appointment(self, response)`
    :   Distribuição de pessoas com &lt;2 ou >=2 consultas médicas em 12 meses.
