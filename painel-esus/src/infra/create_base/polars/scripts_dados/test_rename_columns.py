import polars as pl

from .rename_columns import RENAME_RULE, columns_to_rename, difference_in_list

data = {
    "no_cidadao": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "London", "Paris"],
}
df = pl.DataFrame(data)
print(df)

def test_rename():
    df2 = df.rename(columns_to_rename(df))
    print(df2)

def test_diff_columns():
    list1 = {
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
        "co_dim_unidade_saude": "codigo_unidade_saude",
        "co_fat_cidadao_pec": "cidadao_pec",
        "co_unico_ultima_ficha": "codigo_unico_ultima_ficha",
        "dt_nasc_cidadao": "data_nascimento",
        "dt_ultima_atualizacao_cidadao": "data_ultima_atualizacao_cidadao",
        "dt_ultima_fci": "data_ultima_fci",
        "dt_tratamento_concluido_atendidas": "data_tratamento_concluido_atendidas",
        "dt_tratamento_concluido_cadastradas": "data_tratamento_concluido_cadastradas",
        "dt_primeira_consulta_atendidas": "data_primeira_consulta_atendidas",
        "dt_primeira_consulta_cadastradas": "data_primeira_consulta_cadastradas",
        "dt_TRA_atendidas": "data_TRA_atendidas",
        "dt_TRA_cadastradas": "data_TRA_cadastradas",
        "dt_ultimo_atendimento": "data_ultimo_atendimento",
    }
    result = difference_in_list(list1, RENAME_RULE)
    print(result)
