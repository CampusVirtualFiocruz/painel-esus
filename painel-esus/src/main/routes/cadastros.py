import os
from datetime import datetime, timedelta

import polars as pl


def gera_banco( cnes:int = None, equipe: int= None):
    working_directory  = os.getcwd()
    file_path = working_directory+"/dados/input/" 
    # fai = pl.read_parquet(input_path+"tb_fat_atendimento_individual.parquet")

    atendimento_individual = pl.read_parquet(file_path + 'tb_fat_atendimento_individual.parquet')#, separator=";", dtypes={"nu_altura": pl.Float64})
    atendimento_individual = atendimento_individual.with_columns(
        pl.col("nu_altura").str.strip_chars('"').cast(pl.Int64)
    )
    cids = pl.read_parquet(file_path + "fat_atd_ind_cod.parquet")  # , separator=";")
    cbo = pl.read_parquet(file_path + 'tb_dim_cbo.parquet')#, separator=";")
    cadastro_individual = pl.read_parquet(file_path + 'tb_fat_cad_individual.parquet')#, separator=";")
    cidadao_pec = pl.read_parquet(file_path + 'tb_fat_cidadao_pec.parquet')#, separator=";")
    visita_domiciliar = pl.read_parquet(file_path + 'tb_fat_visita_domiciliar.parquet')#, separator=";")
    tb_cidadao = pl.read_parquet(file_path + 'tb_cidadao.parquet')#, separator=";")
    cadastro_domiciliar = pl.read_parquet(file_path + 'tb_fat_cad_domiciliar.parquet')#, separator=";")

    cidadao_pec = cidadao_pec.with_columns(
        pl.col("co_cidadao")
        .str.strip_chars('"')
        .cast(pl.Int64)
    )

    df = cidadao_pec.join(tb_cidadao,
                  left_on="co_cidadao",
                  right_on="co_seq_cidadao",
                  how="inner"
                  )

    df = df.rename({"nu_cns_right": "nu_cns_right_df"})

    df = df.join(cadastro_individual,
                left_on="co_unico_ultima_ficha",
                right_on="nu_uuid_ficha",
                how="left"
                )

    df = df.with_columns(
        pl.col(["dt_nascimento", 'dt_nascimento_right', "dt_obito", "dt_obito_right"])
        .str.strip_chars('"')
        .cast(pl.Date)
    )

    df = df.with_columns(
        pl.col(["st_faleceu"])
        .str.strip_chars('"')
        .cast(pl.Int64)
    )

    return df

def calcular_idade(dt_nascimento):
  if dt_nascimento is None:
    return 0
    data_atual = datetime.now()
    return data_atual.year - dt_nascimento.year - ((data_atual.month, data_atual.day) < (dt_nascimento.month, dt_nascimento.day))

    df = df.with_columns(pl.col("dt_nascimento").map_elements(calcular_idade).alias("idade"))


def calcular_faixa_etaria(idade):
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

# retorna o Dataframe de total de cadastros por equipe ou ubs
def total_de_cadastro(cnes:int =None, equipe: int= None):
    df.group_by("co_dim_equipe").agg(
        pl.col("co_seq_fat_cidadao_pec")
        .n_unique()
        .alias("total_cadastros")
        ).sort("co_dim_equipe", descending=False)


# retorna o DataFrame de cadastros atualizados
# Nesse caso ja pode filtrar direto equipe ou ubs
def porcentagem_de_cadastros_atualizados(cnes:int =None, equipe: int= None):
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
    cadastros_atualizados_percentual = (cadastros_desatualizados.height / total_registros) * 100


# retorna o DF de total de cadastro por tipo identificacao
def total_de_cadastro_por_tipo_identificacao(cnes:int =None, equipe: int= None):
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


