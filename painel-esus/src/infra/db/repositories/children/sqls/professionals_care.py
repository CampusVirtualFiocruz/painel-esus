from sqlalchemy import text


def professional_cares(cnes:int = None, equipe:int = None):
    where_clause = ' '
    if cnes is not None:
        where_clause += f"""  where  pessoas.codigo_unidade_saude = {cnes}  """
        if equipe and equipe is not None:
            where_clause += f"  and pessoas.codigo_equipe_vinculada = {equipe} "
    sql = f"""select 
        round(sum(n_medicos)/total, 2) medicos , 
        round(sum(n_enfer)/total, 2) enfermeiros, 
        round(sum(n_fono)/total, 2) fonoaudiologo, 
        round(sum(n_psicol)/total, 2) psicologo, 
        round(sum(n_educ_fisica)/total, 2) educador_fisico, 
        round(sum(n_assist_social)/total, 2) assistente_social, 
        round(sum(n_tera_ocup)/total, 2) terapeuta_ocupacional, 
        round(sum(n_farmac)/total, 2) farmaceutico, 
        round(sum(n_fisio)/total, 2) fisioterapeuta, 
        round(sum(n_nutric)/total, 2) nutricionista, 
        round(sum(n_ciru_dent)/total, 2) cirurgiao_dentista, 
        round(sum(n_outros)/total, 2) outros, 
        total
        from crianca
        join pessoas on pessoas.cidadao_pec = crianca.cidadao_pec 
        {where_clause}"""
    return text(sql)



