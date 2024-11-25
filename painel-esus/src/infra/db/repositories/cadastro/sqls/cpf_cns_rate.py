from sqlalchemy import text

from .total import sql_round


def get_cpf_cns_rate(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        partial = f" where pessoas.codigo_unidade_saude = {cnes} "
        where_clause += partial
        if equipe is not None and equipe:
            partial = f" and pessoas.codigo_equipe_vinculada  = {equipe} "
            where_clause += partial

    com_cns_sql = sql_round("select * from com_cpf_cns ", "select * from total")
    sem_cns_sql = sql_round("select * from sem_cpf_cns ", "select * from total")

    sql = f"""with
    lista_pessoas as (
        select distinct cidadao_pec, codigo_unidade_saude, codigo_equipe_vinculada, cpf, cns from pessoas {where_clause}),
    total as ( 
        select count(*) from lista_pessoas
    ),
    com_cpf_cns as (
        select count(distinct cidadao_pec) from lista_pessoas  where cpf is NOT NULL or cns is not null
    ),
    sem_cpf_cns as (
        select count(distinct cidadao_pec) from lista_pessoas  where cpf is NULL and cns is null
    )
    select
{com_cns_sql} "cadastros-identificados-por-cpf-cns",
{sem_cns_sql} "sem-cpf-cnf" """

    return text(sql)
