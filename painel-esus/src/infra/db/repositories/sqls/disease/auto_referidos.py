import duckdb

from ..disease import DIABETES_PATH, HYPERTENSION_PATH


def get_disease_base_sql(cnes: int = None, equipe: int = None, hypertension = True):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                co_dim_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "

    if hypertension:
        return f"""select * from read_parquet('{HYPERTENSION_PATH}') {where_clause}"""
    return f"""select * from read_parquet('{DIABETES_PATH}') {where_clause}"""

def get_autoreferidos(cnes: int = None, equipe: int = None, hypertension = True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    if cnes is not None:
        sql += f"""  AND autoreferido = 1  """
    else:
        sql += f"""  where autoreferido = 1  """
        
    return f""" with cares as ({sql}) select count(*) total from cares"""


def get_total_cares(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" with cares as ({sql}) select count(*) total from cares"""
    return sql

def get_cares(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" {sql}"""
    return sql


def get_complications(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql_total = get_disease_base_sql(None, None, hypertension)
    sql = f""" with 
        atendimentos as ({sql}),
        total_atendimentos as ({sql_total}),
        lista as (
            select 
                sum(n_infarto_agudo) n_infarto_agudo, 
                sum(n_acidente_vascular) n_acidente_vascular, 
                sum(n_renal) n_renal,
                sum(n_coronariana) n_coronariana, 
                sum(n_cerebrovascular) n_cerebrovascular,
                (select count(*) from total_atendimentos) as total    
            from atendimentos
            )
        select  *
            from lista
    """
    return sql


def get_total_patients(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" with patients as ({sql}) select count(*) total from patients"""
    return sql

def get_professionals(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" with patients as ({sql}) 
    select 
        sum(total_medicos) total_medicos,
        sum(total_cirug_dentista) total_cirug_dentista,
        sum(total_farmaceuticos) total_farmaceuticos,
        sum(total_fisioterapeutas) total_fisioterapeutas,
        sum(total_nutricionistas) total_nutricionistas,
        sum(total_fonoaudiologos) total_fonoaudiologos,
        sum(total_terapeutas_ocupacionais) total_terapeutas_ocupacionais,
        sum(total_educação_fisica) total_educação_fisica,
        sum(total_psicologos) total_psicologos,
        sum(total_assist_sociais) total_assist_sociais,
        sum(total_enfermeiros) total_enfermeiros,
        sum(total_outros) total_outros,
        (sum(total_medicos) + 
        sum(total_cirug_dentista) + 
        sum(total_farmaceuticos) + 
        sum(total_fisioterapeutas) + 
        sum(total_nutricionistas) + 
        sum(total_fonoaudiologos) + 
        sum(total_terapeutas_ocupacionais) + 
        sum(total_educação_fisica) + 
        sum(total_psicologos) + 
        sum(total_assist_sociais) + 
        sum(total_enfermeiros) + 
        sum(total_outros)) total from patients"""
    return sql

   

def get_imc(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql_total = get_disease_base_sql(None, None, hypertension)
    sql = f""" with 
    patients as ({sql}),
    total_list as ({sql_total}),
    total as (select count(*) total from total_list),
    imc_lista as (
        select imc_categoria, count(*) total from patients group by imc_categoria
    )
    select 
        imc_categoria, 
        (
            round(total/(select total from total),2)
        ) as total_percentage,
        total total_numeric,
        (select total from total) total_global
        from imc_lista
    """
    return sql

def get_hypertension_exams_count(cnes: int = None, equipe: int = None):
    sql = get_disease_base_sql(cnes, equipe, True)
    sql = f""" with patients as ({sql}) 
    select 
        glicemia, 
        creatinina, 
        eas_equ, 
        sodio,
        potassio,
        colesterol, 
        hemograma, 
        eletro 
    from patients
    """
    return sql

def get_diabetes_exams_count(cnes: int = None, equipe: int = None):
    sql = get_disease_base_sql(cnes, equipe, False)
    sql = f""" with patients as ({sql}) 
    select 
        glicemia, 
        hemob_glica,
        retino,
        creatinina, 
        eas_equ, 
        hemograma, 
        colesterol
    from patients
    """
    return sql