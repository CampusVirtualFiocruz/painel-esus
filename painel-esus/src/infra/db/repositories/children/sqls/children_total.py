from sqlalchemy import text


def children_total(cnes: int = None, equipe: int = None):
    where_clause = "where "
    if cnes is not None and cnes:
        where_clause += f" equipes.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and equipes.codigo_equipe  = {equipe} "
    sql = """
        with
            criancas as (
                SELECT
                    DISTINCT crianca.cidadao_pec AS crianca_cidadao_pec
                FROM
                    crianca
                JOIN pessoas ON
                    pessoas.cidadao_pec = crianca.cidadao_pec
                JOIN equipes ON
                    equipes.cidadao_pec = crianca.cidadao_pec
                {where_clause}
            )
            select count(*) quantidade from criancas
    """
    return text(sql)

def children_total_cares(cnes:int = None, equipe:int = None):
    where_clause = "  "
    if cnes is not None and cnes:
        where_clause += f" where equipes.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and equipes.codigo_equipe  = {equipe} "
    sql = f"""with
criancas as (
	SELECT
		DISTINCT crianca.cidadao_pec AS crianca_cidadao_pec,
		(strftime('%Y', 'now') - strftime('%Y', pessoas.data_nascimento)) idade
	FROM
		crianca
	JOIN pessoas ON
		pessoas.cidadao_pec = crianca.cidadao_pec
	JOIN equipes ON
		equipes.cidadao_pec = crianca.cidadao_pec
    {where_clause}
)
select 
	( select count(*) from criancas where idade <= 2) ate_dois_anos_atendidas ,
	( select count(*) from pessoas where idade <= 2) ate_dois_anos_cadastradas"""
    return text(sql)

def children_location_rate(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where equipes.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and equipes.codigo_equipe  = {equipe} "
    sql = f"""with
                criancas as (
                    SELECT
                        DISTINCT crianca.cidadao_pec AS crianca_cidadao_pec,
                        (strftime('%Y', 'now') - strftime('%Y', pessoas.data_nascimento))*12 + (strftime('%m-%d', 'now')- strftime('%m-%d', pessoas.data_nascimento)) meses,
                        pessoas.nome AS pessoas_nome,
                        pessoas.data_nascimento AS pessoas_data_nascimento,
                        pessoas.sexo ,
                        pessoas.tipo_localidade 
                    FROM
                        crianca
                    JOIN pessoas ON
                        pessoas.cidadao_pec = crianca.cidadao_pec
                    JOIN equipes ON
                        equipes.cidadao_pec = crianca.cidadao_pec
                    {where_clause}
                ),
                total as (SELECT  count(DISTINCT crianca.cidadao_pec ) as total
                            FROM
                                crianca
                            JOIN pessoas ON
                                pessoas.cidadao_pec = crianca.cidadao_pec
                            JOIN equipes ON
                                equipes.cidadao_pec = crianca.cidadao_pec
                            {where_clause}
                )
                select 
                    tipo_localidade, 
                    count(*) quantidade, 
                    ROUND(cast(count(*) as float)/cast( (select total.total from total)as float), 2 ) quantidade_percentual, 
                    (select total.total from total) total 
                from criancas group by tipo_localidade"""
    return text(sql)
