from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas

from .total import sql_round


def group_localidade(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes,equipe)

    porcentagem = sql_round("quantidade", "select * from total")

    sql = f"""with
        pessoas as ({sql_pessoas}),
        lista_pessoas as (
            select distinct co_cidadao, codigo_unidade_saude, codigo_equipe_vinculada, tipo_localidade  from pessoas ),
        total as ( 
            select count(*) from lista_pessoas
        ),
        group_localidade as (
            select tipo_localidade, count(*) quantidade from lista_pessoas group by 1
        )
        select tipo_localidade, quantidade from group_localidade
        """
    return sql
