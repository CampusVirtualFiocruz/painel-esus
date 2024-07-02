# pylint: disable=R1718,C0301
def get_atendimentos(cids, dates=None):
    if dates is not None:
        if isinstance(dates, list):
            dates_sql = f"and  tfai.co_dim_tempo: : text: : date between '{dates[0]}' and '{dates[1]}'"
    else:
        dates_sql = """ and co_dim_tempo::text::date between (
		select
			max(tfai.co_dim_tempo::text::date)
		from
			tb_fat_atendimento_individual tfai)::DATE - interval '12 month' and (
		select
			max(tfai.co_dim_tempo::text::date) from tb_fat_atendimento_individual tfai) """

    return f"""with 
atendimento_individual  as (
    select * from tb_fat_atendimento_individual tfai  where (ds_filtro_ciaps like any (array[ {cids}])
		or ds_filtro_cids like any(array[{cids}]))  {dates_sql}
	order by co_dim_tempo asc
),
atd_individual_filtro_ciaps as (
    select
            co_seq_fat_atd_ind,
            co_dim_tempo,
            atd.nu_cns,
            atd.co_dim_cbo_1,
            coalesce(nu_peso, 0 ) nu_peso,
            coalesce(nu_altura, 0) nu_altura,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_ciaps, '|'), '|'), '|')) as codigo,
            'CIAPS' as tipo
    from
                atendimento_individual atd
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
            atd.nu_cns,
            atd.co_dim_cbo_1,
            coalesce(nu_peso, 0 ) nu_peso,
            coalesce(nu_altura, 0) nu_altura,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_cids, '|'), '|'), '|')) as codigo,
            'CID' as tipo
    from
                atendimento_individual atd
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
            atd.nu_cns,
            atd.co_dim_cbo_1,
            coalesce(nu_peso, 0) nu_peso,
            coalesce(nu_altura, 0) nu_altura,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_proced_solicitados , '|'), '|'), '|')) as codigo,
                    'Procedimentos Solicitados' as tipo
    from
                atendimento_individual atd
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
            atd.nu_cns,
            atd.co_dim_cbo_1,
            coalesce(nu_peso, 0) nu_peso,
            coalesce(nu_altura, 0) nu_altura,
            co_dim_unidade_saude_1 as co_dim_unidade_saude,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_proced_avaliados , '|'), '|'), '|')) as codigo,
                    'Procedimentos Avaliados' as tipo
    from
                atendimento_individual atd
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
        atd.*,
     tfcp.no_cidadao,
        coalesce(tfcd.co_dim_tipo_localizacao, 1) co_dim_tipo_localizacao,
        coalesce(tfcp.co_dim_tempo_nascimento, 0) co_dim_tempo_nascimento,
    coalesce(tc.nu_cbo, '0') as cbo,
    t.dt_registro
from
        atd_individual_filtro_ciaps atd
left join tb_dim_tempo t on
        t.co_seq_dim_tempo = atd.co_dim_tempo
left join tb_fat_familia_territorio tfft on
        tfft.co_fat_cidadao_pec = atd.co_fat_cidadao_pec
left join tb_fat_cad_domiciliar tfcd on
        tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar 
left join tb_fat_cidadao_pec  tfcp on tfcp.co_seq_fat_cidadao_pec  = atd.co_fat_cidadao_pec 
left join tb_dim_cbo tc on atd.co_dim_cbo_1 = tc.co_seq_dim_cbo
"""


ATENDIMENTO_INDIVIDUAL_CID_CIAPS_PROCEDIMENTOS = get_atendimentos
