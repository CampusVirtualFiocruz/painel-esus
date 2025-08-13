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
                no_tipo_logradouro tipo_endereco,
                ds_logradouro endereco,
                nu_numero numero,
                ds_cep cep,
                ds_complemento complemento,
                no_bairro as bairro,
                ds_tipo_localizacao_domicilio tipo_localidade,
                codigo_unidade_saude codigo_unidade_saude, 
                codigo_equipe,
                hipertensao,
                autoreferido,
                faixa_etaria,
                nu_micro_area micro_area,
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
                ---
                coalesce( cast(dt_ultima_afericao_pa as varchar), '-')  ultima_data_afericao_pa,
                agg_afericao_pa alerta_afericao_pa,
                agg_visitas_domiciliares_acs alerta_visita_acs,
                coalesce( cast(dt_ultima_visita_domiciliar_acs as varchar), '-') dt_ultima_visita_acs,
                coalesce( cast(dt_ultimo_atend_odonto as varchar), '-') ultimo_atendimento_odonto,
                coalesce(agg_cirurgiao_dentista, 0) alerta_ultima_consulta_odontologica,
                coalesce( cast(data_ultimo_creatinina as varchar), '-') ultima_data_creatinina,
                agg_creatinina alerta_creatinina,
                coalesce(total_consulta_med_enferm, 0)  total_consulta_med_enferm,
                case 
                    when total_consulta_med_enferm < 2 then 0
                    when total_consulta_med_enferm > 2 then 1
                    when total_consulta_med_enferm is null then 0
                end as alerta_total_de_consultas_medico,
                coalesce(agg_medicos_enfermeiros, 0) alerta_ultima_consulta_medico,
                coalesce( cast(dt_ultima_peso_altura as varchar), '-') data_ultimo_peso_altura,
                dt_ultima_colesterol_total,
                agg_colesterol_total,
                dt_ultima_colesterol_total,
                agg_colesterol_hdl,
                dt_ultima_colesterol_ldl
                agg_colesterol_ldl,
                agg_colesterol,
                tipo_ultima_consulta,
                coalesce( cast(dt_ultima_consulta_med_enferm as varchar), '-') ultimo_atendimento_medico,
                coalesce( cast(dt_primeiro_reg_condicao as varchar), '-') dt_primeiro_reg_condicao,
                hipertensao_codigos_1atend codigos_1atend,
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


def get_hypertension_base_export(cnes: int = None, equipe: int = None):
    sql_base = get_hypertension_base_sql_filter(cnes, equipe)

    return sql_base


