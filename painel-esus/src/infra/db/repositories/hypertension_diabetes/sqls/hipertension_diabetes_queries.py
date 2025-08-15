from src.utils.query_builders import gen_where_cnes_equipe

PARQUET_HYPERTENSION_PATH = "./dados/output/hipertensao.parquet"
PARQUET_DIABETES_PATH = "./dados/output/diabetes.parquet"

def _get_path(type: str):
    if type.lower() == 'diabetes':
        return PARQUET_DIABETES_PATH

    if type.lower() == 'hipertensao':
        return PARQUET_HYPERTENSION_PATH

def get_total(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    sql = f"""
    SELECT 
        sum(n_atendimentos_12_meses) as total
    FROM read_parquet('{_get_path(type)}')
    {where_clause}"""
    return sql


def get_number_of_patients(type: str, cnes: int = None, equipe: int = None): 
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    sql = f"""
    WITH lista as ( SELECT n_atendimentos_12_meses, {type}, autoreferido FROM read_parquet('{_get_path(type)}') {where_clause} )
    SELECT
        (
        SELECT sum(n_atendimentos_12_meses) FROM lista WHERE {type} =1 
    ) as cid_ciaps,
    (
        SELECT sum(n_atendimentos_12_meses) FROM lista WHERE autoreferido =1 
    ) as autoreferido
    """
    return sql


def by_gender(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    sql = f"""
        SELECT 
            lower(sexo), faixa_etaria, count(*) as total 
        FROM read_parquet('{_get_path(type)}') {where_clause}  
        GROUP BY sexo, faixa_etaria ORDER BY faixa_etaria asc;

    """
    return sql

def by_race(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    sql = f"""
        SELECT 
            raca_cor, count(*) as total 
        FROM read_parquet('{_get_path(type)}') {where_clause}  
        GROUP BY raca_cor ORDER BY raca_cor asc;

    """
    return sql

def exams_table(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)

    columns = []
    if type == 'hipertensao':
        columns = [
            'glicemia', 
            'creatinina', 
            'eas_equ', 
            'sodio',
            'potassio',
            'colesterol', 
            'hemograma', 
            'eletro' 
        ]
    if type == 'diabetes':
        columns = [
            'glicemia',
            'hemob_glica',
            'retino',
            'creatinina',
            'eas_equ',
            'hemograma',
            'colesterol',
        ]

    sql = (
        """SELECT 
            {}
            FROM read_parquet('{}') {}
        """.format(
                ", ".join(columns),
                _get_path(type),
                where_clause
            )
    )
    return sql

def complications(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)

    sql = """with 
        atendimentos as (SELECT * from read_parquet('{}') {}),
        lista as (
            select 
                IFNULL(sum(n_infarto_agudo), 0) n_infarto_agudo, 
                IFNULL(sum(n_acidente_vascular), 0) n_acidente_vascular, 
                IFNULL(sum(n_renal), 0) n_renal,
                IFNULL(sum(n_coronariana), 0) n_coronariana, 
                IFNULL(sum(n_cerebrovascular), 0) n_cerebrovascular,
                (select count(*) from atendimentos) as total    
            from atendimentos
            )
        select  *
            from lista""".format(
        _get_path(type), where_clause
    )
    return sql


def imc(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)

    sql = """ WITH 
    patients as (SELECT * from read_parquet('{}') {}),
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
        from imc_lista""".format(
        _get_path(type), where_clause
    )
    return sql


def by_location(type: str, cnes: int = None, equipe: int = None):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)

    sql = """
        with condition as ( select * from from read_parquet('{}') {}),
        cidadaos as (
                select
                    p.*,
                    case 
                        when tipo_localizacao_domicilio is null OR tipo_localizacao_domicilio = 'Não Informado'   then 'nao_definido'
                        when LOWER(tipo_localizacao_domicilio) = 'rural' then 'rural'
                        when LOWER(tipo_localizacao_domicilio) = 'urbana' then 'urbano'
                    end tipo    
                from
                    condition p )
                select tipo, count(*) total  from cidadaos group by 1;""".format(_get_path(type), where_clause)
    return sql


def _hipertensao_query():
    return f"""select 
                cidadao_pec,
                raca_cor,
                cpf,
                cns,
                nome,
                data_nascimento, 
                idade,
                sexo,
                telefone,
                tipo_logradouro tipo_endereco,
                logradouro endereco,
                numero numero,
                cep cep,
                complemento complemento,
                bairro as bairro,
                tipo_localizacao_domicilio tipo_localidade,
                codigo_unidade_saude, 
                codigo_equipe,
                hipertensao,
                autoreferido,
                faixa_etaria,
                micro_area,
                n_infarto_agudo,
                n_acidente_vascular,
                n_coronariana,
                n_cerebrovascular,
                n_renal,
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
            from read_parquet('{PARQUET_HYPERTENSION_PATH}')
            """


def _diabetes_query():
    return f"""select 
                cidadao_pec,
                raca_cor,
                cpf,
                cns,
                nome,
                data_nascimento, 
                idade,
                sexo,
                telefone,
                tipo_logradouro  tipo_endereco,
                logradouro  endereco,
                numero  numero,
                cep  cep,
                complemento  complemento,
                bairro  as bairro,
                tipo_localizacao_domicilio tipo_localidade,
                codigo_unidade_saude, 
                codigo_equipe,
                diabetes,
                autoreferido,
                faixa_etaria,
                micro_area  micro_area,
                n_infarto_agudo,
                n_acidente_vascular,
                n_coronariana,
                n_cerebrovascular,
                n_renal,
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
            from read_parquet('{PARQUET_DIABETES_PATH}')
            """

def get_base_sql(type):
    if type == 'hipertensao':
        return _hipertensao_query()
    if type == "diabetes":
        return _diabetes_query()


def get_diabetes_base_sql_filter(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                codigo_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "
    return f""" select 
        cidadao_pec,
        nome, 
        cpf,
        cns,
        sexo,
        raca_cor,
        micro_area,
        nome_equipe,
        nome_unidade_saude,
        data_nascimento,
        idade,
        telefone,
        tipo_logradouro tipo_endereco,
        logradouro endereco,
        numero numero,
        cep cep,
        complemento complemento,
        bairro bairro,
        tipo_localizacao_domicilio tipo_localidade,
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
        from read_parquet('{PARQUET_DIABETES_PATH}') {where_clause} """


def get_hypertension_base_sql_filter(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
                codigo_unidade_saude = {cnes} """
        if equipe and equipe is not None:
            where_clause += f" and codigo_equipe = {equipe} "
    
    return f""" select cidadao_pec,
nome, 
cpf,
cns,
sexo,
raca_cor,
micro_area,
nome_equipe,
nome_unidade_saude,
data_nascimento,
idade,
telefone,
tipo_logradouro tipo_endereco,
logradouro endereco,
numero numero,
cep cep,
complemento complemento,
bairro bairro,
tipo_localizacao_domicilio tipo_localidade,
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
        from read_parquet('{PARQUET_HYPERTENSION_PATH}') {where_clause} """


def get_sql_base_export(type, cnes: int = None, equipe: int = None):
    if type == 'diabetes':
        return get_diabetes_base_sql_filter(cnes, equipe)
    if type == "hipertensao":
        return get_hypertension_base_sql_filter(cnes, equipe)
