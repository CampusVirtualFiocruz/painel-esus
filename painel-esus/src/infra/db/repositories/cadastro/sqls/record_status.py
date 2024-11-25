from sqlalchemy import text

from .total import sql_round


def group_records_by_status(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" and sr.codigo_unidade_saude   = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and sr.codigo_equipe  = {equipe} "

    invalido = sql_round(
        "select quantidade from cadastros where tipo ='cadastros_invalidos'",
        "select * from total",
    )
    valido = sql_round(
        "select quantidade from cadastros where tipo !='cadastros_invalidos'",
        "select * from total",
    )
    sql = f"""with 
                cadastros as (select tipo, sum(quantidade) quantidade from status_records sr where tipo in ( 'cadastros_invalidos', 'cadastros_ativos') {where_clause} group by 1),
                total as (select sum(quantidade) quantidade from status_records sr where tipo in ( 'cadastros_invalidos', 'cadastros_ativos') {where_clause})
                select 
                (select quantidade from cadastros where tipo !='cadastros_invalidos')  cadastros_validos,
                {valido} cadastros_invalidos_porcentagem,
                (select quantidade from cadastros where tipo ='cadastros_invalidos')  cadastros_invalidos,
                {invalido}  cadastros_invalidos_porcentagem"""
    return text(sql)