def via_de_cadastro_cidadao(cnes:int =None, equipe: int= None):
    if equipe is not None:
        # filtra por equipe
        cadastros_cadastro_individual = df.filter(
            pl.col("co_dim_equipe").is_not_null()).group_by("co_dim_equipe").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cadastro_individual")
            ).sort("co_dim_equipe", descending=False)

        cadastros_cidadao_pec = df.filter(
            pl.col("co_dim_equipe").is_not_null()).group_by("co_dim_equipe").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("co_dim_equipe", descending=False)

        cadastros_recusa = df.filter(
            pl.col("co_dim_equipe").is_not_null()).group_by("co_dim_equipe").agg(
            pl.col("st_recusa_cadastro")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("co_dim_equipe", descending=False)


    else:
        # filtra sem equipe
        cadastros_cadastro_individual = df.filter(
            pl.col("co_dim_equipe").is_null()).group_by("nu_cns").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cadastro_individual")
            ).sort("co_dim_equipe", descending=False)

        cadastros_cidadao_pec = df.filter(
            pl.col("co_dim_equipe").is_null()).group_by("nu_cns").agg(
            pl.col("nu_cns")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("co_dim_equipe", descending=False)

        cadastros_recusa = df.filter(
            pl.col("co_dim_equipe").is_null()).group_by("st_recusa_cadastro").agg(
            pl.col("st_recusa_cadastro")
            .n_unique()
            .alias("total_cadastros_cidadao_pec")
            ).sort("co_dim_equipe", descending=False)


def status_do_cadastro_dos_cidadaos(cnes:int =None, equipe: int= None):
    df = df.with_columns(
        pl.when(pl.col("co_dim_tipo_saida_cadastro") == 1).then(pl.lit("Óbito"))
        .when(pl.col("co_dim_tipo_saida_cadastro") == 2).then(pl.lit("Mudou-se"))
        .when(pl.col("co_dim_tipo_saida_cadastro") == 3).then(pl.lit("Ativo"))
        .when(pl.col("co_dim_tipo_saida_cadastro").is_null()).then(pl.lit("Inconsistente"))
        .otherwise(pl.lit("Desconhecido"))
        .alias("tipo_saida")
        )

    df.group_by(["tipo_saida", "faixa_etaria"]) \
        .agg(pl.col("co_seq_fat_cidadao_pec").count().alias("total_cadastros")) \
            .sort(["tipo_saida", "faixa_etaria"]).filter(
                (pl.col("faixa_etaria") == "0-4") |
                (pl.col("faixa_etaria") == "60-69") |
                (pl.col("faixa_etaria") == "80-79") |
                (pl.col("faixa_etaria") == "80+")
                )

def localizacao_dos_domicilios_cadastrados(cnes:int =None, equipe: int= None):
    df = df.join(cadastro_domiciliar,
                left_on="co_cidadao",
                right_on='co_seq_fat_cad_domiciliar',
                how="full"
                )

    df = df.with_columns(
        pl.when(pl.col("co_dim_tipo_localizacao") == 1).then(pl.lit("Não Informado"))
          .when(pl.col("co_dim_tipo_localizacao") == 2).then(pl.lit("Rural"))
          .when(pl.col("co_dim_tipo_localizacao") == 3).then(pl.lit("Não Informado"))
          .when(pl.col("co_dim_tipo_localizacao").is_null()).then(pl.lit("Inconsistente"))
          .otherwise(pl.lit("Desconhecido"))
          .alias("localizacao")
          )

    if equipe is not None:
        # filtra por equipe
        localizacao_equipe = (df.filter(pl.col("co_dim_equipe").is_not_null())
                                .group_by(["co_dim_equipe", "localizacao", "faixa_etaria", ])
                                .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("localizacao"))
                                .sort("co_dim_equipe")
                                )
    else:
        # filtra sem equipe
        localizacao_sem_equipe = (df.filter(pl.col("co_dim_equipe").is_null())
                                    .group_by(["localizacao", "faixa_etaria", ])
                                    .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("localizacao"))
                                    .sort("localizacao")
                                    )

def total_domicilio_vs_responsavel(cnes:int =None, equipe: int= None):
    if equipe is not None:
        # filtra por equipe
        responsavel_equipe = (df.filter(pl.col("co_dim_equipe").is_not_null())
                                .group_by(["co_dim_equipe", "nu_cns_responsavel", "st_responsavel_familiar", ])
                                .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("responsavel"))
                                .sort("co_dim_equipe")
                                )
    else:
        # filtra sem equipe
        responsavel_sem_equipe = (df.filter(pl.col("co_dim_equipe").is_null())
                                    .group_by(["nu_cns_responsavel", "st_responsavel_familiar", ])
                                    .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("responsavel"))
                                    .sort("nu_cns_responsavel")
                                    )

def total_raca_cor(cnes:int =None, equipe: int= None):
    if equipe is not None:
        # filtra por equipe
        total_raca_cor_equipe = (
            df.filter(pl.col("co_dim_equipe").is_not_null())
            .group_by(["co_dim_equipe", "co_raca_cor", "co_dim_sexo", ])
            .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("total_raca_cor"))
            .sort("co_dim_equipe")
            )
    else:
        # filtra sem equipe
        total_raca_cor_sem_equipe = (
            df.filter(pl.col("co_dim_equipe").is_null())
            .group_by(["co_raca_cor", "co_dim_sexo", ])
            .agg(pl.col("co_seq_fat_cidadao_pec").n_unique().alias("total_raca_cor"))
            .sort("co_raca_cor")
            )
