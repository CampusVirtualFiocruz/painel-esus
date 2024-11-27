# pylint: disable=C0103
equipes_join = """
select distinct
			on(co_fat_cidadao_pec, co_dim_unidade_saude, co_dim_equipe) co_fat_cidadao_pec cidadao_pec,
			co_dim_unidade_saude codigo_unidade_saude,
			tdus.no_unidade_saude nome_unidade_saude,
			co_dim_equipe codigo_equipe,
			tde.no_equipe nome_equipe,
			tde.nu_ine ine,
   			nu_micro_area micro_area
		from
			cidadao_equipe ce
			left join tb_dim_unidade_saude tdus on tdus.co_seq_dim_unidade_saude = ce.co_dim_unidade_saude
			left join tb_dim_equipe tde on tde.co_seq_dim_equipe = ce.co_dim_equipe
			join pessoas_id p on p.co_seq_fat_cidadao_pec = ce.co_fat_cidadao_pec
		where nu_micro_area is not null
		order by
			co_fat_cidadao_pec asc,
			co_dim_unidade_saude asc,
			co_dim_equipe asc
   """
