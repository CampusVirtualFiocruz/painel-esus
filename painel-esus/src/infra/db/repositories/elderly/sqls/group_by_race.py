from sqlalchemy import text


def group_by_race(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None:
        where_clause += f""" where pessoas.codigo_unidade_saude = {cnes}  """
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    sql = f"""
        with
            idosos as (
                SELECT
                    DISTINCT idoso.cidadao_pec AS idoso_cidadao_pec,
                    case
                        when pessoas.raca_cor is null then 'Indefinido'
                        when pessoas.raca_cor is not null then pessoas.raca_cor
                    end raca_cor
                FROM
                    idoso
                JOIN pessoas ON
                    pessoas.cidadao_pec = idoso.cidadao_pec
                JOIN equipes ON
                    equipes.cidadao_pec = idoso.cidadao_pec
                {where_clause}
            ),
            total as (SELECT  count(DISTINCT idoso.cidadao_pec ) as total
                        FROM
                            idoso
                        JOIN pessoas ON
                            pessoas.cidadao_pec = idoso.cidadao_pec
                        JOIN equipes ON
                            equipes.cidadao_pec = idoso.cidadao_pec
                        {where_clause}
            )
            select 
                raca_cor, 
                count(*) quantidade,
                ROUND((CAST( count(*) AS FLOAT)/CAST( (select total.total from total ) AS FLOAT)), 2) porcentagem
            from idosos group by raca_cor
    """
    return text(sql)
