import os
from datetime import datetime, timedelta
from turtle import right

import polars as pl


def gera_banco(cnes:int=None, equipe:int=None):

    working_directory  = os.getcwd()
    file_path = os.path.join(working_directory, "dados", "input")

    cadastro_individual = pl.read_parquet(file_path +os.sep+ 'tb_fat_cad_individual.parquet')
    cidadao_pec = pl.read_parquet(file_path +os.sep+ 'tb_fat_cidadao_pec.parquet')
    tb_cidadao = pl.read_parquet(file_path +os.sep+ 'tb_cidadao.parquet')
    familia_territorio = pl.read_parquet(
        file_path + os.sep + "tb_fat_familia_territorio.parquet"
    )
    cadastro_domiciliar = pl.read_parquet(file_path +os.sep+ 'tb_fat_cad_domiciliar.parquet')

    df = cidadao_pec.join(tb_cidadao,
        left_on="co_cidadao",
        right_on="co_seq_cidadao",
        how="inner",
    )

    # df = df.rename({"nu_cns_right": "nu_cns_right_df"})

    df = df.join(
        cadastro_individual,
        left_on="co_unico_ultima_ficha",
        right_on="nu_uuid_ficha",
        how="left",
        suffix="_cad_individual",
    )

    # # df = df.rename({"nu_micro_area_right_lf": "nu_micro_area_right_right_df"})
    df = df.join(
        familia_territorio,
        left_on="co_seq_fat_cidadao_pec",
        right_on="co_fat_cidadao_pec",
        how="left",
        suffix="_right_familia",
    )
    # df = df.rename({"nu_uuid_ficha_origem_right": "nu_uuid_ficha_origem_right_df"})
    df = df.join(cadastro_domiciliar,
        left_on="co_fat_cad_domiciliar",
        right_on='co_seq_fat_cad_domiciliar',
        how="full",
        suffix="_cad_dom"
    )
    df = df.with_columns(
        pl.col(["dt_nascimento", "dt_obito"])
        .str.strip_chars('"')
        .cast(pl.Date)
    )

    df = df.with_columns(
        pl.col(["st_faleceu"])
        .cast(pl.Utf8)
        .str.strip_chars('"')
        .cast(pl.Int64)
    )

    if cnes is not None:
        if equipe is not None and equipe:
            df = df.filter(
                pl.col("co_dim_unidade_saude") == cnes,
                pl.col("co_dim_equipe") == equipe,
            )
        else:
            df = df.filter(pl.col("co_dim_unidade_saude") == cnes)
    return df

def calcular_idade(dt_nascimento):
  if dt_nascimento is None:
    return 0

  data_atual = datetime.now()
  return data_atual.year - dt_nascimento.year - ((data_atual.month, data_atual.day) < (dt_nascimento.month, dt_nascimento.day))

def aplicar_idade(df):
  return df.with_columns(pl.col("dt_nascimento").map_elements(calcular_idade).alias("idade"))

def calcular_faixa_etaria(df):
  df = df.with_columns(
    pl.when(pl.col("idade") <= 4)
      .then(pl.lit("0-4"))
      .when((pl.col("idade") >= 5) & (pl.col("idade") <= 9))
      .then(pl.lit("5-9"))
      .when((pl.col("idade") >= 10) & (pl.col("idade") <= 14))
      .then(pl.lit("10-14"))
      .when((pl.col("idade") >= 15) & (pl.col("idade") <= 19))
      .then(pl.lit("15-19"))
      .when((pl.col("idade") >= 20) & (pl.col("idade") <= 29))
      .then(pl.lit("20-29"))
      .when((pl.col("idade") >= 30) & (pl.col("idade") <= 39))
      .then(pl.lit("30-39"))
      .when((pl.col("idade") >= 40) & (pl.col("idade") <= 49))
      .then(pl.lit("40-49"))
      .when((pl.col("idade") >= 50) & (pl.col("idade") <= 59))
      .then(pl.lit("50-59"))
      .when((pl.col("idade") >= 60) & (pl.col("idade") <= 69))
      .then(pl.lit("60-69"))
      .when((pl.col("idade") >= 70) & (pl.col("idade") <= 79))
      .then(pl.lit("70-79"))
      .when(pl.col("idade") >= 80)
      .then(pl.lit("80+"))
      .otherwise(pl.lit("Desconhecida"))
      .alias("faixa_etaria")
      )
  return df

