import os
import time
from datetime import date, datetime

import pandas as pd
import polars as pl
from dateutil.relativedelta import relativedelta
from src.env.conf import getenv

from .codigos_cbo import *


# from utils import ler_dados_raw,escrever_dados_raw
def ler_dados_raw(nome_parquet,columns=""):

    try:
        os.getenv("ENV")
    # print("aa")
        lazy_on = getenv("LAZY_ON", False) # se lazy_on true ler e escrever dados lazy, se lazy_on false, ler os dados da forma normal

        working_directory  = os.getcwd()

        input_path = os.path.join(working_directory, "dados", "input") 

        output_path = os.path.join(working_directory, "dados", "output")  

        if lazy_on == 1:
            #tb_pessoa = pl.scan_parquet(input_path + os.sep +"tb_acomp_cidadaos_vinculados.parquet")
            df = pl.scan_parquet(input_path + os.sep +nome_parquet)
            return df
        else:
            df = pl.read_parquet(input_path+os.sep+nome_parquet)
            return df
    except Exception as e:
         raise RuntimeError(f"Ocorreu um erro inesperado: {str(e)}") from e


def escrever_dados_raw(df,nome_parquet):

    os.getenv("ENV")
    
    lazy_on = getenv("LAZY_ON", False) # se lazy_on true ler e escrever dados lazy, se lazy_on false, ler os dados da forma normal

    working_directory  = os.getcwd()

    input_path = os.path.join(working_directory, "dados", "input") 

    output_path = os.path.join(working_directory, "dados", "output")  
    if lazy_on == 1:
         #tb_pessoa = pl.scan_parquet(input_path + os.sep +"tb_acomp_cidadaos_vinculados.parquet")
         #print(output_path + os.sep + nome_parquet)
         #df.collect().sink_parquet(output_path + os.sep + nome_parquet,compression='snappy',lazy=True)
         df.collect().write_parquet(output_path + os.sep +nome_parquet)

    else:
        df.write_parquet(output_path + os.sep +nome_parquet)


