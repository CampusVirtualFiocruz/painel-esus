LISTAGEM_FCI = """
select
    distinct on (t1.co_seq_fat_cidadao_pec)
    t1.co_seq_fat_cidadao_pec as id_cidadao_pec,
    t1.co_cidadao,
    t2.nu_cns,
    t2.nu_cpf,
    t2.no_cidadao,
    t2.dt_nascimento as co_dim_tempo_nascimento,
    upper(t2.no_social) as no_social_cidadao,
    t3.co_dim_unidade_saude as co_dim_unidade_saude,
    t1.co_dim_sexo,
    t15.sg_sexo,
    t1.co_dim_identidade_genero,
    t16.ds_raca_cor,
    coalesce( tfcd.co_dim_tipo_localizacao, '1') co_dim_tipo_localizacao,
    upper(t2.no_mae) as no_mae_cidadao, upper(t2.no_pai) as no_pai_cidadao,
    upper(t13.no_profissional) as no_profissional,
    t2.dt_obito, t2.nu_documento_obito as nu_declaracao_obito,
    extract(year from age(current_date,t2.dt_nascimento)) as idade,
    extract(year from age(current_date, t2.dt_nascimento)) * 12 + extract(month from age(current_date, t2.dt_nascimento)) as total_meses,
    current_date - (t2.dt_nascimento  -  INTERVAL '1 DAY') as total_dias
from
    tb_fat_cidadao_pec t1
    inner join tb_cidadao t2 on t1.co_cidadao = t2.co_seq_cidadao
    left join tb_fat_cad_individual t3 on t2.co_unico_ultima_ficha  = t3.nu_uuid_ficha
    left join tb_dim_unidade_saude t4_fci on t3.co_dim_unidade_saude = t4_fci.co_seq_dim_unidade_saude
    left join tb_dim_equipe t5_fci on t3.co_dim_equipe = t5_fci.co_seq_dim_equipe
    left join tb_dim_profissional t6 on t3.co_dim_profissional = t6.co_seq_dim_profissional
    left join tb_dim_tipo_saida_cadastro t7 on t3.co_dim_tipo_saida_cadastro = t7.co_seq_dim_tipo_saida_cadastro
    left join tb_dim_unidade_saude t8_cc on t8_cc.co_seq_dim_unidade_saude = t1.co_dim_unidade_saude_vinc
    left join tb_dim_equipe t9_cc on t9_cc.co_seq_dim_equipe = t1.co_dim_equipe_vinc
    left join tb_dim_profissional t11 on t11.co_seq_dim_profissional = t3.co_dim_profissional
    left join tb_prof_historico_cns t12 on t12.nu_cns = t11.nu_cns
    left join tb_prof t13 on t13.co_seq_prof = t12.co_prof
    left join tb_dim_tipo_origem_dado_transp t14 on t14.co_seq_dim_tp_orgm_dado_transp = t3.co_dim_tipo_origem_dado_transp
    left join tb_dim_sexo t15 on  t15.co_seq_dim_sexo = t3.co_dim_sexo
    left join tb_dim_raca_cor t16 on t3.co_dim_raca_cor = t16.co_seq_dim_raca_cor
    left join tb_dim_situacao_trabalho t17 on t17.co_seq_dim_situacao_trabalho = t3.co_dim_situacao_trabalho
    left join tb_dim_cbo t18 on t18.co_seq_dim_cbo = t3.co_dim_cbo_cidadao
    left join tb_dim_tipo_escolaridade t19 on t19.co_seq_dim_tipo_escolaridade = t3.co_dim_tipo_escolaridade
    left join tb_dim_tipo_condicao_peso t20 on t20.co_seq_dim_tipo_condicao_peso = t3.co_dim_tipo_condicao_peso
    left join tb_nacionalidade t21 on t21.co_nacionalidade = t3.co_dim_nacionalidade
    left join tb_dim_tipo_orientacao_sexual t22 on t22.co_seq_dim_tipo_orientacao_sxl = t3.co_dim_tipo_orientacao_sexual
    left join tb_dim_povo_comunidad_trad t23 on t23.co_seq_dim_povo_comunidad_trad = t3.co_dim_povo_comunidad_trad
    left join tb_dim_municipio t24 on t24.co_seq_dim_municipio = t3.co_dim_municipio_cidadao
    left join tb_dim_uf t25 on t25.co_seq_dim_uf = t24.co_dim_uf
    left join tb_dim_identidade_genero t26 on t26.co_seq_dim_identidade_genero = t3.co_dim_identidade_genero
    left join tb_unidade_saude t27 on t27.nu_cnes = t8_cc.nu_cnes --unidade cc
    left join tb_tipo_unidade_saude t28 on t27.tp_unidade_saude = t28.co_seq_tipo_unidade_saude
    left join tb_equipe t29 on t29.nu_ine = t9_cc.nu_ine --equipe cc
    left join tb_tipo_equipe t30 on t29.tp_equipe = t30.co_seq_tipo_equipe
    left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = t1.co_seq_fat_cidadao_pec
    left join tb_fat_cad_domiciliar tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
where
    (
        (t2.st_ativo = 1 and t3.co_dim_tipo_saida_cadastro = 3 and t5_fci.nu_ine is not null and t3.st_ficha_inativa = 0)
        or
        (t3.co_dim_tipo_saida_cadastro is null and t2.st_ativo = 1 and t2.st_faleceu = 0 and t29.st_ativo = 1 and t30.nu_ms in ('70', '76'))
    )
"""
