def get_total_ubs(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT count(*) total 
    FROM read_parquet('./dados/output/idoso.parquet') 
    {where_clause}
    """
    
def get_medical_cares(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT sum(pessoa_atendida_12_meses) total 
    FROM read_parquet('./dados/output/idoso.parquet') 
    {where_clause}
    """
    
def get_total_card(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT tipo_localizacao_domicilio, count(*) total 
    FROM read_parquet('./dados/output/idoso.parquet') 
    {where_clause}
    group by tipo_localizacao_domicilio
    """   