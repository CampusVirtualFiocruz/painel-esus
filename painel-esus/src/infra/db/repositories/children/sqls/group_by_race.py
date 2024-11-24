from sqlalchemy import text


def group_by_race(cnes: int= None, equipe: int = None):
    where_clause = ' '
    where_clause_total = ' '
    if cnes is not None:
        where_clause += f"""  where  pessoas.codigo_unidade_saude = {cnes}  """
        where_clause_total = f" and pessoas.codigo_unidade_saude = {cnes}  "
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
            where_clause_total += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    sql = f"""
        with
            criancas as (
                SELECT
                    DISTINCT crianca.cidadao_pec AS crianca_cidadao_pec,
                    pessoas.raca_cor 
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
                        where
                            pessoas.raca_cor  is not NULL
                        {where_clause_total}
            )
            select 
                raca_cor, 
                count(*) quantidade,
                ROUND((CAST( count(*) AS FLOAT)/CAST( (select total.total from total ) AS FLOAT)), 2) porcentagem
            from criancas group by raca_cor
    """
    return text(sql)
