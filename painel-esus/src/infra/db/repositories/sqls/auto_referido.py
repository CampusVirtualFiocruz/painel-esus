# pylint: disable=W0719
def get_auto_referidos_disease(disease_st, ciaps):
    sql = f"""with auto_referido  as (select co_fat_cidadao_pec from tb_fat_cad_individual tfci where tfci.{disease_st} = 1 ),
lista as (select distinct on (tfai.co_fat_cidadao_pec) tfai.* from tb_fat_atendimento_individual tfai, auto_referido where tfai.co_dim_tempo::text::date between (
		select
			max(tfai.co_dim_tempo::text::date)
		from
			tb_fat_atendimento_individual tfai)::DATE - interval '12 month' and (
		select
			max(tfai.co_dim_tempo::text::date) from tb_fat_atendimento_individual tfai) and tfai.co_fat_cidadao_pec in (auto_referido.co_fat_cidadao_pec)
)
select count(*) as qtd from lista where 
ds_filtro_ciaps not like all (array[{ciaps}]) or
ds_filtro_cids not like all (array[{ciaps}])
;"""
    # print(sql)
    return sql


def get_self_reference_disease(disease, ciaps):
    if disease == 'diabetes':
        return get_auto_referidos_disease('st_diabete', ciaps)
    if disease == 'hipertensao':
        return get_auto_referidos_disease('st_hipertensao_arterial', ciaps)
    raise Exception("No disease found")
