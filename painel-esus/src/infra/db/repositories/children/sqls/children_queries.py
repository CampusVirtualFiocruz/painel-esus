import json

from src.utils.query_builders import gen_where_cnes_equipe

PARQUET_PATH = "./dados/output/crianca.parquet"

def get_total_card(
    cnes: int = None,
    equipe: int = None,
    category: str = "atendidas",
):
    where_clause = ""
    where_clause = gen_where_cnes_equipe(where_clause, cnes, equipe)
    return f"""
            SELECT tipo_localizacao_domicilio, count(*) as total
            FROM read_parquet('{PARQUET_PATH}')
            {where_clause}
            group by tipo_localizacao_domicilio """


def sql_total_children(cnes: int = None, equipe: int = None):
    return f"""
            SELECT count(*) as total
            FROM read_parquet('{PARQUET_PATH}')
            {gen_where_cnes_equipe(None, cnes, equipe)}"""


def get_total_ubs(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT count(*) total 
    FROM read_parquet('{PARQUET_PATH}') 
    {where_clause}
    """


def sql_total_and_last_12_months(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
            COUNT(*) AS total,
            COUNT_IF(crianca_atendida_12_meses = 1) AS total_atendidas_12_meses
        FROM read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
    """


def get_medical_cares(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause += f" where codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
    SELECT sum(crianca_atendida_12_meses) total 
    FROM read_parquet('{PARQUET_PATH}') 
    {where_clause}
    """


def sql_by_age_children(cnes: int = None, equipe: int = None):
    base_where = gen_where_cnes_equipe(None, cnes, equipe).strip()
    faixa_where = """faixa_etaria IN (
        '1 a 2 meses',
        '2 a 4 meses',
        '4 a 6 meses',
        '6 a 9 meses',
        '9 a 12 meses',
        '12 a 18 meses',
        '18 a 24 meses',
        '24 a 36 meses'
    )"""
    if base_where:
        where_clause = f"{base_where} AND {faixa_where}"
    else:
        where_clause = f"WHERE {faixa_where}"

    return f"""
        SELECT
            faixa_etaria AS tag,
            SUM(CASE WHEN sexo = 'FEMININO' THEN 1 ELSE 0 END) AS feminino,
            SUM(CASE WHEN sexo = 'MASCULINO' THEN 1 ELSE 0 END) AS masculino,
            SUM(CASE WHEN sexo = 'INDETERMINADO' THEN 1 ELSE 0 END) AS indeterminado,
            SUM(CASE WHEN sexo NOT IN ('FEMININO', 'MASCULINO', 'INDETERMINADO') OR sexo IS NULL THEN 1 ELSE 0 END) AS "nao-informado"
        FROM
            read_parquet('{PARQUET_PATH}')
        {where_clause}
        GROUP BY faixa_etaria
        ORDER BY faixa_etaria
    """


def sql_by_race_children(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
          COALESCE(LOWER(raca_cor), 'nao-informado') AS tag,
          COUNT(*) AS value
        FROM
          read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
        GROUP BY
          COALESCE(LOWER(raca_cor), 'nao-informado')
        ORDER BY
          tag
    """


def sql_first_consult_8d(cnes: int = None, equipe: int = None):
    return f"""
          SELECT
            CASE
              WHEN agg_dashboard_puericultura_ate_8_dias = 1 THEN 'sim'
              WHEN agg_dashboard_puericultura_ate_8_dias = 0 THEN 'nao'
              WHEN agg_dashboard_puericultura_ate_8_dias = 99 OR agg_dashboard_puericultura_ate_8_dias IS NULL THEN 'nao-se-aplica'
            END AS tag,
            COUNT(*) AS value
          FROM
            read_parquet('{PARQUET_PATH}')
          {gen_where_cnes_equipe(None, cnes, equipe)}
          GROUP BY
            tag
          ORDER BY
            tag
      """


def sql_appointments_until_2_years(cnes: int = None, equipe: int = None):
    return f"""
          SELECT
            CASE
              WHEN agg_dashboard_puericultura_9_consultas_ate_2_anos  = 1 THEN 'sim'
              WHEN agg_dashboard_puericultura_9_consultas_ate_2_anos  = 0 THEN 'nao'
              WHEN agg_dashboard_puericultura_9_consultas_ate_2_anos  = 99 OR agg_dashboard_puericultura_9_consultas_ate_2_anos  IS NULL THEN 'nao-se-aplica'
            END AS tag,
            COUNT(*) AS value
          FROM
            read_parquet('{PARQUET_PATH}')
          {gen_where_cnes_equipe(None, cnes, equipe)}
          GROUP BY
            tag
          ORDER BY
            tag
      """


def sql_acs_visit_until_30d(cnes: int = None, equipe: int = None):
    return f"""
          SELECT
            CASE
                WHEN agg_dashboard_visita_acs_ate_30d == 1 THEN 'sim'
                WHEN agg_dashboard_visita_acs_ate_30d == 0 THEN 'nao'
                WHEN agg_dashboard_visita_acs_ate_30d == 99 OR agg_dashboard_visita_acs_ate_30d IS NULL THEN 'nao-se-aplica'
            END AS tag,
            COUNT(*) AS value
          FROM
            read_parquet('{PARQUET_PATH}')
          {gen_where_cnes_equipe(None, cnes, equipe)}
          GROUP BY
            tag
          ORDER BY
            tag
      """


def sql_acs_visit_until_6m(cnes: int = None, equipe: int = None):
    return f"""
          SELECT
            CASE
                WHEN agg_dashboard_visita_acs_ate_6m == 1 THEN 'sim'
                WHEN agg_dashboard_visita_acs_ate_6m == 0 THEN 'nao'
                WHEN agg_dashboard_visita_acs_ate_6m == 99 OR agg_dashboard_visita_acs_ate_6m IS NULL THEN 'nao-se-aplica'
            END AS tag,
            COUNT(*) AS value
        FROM
          read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
        GROUP BY
          tag
        ORDER BY
          tag
    """


def sql_dental_appointments_until_12m(cnes: int = None, equipe: int = None):
    return f"""
          SELECT
            CASE
              WHEN agg_dashboard_odonto_ate_12m = 1 THEN 'sim'
              WHEN agg_dashboard_odonto_ate_12m = 0 THEN 'nao'
              WHEN agg_dashboard_odonto_ate_12m = 99 OR agg_dashboard_odonto_ate_12m IS NULL THEN 'nao-se-aplica'
            END AS tag,
            COUNT(*) AS value
          FROM
            read_parquet('{PARQUET_PATH}')
          {gen_where_cnes_equipe(None, cnes, equipe)}
          GROUP BY
            tag
          ORDER BY
            tag
      """


def sql_dental_appointments_until_24m(cnes: int = None, equipe: int = None):
    return f"""
          SELECT
            CASE
              WHEN agg_dashboard_odonto_12a24m = 1 THEN 'sim'
              WHEN agg_dashboard_odonto_12a24m = 0 THEN 'nao'
              WHEN agg_dashboard_odonto_12a24m = 99 OR agg_dashboard_odonto_12a24m IS NULL THEN 'nao-se-aplica'
            END AS tag,
            COUNT(*) AS value
          FROM
            read_parquet('{PARQUET_PATH}')
          {gen_where_cnes_equipe(None, cnes, equipe)}
          GROUP BY
            tag
          ORDER BY
            tag
      """


def sql_high_weight_records(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
          CASE
            WHEN agg_dashboard_9_peso_altura = 1 THEN 'sim'
            WHEN agg_dashboard_9_peso_altura = 0 THEN 'nao'
            WHEN agg_dashboard_9_peso_altura = 99 THEN 'nao-se-aplica'
          END AS tag,
          COUNT(*) AS value
        FROM
          read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
        GROUP BY
          tag
        ORDER BY
          tag
    """


def sql_milestone(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
          CASE
            WHEN agg_dashboard_marco_desenvolvimento = 1 THEN 'sim'
            WHEN agg_dashboard_marco_desenvolvimento = 0 THEN 'nao'
            WHEN agg_dashboard_marco_desenvolvimento = 99 THEN 'nao-se-aplica'
          END AS tag,
          COUNT(*) AS value
        FROM
          read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
        GROUP BY
          tag
        ORDER BY
          tag
    """


def sql_evaluated_feeding(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
          CASE
            WHEN agg_dashboard_consumo_alimentar = 1 THEN 'sim'
            WHEN agg_dashboard_consumo_alimentar = 0 THEN 'nao'
            WHEN agg_dashboard_consumo_alimentar = 99 THEN 'nao-se-aplica'
          END AS tag,
          COUNT(*) AS value
        FROM
          read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
        GROUP BY
          tag
        ORDER BY
          tag
    """


def sql_get_nominal_list(
    cnes: int = None,
    equipe: int = None,
    page: int = 0,
    page_size: int = 10,
    nome: str = None,
    cpf: str = None,
    nome_unidade_saude: int = None,
    q: str = None,
    sort: list[dict] = None,
):

    base_filters = []
    or_conditions = []
    if cnes or equipe:
        filter_part = gen_where_cnes_equipe(None, cnes, equipe).strip()
        if filter_part.upper().startswith("WHERE"):
            filter_part = filter_part[6:].strip()
        if filter_part:
            base_filters.append(filter_part)

    if nome:
        base_filters.append(f"LOWER(nome) LIKE LOWER('%{nome}%')")
    if cpf:
        base_filters.append(f"cpf = '{cpf}'")
    if nome_unidade_saude:
        base_filters.append(f"codigo_unidade_saude = {nome_unidade_saude}")

    if q is not None and q:
        or_conditions += [
            f"cpf ilike '%{q}%'",
            f"nome ilike '%{q}%'",
            f"cns ilike  '%{q}%'",
        ]
    indicators = """
        (
            agg_card_puericultura_ate_8_dias IN (0, 99) OR
            agg_card_puericultura_9_consultas_ate_2_anos IN (0, 99) OR
            agg_card_9_peso_altura IN (0, 99) OR
            agg_card_visita_acs_ate_30d IN (0, 99) OR
            agg_card_visita_acs_ate_6m IN (0, 99) OR
            agg_card_odonto_ate_12m IN (0, 99) OR
            agg_card_odonto_12a24m IN (0, 99) OR
            agg_card_marco_desenvolvimento IN (0, 99) OR
            agg_card_consumo_alimentar IN (0, 99)
        )
    """
    base_filters.append(indicators)

    where_clause = ""
    if base_filters:
        where_clause = "WHERE " + " AND ".join(base_filters)
    if or_conditions:
        where_clause = f"{where_clause} AND (" + " OR ".join(or_conditions) + ") "

    fields = {
        "nome",
        "cpf",
        "cnes",
        "sexo",
        "micro_area",
        "idade",
        "raca_cor",
        "equipe",
    }

    order_by_clause = "ORDER BY nome ASC"
    if sort:
        sort_fields = []
        for item in sort:
            item = json.loads(item)
            field = item.get("field")
            direction = item.get("direction", "asc").upper()
            if field in fields:
                sort_fields.append(f"{field} {direction}")
        if sort_fields:
            order_by_clause = f"ORDER BY {', '.join(sort_fields)}"

    limit_offset_clause = ""
    if page_size > 0:
        offset = (page - 1) * page_size
        limit_offset_clause = f"LIMIT {page_size} OFFSET {offset}"
    return f"""
        SELECT *
        FROM read_parquet('{PARQUET_PATH}')
        {where_clause}
        {order_by_clause}
        {limit_offset_clause}
    """


def sql_get_nominal_list_download(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
            CASE WHEN agg_card_puericultura_ate_8_dias IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_puericultura_ate_8_dias,
            CASE WHEN agg_card_puericultura_9_consultas_ate_2_anos IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_puericultura_9_consultas_ate_2_anos,
            CASE WHEN agg_card_9_peso_altura IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_9_peso_altura,
            CASE WHEN agg_card_visita_acs_ate_30d IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_visita_acs_ate_30d,
            CASE WHEN agg_card_visita_acs_ate_6m IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_visita_acs_ate_6m,
            CASE WHEN agg_card_odonto_ate_12m IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_odonto_ate_12m,
            CASE WHEN agg_card_odonto_12a24m IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_odonto_12a24m,
            CASE WHEN agg_card_marco_desenvolvimento IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_marco_desenvolvimento,
            CASE WHEN agg_card_consumo_alimentar IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS agg_card_consumo_alimentar,
            cep,
            cnes_equipe,
            cns,
            codigo_unidade_saude,
            cidadao_pec,
            co_seq_acomp_cidadaos_vinc,
            codigo_unico_ultima_ficha,
            codigo_equipe,
            complemento,
            cpf,
            data_nascimento,
            num_consultas_puericultura,
            nu_peso_recentes,
            nu_altura_recentes,
            total_peso_altura,
            idade_em_dias,
            faixa_etaria,
            idade,
            ine_equipe,
            logradouro,
            micro_area,
            bairro,
            nome,
            municipio,
            sexo,
            tipo_logradouro,
            nome_equipe,
            nome_unidade_saude,
            numero,
            raca_cor,
            CASE WHEN status_registro_valido_equipe IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS status_registro_valido_equipe,
            CASE WHEN status_registro_valido_unidade_saude IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS status_registro_valido_unidade_saude,
            telefone,
            tipo_localizacao_domicilio,
            CASE WHEN crianca_atendida_12_meses IN (0, 99) THEN 'NÃO' ELSE 'SIM' END AS crianca_atendida_12_meses
        FROM read_parquet('{PARQUET_PATH}')
        {gen_where_cnes_equipe(None, cnes, equipe)}
        ORDER BY nome ASC
    """
