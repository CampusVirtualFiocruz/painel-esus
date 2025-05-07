from typing import Literal

def gen_where_category(category):
    if category == 'atendidas':
        return 'atendimento_odonto=1 '
    elif category == 'cadastradas':
        return 'cadastradas_odonto=1 '
    else:
        raise ValueError(f"Categoria inválida: '{category}'. Esperado 'atendidas' ou 'cadastradas'.")
    
def gen_where_cnes_equipe(base_clause, cnes, equipe):
    clauses = []

    if base_clause:
        clauses.append(base_clause)

    if cnes:
        clauses.append(f" codigo_unidade_saude  = {cnes} ")

    if equipe:
        clauses.append(f" codigo_equipe = {equipe} ")

    return f"WHERE {' AND '.join(clauses)} " if clauses else ''

def get_suffix(column, category):
    if category == 'atendidas':
        return f'{column}_atendidas'
    else:
        return f'{column}_cadastradas'
    
def by_race(
    cnes: int = None, 
    equipe: int = None, 
    category: str = None,):
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)   
    
    return f"""
            SELECT  raca_cor, count(*) as total
            FROM read_parquet('/home/allanbontempo/programacao/fiocruz/painel-esus/painel-esus/src/infra/db/repositories/oral_health/sqls/dados/output/saude_bucal.parquet') 
            {where_clause}
            group by raca_cor """
            
def by_gender(
    cnes: int = None, 
    equipe: int = None, 
    category: str = None):
    
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    return f"""
        select 
            sexo, faixa_etaria, count(*) as total
        from read_parquet('/home/allanbontempo/programacao/fiocruz/painel-esus/painel-esus/src/infra/db/repositories/oral_health/sqls/dados/output/saude_bucal.parquet') 
        {where_clause}
        group by sexo, faixa_etaria
        order by sexo, max(idade);
                """

def base_chart(
    cnes: int = None, 
    equipe: int = None, 
    category: str = None,
    column: str = None):
    where_clause=''
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)   
    _column = get_suffix(column, category)
    
    return f"""
        select 
            {_column}, count(*)
        from read_parquet('/home/allanbontempo/programacao/fiocruz/painel-esus/painel-esus/src/infra/db/repositories/oral_health/sqls/dados/output/saude_bucal.parquet')  
        {where_clause}
        group by {_column}
        """  
def first_appointment(
    cnes: int = None, 
    equipe: int = None, 
    category: str = None,):
    
    return base_chart(cnes, equipe, category, 'agg_primeira_consulta')         
                
def conclued_treatment(cnes: int = None, 
    equipe: int = None, 
    category: Literal['atendidas','cadastradas'] = 'atendidas',):
    
    return base_chart(cnes, equipe, category, 'agg_tratamento_odonto_concluido')        
        
def extraction(cnes: int = None, 
    equipe: int = None, 
    category: Literal['atendidas','cadastradas'] = 'atendidas',):
    
    return base_chart(cnes, equipe, category, 'agg_realizaram_exodontia')   

def prevention_procedures(cnes: int = None, 
    equipe: int = None, 
    category: Literal['atendidas','cadastradas'] = 'atendidas',):
    
    return base_chart(cnes, equipe, category, 'agg_procedimentos_preventivos')     

def atraumatic_treatment(cnes: int = None, 
    equipe: int = None, 
    category: Literal['atendidas','cadastradas'] = 'atendidas',):
    
    return base_chart(cnes, equipe, category, 'agg_TRA')  
    
def supervised_brushing(cnes: int = None, 
    equipe: int = None, 
    category: Literal['atendidas','cadastradas'] = 'atendidas',):
    
    return base_chart(cnes, equipe, category, 'agg_realizaram_exodontia')    
    
    