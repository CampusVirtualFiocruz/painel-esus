from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


def filter_by_localidade(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes, equipe)

    return f"""WITH pessoas as ({sql_pessoas}),
                cidadaos as (
            select
                p.*,
                case 
                    when LOWER(tipo_localidade) is null  then 'nao_definido'
                    when LOWER(tipo_localidade) = 'urbana' then 'urbano'
                    when LOWER(tipo_localidade) = 'rural' then 'rural'
                    when LOWER(tipo_localidade) = 'urbana' then 'urbano'                    
                end tipo    
            from
                pessoas p )
            select tipo, count(*) total  from cidadaos group by 1 """


