from src.infra.db.repositories.sqls.nominal_list.autoreferido import (
    autorreferidos_check,
)


def get_indicators_hipertensao(cnes: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause = f""" where co_dim_unidade_saude_vinc = {cnes} """
    return f"""with lista as (
	    select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from hipertensao
        {where_clause}
    )
    select 
        case 
            when co_dim_tipo_localizacao = 1 then 'nao_informado'
            when co_dim_tipo_localizacao = 2 then 'urbano'
            when co_dim_tipo_localizacao = 3 then 'rural'
        end co_dim_tipo_localizacao, count(*) total 
    from lista
    group by 1"""


def get_indicators_hipertensao_plus_autorreferidos(cnes: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause = f""" where co_dim_unidade_saude = {cnes} """
    hipertensao_sql = autorreferidos_check(cnes, "hipertensao", "hipertensao")

    sql = f"""with lista as (
	    select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from hipertensao {where_clause}
	    union all
	    {hipertensao_sql}
    )
    select 
        case 
            when co_dim_tipo_localizacao = 1 then 'nao_informado'
            when co_dim_tipo_localizacao = 2 then 'urbano'
            when co_dim_tipo_localizacao = 3 then 'rural'
        end co_dim_tipo_localizacao, count(*) total 
    from lista group by 1;"""
    return sql
