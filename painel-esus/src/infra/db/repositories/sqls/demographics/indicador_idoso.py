def get_indicators_idoso(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None:
        where_clause += f"""            where 
                    pessoas.codigo_unidade_saude = {cnes}
                """
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    return f"""with
    idosos as (
        SELECT
            DISTINCT idoso.cidadao_pec AS idoso_cidadao_pec,
            pessoas.tipo_localidade  
        FROM
            idoso
        JOIN pessoas ON
            pessoas.cidadao_pec = idoso.cidadao_pec
        left JOIN equipes ON
            equipes.cidadao_pec = idoso.cidadao_pec
        {where_clause}    )
select 
   tipo_localidade, count(*)
from idosos group by tipo_localidade"""
