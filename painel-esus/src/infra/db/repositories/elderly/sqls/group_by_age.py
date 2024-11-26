from sqlalchemy import text

IDOSO_BASE_SQL = """SELECT
		DISTINCT idoso.cidadao_pec AS cidadao_pec,
		case 
		    when pessoas.idade  >= 0 and pessoas.idade <= 4 then '0 a 4 anos'
			when pessoas.idade  >= 5 and pessoas.idade <= 9 then '5 a 9 anos'
			when pessoas.idade  >= 10 and pessoas.idade <= 14 then '10 a 14 anos'
			when pessoas.idade  >= 15 and pessoas.idade <= 19 then '15 a 19 anos'
			when pessoas.idade  >= 20 and pessoas.idade <= 24 then '20 a 24 anos'
			when pessoas.idade  >= 25 and pessoas.idade <= 29 then '25 a 29 anos'
			when pessoas.idade  >= 30 and pessoas.idade <= 34 then '30 a 34 anos'
			when pessoas.idade  >= 35 and pessoas.idade <= 39 then '35 a 39 anos'
			when pessoas.idade  >= 40 and pessoas.idade <= 44 then '40 a 44 anos'
			when pessoas.idade  >= 45 and pessoas.idade <= 49 then '45 a 49 anos'
			when pessoas.idade  >= 50 and pessoas.idade <= 54 then '50 a 54 anos'
			when pessoas.idade  >= 55 and pessoas.idade <= 59 then '55 a 59 anos'
			when pessoas.idade  >= 60 and pessoas.idade <= 64 then '60 a 64 anos'
			when pessoas.idade  >= 65 and pessoas.idade <= 69 then '65 a 69 anos'
			when pessoas.idade  >= 70 and pessoas.idade <= 74 then '70 a 74 anos'
			when pessoas.idade  >= 75 and pessoas.idade <= 79 then '75 a 79 anos'
			when pessoas.idade  >= 80 and pessoas.idade <= 84 then '80 a 84 anos'
			when pessoas.idade  >= 85 and pessoas.idade <= 89 then '85 a 89 anos'
			when pessoas.idade  >= 90 and pessoas.idade <= 94 then '90 a 94 anos'
			when pessoas.idade  >= 95 and pessoas.idade <= 99 then '95 a 99 anos'
			when pessoas.idade  >= 100  then '100 ou mais'
        end as faixa_etaria,
		pessoas.tipo_localidade ,
		pessoas.sexo 
	FROM
		idoso
	JOIN pessoas ON
		pessoas.cidadao_pec = idoso.cidadao_pec
	JOIN equipes ON
		equipes.cidadao_pec = idoso.cidadao_pec"""

def group_by_age_gender(cnes:int = None, equipe:int = None):
    where_clause = ' '
    if cnes is not None:
        where_clause += f"""            where 
                    pessoas.codigo_unidade_saude = {cnes}
                """
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    sql = f"""
    WITH
        idosos as ( {IDOSO_BASE_SQL} {where_clause})
        select 
            sexo, 
            faixa_etaria, 
            count(*) quantidade 
        from idosos group by sexo, faixa_etaria order by faixa_etaria asc
    """
    return text(sql)


def group_by_age_location(cnes: int = None, equipe: int = None):
    where_clause = ' '
    if cnes is not None:
        where_clause += f"""            where 
                    pessoas.codigo_unidade_saude = {cnes}
                """
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    sql = f"""
    WITH
        idosos as ( {IDOSO_BASE_SQL} {where_clause})
        select 
            tipo_localidade, 
            faixa_etaria, 
            count(*) quantidade 
        from idosos group by tipo_localidade, faixa_etaria order by faixa_etaria asc
    """
    return text(sql)
