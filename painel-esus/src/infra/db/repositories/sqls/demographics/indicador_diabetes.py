from src.infra.db.repositories.sqls.nominal_list.autoreferido import (
    autorreferidos_check,
)


def get_indicators_diabetes(cnes: int = None, equipe: int = None):
    where_clause = " where co_fat_cidadao_pec NOTNULL and co_dim_tempo_nascimento > 0 "
    if cnes is not None:
        where_clause += f""" and co_dim_unidade = {cnes} """
        if equipe is not None:
            where_clause += f""" and co_dim_equipe = {equipe} """
    return f"""with lista as (
	    select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from diabetes
        {where_clause}
    ), lista_localidade as (
    select 
        case 
            when co_dim_tipo_localizacao = 1 then 'nao_informado'
            when co_dim_tipo_localizacao = 2 then 'urbano'
            when co_dim_tipo_localizacao = 3 then 'rural'
        end co_dim_tipo_localizacao
    from lista 
    )
    select * , count(*) total from lista localidade group by 1"""


def get_indicators_diabetes_plus_autorreferidos(cnes: int = None, equipe: int = None):
    where_clause = "where co_fat_cidadao_pec NOTNULL and co_dim_tempo_nascimento > 0 "
    if cnes is not None:
        where_clause += f""" and co_dim_unidade_saude = {cnes} """
        if equipe is not None:
            where_clause += f""" and co_dim_equipe = {equipe} """
    diabetes_sql = autorreferidos_check(cnes, 'diabetes', 'diabetes', equipe)

    return f"""with lista as (
	    select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from diabetes {where_clause}
	    union all
	    {diabetes_sql}
    )
    select 
        case 
            when co_dim_tipo_localizacao = 1 then 'nao_informado'
            when co_dim_tipo_localizacao = 2 then 'urbano'
            when co_dim_tipo_localizacao = 3 then 'rural'
        end co_dim_tipo_localizacao, count(*) total 
    from lista group by 1;"""
