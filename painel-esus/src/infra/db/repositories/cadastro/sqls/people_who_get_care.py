from sqlalchemy import text


def people_who_get_care(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where pessoas.codigo_unidade_saude = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and pessoas.codigo_equipe_vinculada  = {equipe} "

    sql = f"""
            with
            listas as ( select * from pessoas {where_clause}),
            total as ( select count(*) from listas)
            select acompanhamento, count(*) value from listas group by 1;
            """
    return text(sql)
