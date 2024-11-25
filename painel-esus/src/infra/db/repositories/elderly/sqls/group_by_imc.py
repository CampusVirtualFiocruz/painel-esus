from sqlalchemy import text


def group_by_imc(cnes:int = None, equipe:int = None):
    where_clause = " "
    if cnes is not None:
        where_clause += f""" where pessoas.codigo_unidade_saude = {cnes}  """
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    sql = f"""with 
        lista as (
            select 
            categoria_imc 
            from idoso join pessoas on pessoas.cidadao_pec = idoso.cidadao_pec
            {where_clause}
        )
        select categoria_imc, round(cast(count(*) as float)/cast((select count(*)  from lista)as float),2) quantidade from lista group by 1  """ 
    return text(sql)