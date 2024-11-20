def get_indicators_idoso(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None:
        where_clause += f""" where equipes.codigo_unidade_saude = {cnes} """
        if equipe is not None:
            where_clause += f""" and equipes.codigo_equipe = {equipe} """
    return f"""with
    idosos as (
        SELECT
            DISTINCT idoso.cidadao_pec AS idoso_cidadao_pec,
            pessoas.tipo_localidade  
        FROM
            idoso
        JOIN pessoas ON
            pessoas.cidadao_pec = idoso.cidadao_pec
        JOIN equipes ON
            equipes.cidadao_pec = idoso.cidadao_pec
        {where_clause}
    )
select 
   tipo_localidade, count(*)
from idosos group by tipo_localidade"""
