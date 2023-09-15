ATENDIMENTO_INDIVIDUAL_CID_CIAPS = """
with atd_individual_filtro_ciaps as (
    select
            co_seq_fat_atd_ind,
            co_dim_tempo,
            nu_cns,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_ciaps, '|'), '|'), '|')) as codigo,
            'CIAPS' as tipo
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
        11
    union
    select
                        co_seq_fat_atd_ind,
            co_dim_tempo,
            nu_cns,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_cids, '|'), '|'), '|')) as codigo,
            'CID' as tipo
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
        11
    )		
select
	atd.*,
	tfcd.co_dim_tipo_localizacao
from
		atd_individual_filtro_ciaps atd
join tb_dim_tempo t on
	t.co_seq_dim_tempo = atd.co_dim_tempo
join tb_fat_familia_territorio tfft on
	tfft.co_fat_cidadao_pec = atd.co_fat_cidadao_pec
join tb_fat_cad_domiciliar tfcd on
	tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
 """