def get_patients_by_gender(cnes, table):
    cnes_condition = ""
    if cnes is not None and cnes:
        cnes_condition = f' and d.co_dim_unidade_saude = {cnes}'
    sql = f"""
with 
lista as (
	select 
	distinct co_fat_cidadao_pec , d.co_dim_sexo,
	DATE(substr(co_dim_tempo_nascimento,1,4)||'-'||substr(co_dim_tempo_nascimento,5,2)||'-'||substr(co_dim_tempo_nascimento,7,2)) co_dim_tempo_nascimento
	from {table} d 
	where 	
        d.co_dim_tempo_nascimento IS NOT NULL and d.co_dim_tempo_nascimento > 0
        {cnes_condition}
),
idades as (
	select *, date(
	        date('now'),
	        '-'||(strftime('%m',co_dim_tempo_nascimento)-1)||' months',
	        '-'||(strftime('%d',co_dim_tempo_nascimento)-1)||' days'
	    )-co_dim_tempo_nascimento AS idade  from lista 
)
select
	count(*) qdt , 
	CASE 
		when co_dim_sexo =1 then 'Masculino'
		when co_dim_sexo =2 then 'Feminino'
		when co_dim_sexo =3 then '-'
	END co_dim_sexo,
CASE 
	when idade  >= 0 and idade <= 19 then '0 a 19 anos'
    when idade  >= 20 and idade <= 29 then '20 a 29 anos'
    when idade  >= 30 and idade <= 39 then '30 a 39 anos'
    when idade  >= 40 and idade <= 49 then '40 a 49 anos'
    when idade  >= 50 and idade <= 59 then '50 a 59 anos'
    when idade  >= 60  then '60+ anos'
END faixa_etaria 
from idades
group by co_dim_sexo, faixa_etaria;"""
    return sql


def get_patients_by_location(cnes, table):
    cnes_condition = ""
    if cnes is not None and cnes:
        cnes_condition = f" and d.co_dim_unidade_saude = {cnes}"
    sql = f"""
with 
lista as (
	select 
	distinct co_fat_cidadao_pec , d.co_dim_tipo_localizacao,
	DATE(substr(co_dim_tempo_nascimento,1,4)||'-'||substr(co_dim_tempo_nascimento,5,2)||'-'||substr(co_dim_tempo_nascimento,7,2)) co_dim_tempo_nascimento
	from {table} d 
	where 	
        d.co_dim_tempo_nascimento IS NOT NULL and d.co_dim_tempo_nascimento > 0
        {cnes_condition}
),
idades as (
	select *, date(
	        date('now'),
	        '-'||(strftime('%m',co_dim_tempo_nascimento)-1)||' months',
	        '-'||(strftime('%d',co_dim_tempo_nascimento)-1)||' days'
	    )-co_dim_tempo_nascimento AS idade  from lista 
)
select
	count(*) qdt , 
	CASE 
		when co_dim_tipo_localizacao =1 then 'Urbano'
		when co_dim_tipo_localizacao =2 then 'Rural'
		when co_dim_tipo_localizacao =3 then 'Não Informado'
	END co_dim_tipo_localizacao,
CASE 
    when idade  >= 0 and idade <= 19 then '0 a 19 anos'
    when idade  >= 20 and idade <= 29 then '20 a 29 anos'
    when idade  >= 30 and idade <= 39 then '30 a 39 anos'
    when idade  >= 40 and idade <= 49 then '40 a 49 anos'
    when idade  >= 50 and idade <= 59 then '50 a 59 anos'
    when idade  >= 60  then '60+ anos'
END faixa_etaria 
from idades
group by co_dim_tipo_localizacao, faixa_etaria;"""
    return sql
