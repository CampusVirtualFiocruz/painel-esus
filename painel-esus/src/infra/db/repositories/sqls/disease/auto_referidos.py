import duckdb

from ..disease import DIABETES_PATH, HYPERTENSION_PATH


def get_hypertension_base_sql():

    return f"""select 
                co_fat_cidadao_pec cidadao_pec,
                ds_raca_cor raca_cor,
                nu_cpf_cidadao cpf,
                nu_cns_cidadao cns,
                no_cidadao nome,
                dt_nascimento_cidadao data_nascimento, 
                idade,
                no_sexo_cidadao sexo,
                telefone,
                no_tipo_logradouro_tb_cidadao tipo_endereco,
                ds_logradouro_tb_cidadao endereco,
                nu_numero_tb_cidadao numero,
                ds_cep_tb_cidadao cep,
                ds_complemento_tb_cidadao complemento,
                '' as bairro,
                ds_tipo_localizacao_domicilio tipo_localidade,
                co_dim_unidade_saude codigo_unidade_saude, 
                codigo_equipe,
                hipertensao,
                autoreferido,
                faixa_etaria,
                nu_micro_area_tb_cidadao micro_area,
                n_infarto_agudo,
                n_acidente_vascular,
                n_coronariana,
                n_cerebrovascular,
                n_renal,
                total_medicos,
                total_cirug_dentista,
                total_farmaceuticos,
                total_fisioterapeutas,
                total_nutricionistas,
                total_fonoaudiologos,
                total_terapeutas_ocupacionais,
                total_educação_fisica,
                total_psicologos,
                total_assist_sociais,
                total_enfermeiros,
                total_outros,
                imc_categoria,
                nome_unidade_saude,
                nome_equipe,
                agg_afericao_pa alerta_afericao_pa,
                dt_ultima_afericao_pa,
                indicador_visitas_domiciliares_acs alerta_visita_acs,
                data_ultima_visita_domiciliar_acs,
                data_ultimo_atend_odonto,
                agg_creatinina_avaliada alerta_creatinina,
                data_ultimo_creatinina,
                data_ultimo_peso_altura,
                avaliacao_colesterol,
                tipo_ultima_consulta,
w                total_consulta_med_enferm,
                dt_primeiro_reg_condicao,
                hipertensao_codigos_1atend,
                creatinina,
                colesterol,
                hemograma,
                eletro,
                eas_equ,
                glicemia,
                sodio,
                potassio,
                n_atendimentos_12_meses
            from read_parquet('{HYPERTENSION_PATH}')
            """
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
