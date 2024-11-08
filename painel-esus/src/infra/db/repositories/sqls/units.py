UNITS = """
select 
	a.co_seq_dim_unidade_saude codigo_unidade_saude,
	a.nu_cnes cnes,
	a.no_unidade_saude nome  
from tb_dim_unidade_saude a order by 1 asc	
"""