def gerar_banco():
    start_time = time.time()
    # ## Passo 3. Separar variáveis da(s) tabela(s) necessárias ao desenvolvimento do Indicador

    # ACV
    coluns_acv_geral = [
        "co_unico_ultima_ficha",
        "dt_nascimento_cidadao",
        "no_sexo_cidadao",
        "nu_cpf_cidadao",
        "nu_cns_cidadao",
        "nu_telefone_celular",
        "nu_telefone_contato",
        "no_cidadao",
        "nu_micro_area_domicilio",
        "nu_micro_area_tb_cidadao",
        "nu_ine_vinc_equipe",
        "nu_cnes_vinc_equipe",
        "ds_tipo_localizacao_domicilio",
        "dt_ultima_atualizacao_cidadao",
        "co_seq_acomp_cidadaos_vinc",
    ]

    coluns_acv_end = [
        "no_tipo_logradouro_tb_cidadao",
        "ds_logradouro_tb_cidadao",
        "nu_numero_tb_cidadao",
        "no_bairro_tb_cidadao",
        "ds_complemento_tb_cidadao",
        "ds_cep_tb_cidadao",
        "no_municipio_tb_cidadao",
        "no_tipo_logradouro_domicilio",
        "ds_logradouro_domicilio",
        "nu_numero_domicilio",
        "ds_complemento_domicilio",
        "no_bairro_domicilio",
        "no_municipio_domicilio",
        "ds_cep_domicilio",
    ]

    columns_acv = coluns_acv_geral + coluns_acv_end

    # FCI
    selected_columns_fci = [
        "co_fat_cidadao_pec",
        "co_dim_tempo",
        "nu_uuid_ficha",
        "co_dim_raca_cor",
        "nu_micro_area",
    ]

    # FAI
    selected_columns_atd_ind = [
        "co_fat_cidadao_pec",
        "co_seq_fat_atd_ind",
        "nu_altura",
        "nu_peso",
        "co_dim_tempo",
        "co_dim_cbo_1",
        "co_dim_cbo_2",
        "dt_nascimento",
    ]

    # PROCED / ATEND
    columns_proced = [
        "co_seq_fat_proced_atend",
        "co_fat_cidadao_pec",
        "nu_altura",
        "nu_peso",
        "co_dim_tempo",
        "ds_filtro_procedimento",
        "co_dim_cbo",
    ]

    # FAOI
    columns_fao = [
        "co_fat_cidadao_pec",
        "co_dim_tempo",
        "nu_altura",
        "nu_peso",
        "co_dim_cbo_1",
        "co_dim_cbo_2",
        "co_seq_fat_atd_odnt",
        "ds_filtro_procedimentos",
    ]

    # FAC (atividade coletiva)
    columns_atvdd_coletiva = [
        "co_fat_cidadao_pec",
        "co_dim_tempo",
        "nu_participante_altura",
        "nu_participante_peso",
        "co_seq_fat_atvdd_cltv_part",
    ]

    # VIS_DOM (visita domiciliar)
    columns_vis_dom = [
        "co_seq_fat_visita_domiciliar",
        "co_fat_cidadao_pec",
        "co_dim_tempo",
        "co_dim_cbo",
        "nu_altura",
        "nu_peso",
    ]

    # VACINA (vacinacao)
    columns_vacina = ["co_fat_cidadao_pec", "co_dim_tempo", "ds_filtro_imunobiologico"]

    # IVCF
    columns_ivcf = ["co_fat_cidadao_pec", "co_dim_tempo"]

    #
    # ## Passo 4. Carregar tabelas necessárias ao desenvolvimento do Indicador e nomeá-las

    # tb_pessoa = pl.read_parquet(caminho_pasta+"tb_acomp_cidadaos_vinculados.parquet",columns=columns_acv)
    tb_pessoa = ler_dados_raw("tb_acomp_cidadaos_vinculados.parquet", columns_acv)

    # fci = pl.read_parquet(caminho_pasta+"tb_fat_cad_individual.parquet", columns=selected_columns_fci)
    fci = ler_dados_raw("tb_fat_cad_individual.parquet", selected_columns_fci)
    fci = fci.rename({"nu_micro_area": "nu_micro_area_fci"})

    # fai = pl.read_parquet(caminho_pasta+"tb_fat_atendimento_individual.parquet",columns=selected_columns_atd_ind)
    fai = ler_dados_raw(
        "tb_fat_atendimento_individual.parquet", selected_columns_atd_ind
    )

    # fao = pl.read_parquet(caminho_pasta+"tb_fat_atendimento_odonto.parquet",columns = columns_fao)
    fao = ler_dados_raw("tb_fat_atendimento_odonto.parquet", columns_fao)

    # fai_cods = pl.read_parquet(caminho_pasta+"fat_atd_ind_cod.parquet")
    fai_cods = ler_dados_raw("fat_atd_ind_cod.parquet")

    # vis_dom = pl.read_parquet(caminho_pasta+"tb_fat_visita_domiciliar.parquet", columns= columns_vis_dom)
    vis_dom = ler_dados_raw("tb_fat_visita_domiciliar.parquet", columns_vis_dom)

    # proced_atend = pl.read_parquet(caminho_pasta+"tb_fat_proced_atend.parquet",columns= columns_proced)
    proced_atend = ler_dados_raw("tb_fat_proced_atend.parquet", columns_proced)

    vacina = ler_dados_raw("tb_fat_vacinacao.parquet", columns_vacina)

    ivcf = ler_dados_raw("tb_fat_ivcf.parquet", columns_ivcf)

    # tb_dim_equipe = pl.read_parquet(caminho_pasta+"tb_dim_equipe.parquet")
    tb_dim_equipe = ler_dados_raw("tb_dim_equipe.parquet")

    # tb_dim_und_saude = pl.read_parquet(caminho_pasta+"tb_dim_unidade_saude.parquet")
    tb_dim_und_saude = ler_dados_raw("tb_dim_unidade_saude.parquet")

    # dim_raca_cor = pl.read_parquet(caminho_pasta+"tb_dim_raca_cor.parquet")
    dim_raca_cor = ler_dados_raw("tb_dim_raca_cor.parquet")
    dim_raca_cor = dim_raca_cor.rename(
        {"co_seq_dim_raca_cor": "co_dim_raca_cor"}
    ).select("co_dim_raca_cor", "ds_raca_cor")

    fci = fci.join(dim_raca_cor, on="co_dim_raca_cor", how="left")

    # ## Passo 5. Criar variáveis de tempo de acordo com Indicadores

    dt_12meses = datetime.today() - relativedelta(months=12)

    dt_24meses = datetime.today() - relativedelta(months=24)

    def calcular_data(meses: int):
        return datetime.today() - relativedelta(months=meses)

    # ## Passo 6. Filtrar os códigos de profissionais, exames ou condições de saúde dos Indicadores

    coluns_cbo = ["nu_cbo", "co_seq_dim_cbo"]
    # dim_cbo = pl.read_parquet(caminho_pasta + "tb_dim_cbo.parquet",columns=coluns_cbo)
    dim_cbo = ler_dados_raw("tb_dim_cbo.parquet", coluns_cbo)

    dim_cbo = dim_cbo.with_columns(pl.col("co_seq_dim_cbo").cast(pl.Int64))

    # AJUSTE de CBO

    # FAI

    fai = (
        fai.join(dim_cbo, left_on="co_dim_cbo_1", right_on="co_seq_dim_cbo", how="left")
        .drop("co_dim_cbo_1")
        .rename({"nu_cbo": "co_dim_cbo_1"})
        .join(dim_cbo, left_on="co_dim_cbo_2", right_on="co_seq_dim_cbo", how="left")
        .drop("co_dim_cbo_2")
        .rename({"nu_cbo": "co_dim_cbo_2"})
    )

    # FAO

    fao = (
        fao.join(dim_cbo, left_on="co_dim_cbo_1", right_on="co_seq_dim_cbo", how="left")
        .drop("co_dim_cbo_1")
        .rename({"nu_cbo": "co_dim_cbo_1"})
        .join(dim_cbo, left_on="co_dim_cbo_2", right_on="co_seq_dim_cbo", how="left")
        .drop("co_dim_cbo_2")
        .rename({"nu_cbo": "co_dim_cbo_2"})
    )

    # VIS_DOM

    vis_dom = (
        vis_dom.join(
            dim_cbo, left_on="co_dim_cbo", right_on="co_seq_dim_cbo", how="left"
        )
        .drop("co_dim_cbo")
        .rename({"nu_cbo": "co_dim_cbo"})
    )

    # PROCED_ATEND

    proced_atend = (
        proced_atend.join(
            dim_cbo, left_on="co_dim_cbo", right_on="co_seq_dim_cbo", how="left"
        )
        .drop("co_dim_cbo")
        .rename({"nu_cbo": "co_dim_cbo"})
    )

    # In[10]:

    ### separando informações de interesse exames - sem ciaps e cids, apenas procedimentos avaliados ou solicitados

    # In[11]:

    exames = fai_cods.select("co_seq_fat_atd_ind", "codigo", "tipo").filter(
        (pl.col("tipo") == "Procedimentos Avaliados")
        | (pl.col("tipo") == "Procedimentos Solicitados")
    )

    # ## Passo 7. Manipular dados conforme necessidades dos Indicadores

    # ### Manipulando dados comuns aos indicadores

    # In[12]:

    cad_grouped = (
        fci.with_columns(
            pl.col("co_dim_tempo")
            .cast(pl.Utf8)
            .str.strptime(pl.Date, "%Y%m%d")
            .alias("dt_atendimento")
        )
        .filter(pl.col("co_fat_cidadao_pec").is_not_null())
        .group_by("co_fat_cidadao_pec")
        .agg(
            [
                pl.col("dt_atendimento").max().alias("dt_ultima_fci"),
                pl.col("ds_raca_cor").first().alias("ds_raca_cor"),
            ]
        )
    )

    fci_v2 = fci.select("co_fat_cidadao_pec", "nu_uuid_ficha", "nu_micro_area_fci")

    tb_pessoa = tb_pessoa.with_columns(
        pl.col("dt_ultima_atualizacao_cidadao")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, "%Y-%m-%d")
        .alias("dt_ultima_atualizacao_cidadao")
    )

    tb_pessoa_v2 = tb_pessoa.join(
        fci_v2, left_on="co_unico_ultima_ficha", right_on="nu_uuid_ficha", how="left"
    ).join(cad_grouped, on="co_fat_cidadao_pec", how="left")

    # criando dt_atendimento para FAI, usada em mais de um indicador, e filtrando cidadaos não nulos

    fai_v2 = fai.with_columns(
        pl.col("co_dim_tempo")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, "%Y%m%d")
        .alias("dt_atendimento")
    ).filter(
        (
            pl.col("co_fat_cidadao_pec").is_not_null()
        )  # &  (pl.col("dt_atendimento") >= dt_24meses)
    )

    # criando dt_atendimento para VIS_DOM, usada em mais de um indicador, e filtrando cidadaos não nulos

    vis_dom_v2 = vis_dom.with_columns(
        pl.col("co_dim_tempo")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, "%Y%m%d")
        .alias("dt_atendimento")
    ).filter(
        (
            pl.col("co_fat_cidadao_pec").is_not_null()
        )  # &  (pl.col("dt_atendimento") >= dt_24meses)
    )

    # criando dt_atendimento para FAO, usada em mais de um indicador, e filtrando cidadaos não nulos

    fao_v2 = fao.with_columns(
        pl.col("co_dim_tempo")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, "%Y%m%d")
        .alias("dt_atendimento")
    ).filter(
        (
            pl.col("co_fat_cidadao_pec").is_not_null()
        )  # &  (pl.col("dt_atendimento") >= dt_24meses)
    )

    vacina_v2 = vacina.with_columns(
        pl.col("co_dim_tempo")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, "%Y%m%d")
        .alias("dt_atendimento")
    ).filter(
        (
            pl.col("co_fat_cidadao_pec").is_not_null()
        )  # &  (pl.col("dt_atendimento") >= dt_24meses)
    )

    ivcf_v2 = ivcf.with_columns(
        pl.col("co_dim_tempo")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, "%Y%m%d")
        .alias("dt_atendimento")
    ).filter(
        (
            pl.col("co_fat_cidadao_pec").is_not_null()
        )  # &  (pl.col("dt_atendimento") >= dt_24meses)
    )

    # In[13]:

    # print(tb_pessoa_v2.glimpse())

    # ### Total de pessoas idosas - Dashboard

    # In[14]:

    today = date.today()

    tb_pessoa_v2 = (
        tb_pessoa_v2.filter(pl.col("co_fat_cidadao_pec").is_not_null())
        .with_columns(
            pl.col("dt_nascimento_cidadao")
            .cast(pl.Utf8)
            .str.strptime(pl.Date, "%Y-%m-%d")
            .alias("dt_nasc_cidadao")
        )
        .with_columns(
            pl.when(
                pl.date(pl.col("dt_nasc_cidadao").dt.year(), today.month, today.day)
                >= pl.col("dt_nasc_cidadao")
            )
            .then(today.year - pl.col("dt_nasc_cidadao").dt.year())
            .otherwise(today.year - pl.col("dt_nasc_cidadao").dt.year() - 1)
            .alias("idade")
        )
    )

    # In[15]:

    idoso = tb_pessoa_v2.filter(pl.col("idade") >= 60)

    # In[16]:

    # dataframe para adicionar a todo os indicadores para conferir se a idade é maior ou igual a 61 anos
    df_idade = idoso.select("co_fat_cidadao_pec", "idade")

    # ### Pessoas idosas por sexo - Dashboard

    # In[17]:

    # COUNT ACV
    # tb_pessoa_v2['no_sexo_cidadao'].value_counts()
    categorias_validas_sexo = ["MASCULINO", "FEMININO", "INDETERMINADO"]

    idoso = idoso.with_columns(
        pl.when(
            pl.col("no_sexo_cidadao").str.to_uppercase().is_in(categorias_validas_sexo)
        )
        .then(
            pl.col("no_sexo_cidadao").str.to_uppercase()
        )  # Mantém e padroniza para maiúsculas
        .otherwise(pl.lit("NÃO INFORMADO"))  # Substitui valores inválidos
        .alias("no_sexo_cidadao")  # Atualiza a coluna original
    )

    # ### Pessoas idosas por raça/cor - Dashboard

    # In[18]:

    categorias_validas = ["Branca", "Preta", "Amarela", "Parda", "Indígena"]

    idoso = idoso.with_columns(
        pl.when(pl.col("ds_raca_cor").is_in(categorias_validas))
        .then(pl.col("ds_raca_cor"))  # Mantém o valor original se for válido
        .otherwise(pl.lit("NÃO INFORMADO"))  # Substitui valores inválidos
        .alias("ds_raca_cor")  # Atualiza a coluna original
    )

    # ### Pessoas idosas por faixa etária - Dashboard

    # In[19]:

    idoso = idoso.with_columns(
        pl.when((pl.col("idade") >= 60) & (pl.col("idade") <= 69))
        .then(pl.lit("60a69"))
        .when((pl.col("idade") >= 70) & (pl.col("idade") <= 79))
        .then(pl.lit("70a79"))
        .when((pl.col("idade") >= 80) & (pl.col("idade") <= 89))
        .then(pl.lit("80a89"))
        .when((pl.col("idade") >= 90) & (pl.col("idade") <= 99))
        .then(pl.lit("90a99"))
        .when(pl.col("idade") >= 100)
        .then(pl.lit("100mais"))
        .otherwise(pl.lit("idade_invalida"))
        .alias("faixa_etaria")
    )

    # In[20]:

    # idoso['faixa_etaria'].value_counts()

    # ### Total de pessoas atendidas  nos últimos 12 meses - Dashboard

    # In[21]:

    total_pessoas_atd = (
        fai_v2.filter(pl.col("dt_atendimento") >= dt_12meses)
        .group_by("co_fat_cidadao_pec")
        .agg()
        .with_columns(pl.lit(1).alias("pessoa_atendida_12_meses"))
    )

    idoso = idoso.join(
        total_pessoas_atd, on="co_fat_cidadao_pec", how="left"
    ).with_columns(
        pl.col("pessoa_atendida_12_meses").fill_null(0),
    )

    # ### **Indicador I** - Pessoa idosa com duas consultas médica e/ou de enfermagem nos últimos 12 meses - Dashboard
    #
    # ### Lista Nominal: Alerta quando  a quantidade for < 2

    # In[22]:

    fai_idoso_12meses = (
        fai_v2.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .select(
            "co_seq_fat_atd_ind",
            "co_fat_cidadao_pec",
            "dt_atendimento",
            "co_dim_cbo_1",
            "co_dim_cbo_2",
            "idade",
        )
        .filter(
            (
                pl.col("co_dim_cbo_1").is_in(medicos_codigos)
                | pl.col("co_dim_cbo_2").is_in(medicos_codigos)
            )
            | (
                pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)
                | pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos)
            )
        )
        .with_columns(
            (
                pl.col("co_dim_cbo_1").is_in(medicos_codigos)
                | pl.col("co_dim_cbo_2").is_in(medicos_codigos)
            ).alias("is_medico"),
            (
                pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)
                | pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos)
            ).alias("is_enfermeiro"),
        )
        # .unique(["co_seq_fat_atd_ind"])  # Remove duplicatas de mesmo ID
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("idade").first().alias("idade"),
            # Pega as duas últimas datas, de atendimentos distintos
            pl.col("dt_atendimento")
            .filter((pl.col("dt_atendimento") >= dt_12meses))
            .sort(descending=True)
            .head(2)
            .alias("duas_ultimas_datas_combinadas"),
            # Contagem de atendimentos distintos
            pl.col("co_seq_fat_atd_ind")
            .filter((pl.col("dt_atendimento") >= dt_12meses))
            .n_unique()
            .alias("total_consulta_med_enferm"),
            # Indicador binário
            (
                pl.col("co_seq_fat_atd_ind")
                .filter((pl.col("dt_atendimento") >= dt_12meses))
                .n_unique()
                >= 2
            )
            .cast(pl.Int8)
            .alias("agg_medicos_enfermeiros"),
            # alerta 12
            pl.when(
                (
                    pl.col("co_seq_fat_atd_ind")
                    .filter(pl.col("dt_atendimento") >= dt_12meses)
                    .n_unique()
                    >= 2
                )
            )
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_medicos_enfermeiros"),
            (
                pl.col("co_seq_fat_atd_ind")
                .filter((pl.col("dt_atendimento") >= dt_12meses))
                .n_unique()
                >= 2
            )
            .cast(pl.Int8)
            .alias("agg_dashboard_medicos_enfermeiros"),
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_medicos_enfermeiros"))
            .alias("agg_alerta_medicos_enfermeiros"),
        )
        .select(
            "co_fat_cidadao_pec",
            "agg_medicos_enfermeiros",
            "agg_alerta_medicos_enfermeiros",
            "total_consulta_med_enferm",
            "idade",
            "duas_ultimas_datas_combinadas",
        )
    )

    # In[23]:

    # fai_idoso_12meses.filter(pl.col("co_fat_cidadao_pec") == 3901)

    # In[24]:

    # separando as datas

    fai_idoso_12meses = (
        fai_idoso_12meses.with_columns(
            # Primeira data (mais recente)
            pl.col("duas_ultimas_datas_combinadas")
            .list.first()
            .alias("dt_ultima_medico_enferm"),
            # Segunda data (penúltima)
            pl.col("duas_ultimas_datas_combinadas")
            .list.slice(1, 1)  # Pega 1 elemento a partir da posição 1
            .list.first()  # Extrai o elemento da sub-lista
            .alias("dt_penultima_medico_enferm"),
        )
        .drop("duas_ultimas_datas_combinadas")
        .select(
            "co_fat_cidadao_pec",
            "agg_medicos_enfermeiros",
            "agg_alerta_medicos_enfermeiros",
            "total_consulta_med_enferm",
            "dt_ultima_medico_enferm",
            "dt_penultima_medico_enferm",
        )
    )

    # #### Indicador I e Itens da **Lista nominal** do Indicador I no df **"idoso"**:
    # #### *A saber:*
    # ##### Número de pessoas idosas que tiveram pelo menos duas consultas médicas e/ou de enfermagem nos últimos 12 meses: **'agg_medicos_enfermeiros'= 1**
    # ##### - datas das duas últimas consultas realizadas com profissional médico ou de enfermagem (**"ultima_dt_medico_enferm e penultima_dt_medico_enferm"**)
    # ##### - e quantidade de consultas realizadas nos últimos 12 meses (**"total_consulta_med_enferm"**)
    # ##### - Alerta se **"agg_medicos_enfermeiros" = 0**

    # In[25]:

    # Left join idoso com indicador_medicos_enfermeiros

    idoso = idoso.join(
        fai_idoso_12meses, on="co_fat_cidadao_pec", how="left"
    ).with_columns(
        pl.col("agg_medicos_enfermeiros").fill_null(0),
        pl.when(pl.col("idade") > 60)
        .then(pl.col("agg_alerta_medicos_enfermeiros").fill_null(1))
        .otherwise(pl.col("agg_alerta_medicos_enfermeiros").fill_null(0))
        .alias("agg_alerta_medicos_enfermeiros"),
        pl.col("total_consulta_med_enferm").fill_null(0),
    )

    # In[26]:

    # idoso['agg_medicos_enfermeiros'].value_counts()

    # ### **Indicador II** - Dois registros de peso e altura  realizados na data das consultas com médico e/ou enfermeiro nos últimos 12 meses - Dashboard
    #
    # ### Lista Nominal: Alerta quando for "não"

    # In[27]:

    # tabelas fonte: fai, fao e vis_dom

    # obs.: O indicador é sim/não respondendo à pergunta: "o idoso teve registro de duas medidas de peso/altura
    #  (em qualquer atendimento, com qualquer profissional considerado) realizadas na mesma data em que ele fez
    # consultas com médico/enfermeiro?"

    # Primeiro, pegando as datas de registro de peso e altura com todos profissionais considerados

    peso_altura = pl.concat([fao_v2, fai_v2, vis_dom_v2], how="diagonal")

    indicador_peso_altura_v1 = (
        peso_altura.filter(
            (pl.col("co_dim_cbo").is_in(peso_altura_cbo))
            | (
                pl.col("co_dim_cbo_1").is_in(peso_altura_cbo)
                | pl.col("co_dim_cbo_2").is_in(peso_altura_cbo)
            )
        )
        .filter((pl.col("nu_peso").is_not_null()) & (pl.col("nu_altura").is_not_null()))
        .sort("dt_atendimento", descending=True)
        .group_by("co_fat_cidadao_pec")
        .agg(
            (pl.col("dt_atendimento") >= calcular_data(24))
            .sum()
            .alias("total_peso_altura_24"),
            (pl.col("dt_atendimento") >= calcular_data(12))
            .sum()
            .alias("total_peso_altura_12"),
            pl.col("nu_peso")
            .filter(pl.col("dt_atendimento") >= calcular_data(24))  # Filtro
            .head(2)
            .alias("nu_peso_recentes"),
            # Altura: mesma lógica
            pl.col("nu_altura")
            .filter(pl.col("dt_atendimento") >= calcular_data(24))  # Filtro
            .head(2)
            .alias("nu_altura_recentes"),
            pl.col("dt_atendimento")
            .filter(pl.col("dt_atendimento") >= calcular_data(12))  # Filtro aplicado
            .unique()
            .alias("dt_atendimentos_12"),
            pl.col("dt_atendimento")
            .filter(pl.col("dt_atendimento") >= calcular_data(24))  # Filtro aplicado
            .unique()
            .alias("dt_atendimentos_24"),
        )
        .with_columns(
            pl.when(
                pl.col("total_peso_altura_24") >= 2
            )  # Coluna indicando se há pelo menos 2 registros simultâneos
            .then(1)
            .otherwise(0)
            .alias("2_peso_altura_24"),
            pl.when(
                pl.col("total_peso_altura_12") >= 2
            )  # Coluna indicando se há pelo menos 2 registros simultâneos
            .then(1)
            .otherwise(0)
            .alias("2_peso_altura_12"),
        )
        .select(
            "co_fat_cidadao_pec",
            #    "nu_peso_recentes",
            #    "nu_altura_recentes",
            "dt_atendimentos_24",
            "dt_atendimentos_12",
            "total_peso_altura_12",
            "total_peso_altura_24",
            "2_peso_altura_12",
            "2_peso_altura_24",
        )
    )

    # In[28]:

    # peso_altura.filter(pl.col("co_fat_cidadao_pec") == 64756).sort("dt_atendimento", descending=True).select("co_fat_cidadao_pec","nu_altura","nu_peso","dt_atendimento","dt_nascimento")

    # In[29]:

    # indicador_peso_altura_v1.filter(pl.col("co_fat_cidadao_pec") == 64756)

    # In[30]:

    # indicador_peso_altura_v1

    # In[31]:

    # Agora, pegando as datas de consultas com médicos e/ou enfermeiros
    # tabelas fonte: fai, fao e vis_dom

    peso_altura_medico_enf = (
        peso_altura.select(
            "co_fat_cidadao_pec",
            "dt_atendimento",
            "co_dim_cbo",
            "co_dim_cbo_1",
            "co_dim_cbo_2",
        )
        .filter(
            (
                pl.col("co_dim_cbo_1").is_in(medicos_codigos)
                | pl.col("co_dim_cbo_2").is_in(medicos_codigos)
                | pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)
                | pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos)
                | pl.col("co_dim_cbo").is_in(medicos_codigos)
                | pl.col("co_dim_cbo").is_in(enfermeiros_codigos)
            )
        )
        .with_columns(
            # (pl.col("co_dim_cbo_1").is_in(medicos_codigos) | pl.col("co_dim_cbo_2").is_in(medicos_codigos) | pl.col("co_dim_cbo").is_in(medicos_codigos)).alias("is_medico"),
            # (pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos) | pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos) | pl.col("co_dim_cbo").is_in(enfermeiros_codigos)).alias("is_enfermeiro")
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            #  pl.col("dt_atendimento").filter(pl.col("is_medico") & (pl.col("dt_atendimento")>= dt_12meses)).alias("dts_medico"),
            # pl.col("dt_atendimento").filter(pl.col("is_enfermeiro") & (pl.col("dt_atendimento")>= dt_12meses)).alias("dts_enfermeiro"),
            pl.col("dt_atendimento")
            .filter((pl.col("dt_atendimento") >= dt_24meses))
            .unique()
            .alias("dts_24"),
            pl.col("dt_atendimento")
            .filter((pl.col("dt_atendimento") >= dt_12meses))
            .unique()
            .alias("dts_12"),
        )
        .filter((pl.col("dts_24").list.len() > 0) & (pl.col("dts_12").list.len() > 0))
    )

    # In[ ]:

    # In[32]:

    # Juntando dados datas peso e altura + medicos e enfermeiros

    indicador_idoso_peso_altura = (
        indicador_peso_altura_v1.join(
            peso_altura_medico_enf, on="co_fat_cidadao_pec", how="left"
        )
        .with_columns(
            pl.col("dt_atendimentos_12")
            .list.set_intersection("dts_12")
            .alias("datas_match_12"),
            pl.col("dt_atendimentos_24")
            .list.set_intersection("dts_24")
            .alias("datas_match_24"),
        )
        .with_columns(
            pl.col("datas_match_12").list.len().alias("qtd_12"),
            pl.col("datas_match_24").list.len().alias("qtd_24"),
        )
    )

    # #### **Indicador II** e Itens da **Lista nominal** do Indicador II no df **"idoso"**:
    # ##### *A saber:*
    # ##### Número de pessoas idosas que tiveram dois registros de peso e altura simultâneos ocorridos na data das consultas com médico e/ou enfermeiro, realizados nos últimos 12 meses:**"agg_peso_altura" = 1**
    #
    # ##### - Registro de peso e altura na mesma data de duas consultas médicas ou de enfermagem **(Sim = 1/Não = 0)**
    # ##### - Alerta se **"agg_peso_altura" = 0**

    # In[33]:

    indicador_idoso_peso_altura_v2 = (
        indicador_idoso_peso_altura.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .with_columns(
            pl.when((pl.col("2_peso_altura_12") == 1) & (pl.col("qtd_12") >= 2))
            .then(1)
            .otherwise(0)
            .alias("peso_altura_12"),
            pl.when((pl.col("2_peso_altura_24") == 1) & (pl.col("qtd_24") >= 2))
            .then(1)
            .otherwise(0)
            .alias("peso_altura_24"),
        )
        .select("co_fat_cidadao_pec", "peso_altura_12", "peso_altura_24", "idade")
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("idade").first().alias("idade"),
            pl.col("peso_altura_12").max().alias("agg_dashboard_peso_altura"),
            pl.col("peso_altura_24").max().alias("agg_peso_altura"),
        )
        .with_columns(
            pl.when((pl.col("agg_dashboard_peso_altura") == 1))
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_peso_altura")
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_peso_altura"))
            .alias("agg_alerta_peso_altura"),
        )
    )

    # In[34]:

    # Left join idoso com indicador_peso_altura

    idoso = idoso.join(
        indicador_idoso_peso_altura_v2, on="co_fat_cidadao_pec", how="left"
    ).with_columns(
        pl.col("agg_dashboard_peso_altura").fill_null(0),
        pl.col("agg_peso_altura").fill_null(0),
        pl.when(pl.col("idade") > 60)
        .then(pl.col("agg_alerta_peso_altura").fill_null(1))
        .otherwise(pl.col("agg_alerta_peso_altura").fill_null(0))
        .alias("agg_alerta_peso_altura"),
    )

    # In[35]:

    # idoso['agg_peso_altura'].value_counts()

    # ### **Indicador III** - Avaliação de creatinina nos últimos 12 meses - Dashboard
    #
    # ### Lista Nominal: Data da última avaliação e Alerta quando for "não consta"

    # In[36]:

    creatinina_dfs = pl.concat([fao_v2, fai_v2], how="diagonal")

    fai_exames_creatinina_grouped = (
        creatinina_dfs.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .join(exames, on="co_seq_fat_atd_ind", how="left")
        .filter(
            (pl.col("co_dim_cbo_1").is_in(creatina_cbo))
            | (pl.col("co_dim_cbo_2").is_in(creatina_cbo))
        )
        .with_columns(
            pl.when(
                (
                    (pl.col("ds_filtro_procedimentos").is_in(creatinina_codigos))
                    | (pl.col("tipo") == "Procedimentos Avaliados")
                    & (pl.col("codigo").is_in(creatinina_codigos))
                )
            )
            .then(1)
            .otherwise(0)
            .alias("creatinina"),
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("idade").first().alias("idade"),
            pl.max("creatinina").alias("agg_creatinina_semdata"),
            pl.col("dt_atendimento")
            .filter(
                (pl.col("creatinina") == 1)
                & (pl.col("dt_atendimento") >= calcular_data(24))
            )
            .max()
            .alias("dt_ultimo_creatinina"),
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultimo_creatinina") >= calcular_data(24))
                & (pl.col("agg_creatinina_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_creatinina"),
            pl.when(
                (pl.col("dt_ultimo_creatinina") >= calcular_data(12))
                & (pl.col("agg_creatinina_semdata") == 1)
            )
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_creatinina"),
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_creatinina"))
            .alias("agg_alerta_creatinina"),
            pl.when(
                (pl.col("dt_ultimo_creatinina") >= calcular_data(12))
                & (pl.col("agg_creatinina_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_creatinina"),
        )
    ).select(
        "co_fat_cidadao_pec",
        "agg_creatinina",
        "agg_alerta_creatinina",
        "agg_dashboard_creatinina",
        "dt_ultimo_creatinina",
    )

    # #### **Indicador III** e Itens da **Lista nominal** do Indicador III no df **"idoso"**:
    # ##### *A saber*
    # #### Número de pessoas idosas que tiveram avaliação de creatinina realizada nos últimos 12 meses: **"agg_creatinina" = 1**
    #
    # ##### - Data da última avaliação: **"dt_ultimo_creatinina"**
    # ##### - Alerta se "Não consta": **"agg_creatinina" = 0**

    # In[37]:

    # Left join idoso com indicador_creatinina

    idoso = idoso.join(
        fai_exames_creatinina_grouped, on="co_fat_cidadao_pec", how="left"
    ).with_columns(
        pl.col("agg_creatinina").fill_null(0),
        # pl.col("agg_alerta_creatinina").fill_null(1),
        pl.col("agg_dashboard_creatinina").fill_null(0),
        pl.when(pl.col("idade") > 60).then(pl.col("agg_alerta_creatinina").fill_null(1))
        # .otherwise(pl.col("agg_alerta_creatinina"))
        .otherwise(pl.col("agg_alerta_creatinina").fill_null(0)).alias(
            "agg_alerta_creatinina"
        ),
    )

    # ### **Indicador IV** - Duas visitas domiciliares por ACS/TACS nos últimos 12 meses com intervalo mínimo de 30 dias entre as visitas - Dashboard
    #
    # ### Lista Nominal:  ALERTA quando a quantidade for < 2

    # In[38]:

    visita_asc = (
        vis_dom_v2.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .select("co_fat_cidadao_pec", "dt_atendimento", "co_dim_cbo", "idade")
        .filter((pl.col("co_dim_cbo").is_in(acs_tacs)))
        .group_by("co_fat_cidadao_pec")
        .agg(
            [
                pl.col("idade").first().alias("idade"),
                pl.col("dt_atendimento")
                .filter(pl.col("dt_atendimento") >= calcular_data(24))
                .count()
                .alias("total_visitas_domiciliares_acs"),
                pl.col("dt_atendimento")
                .filter(pl.col("dt_atendimento") >= calcular_data(12))
                .count()
                .alias("total_visitas_domiciliares_acs_12"),
                pl.min("dt_atendimento").alias("min_date"),
                pl.max("dt_atendimento").alias("max_date"),
            ]
        )
        .with_columns(
            (pl.col("max_date") - pl.col("min_date")).dt.total_days().alias("diff_dias")
        )
        .with_columns(
            pl.when(
                (pl.col("total_visitas_domiciliares_acs") >= 2)
                & (pl.col("diff_dias") >= 30)
                & (pl.col("max_date") >= calcular_data(24))
            )
            .then(1)
            .otherwise(0)
            .alias("agg_visitas_domiciliares_acs"),
            pl.when(
                (pl.col("total_visitas_domiciliares_acs_12") >= 2)
                & (pl.col("diff_dias") >= 30)
                & (pl.col("max_date") >= calcular_data(12))
            )
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_visitas_domiciliares_acs"),
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_visitas_domiciliares_acs"))
            .alias("agg_alerta_visitas_domiciliares_acs"),
            pl.when(
                (pl.col("total_visitas_domiciliares_acs_12") >= 2)
                & (pl.col("diff_dias") >= 30)
                & (pl.col("max_date") >= calcular_data(12))
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_visitas_domiciliares_acs"),
        )
    ).select(
        "co_fat_cidadao_pec",
        "agg_visitas_domiciliares_acs",
        "agg_alerta_visitas_domiciliares_acs",
        "agg_dashboard_visitas_domiciliares_acs",
        "total_visitas_domiciliares_acs",
    )

    # #### **Indicador IV** e Itens da **Lista nominal** do Indicador IV no df **"idoso"**:
    # ##### *A saber*
    # #### Duas visitas domiciliares por ACS/TACS nos últimos 12 meses com intervalo mínimo de 30 dias entre as visitas: **"agg_visitas_domiciliares_acs" = 1**
    #
    # ##### - Quantidade de visitas recebidas **"total_visitas_domiciliares_acs**
    # ##### - Alerta se "Não consta": **"agg_visitas_domiciliares_acs" = 0**

    #

    # In[39]:

    # Left join idoso com indicador_acs/tacs

    idoso = idoso.join(visita_asc, on="co_fat_cidadao_pec", how="left").with_columns(
        pl.col("agg_visitas_domiciliares_acs").fill_null(0),
        pl.col("agg_dashboard_visitas_domiciliares_acs").fill_null(0),
        pl.col("total_visitas_domiciliares_acs").fill_null(0),
        # pl.col("agg_alerta_visitas_domiciliares_acs").fill_null(1),
        pl.when(pl.col("idade") > 60).then(
            pl.col("agg_alerta_visitas_domiciliares_acs").fill_null(1)
        )
        # .otherwise(pl.col("agg_alerta_visitas_domiciliares_acs"))
        .otherwise(pl.col("agg_alerta_visitas_domiciliares_acs").fill_null(0)).alias(
            "agg_alerta_visitas_domiciliares_acs"
        ),
    )

    # In[40]:

    # idoso['agg_visitas_domiciliares_acs'].value_counts()

    # ### **Indicador V** - Registro de vacina influenza nos últimos 12 meses - Dashboard
    #
    # ### Lista Nominal: Data da última vacina e Alerta quando for "não consta"

    # In[41]:

    vacina_registro = (
        vacina_v2.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .with_columns(
            pl.when((pl.col("ds_filtro_imunobiologico").str.contains(r"\b(33|77)\b")))
            .then(1)
            .otherwise(0)
            .alias("tem_vacina_influenza"),
        )
        .sort("dt_atendimento", descending=True)
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("idade").first().alias("idade"),
            pl.col("dt_atendimento")
            .filter(
                (pl.col("tem_vacina_influenza") == 1)
                & (pl.col("dt_atendimento") >= calcular_data(24))
            )
            .max()
            .alias("dt_ultimo_vacina_influenza"),
            pl.max("tem_vacina_influenza").alias("agg_vacina_influenza_semdata"),
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultimo_vacina_influenza") >= calcular_data(12))
                & (pl.col("agg_vacina_influenza_semdata") == 1)
            )
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_vacinas_influenza"),
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_vacinas_influenza"))
            .alias("agg_alerta_vacinas_influenza"),
            pl.when(
                (pl.col("dt_ultimo_vacina_influenza") >= calcular_data(24))
                & (pl.col("agg_vacina_influenza_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_vacinas_influenza"),
            pl.when(
                (pl.col("dt_ultimo_vacina_influenza") >= calcular_data(12))
                & (pl.col("agg_vacina_influenza_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_vacinas_influenza"),
            pl.col("dt_ultimo_vacina_influenza").alias("dt_ultima_vacina"),
        )
    ).drop("dt_ultimo_vacina_influenza", "idade")

    # #### **Indicador V** e Itens da **Lista nominal** do Indicador V no df **"idoso"**:
    # ##### *A saber*
    # #### Número de pessoas idosas com registro de aplicação/transcrição da vacina influenza nos últimos 12 meses: **"agg_vacinas_influenza" = 1**
    #
    # ##### - Data da última avaliação: **"dt_ultima_vacina"**
    # ##### - Alerta se "Não consta": **"agg_vacinas_influenza" = 0**

    # In[42]:

    # Left join idoso com indicador_vacina

    idoso = idoso.join(
        vacina_registro, on="co_fat_cidadao_pec", how="left"
    ).with_columns(
        pl.col("agg_vacinas_influenza").fill_null(0),
        # pl.col("agg_alerta_vacinas_influenza").fill_null(1),
        pl.col("agg_dashboard_vacinas_influenza").fill_null(0),
        pl.when(pl.col("idade") > 60).then(
            pl.col("agg_alerta_vacinas_influenza").fill_null(1)
        )
        # .otherwise(pl.col("agg_alerta_vacinas_influenza"))
        .otherwise(pl.col("agg_alerta_vacinas_influenza").fill_null(0)).alias(
            "agg_alerta_vacinas_influenza"
        ),
    )

    # ### **Indicador VI** - Consulta com dentista na APS nos últimos 12 meses - Dashboard
    #
    # ### Lista Nominal: Data da última consulta e Alerta quando for "não consta"

    # In[43]:

    fao_atend_odonto = (
        fao_v2.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .with_columns(
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cirurgioes_dentistas_codigos))
                | (pl.col("co_dim_cbo_2").is_in(cirurgioes_dentistas_codigos))
            )
            .then(1)
            .otherwise(0)
            .alias("cirurgiao_dentista"),
        )
        .sort("dt_atendimento", descending=True)
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("idade").first().alias("idade"),
            pl.max("cirurgiao_dentista").alias("agg_cirurgiao_dentista_semdata"),
            pl.col("dt_atendimento")
            .filter(
                (pl.col("cirurgiao_dentista") == 1)
                & (pl.col("dt_atendimento") >= calcular_data(24))
            )
            .max()
            .alias("dt_ultimo_atend_odonto"),
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultimo_atend_odonto") >= calcular_data(24))
                & (pl.col("agg_cirurgiao_dentista_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_cirurgiao_dentista"),
            pl.when(
                (pl.col("dt_ultimo_atend_odonto") >= calcular_data(12))
                & (pl.col("agg_cirurgiao_dentista_semdata") == 1)
                & (pl.col("idade") >= 61)
            )
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_cirurgiao_dentista"),
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_cirurgiao_dentista"))
            .alias("agg_alerta_cirurgiao_dentista"),
            pl.when(
                (pl.col("dt_ultimo_atend_odonto") >= calcular_data(12))
                & (pl.col("agg_cirurgiao_dentista_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_cirurgiao_dentista"),
        )
    ).drop("idade")

    # #### **Indicador VI** e Itens da **Lista nominal** do Indicador VI no df **"idoso"**:
    # ##### *A saber*
    # #### Número de pessoas idosas que realizaram consulta com dentista na APS nos últimos 12 meses: **"agg_cirurgiao_dentista" = 1**
    #
    # ##### - Data da última avaliação: **"dt_ultimo_atend_odonto"**
    # ##### - Alerta se "Não consta": **"agg_cirurgiao_dentista" = 0**

    # In[44]:

    # Left join idoso com indicador_dentista

    idoso = idoso.join(
        fao_atend_odonto, on="co_fat_cidadao_pec", how="left"
    ).with_columns(
        pl.col("agg_cirurgiao_dentista").fill_null(0),
        # pl.col("agg_alerta_cirurgiao_dentista").fill_null(1),
        pl.col("agg_dashboard_cirurgiao_dentista").fill_null(0),
        pl.when(pl.col("idade") > 60).then(
            pl.col("agg_alerta_cirurgiao_dentista").fill_null(1)
        )
        # .otherwise(pl.col("agg_alerta_cirurgiao_dentista"))
        .otherwise(pl.col("agg_alerta_cirurgiao_dentista").fill_null(0)).alias(
            "agg_alerta_cirurgiao_dentista"
        ),
    )

    # In[ ]:

    # ### **Indicador VII** - Aplicação da IVCF-20 - Dashboard
    #
    # ### Lista Nominal: Alerta quando for "não"

    # In[45]:

    ivcf_aplicado = (
        ivcf_v2.join(df_idade, on="co_fat_cidadao_pec", how="inner")
        .with_columns(pl.lit(1).alias("ivcf"))
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("idade").first().alias("idade"),
            pl.max("ivcf").alias("agg_ivcf_semdata"),
            pl.col("dt_atendimento")
            .filter(
                (pl.col("ivcf") == 1) & (pl.col("dt_atendimento") >= calcular_data(24))
            )
            .max()
            .alias("dt_ultimo_ivcf"),
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultimo_ivcf") >= calcular_data(24))
                & (pl.col("agg_ivcf_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_ivcf_aplicado"),
            pl.when((pl.col("agg_ivcf_semdata") == 1))
            .then(0)
            .otherwise(1)
            .alias("agg_alerta_ivcf_aplicado"),
        )
        .with_columns(
            pl.when((pl.col("idade") <= 60))
            .then(0)
            .otherwise(pl.col("agg_alerta_ivcf_aplicado"))
            .alias("agg_alerta_ivcf_aplicado"),
            pl.when(
                (pl.col("dt_ultimo_ivcf") >= calcular_data(12))
                & (pl.col("agg_ivcf_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_ivcf_aplicado"),
        )
    ).select(
        "co_fat_cidadao_pec",
        "agg_ivcf_aplicado",
        "agg_alerta_ivcf_aplicado",
        "agg_dashboard_ivcf_aplicado",
    )

    # Left join idoso com indicador_ivcf

    idoso = idoso.join(ivcf_aplicado, on="co_fat_cidadao_pec", how="left").with_columns(
        pl.col("agg_ivcf_aplicado").fill_null(0),
        # pl.col("agg_alerta_ivcf_aplicado").fill_null(1),
        pl.col("agg_dashboard_ivcf_aplicado").fill_null(0),
        pl.when(pl.col("idade") > 60).then(
            pl.col("agg_alerta_ivcf_aplicado").fill_null(1)
        )
        # .otherwise(pl.col("agg_alerta_ivcf_aplicado"))
        .otherwise(pl.col("agg_alerta_ivcf_aplicado").fill_null(0)).alias(
            "agg_alerta_ivcf_aplicado"
        ),
    )

    # #### **Indicador VII** e Itens da **Lista nominal** do Indicador VII no df **"idoso"**:
    # ##### *A saber*
    # #### Número de pessoas idosas que foram avaliadas com o instrumento (Índice de Vulnerabilidade Clínico Funcional - IVCF-20):
    #  **"agg_ivcf_avaliado" = 1**
    #
    # ##### - Alerta se "Não consta": **"agg_ivcf_avaliado" = 0**

    # ## Passo 8. Criar tabela pessoa final com todas as variáveis necessárias para próximas etapas de desenvolvimento do Painel

    # In[46]:

    # arrumando variáveis de unidade de saúde e equipe

    tb_dim_und_saude_v2 = (
        tb_dim_und_saude.select(
            [
                "co_seq_dim_unidade_saude",
                "nu_cnes",
                "no_unidade_saude",
                "st_registro_valido",
            ]
        )
        .rename(
            {
                "nu_cnes": "codigo_unidade_saude",
                "co_seq_dim_unidade_saude": "co_dim_unidade_saude",
                "st_registro_valido": "st_registro_valido_und_saude",
                "no_unidade_saude": "nome_unidade_saude",
            }
        )
        .with_columns(
            [
                pl.when((pl.col("codigo_unidade_saude") == "-"))
                .then(None)
                .otherwise(pl.col("codigo_unidade_saude"))
                .alias("codigo_unidade_saude"),
            ]
        )
    )

    tb_dim_und_saude_v3 = tb_dim_und_saude_v2.select(
        "codigo_unidade_saude",
        "nome_unidade_saude",
        "st_registro_valido_und_saude",
        "co_dim_unidade_saude",
    )

    tb_dim_equipe_v2 = (
        tb_dim_equipe.select(
            ["nu_ine", "no_equipe", "co_seq_dim_equipe", "st_registro_valido"]
        )
        .rename(
            {
                "co_seq_dim_equipe": "codigo_equipe",
                "st_registro_valido": "st_registro_valido_equipe",
                "no_equipe": "nome_equipe",
            }
        )
        .with_columns(
            [
                pl.when((pl.col("nu_ine") == "-"))
                .then(None)
                .otherwise(pl.col("nu_ine"))
                .alias("nu_ine"),
            ]
        )
        .filter(pl.col("st_registro_valido_equipe") == 1)
    )

    # In[47]:

    # adicionando informações cidadaos conforme prioridades entre tabelas

    tabela_idoso_final = (
        idoso.with_columns(
            [
                pl.coalesce(["nu_telefone_celular", "nu_telefone_contato"]).alias(
                    "telefone"
                )
            ]
        )
        .drop(["nu_telefone_celular", "nu_telefone_contato"])
        .join(
            tb_dim_equipe_v2,
            left_on="nu_ine_vinc_equipe",
            right_on="nu_ine",
            how="left",
        )
        .join(
            tb_dim_und_saude_v3,
            left_on="nu_cnes_vinc_equipe",
            right_on="codigo_unidade_saude",
            how="left",
        )
        .with_columns(
            pl.when((pl.col("ds_tipo_localizacao_domicilio").is_null()))
            .then(pl.lit("Não Informado"))
            .otherwise(pl.col("ds_tipo_localizacao_domicilio"))
            .alias("ds_tipo_localizacao_domicilio"),
            pl.coalesce(
                [
                    pl.col("nu_micro_area_domicilio"),
                    pl.col("nu_micro_area_fci"),
                    pl.col("nu_micro_area_tb_cidadao"),
                ]
            ).alias("nu_micro_area"),
        )
    )

    # In[48]:

    # padronizando informações de endereço
    # endereço prioridade: domilicio -> cidadao
    colunas_cidadao = [
        "no_tipo_logradouro_tb_cidadao",
        "ds_logradouro_tb_cidadao",
        "nu_numero_tb_cidadao",
        "no_bairro_tb_cidadao",
        "ds_complemento_tb_cidadao",
        "ds_cep_tb_cidadao",
        "no_municipio_tb_cidadao",
    ]

    # Gerar automaticamente os nomes das colunas de domicílio correspondentes
    colunas_domicilio = [
        col.replace("_tb_cidadao", "_domicilio") for col in colunas_cidadao
    ]
    colunas_nomes = [col.replace("_tb_cidadao", "") for col in colunas_cidadao]

    condicao = pl.col("ds_logradouro_domicilio").is_not_null() & (
        pl.col("ds_logradouro_domicilio") != ""
    )

    expressoes = [
        pl.when(condicao)
        .then(pl.col(domicilio))
        .otherwise(pl.col(cidadao))
        .alias(nomes)  # Mantém o nome original da coluna do cidadão
        for cidadao, domicilio, nomes in zip(
            colunas_cidadao, colunas_domicilio, colunas_nomes
        )
    ]
    tabela_idoso_final = tabela_idoso_final.with_columns(expressoes)

    tabela_idoso_final = tabela_idoso_final.rename({
        'nu_cnes_vinc_equipe': 'cnes_equipe',
        'nu_ine_vinc_equipe': 'ine_equipe',
        'ds_cep': 'cep',
        'ds_complemento': 'complemento',
        'ds_logradouro': 'logradouro',
        'ds_raca_cor': 'raca_cor',
        'ds_tipo_localizacao_domicilio': 'tipo_localizacao_domicilio',
        'nu_cns_cidadao': 'cns',
        'nu_cpf_cidadao': 'cpf',
        'nu_micro_area': 'micro_area',
        'nu_numero': 'numero',
        'no_cidadao': 'nome',
        'no_sexo_cidadao': 'sexo',
        'no_municipio': 'municipio',
        'no_tipo_logradouro': 'tipo_logradouro',
        'no_bairro': 'bairro',

        # Novas renomeações adicionadas
        'st_registro_valido_equipe': 'status_registro_valido_equipe',
        'st_registro_valido_und_saude': 'status_registro_valido_unidade_saude',
        'total_consulta_med_enferm': 'total_consulta_medico_enfermeiro',
        'co_dim_unidade_saude': 'codigo_unidade_saude',
        'co_fat_cidadao_pec': 'cidadao_pec',
        'co_unico_ultima_ficha': 'codigo_unico_ultima_ficha',
        'dt_nasc_cidadao': 'data_nascimento',
        'dt_penultima_medico_enferm': 'data_penultima_consulta_medico_enfermeiro',
        'dt_ultima_atualizacao_cidadao': 'data_ultima_atualizacao_cidadao',
        'dt_ultima_fci': 'data_ultima_fci',
        'dt_ultima_medico_enferm': 'data_ultima_consulta_medico_enfermeiro',
        'dt_ultima_vacina': 'data_ultima_vacina',
        'dt_ultimo_atend_odonto': 'data_ultimo_atendendimento_odonto',
        'dt_ultimo_creatinina': 'data_ultimo_creatinina'
    })
    tabela_idoso_final = (tabela_idoso_final
                        .select(
                                'agg_cirurgiao_dentista',
                                'agg_alerta_cirurgiao_dentista',
                                'agg_dashboard_cirurgiao_dentista',
                                'agg_creatinina',
                                'agg_alerta_creatinina',
                                'agg_dashboard_creatinina',
                                'agg_ivcf_aplicado',
                                'agg_alerta_ivcf_aplicado',
                                'agg_dashboard_ivcf_aplicado',
                                'agg_medicos_enfermeiros',
                                'agg_alerta_medicos_enfermeiros',
                                'agg_peso_altura',
                                'agg_dashboard_peso_altura',
                                'agg_alerta_peso_altura',
                                'agg_vacinas_influenza',
                                'agg_alerta_vacinas_influenza',
                                'agg_dashboard_vacinas_influenza',
                                'agg_visitas_domiciliares_acs',
                                'agg_dashboard_visitas_domiciliares_acs',
                                'agg_alerta_visitas_domiciliares_acs',
                                'cep',
                                'cnes_equipe',
                                'cns',
                                'codigo_unidade_saude',
                                'cidadao_pec',
                                'co_seq_acomp_cidadaos_vinc',
                                'codigo_unico_ultima_ficha',
                                'codigo_equipe',
                                'complemento',
                                'cpf',
                                'data_nascimento',
                                'data_penultima_consulta_medico_enfermeiro',
                                'data_ultima_atualizacao_cidadao',
                                'data_ultima_fci',
                                'data_ultima_consulta_medico_enfermeiro',
                                'data_ultima_vacina',
                                'data_ultimo_atendendimento_odonto',
                                'data_ultimo_creatinina',
                                'faixa_etaria',
                                'idade',
                                'ine_equipe',
                                'logradouro',
                                'micro_area',
                                'bairro',
                                'nome',
                                'municipio',
                                'sexo',
                                'tipo_logradouro',
                                'nome_equipe',
                                'nome_unidade_saude',
                                'numero',
                                'raca_cor',
                                'status_registro_valido_equipe',
                                'status_registro_valido_unidade_saude',
                                'telefone',
                                'tipo_localizacao_domicilio',
                                'total_consulta_medico_enfermeiro',
                                'total_visitas_domiciliares_acs',
                                'pessoa_atendida_12_meses'

                            )
                        )
    escrever_dados_raw(tabela_idoso_final,"idoso.parquet")
