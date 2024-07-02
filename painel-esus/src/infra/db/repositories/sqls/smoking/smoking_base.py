SMOKING_BASE = """
with tfai as (
    select
            co_seq_fat_atd_ind,
            co_dim_tempo,
            nu_cns,
            dt_nascimento,
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
            co_dim_cbo_1
    from
                tb_fat_atendimento_individual
    group by
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11, 12, 13
    union
    select
            co_seq_fat_atd_ind,
            co_dim_tempo,
            nu_cns,
            dt_nascimento,
            coalesce(nu_peso, 0 ) nu_peso,
            coalesce(nu_altura, 0) nu_altura,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_cids, '|'), '|'), '|')) as codigo,
            'CID' as tipo,
            co_dim_cbo_1
    from
                tb_fat_atendimento_individual
    group by
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11, 12, 13
    )	
select
	tfai.*,
	ttl.ds_tipo_localizacao, 
	te.no_escolaridade
from
	tfai
left join
	tb_fat_atendimento_odonto tfao on tfai.co_fat_cidadao_pec = tfao.co_fat_cidadao_pec 
left join tb_fat_cidadao_pec tfcp on tfai.co_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec  
left join tb_cidadao tc  on  tfcp.co_cidadao = tc.co_seq_cidadao 
left join tb_escolaridade te on te.co_escolaridade = tc.co_escolaridade
left join tb_fat_cad_individual tfci on tfai.co_fat_cidadao_pec = tfai.co_fat_cidadao_pec 
join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfai.co_fat_cidadao_pec
left join tb_fat_cad_domiciliar tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
left join tb_dim_tipo_localizacao ttl on ttl.co_seq_dim_tipo_localizacao  = tfcd.co_dim_tipo_localizacao 
where
	tfai.codigo in ('P17', 'ABP011') and tfai.co_fat_cidadao_pec is not null
"""
