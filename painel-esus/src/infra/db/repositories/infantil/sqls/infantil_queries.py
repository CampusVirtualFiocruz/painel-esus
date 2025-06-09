from src.utils.query_builders import gen_where_cnes_equipe


def sql_total_infantil(cnes: int = None, equipe: int = None):
    return f"""
            SELECT count(*) as total
            FROM read_parquet('src/infra/db/repositories/infantil/sqls/dados/crianca.parquet')
            {gen_where_cnes_equipe(None, cnes, equipe)}"""


def sql_by_age_infantil(cnes: int = None, equipe: int = None):
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
            read_parquet('src/infra/db/repositories/infantil/sqls/dados/crianca.parquet')
        {where_clause}
        GROUP BY faixa_etaria
        ORDER BY faixa_etaria
    """


def sql_by_race_infantil(cnes: int = None, equipe: int = None):
    return f"""
        SELECT
          COALESCE(LOWER(raca_cor), 'nao-informado') AS tag,
          COUNT(*) AS value
        FROM
          read_parquet('src/infra/db/repositories/infantil/sqls/dados/crianca.parquet')
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
            read_parquet('src/infra/db/repositories/infantil/sqls/dados/crianca.parquet')
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
            read_parquet('src/infra/db/repositories/infantil/sqls/dados/crianca.parquet')
          {gen_where_cnes_equipe(None, cnes, equipe)}
          GROUP BY
            tag
          ORDER BY
            tag
      """