def total_de_cadastro(df, cnes:int=None, equipe:int=None):
    df_ = df.clone()
    df_ = df_.group_by("co_dim_equipe").agg(
        pl.col("co_seq_fat_cidadao_pec")
        .n_unique()
        .alias("total_cadastros")
        ).sort("co_dim_equipe", descending=False)

    return df_

def porcentagem_de_cadastros_atualizados(df, cnes:int=None, equipe:int=None, filtro:str=None):
    df = df.with_columns(
        pl.col('co_dim_tempo')
        .cast(pl.Utf8)
        .str
        .strptime(pl.Date,
        format="%Y%m%d",
        strict=False
        ))

    two_years_ago = datetime.now() - timedelta(days=2*365)

    total_registros = df.select(pl.col('co_seq_fat_cidadao_pec')).n_unique()

    cadastros_validos = df.filter(
      (pl.col("co_dim_tipo_saida_cadastro") == 3) &
      (pl.col('st_ativo') == 1) &
      (pl.col('dt_obito').is_null()))
    cadastros_validos_percentual = (cadastros_validos.height / total_registros) * 100


    cadastros_invalidos = df.filter(
      (pl.col("co_dim_tipo_saida_cadastro") == 1) |
      (pl.col("co_dim_tipo_saida_cadastro") == 2) |
      (pl.col("co_dim_tipo_saida_cadastro").is_null()))
    cadastros_invalidos_percentual = (cadastros_invalidos.height / total_registros) * 100


    cadastros_atualizados = df.filter(
      (pl.col('co_dim_tempo') >= two_years_ago) &
      (pl.col('co_dim_tipo_saida_cadastro') == 3) &
      (pl.col('st_ativo') == 1) &
      (pl.col('dt_obito').is_null()))
    cadastros_atualizados_percentual = (cadastros_atualizados.height / total_registros) * 100


    cadastros_desatualizados = df.filter(
      (pl.col('co_dim_tempo') <= two_years_ago) &
      (pl.col('co_dim_tipo_saida_cadastro') == 3) &
      (pl.col('st_ativo') == 1) &
      (pl.col('dt_obito').is_null()))
    cadastros_desatualizados_percentual = (cadastros_desatualizados.height / total_registros) * 100

    return {
        "cadastros_validos_percentual": cadastros_validos_percentual,
        "cadastros_invalidos_percentual": cadastros_invalidos_percentual,
        "cadastros_atualizados_percentual": cadastros_atualizados_percentual,
        "cadastros_desatualizados_percentual": cadastros_desatualizados_percentual,
    }

def total_de_cadastro_por_tipo_identificacao(_df, cnes:int=None, equipe:int=None):
    df = _df.clone()
    total_com_cpf = df.filter(
        pl.col("nu_cpf")
        .is_not_null()) \
            .n_unique()

    total_sem_cpf = df.filter(
        pl.col("nu_cpf")
        .is_null()) \
            .n_unique()

    total_com_cns = df.filter(
        pl.col("nu_cns")
        .is_not_null()) \
            .n_unique()

    total_sem_cns = df.filter(
        pl.col("nu_cns")
        .is_null()) \
            .n_unique()

    total_com_cpf_cns = df.filter(
        pl.col("nu_cpf").is_not_null() & pl.col("nu_cns").is_not_null()
        ).select(pl.col("co_seq_fat_cidadao_pec")).n_unique()

    total_sem_cpf_cns = df.filter(
        pl.col("nu_cpf").is_null() & pl.col("nu_cns").is_null()
        ).select(pl.col("co_seq_fat_cidadao_pec")).n_unique()

