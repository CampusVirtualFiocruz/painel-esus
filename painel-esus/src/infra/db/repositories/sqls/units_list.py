UNITS_LIST = """
select 
	a.co_seq_dim_unidade_saude,
	a.nu_cnes,
	a.no_unidade_saude 
from tb_dim_unidade_saude a
where exists (
      select 1 from tb_fat_atendimento_individual b
      where b.co_dim_unidade_saude_1 = a.co_seq_dim_unidade_saude 
      and b.co_dim_tempo::text::date between (
		select
			max(co_dim_tempo)
		from
			tb_fat_atendimento_individual)::text::DATE - interval '12 month' and (
		select
			max(co_dim_tempo)
		from
			tb_fat_atendimento_individual)::text::DATE
) order by no_unidade_saude asc; 
"""
