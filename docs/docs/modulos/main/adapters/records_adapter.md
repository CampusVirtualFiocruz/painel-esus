Module adapters.records_adapter
===============================
Adapters de agregação e transformação para Cadastros.

Converte respostas de consultas SQL em estruturas prontas para o frontend,
incluindo totais, percentuais e listas nominais com anonimização.

Classes
-------

`RecordsAdapter()`
:   Utilitários para montar respostas de Cadastros.

    ### Methods

    `get_cpf_cns_rate(self, response)`
    :   Percentual de cadastros identificados por CPF/CNS e não identificados.

    `get_total_group(self, response)`
    :   Agrupa total de cadastros e percentual de atualizados.

    `group_localidade(self, response)`
    :   Distribuição por localidade (urbana/rural/não informado).

    `group_raca_cor(self, response)`
    :   Distribuição por raça/cor com percentuais e valores absolutos.

    `group_records_by_origin(self, response)`
    :   Totais por origem do cadastro (FCI/PEC/recusa).

    `nominal_list(self, response)`
    :   Transforma itens de saída em dicionários anonimizados.

    `people_who_get_care(self, response)`
    :   Percentual de acompanhados e não acompanhados.

    `records_status(self, response)`
    :   Distribuição por status de cadastro.