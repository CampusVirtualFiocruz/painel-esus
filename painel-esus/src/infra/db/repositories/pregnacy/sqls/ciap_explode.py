CIAP_EXPLODE = """
select
        co_seq_fat_atd_ind,
        co_dim_tempo,
        co_dim_tempo_dum,
        nu_cns,
        coalesce(nu_peso, 0 ) nu_peso,
        coalesce(nu_altura, 0) nu_altura,
        co_dim_unidade_saude_1 as co_dim_unidade_saude,
        co_dim_faixa_etaria,
        co_dim_sexo,
        co_dim_local_atendimento,
        co_fat_cidadao_pec,
        nu_cpf_cidadao,
        unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_ciaps, '|'), '|'), '|')) as codigo,
            'CIAPS' as tipo,
        co_dim_cbo_1,
        co_dim_unidade_saude_1
from
            tb_fat_atendimento_individual
group by
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14	
"""
