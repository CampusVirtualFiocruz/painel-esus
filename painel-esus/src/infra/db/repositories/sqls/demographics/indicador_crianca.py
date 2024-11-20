def get_indicators_crianca(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None:
        where_clause += f""" where equipes.codigo_unidade_saude = {cnes} """
        if equipe is not None:
            where_clause += f""" and equipes.codigo_equipe = {equipe} """
    return f"""with
    criancas as (
        SELECT
            DISTINCT crianca.cidadao_pec AS crianca_cidadao_pec,
            pessoas.tipo_localidade  
        FROM
            crianca
        JOIN pessoas ON
            pessoas.cidadao_pec = crianca.cidadao_pec
        JOIN equipes ON
            equipes.cidadao_pec = crianca.cidadao_pec
        {where_clause}
    )
select 
   tipo_localidade, count(*)
from criancas group by tipo_localidade"""
