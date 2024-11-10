# pylint: disable=C0103
lista_cidadao_pec_from_fichas = """
		select distinct co_fat_cidadao_pec  from tb_fat_atendimento_individual tfai  
		union all 
		select distinct co_fat_cidadao_pec  from tb_fat_atendimento_odonto tfao
		union all  
		select distinct co_fat_cidadao_pec  from tb_fat_cad_individual tfci 
		union all 
		select distinct co_fat_cidadao_pec  from tb_fat_proced_atend tfpa  
		union all 
		select distinct co_fat_cidadao_pec   from tb_fat_familia_territorio tfft join tb_fat_cad_domiciliar tfcd  on tfft.co_fat_cad_domiciliar = tfcd.co_seq_fat_cad_domiciliar
"""
