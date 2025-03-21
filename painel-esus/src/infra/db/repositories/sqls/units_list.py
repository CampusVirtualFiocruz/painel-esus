# UNITS_LIST = """
# with
# unidades as (
# 	select co_dim_unidade_saude, sum(qtd) qtd
# 	from (
# 		select co_dim_unidade_saude, count(*) qtd from diabetes d group by 1
# 		union all
# 		select co_dim_unidade_saude, count(*) qtd from diabetes d group by 1
# 		) as unidades
# 	group by 1
# )
# select
# 	us.codigo_unidade_saude co_seq_dim_unidade_saude,
#  	us.nome no_unidade_saude,
#   	us.cnes nu_cnes,
#    	COALESCE (u.qtd, 0)
# qtd  from unidades_saude us left join unidades u on us.codigo_unidade_saude = u.co_dim_unidade_saude
# where qtd > 0
# """

UNITS_LIST = """
select 
	co_seq_dim_unidade_saude, 
 	no_unidade_saude, 
  	nu_cnes, 
   	1 qtd   
    from read_parquet('./dados/input/tb_dim_unidade_saude.parquet') """


UNIT_LIST_WITH_PATIENTS = """
with unidades as ( 
	SELECT distinct (co_dim_unidade_saude) co_dim_unidade_saude 
 	FROM read_parquet('./dados/output/cadastro_db.parquet') 
  )
	select 
	co_seq_dim_unidade_saude, 
 	no_unidade_saude, 
  	nu_cnes, 
   	1 qtd   
    from read_parquet('./dados/input/tb_dim_unidade_saude.parquet')
    WHERE co_seq_dim_unidade_saude in (select co_dim_unidade_saude from unidades) """
