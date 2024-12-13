AUTORREFERIDO = """
with 
atendimento as (
	select tfci.co_fat_cidadao_pec , tfci.co_dim_tempo  from tb_fat_cad_individual tfci where st_hipertensao_arterial = 1 or st_diabete = 1 group by co_fat_cidadao_pec , co_dim_tempo having max(co_dim_tempo::text::date) = co_dim_tempo::text::date
),
lista as (
	select tfci.* from tb_fat_cad_individual tfci join atendimento a on a.co_fat_cidadao_pec = tfci.co_fat_cidadao_pec and a.co_dim_tempo = tfci.co_dim_tempo
),
autorreferidos as (
	select co_fat_cidadao_pec, max(co_dim_tempo) co_dim_tempo, st_hipertensao_arterial, st_diabete  from lista group by 1,3,4
),
autorreferidos_lista as (
	select  distinct on (co_fat_cidadao_pec) co_fat_cidadao_pec, st_hipertensao_arterial, st_diabete from autorreferidos
)
select co_fat_cidadao_pec cidadao_pec, st_hipertensao_arterial, st_diabete from autorreferidos_lista
"""

def autorreferidos_check(cnes, status, table, equipe:int = None):
    cnes_condition, status_condition= "",""
    join = ""
    if cnes is not None and cnes:
        join = " join equipes e on e.cidadao_pec  = a.cidadao_pec  "
        cnes_condition = f'e.codigo_unidade_saude = {cnes} and '
        if equipe is not None and equipe:
            cnes_condition = f"e.codigo_equipe = {equipe} and "
    if status is not None and status:
        if status == 'hipertensao':
            status_condition = "a.st_hipertensao_arterial  = 1 and"

        if status == 'diabetes':
            status_condition = 'a.st_diabete  = 1 and'

    return f"""select 	distinct a.cidadao_pec co_fat_cidadao_pec, 
			CASE 
				when p.tipo_localidade = 'N/I' or p.tipo_localidade is null then 1
				when p.tipo_localidade = 'Urbana' then 2
				when p.tipo_localidade = 'Rural' then 3
			END co_dim_tipo_localizacao   
from 
	autorreferidos a 
    join pessoas p on p.cidadao_pec = a.cidadao_pec 
    {join}
where 
	{cnes_condition}
	{status_condition} """
