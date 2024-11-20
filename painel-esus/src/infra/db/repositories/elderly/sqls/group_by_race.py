from sqlalchemy import text


def group_by_race(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where equipes.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and equipes.codigo_equipe  = {equipe} "
    sql = f"""
        with
            idosos as (
                SELECT
                    DISTINCT idoso.cidadao_pec AS idoso_cidadao_pec,
                    pessoas.raca_cor 
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
            )
            select 
                raca_cor, 
                count(*) quantidade,
                ROUND((CAST( count(*) AS FLOAT)/CAST( (select total.total from total ) AS FLOAT)), 2) porcentagem
            from idosos group by raca_cor
    """
    return text(sql)
