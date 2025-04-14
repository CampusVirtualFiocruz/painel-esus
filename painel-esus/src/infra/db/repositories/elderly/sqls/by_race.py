def by_race(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause = " where "
        where_clause += f" codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT raca_cor, count(*) total
    FROM read_parquet('./dados/output/idoso.parquet')
    {where_clause} 
    group by raca_cor
    """