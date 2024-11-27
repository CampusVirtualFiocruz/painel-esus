def filter_by_gender_age(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                    p.codigo_unidade_saude = {cnes}
                """
        if equipe and equipe is not None:
            where_clause += f"  and p.codigo_equipe_vinculada = {equipe} "
    return f"""
    with 
    cidadaos as (
     select
	        distinct p.*
	    from
	        pessoas p        
	    join equipes e on e.cidadao_pec = p.cidadao_pec
    {where_clause}
    ), lista as (
    select 
        UPPER(substr(sexo, 1,1))||LOWER(substr( sexo, 2)) sexo, case 
    when idade  >= 0 and idade <= 4 then '0 a 4 anos'
    when idade  >= 5 and idade <= 9 then '5 a 9 anos'
    when idade  >= 10 and idade <= 14 then '10 a 14 anos'
    when idade  >= 15 and idade <= 19 then '15 a 19 anos'
    when idade  >= 20 and idade <= 24 then '20 a 24 anos'
    when idade  >= 25 and idade <= 29 then '25 a 29 anos'
    when idade  >= 30 and idade <= 34 then '30 a 34 anos'
    when idade  >= 35 and idade <= 39 then '35 a 39 anos'
    when idade  >= 40 and idade <= 44 then '40 a 44 anos'
    when idade  >= 45 and idade <= 49 then '45 a 49 anos'
    when idade  >= 50 and idade <= 54 then '50 a 54 anos'
    when idade  >= 55 and idade <= 59 then '55 a 59 anos'
    when idade  >= 60 and idade <= 64 then '60 a 64 anos'
    when idade  >= 65 and idade <= 69 then '65 a 69 anos'
    when idade  >= 70 and idade <= 74 then '70 a 74 anos'
    when idade  >= 75 and idade <= 79 then '75 a 79 anos'
    when idade  >= 80 and idade <= 84 then '80 a 84 anos'
    when idade  >= 85 and idade <= 89 then '85 a 89 anos'
    when idade  >= 90 and idade <= 94 then '90 a 94 anos'
    when idade  >= 95 and idade <= 99 then '95 a 99 anos'
    when idade  >= 100  then '100 ou mais'
        end as tipo ,
     case 
		when LOWER(tipo_localidade) is null or LOWER(tipo_localidade) = 'n/i' then 'Nao Informado'
		when LOWER(tipo_localidade) = 'zona rural' then 'Rural'
		when LOWER(tipo_localidade) is not null  and LOWER(tipo_localidade) != 'zona rural' then 'Urbano'
	end localidade	
        from cidadaos
        )
    select *, count(*) total from lista
        group by sexo, tipo, localidade
    """
