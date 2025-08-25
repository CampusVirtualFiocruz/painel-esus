from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas

from .total import sql_round


def get_cpf_cns_rate(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes, equipe)

    com_cns_sql = sql_round(
        "select qtd from com_cpf_cns where tipo_ident_cpf_cns = 1 ", "select * from total"
    )
    sem_cns_sql = sql_round(
        "select qtd from com_cpf_cns where tipo_ident_cpf_cns = 0 ",
        "select * from total",
    )

    sql = f"""with
    pessoas as ({sql_pessoas}),
    lista_pessoas as (
        select distinct co_cidadao, codigo_unidade_saude, codigo_equipe_vinculada, cpf, cns from pessoas ),
    total as ( 
        select count(*) from lista_pessoas
    ),
    com_cpf_cns as (
        select tipo_ident_cpf_cns, count(*) qtd from pessoas group by 1
    )
    select
(select qtd from com_cpf_cns where tipo_ident_cpf_cns = 1)  "cadastros-identificados-por-cpf-cns",
(select qtd from com_cpf_cns where tipo_ident_cpf_cns = 0)  "sem-cpf-cnf" """

    # print(text(sql))
    return sql
