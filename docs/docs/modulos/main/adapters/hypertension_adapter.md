Module adapters.hypertension_adapter
====================================
Adapters para hipertensão e diabetes.

Formata respostas de repositórios em estruturas consumíveis pelo frontend:
totais, IMC, complicações, por sexo/raça.

Classes
-------

`DiabetesAdapter()`
:   Adapter de Hipertensão.

    ### Ancestors (in MRO)

    * adapters.hypertension_adapter.HypertensionAdapter
    * src.main.adapters.base.base_dashboard_adapter.BaseDashboardAdapter

`HypertensionAdapter()`
:   Adapter de Hipertensão.

    ### Ancestors (in MRO)

    * src.main.adapters.base.base_dashboard_adapter.BaseDashboardAdapter

    ### Descendants

    * adapters.hypertension_adapter.DiabetesAdapter

    ### Methods

    `get_by_gender(self, response)`
    :   Agrupamento por sexo e faixa etária.

    `get_by_race(self, response)`
    :   Agrupamento por raça/cor.

    `get_complications(self, response)`
    :   Percentual de complicações associadas dividido em blocos binários.

    `get_exams_count(self, response)`
    :   Contagem do status de exames solicitados/pendentes/registrados por tipo.

    `get_imc(self, response)`
    :   Distribuição de IMC com valores percentuais e binários por classe.

    `get_total(self, response)`
    :   Repasse direto do agregado de totais já estruturado no repositório.