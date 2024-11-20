from sqlalchemy import text

CHILDREN_BASE_QUERY = """SELECT
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
        equipes.cidadao_pec = crianca.cidadao_pec"""

def children_by_age_and_gender( cnes: int = None, equipe: int = None):
    where_clause = ' '
    if cnes is not None and cnes:
        where_clause += f" where equipes.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and equipes.codigo_equipe  = {equipe} "
    sql = f"""
        with
            criancas as (
               {CHILDREN_BASE_QUERY}
               {where_clause}
            )
            select meses,sexo, count(*) quantidade from criancas group by meses, sexo
            """
    return text(sql)


def children_by_age_and_location( cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None and cnes:
        where_clause += f" where equipes.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and equipes.codigo_equipe  = {equipe} "
    sql = f"""
        with
            criancas as (
               {CHILDREN_BASE_QUERY}
               {where_clause}
            )
            select meses,tipo_localidade, count(*) quantidade from criancas group by meses, tipo_localidade
            """
    return text(sql)
