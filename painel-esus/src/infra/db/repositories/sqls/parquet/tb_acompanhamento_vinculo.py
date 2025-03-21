def get_pessoas_sql():
    return f"""select 
                    co_fat_cidadao_pec cidadao_pec,
                    co_cidadao ,
                    nu_cnes_vinc_equipe ,
                    nu_ine_vinc_equipe ,
                    dt_nasc_cidadao data_nascimento,
                    nu_cpf_cidadao cpf,
                    nu_cns_cidadao cns,
                    acompanhamento ,
                    status_cadastro ,
                    idade ,
                    tipo_ident_cpf_cns ,
                    faixa_etaria,
                    ds_raca_cor raca_cor,
                    no_tipo_logradouro tipo_endereco,
                    ds_logradouro  endereco,
                    nu_numero  numero,
                    no_bairro  bairro,
                    ds_complemento  complemento,
                    ds_cep  cep,
                    ds_tipo_localizacao_domicilio tipo_localidade,
                    telefone , 
                    no_cidadao nome,
                    no_sexo_cidadao sexo,
                    nu_micro_area micro_area,
                    nome_equipe ,
                    nome_unidade_saude,
                    fci_att_2anos,
                    fcdt_att_2anos,
                    alerta_status_cadastro,
                    alerta,
                    co_dim_unidade_saude codigo_unidade_saude, 
                    codigo_equipe codigo_equipe_vinculada,
                    cast(dt_update_fci AS VARCHAR)  ultima_atualizacao_fci,
                    cast(dt_atualizacao_fcd AS VARCHAR) ultima_atualizacao_fcd
                from read_parquet('./dados/output/cadastro_db.parquet')"""

def get_pessoas(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas_sql()
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                co_dim_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "
    sql = f""" {sql_pessoas}
               {where_clause}  """

    return sql
