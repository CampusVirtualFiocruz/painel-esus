from ..disease import DIABETES_PATH, HYPERTENSION_PATH
from .auto_referidos import get_disease_base_sql


def get_patients_by_gender(cnes, table, equipe:int = None):

    sql_disease = get_disease_base_sql(cnes, equipe, table=='hipertensao')

    sql = f"""
        with 
        condicao as ({sql_disease}),
        listafinal as (
            select
                no_sexo_cidadao co_dim_sexo,
            CASE 
                when (faixa_etaria = '1a4' OR faixa_etaria = '5a9' OR faixa_etaria = '10a14'OR faixa_etaria = '15a19' OR faixa_etaria = '0a19'  ) then '0 a 19 anos'
            when faixa_etaria = '20a29'  then '20 a 29 anos'
            when faixa_etaria = '30a39'  then '30 a 39 anos'
            when faixa_etaria = '40a49'  then '40 a 49 anos'
            when faixa_etaria = '50a59'  then '50 a 59 anos'
            when faixa_etaria = '60mais' then '60+ anos'
            END faixa_etaria 
            from condicao
        )
        select count(*) as qtd, co_dim_sexo, faixa_etaria from listafinal
        group by co_dim_sexo, faixa_etaria order by faixa_etaria;"""
    return sql

def get_patients_by_location(cnes, table, equipe:int = None):
    sql_disease = get_disease_base_sql(cnes, equipe, table == "hipertensao")
    sql = f"""
with 
    condicao as ({sql_disease}),
    listafinal as (
        select
            ds_tipo_localizacao_domicilio co_dim_tipo_localizacao,
        CASE  
            when (faixa_etaria = '1a4' OR faixa_etaria = '5a9' OR faixa_etaria = '10a14'OR faixa_etaria = '15a19' OR faixa_etaria = '0a19' ) then '0 a 19 anos'
            when faixa_etaria = '20a29'  then '20 a 29 anos'
            when faixa_etaria = '30a39'  then '30 a 39 anos'
            when faixa_etaria = '40a49'  then '40 a 49 anos'
            when faixa_etaria = '50a59'  then '50 a 59 anos'
            when faixa_etaria = '60mais' then '60+ anos'
        END faixa_etaria 
        from condicao
    )
    select count(*) as qtd, co_dim_tipo_localizacao, faixa_etaria from listafinal
    group by co_dim_tipo_localizacao, faixa_etaria order by faixa_etaria;"""
    return sql
