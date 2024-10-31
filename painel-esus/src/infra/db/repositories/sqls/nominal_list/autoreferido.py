AUTORREFERIDO = """
select distinct tfci.co_fat_cidadao_pec cidadao_pec, tfci.st_hipertensao_arterial, tfci.st_diabete from tb_fat_cad_individual tfci where  tfci.st_hipertensao_arterial = 1 or tfci.st_diabete = 1
"""

def autorreferidos_check(cnes, status, table):
    cnes_condition, status_condition= "",""
    if cnes is not None and cnes:
        cnes_condition = f'e.codigo_unidade_saude = {cnes} and '
    if status is not None and status:
        if status == 'hipertensao':
            status_condition = "a.st_hipertensao_arterial  = 1 and"

        if status == 'diabetes':
            status_condition = 'a.st_diabete  = 1 and'

    return f"""select 	distinct a.cidadao_pec co_fat_cidadao_pec, 
			CASE 
				when p.tipo_localidade = 'N/I' then 1
				when p.tipo_localidade = 'Zona Urbana' then 2
				when p.tipo_localidade = 'Zona Rural' then 3
			END co_dim_tipo_localizacao   
from 
	autorreferidos a 
	join equipes e on e.cidadao_pec  = a.cidadao_pec 
    join pessoas p on p.cidadao_pec = a.cidadao_pec 
where 
	{cnes_condition}
	{status_condition}
	a.cidadao_pec not in (select co_fat_cidadao_pec from {table})"""
