def get_indicators_diabetes(cnes: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause = f""" where co_dim_unidade_saude = {cnes} """
    return f"""with lista as (
	    select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from diabetes
        {where_clause}
    )
    select 
        case 
            when co_dim_tipo_localizacao = 1 then 'nao_informado'
            when co_dim_tipo_localizacao = 2 then 'urbano'
            when co_dim_tipo_localizacao = 3 then 'rural'
        end co_dim_tipo_localizacao, count(*) total 
    from lista group by 1"""
