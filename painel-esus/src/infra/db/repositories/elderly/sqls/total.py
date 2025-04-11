def get_total_ubs(cnes: int = None, equipe: int = None):
    where_clause = "where "
    if cnes is not None and cnes:
        where_clause += f" codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT count(*) total 
    FROM read_parquet('./dados/output/idoso.parquet') 
    {where_clause}
    """
    
def get_medical_cares(cnes: int = None, equipe: int = None):
    where_clause = "where "
    if cnes is not None and cnes:
        where_clause += f" codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT count(*) total 
    FROM read_parquet('./dados/output/idoso.parquet') 
    {where_clause}
    """