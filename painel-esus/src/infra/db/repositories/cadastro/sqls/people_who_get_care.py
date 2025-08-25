from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


def people_who_get_care(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes, equipe)

    sql = f"""
            with
            listas as ({sql_pessoas}),
            total as ( select count(*) from listas)
            select acompanhamento, count(*) as value from listas group by 1;
            """
    return sql
