from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


def filter_by_sexo(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes, equipe)
    return f"""
        WITH pessoas as ({sql_pessoas}),
        cidadaos as (
            select
                distinct p.sexo, p.co_cidadao
            from
                pessoas p
        )
        select 
            lower(sexo),
            count(*) total 
        from cidadaos
        group by 1
    """
