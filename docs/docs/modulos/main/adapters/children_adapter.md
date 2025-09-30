Module adapters.children_adapter
================================
Adapter para o módulo Crianças.

Formata respostas de repositórios em estruturas consumíveis pelo frontend:
totais, distribuiçoes por raça/idade/indicadores e lista nominal.

Classes
-------

`ChildrenAdapter()`
:   Converte respostas do domínio Crianças em objetos prontos para UI.

    ### Methods

    `acs_visit_until_30d(self, response)`
    :

    `acs_visit_until_6m(self, response)`
    :

    `appointments_until_2_years(self, response)`
    :

    `by_age_children(self, response)`
    :   Distribuição por faixas etárias e sexo.

    `by_race_children(self, response)`
    :

    `dental_appointments_until_12m(self, response)`
    :

    `dental_appointments_until_24m(self, response)`
    :

    `evaluated_feeding(self, response)`
    :

    `first_consult_8d(self, response)`
    :

    `high_weight_records(self, response)`
    :

    `milestone(self, response)`
    :

    `nominal_list(self, response)`
    :

    `total_and_12_months_adapter(self, response)`
    :   Retorna total acumulado e total dos últimos 12 meses.

    `total_count_children(self, response)`
    :   Extrai total de crianças de uma consulta agregada.

    `total_medical_cares(self, response)`
    :   Total de atendimentos médicos.

    `total_ubs(self, response)`
    :   Total de UBS relacionadas ao módulo Crianças.