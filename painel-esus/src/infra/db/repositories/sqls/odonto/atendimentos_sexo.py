def get_oral_health_cares_by_gender(cnes: int = None):
    if cnes:
        return """
            with 
                gender as (
                    select 
                    distinct ds_sexo, ds_faixa_etaria, co_seq_fat_atd_odnt, (dt_registro - dt_nascimento) as age  
                    from atendimento_odontologico where co_dim_unidade_saude_1 = :cnes
                ),
                faixas as (
                    select *, case 
                        when age <= 2 then '0 a 24 meses' 
                        when age > 2 and age <= 9 then '2 a 9 anos' 
                        when age > 9 and age <= 19 then '10 a 19 anos' 
                        when age > 19 and age <= 59 then '20 a 59 anos' 
                        when age > 59 then '> de 60 anos' 
                    end as tipo from gender
                )
                select ds_sexo, co_seq_fat_atd_odnt , tipo as ds_faixa_etaria, count(*) as total from faixas group by tipo, ds_sexo ;
        """
    return """
            with 
                gender as (
                    select 
                    distinct ds_sexo, ds_faixa_etaria, co_seq_fat_atd_odnt, (dt_registro - dt_nascimento) as age  
                    from atendimento_odontologico 
                ),
                faixas as (
                    select *, case 
                        when age <= 2 then '0 a 24 meses' 
                        when age > 2 and age <= 9 then '2 a 9 anos' 
                        when age > 9 and age <= 19 then '10 a 19 anos' 
                        when age > 19 and age <= 59 then '20 a 59 anos' 
                        when age > 59 then '> de 60 anos' 
                    end as tipo from gender
                )
                select ds_sexo, co_seq_fat_atd_odnt , tipo as ds_faixa_etaria, count(*) as total from faixas group by tipo, ds_sexo ;
        """


CARES_LOCATION_BY_GENDER = get_oral_health_cares_by_gender
