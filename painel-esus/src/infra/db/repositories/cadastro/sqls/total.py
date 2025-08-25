from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


def sql_round(numerador, denominador):
    sql_float = lambda x: f"cast(( {x} ) as flOAT)"
    sql = f"""ROUND(
    {sql_float(numerador)}/{sql_float(denominador)},
    2)"""
    return sql


def get_total_cadastros(cnes:int = None, equipe:int=None):
    sql_pessoas = get_pessoas(cnes, equipe)
    round_sql = sql_round("select * from cadastros_atualizados", "select * from total")

    sql = f"""with
    pessoas as ({sql_pessoas}),
    total as ( 
        select count(distinct co_cidadao) from pessoas ),
        cadastros_atualizados as (
            select count(distinct co_cidadao) from pessoas where pessoas.fci_att_2anos = 1 )
    select
        ( select * from total) total,
        {round_sql} cadastros_atualizados """
    return sql