def via_de_cadastro_cidadao(df, cnes:int=None, equipe:int=None):
    if equipe is not None:
        cadastros_cadastro_individual = df.filter(
            pl.col("co_dim_equipe").is_not_null()).group_by("co_dim_equipe").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cadastro_individual")
            ).sort("total_cadastros_cadastro_individual", descending=False)

        cadastros_cidadao_pec = df.filter(
            pl.col("co_dim_equipe").is_not_null()).group_by("co_dim_equipe").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("total_cadastros_cidadao_pec", descending=False)

        cadastros_recusa = df.filter(
            pl.col("co_dim_equipe").is_not_null()).group_by("co_dim_equipe").agg(
            pl.col("st_recusa_cadastro")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("total_cadastros_cidadao_pec", descending=False)

        return {
            'cadastros_cadastro_individual': cadastros_cadastro_individual,
            'cadastros_cidadao_pec': cadastros_cidadao_pec,
            'cadastros_recusa': cadastros_recusa,
            }


    else:
        cadastros_cadastro_individual = df.filter(
            pl.col("co_dim_equipe").is_null()).group_by("nu_cns").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cadastro_individual")
            ).sort("total_cadastros_cadastro_individual", descending=False)

        cadastros_cidadao_pec = df.filter(
            pl.col("co_dim_equipe").is_null()).group_by("nu_cns").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("total_cadastros_cidadao_pec", descending=False)

        cadastros_recusa = df.filter(
            pl.col("co_dim_equipe").is_null()).group_by("st_recusa_cadastro").agg(
            pl.col("st_recusa_cadastro")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("total_cadastros_cidadao_pec", descending=False)

        return {
            'cadastros_cadastro_individual': cadastros_cadastro_individual,
            'cadastros_cidadao_pec': cadastros_cidadao_pec,
            'cadastros_recusa': cadastros_recusa,
            }

def status_do_cadastro_dos_cidadaos(df, cnes:int=None, equipe:int=None):
    df = df.with_columns(
        pl.when(pl.col("co_dim_tipo_saida_cadastro") == 1).then(pl.lit("Óbito"))
        .when(pl.col("co_dim_tipo_saida_cadastro") == 2).then(pl.lit("Mudou-se"))
        .when(pl.col("co_dim_tipo_saida_cadastro") == 3).then(pl.lit("Ativo"))
        .when(pl.col("co_dim_tipo_saida_cadastro").is_null()).then(pl.lit("Inconsistente"))
        .otherwise(pl.lit("Desconhecido"))
        .alias("tipo_saida")
        )

    df = df.group_by(["tipo_saida", "faixa_etaria"]) \
           .agg(pl.col("co_seq_fat_cidadao_pec").count().alias("total_cadastros")) \
           .sort(["tipo_saida", "faixa_etaria"]).filter(
               (pl.col("faixa_etaria") == "0-4") |
               (pl.col("faixa_etaria") == "60-69") |
               (pl.col("faixa_etaria") == "80-79") |
               (pl.col("faixa_etaria") == "80+")
               )

    return df

def localizacao_dos_domicilios_cadastrados(df, cnes:int=None, equipe:int=None):
    df_ = df.clone()
    df_ = (
        df_.with_columns(
            pl.when(pl.col("co_dim_tipo_localizacao") == 1)
            .then(pl.lit("Não Informado"))
            .when(pl.col("co_dim_tipo_localizacao") == 2)
            .then(pl.lit("Rural"))
            .when(pl.col("co_dim_tipo_localizacao") == 3)
            .then(pl.lit("Não Informado"))
            .when(pl.col("co_dim_tipo_localizacao").is_null())
            .then(pl.lit("Inconsistente"))
            .otherwise(pl.lit("Desconhecido"))
            .alias("localizacao")
        )
        .group_by("localizacao")
        .count()
    )

    return df_

def total_domicilio_vs_responsavel(df, cnes:int=None, equipe:int=None):
    if equipe is not None:
        responsavel_equipe = (df.filter(pl.col("co_dim_equipe").is_not_null())
                                .group_by(["co_dim_equipe", "nu_cns_responsavel", "st_responsavel_familiar", ])
                                .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("responsavel"))
                                .sort("co_dim_equipe")
                                )
        return responsavel_equipe

    else:
        responsavel_sem_equipe = (df.filter(pl.col("co_dim_equipe").is_null())
                                    .group_by(["nu_cns_responsavel", "st_responsavel_familiar", ])
                                    .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("responsavel"))
                                    .sort("nu_cns_responsavel")
                                    )
        return responsavel_sem_equipe

def total_raca_cor(df, cnes:int=None, equipe:int=None):
    if equipe is not None:
        total_raca_cor_equipe = (
            df.filter(pl.col("co_dim_equipe").is_not_null())
            .group_by(["co_dim_equipe", "co_raca_cor", "co_dim_sexo", ])
            .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("total_raca_cor"))
            .sort("co_dim_equipe")
            )
        return total_raca_cor_equipe

    else:
        total_raca_cor_sem_equipe = (
            df.filter(pl.col("co_dim_equipe").is_null())
            .group_by(["co_raca_cor", "co_dim_sexo", ])
            .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("total_raca_cor"))
            .sort("co_raca_cor")
            )
        return total_raca_cor_sem_equipe
