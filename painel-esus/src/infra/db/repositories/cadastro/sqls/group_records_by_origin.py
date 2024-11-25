from sqlalchemy import text

from .total import sql_round


def group_records_by_origin(cnes: int = None, equipe: int = None):
    where_clause = " "
    where_clause_pessoas = ""
    if cnes is not None and cnes:
        where_clause += f" and pessoas.codigo_unidade_saude = {cnes} "
        where_clause_pessoas += f" where pessoas.codigo_unidade_saude = {cnes} "
        if equipe is not None and equipe:
            where_clause_pessoas += f" and pessoas.codigo_equipe_vinculada  = {equipe} "
            where_clause += f" and pessoas.codigo_equipe_vinculada  = {equipe} "

    sql = f"""with 
                total_pessoas as (select count(*) from pessoas {where_clause_pessoas}),
                recusa_cadastro as (select count(*) from pessoas  where pessoas.st_recusa_cadastro =1  {where_clause}),
                usar_cadastro_individual as (select count(*) from pessoas  where pessoas.st_usar_cadastro_individual  = 1  {where_clause}),
                nao_usar_cadastro_individual as (select count(*) from pessoas  where pessoas.st_usar_cadastro_individual  = 0  {where_clause}),
                somente_pec as (select count(*) from pessoas  where pessoas.st_usar_cadastro_individual  is null  {where_clause})
            select 
                (select * from total_pessoas ) total_pessoas,
                (select * from recusa_cadastro) recusa_cadastro,
                (select * from usar_cadastro_individual) usar_cadastro_individual,
                (select * from nao_usar_cadastro_individual) nao_usar_cadastro_individual,
                (select * from somente_pec) somente_pec,
                (
                    (select * from nao_usar_cadastro_individual)+(select * from somente_pec)
                ) pec_nao_usam_cadastro_individual """
    return text(sql)
