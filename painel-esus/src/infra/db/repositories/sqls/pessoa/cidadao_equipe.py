# pylint: disable= R1703, W0612,C0103
cidadao_equipe = """
select distinct co_fat_cidadao_pec, co_dim_unidade_saude,  co_dim_equipe, nu_micro_area  from tb_fat_cad_individual tfci 
	union all 
select distinct co_fat_cidadao_pec, co_dim_unidade_saude,  co_dim_equipe, nu_micro_area from tb_fat_familia_territorio tfft 
	union all 
select distinct co_fat_cidadao_pec, co_dim_unidade_saude,  co_dim_equipe, nu_micro_area from tb_fat_cad_dom_familia
	union all
select co_seq_fat_cidadao_pec, co_dim_unidade_saude_vinc co_dim_unidade_saude,	co_dim_equipe_vinc co_dim_equipe, nu_micro_area  from tb_fat_cidadao_pec tfcp left join ta_cidadao tc on tc.co_seq_cidadao = tfcp.co_cidadao where 
nu_micro_area is not null and co_dim_unidade_saude_vinc is not null and co_dim_equipe_vinc is not null
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude_1 co_dim_unidade_saude,  co_dim_equipe_1 co_dim_equipe, null nu_micro_area from tb_fat_atendimento_individual
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude_1 co_dim_unidade_saude,  co_dim_equipe_2 co_dim_equipe, null nu_micro_area from tb_fat_atendimento_individual where co_dim_equipe_2 > 1
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude_2 co_dim_unidade_saude,  co_dim_equipe_2 co_dim_equipe, null nu_micro_area from tb_fat_atendimento_individual where co_dim_unidade_saude_2 > 1
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude_1 co_dim_unidade_saude,  co_dim_equipe_1 co_dim_equipe, null nu_micro_area from tb_fat_atendimento_odonto
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude_1 co_dim_unidade_saude,  co_dim_equipe_2 co_dim_equipe, null nu_micro_area from tb_fat_atendimento_odonto where co_dim_equipe_2 > 1
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude_2 co_dim_unidade_saude,  co_dim_equipe_2 co_dim_equipe, null nu_micro_area from tb_fat_atendimento_odonto where co_dim_unidade_saude_2 > 1
	union all
select distinct co_fat_cidadao_pec, co_dim_unidade_saude,  co_dim_equipe, null nu_micro_area from tb_fat_proced_atend tfpa
"""
