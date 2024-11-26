from src.infra.db.repositories.sqls.nominal_list.autoreferido import (
    autorreferidos_check,
)


def get_indicators_hipertensao(cnes: int = None, equipe: int = None):
    where_clause = " where co_fat_cidadao_pec NOTNULL and co_dim_tempo_nascimento > 0 "
    if cnes is not None:
        where_clause += f""" and co_dim_unidade_saude_vinc = {cnes} """
        if equipe is not None:
            where_clause += f""" and co_dim_equipe = {equipe} """
    return f"""with lista as (
	    select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from hipertensao
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
    select *, count(*) total  from lista_localidade group by 1"""


def get_indicators_hipertensao_plus_autorreferidos(cnes: int = None, equipe: int = None):
    where_clause = " where co_fat_cidadao_pec NOTNULL and co_dim_tempo_nascimento > 0 "
    if cnes is not None:
        where_clause += f""" and co_dim_unidade_saude = {cnes} """
        if equipe is not None:
            where_clause += f""" and co_dim_equipe = {equipe} """
    hipertensao_sql = autorreferidos_check(cnes, "hipertensao", "hipertensao", equipe)

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
