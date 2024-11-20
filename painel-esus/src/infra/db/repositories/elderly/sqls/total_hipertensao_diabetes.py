from sqlalchemy import text


def total_hipertension_diabetes(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None and cnes:
        where_clause += f" where e.codigo_unidade_saude = {cnes}"
        if equipe is not None and equipe:
            where_clause += f" and e.codigo_equipe = {equipe} "

    sql = f"""with 
                diabete_equipe as ( select distinct d.co_fat_cidadao_pec from  diabetes d join equipes e on e.cidadao_pec = d.co_fat_cidadao_pec {where_clause}),
                hipertensao_equipe as ( select distinct d.co_fat_cidadao_pec from  hipertensao d join equipes e on e.cidadao_pec = d.co_fat_cidadao_pec {where_clause}),
                duas_condicoes as ( select distinct de.co_fat_cidadao_pec from diabete_equipe de join hipertensao_equipe he on he.co_fat_cidadao_pec=de.co_fat_cidadao_pec)
            select 
            ( select count(*) from hipertensao_equipe ) hipertensao,
            ( select count(*) from diabete_equipe) diabetes,
            (select count(*) from duas_condicoes) diabetes_hipertensao"""
    return text(sql)
