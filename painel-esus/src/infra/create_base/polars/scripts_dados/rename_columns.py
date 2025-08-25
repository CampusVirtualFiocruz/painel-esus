RENAME_RULE = {
    "nu_cnes_vinc_equipe": "cnes_equipe",
    "nu_ine_vinc_equipe": "ine_equipe",
    "ds_cep": "cep",
    "ds_complemento": "complemento",
    "ds_logradouro": "logradouro",
    "ds_raca_cor": "raca_cor",
    "ds_tipo_localizacao_domicilio": "tipo_localizacao_domicilio",
    "nu_cns_cidadao": "cns",
    "nu_cpf_cidadao": "cpf",
    "nu_micro_area": "micro_area",
    "nu_numero": "numero",
    "no_cidadao": "nome",
    "no_sexo_cidadao": "sexo",
    "no_municipio": "municipio",
    "no_tipo_logradouro": "tipo_logradouro",
    "no_bairro": "bairro",
    "st_registro_valido_equipe": "status_registro_valido_equipe",
    "st_registro_valido_und_saude": "status_registro_valido_unidade_saude",
    "total_consulta_med_enferm": "total_consulta_medico_enfermeiro",
    "co_dim_unidade_saude": "codigo_unidade_saude",
    "co_fat_cidadao_pec": "cidadao_pec",
    "co_unico_ultima_ficha": "codigo_unico_ultima_ficha",
    "dt_nasc_cidadao": "data_nascimento",
    "dt_penultima_medico_enferm": "data_penultima_consulta_medico_enfermeiro",
    "dt_ultima_atualizacao_cidadao": "data_ultima_atualizacao_cidadao",
    "dt_ultima_fci": "data_ultima_fci",
    "dt_ultima_medico_enferm": "data_ultima_consulta_medico_enfermeiro",
    "dt_ultima_vacina": "data_ultima_vacina",
    "dt_ultimo_atend_odonto": "data_ultimo_atendendimento_odonto",
    "dt_ultimo_creatinina": "data_ultimo_creatinina",
    "dt_ultimo_atendimento": "data_ultimo_atendimento",
    "dt_TRA_cadastradas": "data_TRA_cadastradas",
    "dt_primeira_consulta_cadastradas": "data_primeira_consulta_cadastradas",
    "dt_tratamento_concluido_cadastradas": "data_tratamento_concluido_cadastradas",
    "dt_TRA_atendidas": "data_TRA_atendidas",
    "dt_primeira_consulta_atendidas": "data_primeira_consulta_atendidas",
    "dt_tratamento_concluido_atendidas": "data_tratamento_concluido_atendidas",
}

def columns_to_rename(input_dt):

    current_columns = set(input_dt.columns)
    columns_to_rename = RENAME_RULE
    target_columns = set(columns_to_rename.keys())

    intersections = list(current_columns.intersection(target_columns))

    result = {
        key: columns_to_rename[key] for key in intersections if key in columns_to_rename
    }

    return result

def difference_in_list(list1, list2):
    diff = list(set(list1) - set(list2))
    result = {key: list1[key] for key in diff if key in list1}

    result2 = {key: list2[key] for key in diff if key in list2}
    return {**result, **result2}
