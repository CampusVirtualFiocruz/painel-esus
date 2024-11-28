from sqlalchemy import text

from .total import sql_round


def group_localidade(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        partial = f" where pessoas.codigo_unidade_saude = {cnes} "
        where_clause += partial
        if equipe is not None and equipe:
            partial = f" and pessoas.codigo_equipe_vinculada  = {equipe} "
            where_clause += partial

    porcentagem = sql_round("quantidade", "select * from total")

    sql = f"""with
        lista_pessoas as (
            select distinct cidadao_pec, codigo_unidade_saude, codigo_equipe_vinculada, tipo_localidade  from pessoas {where_clause} ),
        total as ( 
            select count(*) from lista_pessoas
        ),
        group_localidade as (
            select tipo_localidade, count(*) quantidade from lista_pessoas group by 1
        )
        select tipo_localidade, quantidade from group_localidade
        """
    return text(sql)