def get_hypertension_base_sql_filter(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                codigo_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "
    sql = get_hypertension_base_sql()
    return f""" select co_fat_cidadao_pec codigo_cidadao,
        co_fat_cidadao_pec codigo_cidadao,
no_cidadao nome, 
nu_cpf_cidadao cpf,
nu_cns_cidadao cns,
no_sexo_cidadao sexo,
ds_raca_cor raca_cor,
nu_micro_area micro_area,
nome_equipe,
nome_unidade_saude,
dt_nascimento_cidadao data_nascimento,
idade,
telefone,
no_tipo_logradouro tipo_endereco,
ds_logradouro endereco,
nu_numero numero,
ds_cep cep,
ds_complemento complemento,
no_bairro bairro,
ds_tipo_localizacao_domicilio tipo_localidade,
case 
    when autoreferido = 1 then 'autorreferido'
    when autoreferido != 1 then 'cid/ciap'
end grupo_condicao,
tipo_ultima_consulta,
coalesce(total_consulta_med_enferm, 0) total_consulta_medicos_enfermeiros,
strftime(dt_ultima_consulta_med_enferm, '%d/%m/%Y') data_ultima_consulta_medicos_enfermeiros,
case
    when agg_peso_altura = 1 then 'NÃO'
    when agg_peso_altura = 0 then 'SIM'
end  indicador_medicoes_peso_altura,
strftime(dt_ultima_peso_altura, '%d/%m/%Y') data_ultima_medicao_peso_altura,
imc_categoria,
case
    when agg_creatinina = 1 then 'NÃO'
    when agg_creatinina = 0 then 'SIM'
end  indicador_creatinina,
strftime(data_ultimo_creatinina, '%d/%m/%Y') data_ultimo_registro_creatinina,
case
    when agg_visitas_domiciliares_acs = 1 then 'NÃO'
    when agg_visitas_domiciliares_acs = 0 then 'SIM'
end  indicador_visitas_domiciliares_acs,
strftime(dt_ultima_visita_domiciliar_acs, '%d/%m/%Y') data_ultima_visita_domiciliar_acs,
case
    when agg_cirurgiao_dentista = 1 then 'NÃO'
    when agg_cirurgiao_dentista = 0 then 'SIM'
end  indicador_atendimento_odontologico,
strftime(dt_ultimo_atend_odonto, '%d/%m/%Y') data_ultimo_atendimento_odontologico 
        from read_parquet('{HYPERTENSION_PATH}') {where_clause} """


def get_diabetes_base_sql():

    return f"""select 
                co_fat_cidadao_pec cidadao_pec,
                ds_raca_cor raca_cor,
                nu_cpf_cidadao cpf,
                nu_cns_cidadao cns,
                no_cidadao nome,
                dt_nasc_cidadao data_nascimento, 
                idade,
                no_sexo_cidadao sexo,
                telefone,
                no_tipo_logradouro  tipo_endereco,
                ds_logradouro  endereco,
                nu_numero  numero,
                ds_cep  cep,
                ds_complemento  complemento,
                no_bairro  as bairro,
                ds_tipo_localizacao_domicilio tipo_localidade,
                codigo_unidade_saude codigo_unidade_saude, 
                codigo_equipe,
                diabetes,
                autoreferido,
                faixa_etaria,
                nu_micro_area  micro_area,
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
                ---
                coalesce( cast(dt_ultima_afericao_pa as varchar), '-')  ultima_data_afericao_pa,
                agg_afericao_pa alerta_afericao_pa,
                agg_visitas_domiciliares_acs alerta_visita_acs,
                coalesce( cast(dt_ultima_visita_domiciliar_acs as varchar), '-') dt_ultima_visita_acs,
                coalesce( cast(dt_ultimo_atend_odonto as varchar), '-') ultimo_atendimento_odonto,
                coalesce(agg_cirurgiao_dentista, 1) alerta_ultima_consulta_odontologica,
                coalesce( cast(dt_ultimo_creatinina as varchar), '-') ultima_data_creatinina,
                agg_creatinina alerta_creatinina,
                coalesce(total_consulta_med_enferm, 0)  total_consulta_med_enferm,
                case 
                    when total_consulta_med_enferm < 2 then 0
                    when total_consulta_med_enferm > 2 then 1
                    when total_consulta_med_enferm is null then 0
                end as alerta_total_de_consultas_medico,
                agg_medicos_enfermeiros alerta_ultima_consulta_medico,
                coalesce( cast(dt_ultima_peso_altura as varchar), '-') data_ultimo_peso_altura,
                tipo_ultima_consulta,
                coalesce( cast(dt_ultima_consulta_med_enferm as varchar), '-') ultimo_atendimento_medico,
                coalesce( cast(dt_primeiro_reg_condicao as varchar), '-') dt_primeiro_reg_condicao,
                diabetes_codigos_1atend codigos_1atend,
                coalesce( cast(dt_ultima_hemoglobina_avaliado as varchar), '-') ultima_data_hemoglobina_glicada,
                agg_hemoglobina alerta_ultima_hemoglobina_glicada,
                creatinina,
                colesterol,
                hemograma,
                eas_equ,
                glicemia,
                retino,
                hemob_glica,
                n_atendimentos_12_meses
            from read_parquet('{DIABETES_PATH}')
            """


def get_diabetes_base_sql_filter(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                codigo_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "
    return f""" select 
        co_fat_cidadao_pec codigo_cidadao,
        no_cidadao nome, 
        nu_cpf_cidadao cpf,
        nu_cns_cidadao cns,
        no_sexo_cidadao sexo,
        ds_raca_cor raca_cor,
        nu_micro_area micro_area,
        nome_equipe,
        nome_unidade_saude,
        dt_nasc_cidadao data_nascimento,
        idade,
        telefone,
        no_tipo_logradouro tipo_endereco,
        ds_logradouro endereco,
        nu_numero numero,
        ds_cep cep,
        ds_complemento complemento,
        no_bairro bairro,
        ds_tipo_localizacao_domicilio tipo_localidade,
        tipo_ultima_consulta,
        coalesce(total_consulta_med_enferm, 0) total_consulta_medicos_enfermeiros,
        strftime(dt_ultima_consulta_med_enferm, '%d/%m/%Y') data_ultima_consulta_medicos_enfermeiros,
        case
            when agg_peso_altura = 1 then 'NÃO'
            when agg_peso_altura = 0 then 'SIM'
        end  indicador_medicoes_peso_altura,
        strftime(dt_ultima_peso_altura, '%d/%m/%Y') data_ultima_medicao_peso_altura,
        imc_categoria,
        case
            when agg_creatinina = 1 then 'NÃO'
            when agg_creatinina = 0 then 'SIM'
        end  indicador_creatinina,
        strftime(dt_ultimo_creatinina, '%d/%m/%Y') data_ultimo_registro_creatinina,
        case
            when agg_visitas_domiciliares_acs = 1 then 'NÃO'
            when agg_visitas_domiciliares_acs = 0 then 'SIM'
        end  indicador_visitas_domiciliares_acs,
        strftime(dt_ultima_visita_domiciliar_acs, '%d/%m/%Y') data_ultima_visita_domiciliar_acs,
        case
            when agg_cirurgiao_dentista = 1 then 'NÃO'
            when agg_cirurgiao_dentista = 0 then 'SIM'
        end  indicador_atendimento_odontologico,
        strftime(dt_ultimo_atend_odonto, '%d/%m/%Y') data_ultimo_atendimento_odontologico 
        from read_parquet('{DIABETES_PATH}') {where_clause} """


def get_diabetes_base_export(cnes: int = None, equipe: int = None):
    sql_base = get_diabetes_base_sql_filter(cnes, equipe)

    return sql_base


def get_disease_base_sql(cnes: int = None, equipe: int = None, hypertension = True):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                codigo_unidade_saude = {cnes} """
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


def get_total_cares_12(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" with cares as ({sql}) select sum(n_atendimentos_12_meses) total from cares"""
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
        lista as (
            select 
                sum(n_infarto_agudo) n_infarto_agudo, 
                sum(n_acidente_vascular) n_acidente_vascular, 
                sum(n_renal) n_renal,
                sum(n_coronariana) n_coronariana, 
                sum(n_cerebrovascular) n_cerebrovascular,
                (select count(*) from atendimentos) as total    
            from atendimentos
            )
        select  *
            from lista
    """
    return sql


def get_total_patients(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" with patients as ({sql}) select count(*) total from patients where autoreferido = 0"""
    return sql

def get_professionals(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql = f""" with patients as ({sql}) 
        select 
        sum(coalesce(total_medicos,0)) total_medicos,
        sum(coalesce(total_cirug_dentista,0)) total_cirug_dentista,
        sum(coalesce(total_farmaceuticos,0)) total_farmaceuticos,
        sum(coalesce(total_fisioterapeutas,0)) total_fisioterapeutas,
        sum(coalesce(total_nutricionistas,0)) total_nutricionistas,
        sum(coalesce(total_fonoaudiologos,0)) total_fonoaudiologos,
        sum(coalesce(total_terapeutas_ocupacionais,0)) total_terapeutas_ocupacionais,
        sum(coalesce(total_educação_fisica,0)) total_educação_fisica,
        sum(coalesce(total_psicologos,0)) total_psicologos,
        sum(coalesce(total_assist_sociais,0)) total_assist_sociais,
        sum(coalesce(total_enfermeiros,0)) total_enfermeiros,
        sum(coalesce(total_outros,0)) total_outros,
        sum(coalesce(n_atendimentos_12_meses,0))  total from patients"""
    return sql


def get_imc(cnes: int = None, equipe: int = None, hypertension=True):
    sql = get_disease_base_sql(cnes, equipe, hypertension)
    sql_total = get_disease_base_sql(None, None, hypertension)
    sql = f""" with 
    patients as ({sql}),
    total as (select count(*) total from patients),
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

def filter_diabetes_by_localidade(cnes: int = None, equipe: int = None):
    sql = get_disease_base_sql(cnes, equipe,False)
    return f"""
    with condition as ({sql}),
    cidadaos as (
            select
                p.*,
                case 
                    when LOWER(tipo_localizacao_domicilio) is null  then 'nao_definido'
                    when LOWER(tipo_localizacao_domicilio) = 'rural' then 'rural'
                    when LOWER(tipo_localizacao_domicilio) = 'urbana' then 'urbano'
                end tipo    
            from
                condition p )
            select tipo, count(*) total  from cidadaos group by 1
    """


def filter_hypertension_by_localidade(cnes: int = None, equipe: int = None):
    sql = get_disease_base_sql(cnes, equipe,True)
    return f"""
    with condition as ({sql}),
    cidadaos as (
            select
                p.*,
                case 
                    when LOWER(tipo_localizacao_domicilio) is null  then 'nao_definido'
                    when LOWER(tipo_localizacao_domicilio) = 'rural' then 'rural'
                    when LOWER(tipo_localizacao_domicilio) = 'urbana' then 'urbano'
                end tipo    
            from
                condition p )
            select tipo, count(*) total  from cidadaos group by 1
    """
    