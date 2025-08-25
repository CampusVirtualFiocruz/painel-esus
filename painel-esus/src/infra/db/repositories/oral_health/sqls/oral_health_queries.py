from typing import Literal


def gen_where_category(category):
    if category == "atendidas":
        return "atendimento_odonto=1 "
    elif category == "cadastradas":
        return "cadastradas_odonto=1 "
    else:
        raise ValueError(
            f"Categoria inválida: '{category}'. Esperado 'atendidas' ou 'cadastradas'."
        )


def gen_where_cnes_equipe(base_clause, cnes, equipe):
    clauses = []

    if base_clause:
        clauses.append(base_clause)

    if cnes:
        clauses.append(f" codigo_unidade_saude  = {cnes} ")

    if equipe:
        clauses.append(f" codigo_equipe = {equipe} ")

    return f"WHERE {' AND '.join(clauses)} " if clauses else ""


def get_suffix(column, category):
    if category == "atendidas":
        return f"{column}_atendidas"
    elif category == "cadastradas":
        return f"{column}_cadastradas"
    else:
        raise ValueError(
            f"Categoria inválida: '{category}'. Esperado 'atendidas' ou 'cadastradas'."
        )


def oral_healt_base_sql():

    return f"""
            SELECT  *
            FROM read_parquet('./dados/output/saude_bucal.parquet')
            """


def get_total_card(
    cnes: int = None,
    equipe: int = None,
    category: str = "atendidas",
):
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    return f"""
            SELECT tipo_localizacao_domicilio, count(*) as total
            FROM read_parquet('./dados/output/saude_bucal.parquet')
            {where_clause}
            group by tipo_localizacao_domicilio """


def get_total_ubs(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    return f"""
    SELECT count(*) total 
    FROM read_parquet('./dados/output/saude_bucal.parquet') 
    {where_clause} 
    """


def by_race(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)

    return f"""
            SELECT  raca_cor, count(*) as total
            FROM read_parquet('./dados/output/saude_bucal.parquet') 
            {where_clause}
            group by raca_cor """


def by_gender(cnes: int = None, equipe: int = None, category: str = None):

    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    return f"""
        select 
            sexo, faixa_etaria, count(*) as total
        from read_parquet('./dados/output/saude_bucal.parquet') 
        {where_clause}
        group by sexo, faixa_etaria
        order by sexo, max(idade_anos_completos);
                """


def base_chart(
    cnes: int = None, equipe: int = None, category: str = None, column: str = None
):
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    _column = get_suffix(column, category)

    return f"""
        select 
            {_column}, count(*)
        from read_parquet('./dados/output/saude_bucal.parquet')  
        {where_clause}
        group by {_column}
        """


def first_appointment(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):

    return base_chart(cnes, equipe, category, "agg_primeira_consulta")


def conclued_treatment(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):

    return base_chart(cnes, equipe, category, "agg_tratamento_odonto_concluido")


def extraction(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):

    return base_chart(cnes, equipe, category, "agg_realizaram_exodontia")


def prevention_procedures(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):

    return base_chart(cnes, equipe, category, "agg_procedimentos_preventivos")


def atraumatic_treatment(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):

    return base_chart(cnes, equipe, category, "agg_TRA")


def supervised_brushing(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):

    return base_chart(cnes, equipe, category, "agg_realizaram_exodontia")


def donwload_nominal_list(
    cnes: int = None,
    equipe: int = None,
    category: str = None,
):
    where_clause = gen_where_category(category)
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    return f"""Select
                nome,
                cidadao_pec,
                cpf,
                cns,
                sexo,
                idade,
                data_nascimento,
                logradouro,
                bairro,
                cep,
                municipio,
                ine_equipe,
                micro_area,
                case 
                when atendimento_odonto = 1 then 'atendidas'
                when cadastradas_odonto = 1 then 'cadastradas'
                end situacao,
                cnes_equipe,
                codigo_unidade_saude,
                codigos_procedimentos_preventivos_atendidas,
                codigos_procedimentos_preventivos_cadastradas,
                codigo_equipe,
                complemento,
                faixa_etaria,
                tipo_logradouro,
                nome_equipe,
                nome_unidade_saude,
                numero,
                raca_cor,
                telefone,
                case
                when agg_primeira_consulta_atendidas = 0 then 'SIM'
                when agg_primeira_consulta_atendidas != 0 then 'NÃO'
                end alerta_primeira_consuta_programatica_pessoas_atendidas,
                case
                when agg_primeira_consulta_cadastradas = 0 then 'SIM'
                when agg_primeira_consulta_cadastradas != 0 then 'NÃO'
                end alerta_primeira_consuta_programatica_pessoas_cadastradas,
                data_TRA_atendidas,
                data_TRA_cadastradas,
                data_primeira_consulta_atendidas,
                data_primeira_consulta_cadastradas,
                data_tratamento_concluido_atendidas,
                data_tratamento_concluido_cadastradas,
                data_ultima_atualizacao_cidadao,
                data_ultima_fci,
                data_ultimo_atendimento,
                descricao_procedimentos_preventivos_atendidas,
                descricao_procedimentos_preventivos_cadastradas,
                status_registro_valido_equipe,
                status_registro_valido_unidade_saude,
                tipo_localizacao_domicilio,
                total_exodontia_atendidas,
                total_exodontia_cadastradas,
                st_comunidade_tradicional as 'povos_de_comunidades',
                st_gestante gestante,
                st_paciente_necessidades_espec as 'necessidades_especiais',
                tp_identidade_genero_cidadao as 'identidade_genero'
            from read_parquet('./dados/output/saude_bucal.parquet')  
            {where_clause}"""
