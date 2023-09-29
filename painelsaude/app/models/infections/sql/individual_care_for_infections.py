INDIVIDUAL_CARE_FOR_INFECTIONS = """
with atd_individual_filtro_ciaps as (
    select
            co_seq_fat_atd_ind,
            co_dim_tempo,
            nu_cns,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_ciaps, '|'), '|'), '|')) as codigo,
            'CIAPS' as tipo
    from
                tb_fat_atendimento_individual
    group by 1,2,3,4,5,6,7,8,9,10
    union
    select
                        co_seq_fat_atd_ind,
            co_dim_tempo,
            nu_cns,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_cids, '|'), '|'), '|')) as codigo,
            'CID' as tipo			
    from
                tb_fat_atendimento_individual
    group by 1,2,3,4,5,6,7,8,9,10
    ), total as ( select count(*) as total from tb_fat_atendimento_individual tfai )
"""