def get_pessoas(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                co_dim_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "
    sql = f"""
                select 
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
                    no_tipo_logradouro_tb_cidadao tipo_endereco,
                    ds_logradouro_tb_cidadao endereco,
                    nu_numero_tb_cidadao numero,
                    no_bairro_tb_cidadao bairro,
                    ds_complemento_tb_cidadao complemento,
                    ds_cep_tb_cidadao cep,
                    ds_tipo_localizacao_domicilio  tipo_localidade,
                    telefone , 
                    no_cidadao nome,
                    no_sexo_cidadao sexo,
                    nu_micro_area_domicilio micro_area,
                    nome_equipe ,
                    nome_unidade_saude,
                    fci_att_2anos,
                    fcdt_att_2anos,
                    alerta_status_cadastro,
                    alerta,
                    co_dim_unidade_saude codigo_unidade_saude, 
                    codigo_equipe codigo_equipe_vinculada,
                    dt_update_fci ultima_atualizacao_fci,
                    dt_atualizacao_fcd ultima_atualizacao_fcd
                from read_parquet('./dados/output/cadastro_db.parquet') 
                {where_clause}    
            """

    return sql
