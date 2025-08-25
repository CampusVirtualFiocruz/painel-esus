from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


def group_records_by_status(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes, equipe)

    sql = f"""with
                pessoas as ({sql_pessoas}),
                listas as ( select * from pessoas )
                select status_cadastro, count(*) as 'value' from listas group by status_cadastro
              """
    return sql
