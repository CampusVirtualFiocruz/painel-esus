from sqlalchemy import text


def sql_round(numerador, denominador):
    sql_float = lambda x: f"cast(( {x} ) as flOAT)"
    sql = f"""ROUND(
    {sql_float(numerador)}/{sql_float(denominador)},
    2)"""
    return sql


def get_total_cadastros(cnes:int = None, equipe:int=None):
    where_clause = " "
    where_clause2 = "  "
    if cnes is not None and cnes:
        partial = f" pessoas.codigo_unidade_saude = {cnes} "
        where_clause2 += " and "+partial
        where_clause += " where  "+partial
        if equipe is not None and equipe:
            partial = f" and pessoas.codigo_equipe_vinculada  = {equipe} "
            where_clause2 += partial
            where_clause += partial
    round_sql = sql_round("select * from cadastros_atualizados", "select * from total")

    sql = f"""with
    total as ( 
        select count(distinct co_cidadao) from pessoas {where_clause}),
        cadastros_atualizados as (
            select count(distinct co_cidadao) from pessoas where pessoas.fci_att_2anos = 1 {where_clause2})
    select
        ( select * from total) total,
        {round_sql} cadastros_atualizados """
    print(sql)
    return text(sql)
