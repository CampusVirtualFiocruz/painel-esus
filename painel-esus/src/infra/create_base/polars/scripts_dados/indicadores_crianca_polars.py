#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import os
import polars as pl
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from src.env.conf import getenv

from .codigos_cbo import *

#from utils import ler_dados_raw,escrever_dados_raw
def ler_dados_raw(nome_parquet,columns=""):

    try:
        os.getenv("ENV")
    # print("aa")
        lazy_on = getenv("LAZY_ON", False) # se lazy_on true ler e escrever dados lazy, se lazy_on false, ler os dados da forma normal

        working_directory  = os.getcwd()

        input_path = os.path.join(working_directory, "dados", "input") 

        output_path = os.path.join(working_directory, "dados", "output")  

        if lazy_on == 1:
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
         print(output_path + os.sep + nome_parquet)
         df.collect().write_parquet(output_path + os.sep +nome_parquet)

    else:
        df.write_parquet(output_path + os.sep +nome_parquet)



def gerar_banco():

    start_time = time.time()
    coluns_acv_geral = ['co_unico_ultima_ficha','dt_nascimento_cidadao','no_sexo_cidadao','nu_cpf_cidadao',
                'nu_cns_cidadao','nu_telefone_celular','nu_telefone_contato','no_cidadao'
                ,'nu_micro_area_domicilio','nu_micro_area_tb_cidadao','nu_ine_vinc_equipe','nu_cnes_vinc_equipe',
                'ds_tipo_localizacao_domicilio','dt_ultima_atualizacao_cidadao','co_seq_acomp_cidadaos_vinc']


    coluns_acv_end = ['no_tipo_logradouro_tb_cidadao','ds_logradouro_tb_cidadao',
                'nu_numero_tb_cidadao','no_bairro_tb_cidadao','ds_complemento_tb_cidadao',
                'ds_cep_tb_cidadao','no_municipio_tb_cidadao','no_tipo_logradouro_domicilio',
                'ds_logradouro_domicilio','nu_numero_domicilio',
                'ds_complemento_domicilio','no_bairro_domicilio','no_municipio_domicilio','ds_cep_domicilio']

    columns_acv = coluns_acv_geral + coluns_acv_end

    # FCI
    selected_columns_fci = ["co_fat_cidadao_pec","co_dim_tempo","nu_uuid_ficha","co_dim_raca_cor","nu_micro_area"]

    # FAI
    selected_columns_atd_ind = ["co_fat_cidadao_pec", "co_seq_fat_atd_ind","nu_altura","nu_peso","co_dim_tempo","co_dim_cbo_1", "co_dim_cbo_2", "dt_nascimento", "ds_filtro_proced_avaliados"]

    # FAOI
    columns_fao = ['co_fat_cidadao_pec','co_dim_tempo',"nu_altura","nu_peso",'co_dim_cbo_1','co_dim_cbo_2','co_seq_fat_atd_odnt','ds_filtro_procedimentos']

    # FAC (atividade coletiva)
    columns_atvdd_coletiva = ['co_fat_cidadao_pec','co_dim_tempo',"nu_participante_altura","nu_participante_peso",'co_seq_fat_atvdd_cltv_part']

    # VIS_DOM (visita domiciliar)
    columns_vis_dom = ['co_seq_fat_visita_domiciliar','co_fat_cidadao_pec','co_dim_tempo','co_dim_cbo',"nu_altura","nu_peso"]

    # MCA
    columns_mca = ['co_fat_cidadao_pec','co_dim_tempo']



    tb_pessoa = ler_dados_raw("tb_acomp_cidadaos_vinculados.parquet",columns_acv)

    #fci = pl.read_parquet(caminho_pasta+"tb_fat_cad_individual.parquet", columns=selected_columns_fci)
    fci = ler_dados_raw("tb_fat_cad_individual.parquet",selected_columns_fci)
    fci = fci.rename({"nu_micro_area" : "nu_micro_area_fci"})


    fai = ler_dados_raw("tb_fat_atendimento_individual.parquet", selected_columns_atd_ind)

    fao = ler_dados_raw("tb_fat_atendimento_odonto.parquet", columns_fao)

    vis_dom = ler_dados_raw("tb_fat_visita_domiciliar.parquet", columns_vis_dom)

    mca = ler_dados_raw("tb_fat_marca_consumo_alimnt.parquet", columns_mca)

    dim_raca_cor = ler_dados_raw("tb_dim_raca_cor.parquet")
    dim_raca_cor = dim_raca_cor.rename({"co_seq_dim_raca_cor" : "co_dim_raca_cor"}).select("co_dim_raca_cor","ds_raca_cor")

    tb_dim_equipe = ler_dados_raw("tb_dim_equipe.parquet")

    tb_dim_und_saude = ler_dados_raw("tb_dim_unidade_saude.parquet")

    fci = fci.join(dim_raca_cor,on="co_dim_raca_cor",how='left')


    coluns_cbo = ['nu_cbo','co_seq_dim_cbo']

    dim_cbo = ler_dados_raw("tb_dim_cbo.parquet", coluns_cbo)



    dt_12meses = datetime.today() - relativedelta(months=12)
    dt_24meses = datetime.today() - relativedelta(months=24)
    dt_36meses = datetime.today() - relativedelta(months=36)
    today = date.today()

    def calcular_data(meses: int):
        return datetime.today() - relativedelta(months=meses)


    # ### Passo 7. Filtrar os códigos de profissionais, exames ou condições de saúde dos Indicadores

    # In[7]:


    # AJUSTE de CBO

    #FAI

    fai = (
        fai
        .join(
            dim_cbo,
            left_on="co_dim_cbo_1",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo_1")
        .rename({"nu_cbo": "co_dim_cbo_1"})
        .join(
            dim_cbo,
            left_on="co_dim_cbo_2",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo_2")
        .rename({"nu_cbo": "co_dim_cbo_2"})
    )

    # FAO

    fao = (
        fao
        .join(
            dim_cbo,
            left_on="co_dim_cbo_1",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo_1")
        .rename({"nu_cbo": "co_dim_cbo_1"})
        .join(
            dim_cbo,
            left_on="co_dim_cbo_2",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo_2")
        .rename({"nu_cbo": "co_dim_cbo_2"})
    )

    #VIS_DOM

    vis_dom = (
        vis_dom
        .join(
            dim_cbo,
            left_on="co_dim_cbo",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo")
        .rename({"nu_cbo": "co_dim_cbo"})
    )


    # ### Passo 8. Manipular dados conforme necessidades dos Indicadores

    # ### Manipulando dados comuns aos indicadores

    # In[8]:


    cad_grouped = (
        fci
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        )
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.col("dt_atendimento").max().alias("dt_ultima_fci"),
            pl.col("ds_raca_cor").first().alias("ds_raca_cor")  ,
        ])
    )


    fci_v2 = fci.select("co_fat_cidadao_pec","nu_uuid_ficha","nu_micro_area_fci")


    tb_pessoa = (
        tb_pessoa
        .with_columns(
            pl.col("dt_ultima_atualizacao_cidadao").cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d").alias("dt_ultima_atualizacao_cidadao")
        )
    )


    tb_pessoa_v2 = tb_pessoa.join(
        fci_v2,
        left_on="co_unico_ultima_ficha",
        right_on="nu_uuid_ficha",
        how="left"
    ).join(
        cad_grouped,
        on="co_fat_cidadao_pec",
        how="left"
    )

    # criando dt_atendimento para FAI, usada em mais de um indicador, e filtrando cidadaos não nulos

    fai_v2 = (
        fai
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))

    # criando dt_atendimento para VIS_DOM, usada em mais de um indicador, e filtrando cidadaos não nulos

    vis_dom_v2 = (
        vis_dom
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))

    # criando dt_atendimento para FAO, usada em mais de um indicador, e filtrando cidadaos não nulos

    fao_v2 = (
        fao
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))

    mca_v2 = (
        mca
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))


    # ## Total de crianças - Dashboard

    # In[9]:


    tb_pessoa_v2 = (
        tb_pessoa_v2
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        )
        .with_columns(
            pl.col("dt_nascimento_cidadao")
            .cast(pl.Utf8)
            .str.strptime(pl.Date, "%Y-%m-%d")
            .alias("dt_nasc_cidadao")
        )
        .with_columns(
            pl.when(
                pl.date(
                    pl.col("dt_nasc_cidadao").dt.year(),
                    today.month,
                    today.day
                ) >= pl.col("dt_nasc_cidadao")
            )
            .then(today.year - pl.col("dt_nasc_cidadao").dt.year())
            .otherwise(today.year - pl.col("dt_nasc_cidadao").dt.year() - 1)
            .alias("idade")
        )
        .with_columns(
            (today - pl.col("dt_nasc_cidadao")).dt.total_days().alias("idade_em_dias")
        )
        .with_columns([
            (pl.col("idade_em_dias") // 365).alias("idade_anos"),
            ((pl.col("idade_em_dias") // 30) % 12).alias("idade_meses")
        ])
        .with_columns(
            pl.when(pl.col("idade_em_dias") <= 1095)
            .then(
                pl.concat_str([
                    pl.col("idade_anos").cast(pl.Utf8),
                    pl.lit(" anos e "),
                    pl.col("idade_meses").cast(pl.Utf8),
                    pl.lit(" meses")
                ])
            )
            .alias("idade_mes_ano")
        )
    )


    # In[10]:


    crianca = tb_pessoa_v2.filter(
        pl.col("idade_em_dias") <= 1095
    )


    # In[41]:


    #crianca.height


    # ### Total de crianças Atendidas - Dashboard

    # In[12]:


    total_criancas_atd = (
        fai_v2
        .filter( pl.col("dt_atendimento") >= dt_12meses )
        .group_by("co_fat_cidadao_pec")
        .agg()
        .with_columns(pl.lit(1).alias("crianca_atendida_12_meses"))

    )

    crianca = crianca.join(
        total_criancas_atd,
        on="co_fat_cidadao_pec",
        how="left"
    ).with_columns(
        pl.col("crianca_atendida_12_meses").fill_null(0),
    )


    # ### Crianças segundo sexo - Dashboard

    # In[13]:


    # COUNT ACV
    #tb_pessoa_v2['no_sexo_cidadao'].value_counts()
    categorias_validas_sexo = ["MASCULINO", "FEMININO", "INDETERMINADO"]

    crianca = crianca.with_columns(
        pl.when(pl.col("no_sexo_cidadao").str.to_uppercase().is_in(categorias_validas_sexo))
        .then(pl.col("no_sexo_cidadao").str.to_uppercase())  # Mantém e padroniza para maiúsculas
        .otherwise(pl.lit("NÃO INFORMADO"))  # Substitui valores inválidos
        .alias("no_sexo_cidadao")  # Atualiza a coluna original
    )


    # ### Crianças segundo Raça/Cor - Dashboard

    # In[14]:


    categorias_validas = ["Branca", "Preta", "Amarela", "Parda", "Indígena"]

    crianca = crianca.with_columns(
        pl.when(pl.col("ds_raca_cor").is_in(categorias_validas))
            .then(pl.col("ds_raca_cor"))  # Mantém o valor original se for válido
            .otherwise(pl.lit("NÃO INFORMADO"))  # Substitui valores inválidos
            .alias("ds_raca_cor")  # Atualiza a coluna original
    )


    # ### Crianças segundo Faixa Etária - Dashboard

    # In[40]:


    #crianca['idade'].value_counts()


    # In[16]:


    # Faixas etárias com base em dias exatos
    crianca = crianca.with_columns(
        pl.when(pl.col("idade_em_dias") <= 8)
        .then(pl.lit("0 a 8 dias"))
        .when((pl.col("idade_em_dias") > 8) & (pl.col("idade_em_dias") <= 30))
        .then(pl.lit("9 a 30 dias"))
        .when((pl.col("idade_em_dias") > 30) & (pl.col("idade_em_dias") <= 60))
        .then(pl.lit("1 a 2 meses"))
        .when((pl.col("idade_em_dias") > 60) & (pl.col("idade_em_dias") <= 120))
        .then(pl.lit("2 a 4 meses"))
        .when((pl.col("idade_em_dias") > 120) & (pl.col("idade_em_dias") <= 180))
        .then(pl.lit("4 a 6 meses"))
        .when((pl.col("idade_em_dias") > 180) & (pl.col("idade_em_dias") <= 270))
        .then(pl.lit("6 a 9 meses"))
        .when((pl.col("idade_em_dias") > 270) & (pl.col("idade_em_dias") <= 365))
        .then(pl.lit("9 a 12 meses"))
        .when((pl.col("idade_em_dias") > 365) & (pl.col("idade_em_dias") <= 540))
        .then(pl.lit("12 a 18 meses"))
        .when((pl.col("idade_em_dias") > 540) & (pl.col("idade_em_dias") <= 730))
        .then(pl.lit("18 a 24 meses"))
        .when((pl.col("idade_em_dias") > 730) & (pl.col("idade_em_dias") <= 1095))
        .then(pl.lit("24 a 36 meses"))
        .otherwise(pl.lit("3 anos completos"))
        .alias("faixa_etaria_0_3_anos")
    )


    # In[39]:


    #crianca['faixa_etaria_0_3_anos'].value_counts()


    # In[18]:


    crianca_dt_nasc = crianca.select('co_fat_cidadao_pec', 'dt_nasc_cidadao')


    # ### regex puericultura

    # In[19]:


    regex_puericultura = "|".join([f"\\|{c}\\|" for c in puericultura])
    #regex_puericultura


    # ## **Indicador I** - Crianças com primeira consulta até o 8° dia de vida - Dashboard - (% por categoria)
    # 
    # ### Lista Nominal: (Sim / Não) - ALERTA: Não

    # In[20]:


    indicadorI = (
        fai_v2
        # Etapa 1: Marcar atendimentos de puericultura com 1 (verdadeiro) ou 0 (falso)
        .with_columns(
            pl.when(pl.col("ds_filtro_proced_avaliados").str.contains(regex_puericultura))
            .then(1)
            .otherwise(0)
            .alias("puericultura")
        )

        # Etapa 2: Filtrar atendimentos realizados por médicos ou enfermeiros
        .filter(
            (
                (pl.col("co_dim_cbo_1").is_in(medicos_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(medicos_codigos)) |
                (pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos))
            )
        )

        # Etapa 3: (Comentada) Filtrar apenas atendimentos de puericultura
        # Se quiser incluir somente esses casos, descomente a linha abaixo:
        .filter(pl.col("puericultura") == 1)

        # Etapa 4: Obter a primeira consulta por criança (menor data de atendimento)
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento").min().alias("dt_primeira_consulta")
        )

        # Etapa 5: Juntar com a tabela de crianças para obter a data de nascimento
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

        # Etapa 6: Calcular dias entre nascimento e primeira consulta (fazer tambem esse ponto em uma etapa anterior para nao fazer em cada indicador)
        .with_columns([
            (pl.col("dt_primeira_consulta") - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("dias_ate_primeira_consulta")
        ])
        .with_columns(
            ((pl.lit(today) - pl.col("dt_nasc_cidadao")).dt.total_days()).alias("idade_em_dias")
        )

        # Etapa 8: Criar indicador - 1 se a consulta foi até 8 dias após nascimento, senão 0 (conectar com a etapa 9)
        .with_columns(
            pl.when(pl.col("dias_ate_primeira_consulta") <= 8)
            .then(1)
            .otherwise(
                pl.when(pl.col("idade_em_dias") < 8) #equipe < 8 ou <= 8
                .then(99)
                .otherwise(0)
            )
            .alias("agg_puericultura_ate_8_dias")
        )

        # Etapa 9: Indicadores adicionais (dashboard e lista nominal com base no indicador anterior + datas)
        .with_columns([
            # agg_dashboard: consulta nos últimos 24 meses E indicador de até 8 dias ativo
            pl.when(
                (pl.col("dt_primeira_consulta") >= dt_24meses) &
                (pl.col("agg_puericultura_ate_8_dias") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_puericultura_ate_8_dias"),

            # agg_card_lista_nominal: consulta nos últimos 36 meses E indicador de até 8 dias ativo
            pl.when(
                (pl.col("dias_ate_primeira_consulta") >= dt_36meses) &
                (pl.col("agg_puericultura_ate_8_dias") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_card_puericultura_ate_8_dias")
        ])

        # Etapa 10: Selecionar apenas colunas relevantes para o resultado final
        .select([
            "co_fat_cidadao_pec",
            "agg_puericultura_ate_8_dias",
            "agg_dashboard_puericultura_ate_8_dias",
            "agg_card_puericultura_ate_8_dias"
        ])
    )


    # ## **Indicador II** - Crianças com 9 consultas de puericultura até 2 anos de vida - Dashboard - (% por categoria)
    # 
    # ### Lista Nominal: (Sim / Não / Não se aplica) - ALERTA: Não

    # In[21]:


    indicador_II = (
        # Etapa 1: Juntar diretamente fai_v2 com crianca
        fai_v2
        .join(crianca_dt_nasc, on="co_fat_cidadao_pec", how="inner")

        # Etapa 2: Marcar puericultura
        .with_columns(
            pl.when(pl.col("ds_filtro_proced_avaliados").str.contains(regex_puericultura))
            .then(1)
            .otherwise(0)
            .alias("puericultura")
        )

        # Etapa 3: Filtrar atendimentos de médicos/enfermeiros e puericultura
        .filter(
            (
                (pl.col("co_dim_cbo_1").is_in(medicos_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(medicos_codigos)) |
                (pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos))
            )
        & (pl.col("puericultura") == 1)
        )

        # Etapa 4: Calcular idade no atendimento
        .with_columns([
            (pl.col("dt_atendimento") - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias_atendimento")
        ])

        # Etapa 5: Filtrar apenas atendimentos até 2 anos de idade (730 dias)
        .filter(pl.col("idade_em_dias_atendimento") <= 730)

        # Etapa 6: Agrupar por criança e calcular total de consultas e data do último atendimento
        .group_by("co_fat_cidadao_pec")
        .agg([
        # pl.col("co_dim_tempo").max().cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_ultimo_atd"),
            pl.col("dt_atendimento").max().alias("dt_ultimo_atd"),

            pl.len().alias("num_consultas_puericultura"),
            pl.col("dt_nasc_cidadao").last().alias("dt_nasc_cidadao")
        ])

        # Etapa 7: Calcular idade atual
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao")).dt.total_days().alias("idade_em_dias")
        )

        # Etapa 8: Indicador principal
        .with_columns(
            pl.when(pl.col("num_consultas_puericultura") >= 9)
            .then(1)
            .otherwise(
                pl.when(pl.col("idade_em_dias") < 730)
                .then(99)
                .otherwise(0)
            )
            .alias("agg_puericultura_9_consultas_ate_2_anos")
        )

        # Etapa 9: Indicadores adicionais (dashboard e lista nominal)
        .with_columns([
            pl.when(
                (pl.col("dt_ultimo_atd") >= dt_24meses) &
                (pl.col("agg_puericultura_9_consultas_ate_2_anos") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_puericultura_9_consultas_ate_2_anos"),

            pl.when(
                (pl.col("dt_ultimo_atd") >= dt_36meses) &
                (pl.col("agg_puericultura_9_consultas_ate_2_anos") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_card_puericultura_9_consultas_ate_2_anos")
        ])

        # Etapa 10: Selecionar colunas finais
        .select([
            "co_fat_cidadao_pec",
            "num_consultas_puericultura",
            "agg_puericultura_9_consultas_ate_2_anos",
            "agg_dashboard_puericultura_9_consultas_ate_2_anos",
            "agg_card_puericultura_9_consultas_ate_2_anos",
        ])
    )


    # ## **Indicador III** - Crianças com registro de peso e altura nas 9 consultas de puericultura correspondentes - Dashboard
    # 
    # ### Lista Nominal: Sim / Não / Não se aplica (criança com menos de 2 anos de vida)
    # 

    # In[22]:


    # Etapa 0: Identificar datas de puericultura
    fichas_puericultura = (
        fai_v2
        .filter(pl.col("ds_filtro_proced_avaliados").str.contains(regex_puericultura))
        .select(["co_fat_cidadao_pec", "dt_atendimento"])
        .unique()
    )

    # Etapa 1: Consolidar registros com peso e altura aferidos
    registros_com_peso_altura = (
        pl.concat([fao_v2, fai_v2, vis_dom_v2], how="diagonal")
        .filter(
            pl.col("nu_peso").is_not_null() &
            pl.col("nu_altura").is_not_null()
        )
    )

    # Etapa 2: Cruzar com puericultura na mesma data
    peso_altura_na_puericultura = (
        registros_com_peso_altura
        .join(
            fichas_puericultura,
            on=["co_fat_cidadao_pec", "dt_atendimento"],
            how="inner"
        )
    )

    # Etapa 3: Juntar com dados da criança
    indicadorIII = (
        peso_altura_na_puericultura
        .join(
            crianca,
            on="co_fat_cidadao_pec",
            how="inner"
        )
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias")
        )
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.len().alias("total_peso_altura"),
            pl.col("nu_peso").sort_by("dt_atendimento", descending=True).alias("nu_peso_recentes"),
            pl.col("nu_altura").sort_by("dt_atendimento", descending=True).alias("nu_altura_recentes"),
            pl.col("dt_atendimento").max().alias("dt_ultima_avaliacao_peso_altura"),
            pl.col("dt_nasc_cidadao").last().alias("dt_nasc_cidadao")
        ])
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao")).dt.total_days().alias("idade_em_dias")
        )
        .with_columns(
            pl.when(pl.col("total_peso_altura") >= 9)
            .then(1)
            .when(
                (pl.col("idade_em_dias") < 730) &
                (pl.col("total_peso_altura") < 9)
            ).then(99)
            .otherwise(0)
            .alias("agg_9_peso_altura")
        )
        .with_columns([
            pl.when(
                (pl.col("dt_ultima_avaliacao_peso_altura") >= dt_24meses) &
                (pl.col("agg_9_peso_altura") == 1)
            ).then(1).otherwise(0).alias("agg_dashboard_9_peso_altura"),

            pl.when(
                (pl.col("dt_ultima_avaliacao_peso_altura") >= dt_36meses) &
                (pl.col("agg_9_peso_altura") == 1)
            ).then(1).otherwise(0).alias("agg_card_9_peso_altura")
        ])
        .select([
            "co_fat_cidadao_pec",
            "nu_peso_recentes",
            "nu_altura_recentes",
            "total_peso_altura",
            "agg_9_peso_altura",
            "agg_dashboard_9_peso_altura",
            "agg_card_9_peso_altura"
        ])
    )


    # ## **Indicador IV** - Crianças com uma visita domiciliar do ACS/TACS até 30 dias de vida  - Dashboard - (% por categoria)
    # 
    # ### Lista Nominal: (Sim / Não / Não se aplica) - ALERTA: Não

    # In[23]:


    indicadorIV = (
        # Etapa 1: Filtrar apenas visitas feitas por ACS/TACS
        vis_dom_v2
        .filter(pl.col("co_dim_cbo").is_in(acs_tacs))
        .select(["co_fat_cidadao_pec", "dt_atendimento"])

        # Etapa 2: Juntar com informações da criança (nascimento)
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

        # Etapa 3: Calcular dias de vida no momento da visita
        .with_columns(
            (pl.col("dt_atendimento") - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("dias_de_vida")
        )

        # Etapa 4: Filtrar visitas até 30 dias de vida
        .filter(
            (pl.col("dias_de_vida") >= 0) &
            (pl.col("dias_de_vida") <= 30)
        )

        # Etapa 5: Agrupar por criança e contar visitas
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.len().alias("total_visitas_ate_30dias"),
            pl.col("dt_atendimento").max().alias("dt_ultima_visita_30d"),
            pl.col("dt_nasc_cidadao").last().alias("dt_nasc_cidadao")
        ])

        # Etapa 6: Calcular idade atual
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias")
        )

        # Etapa 7: Criar indicador com tratamento para crianças < 2 anos
        .with_columns(
            pl.when(pl.col("total_visitas_ate_30dias") >= 1)
            .then(pl.lit(1))
            .when(
                (pl.col("idade_em_dias") < 30) &
                (pl.col("total_visitas_ate_30dias") < 1)
            )
            .then(pl.lit(99))
            .otherwise(pl.lit(0))
            .alias("agg_visita_acs_ate_30d")
        )

        # Etapa 8: Indicadores adicionais (dashboard e lista nominal)
        .with_columns([
            pl.when(
                (pl.col("dt_ultima_visita_30d") >= dt_24meses) &
                (pl.col("agg_visita_acs_ate_30d") >= 1)
            ).then(1)
            .otherwise(0)
            .alias("agg_dashboard_visita_acs_ate_30d"),

            pl.when(
                (pl.col("dt_ultima_visita_30d") >= dt_36meses) &
                (pl.col("agg_visita_acs_ate_30d") >= 1)
            ).then(1)
            .otherwise(0)
            .alias("agg_card_visita_acs_ate_30d")
        ])

        # Etapa 9: Selecionar colunas finais
        .select([
            "co_fat_cidadao_pec",
            "agg_dashboard_visita_acs_ate_30d",
            "agg_card_visita_acs_ate_30d"
        ])
    )


    # ## **Indicador V** - Crianças com uma visita domiciliar do ACS/TACS dos 31 dias até os 6 meses de vida  - Dashboard
    # 
    # ### Lista Nominal: Sim / Não / Não se aplica (crianças com menos de 6 meses de vida)
    # 

    # In[24]:


    indicadorV = (
        vis_dom_v2

        # Etapa 1: Filtrar visitas realizadas por ACS ou TACS
        .filter(pl.col("co_dim_cbo").is_in(acs_tacs))

        # Etapa 2: Juntar com a tabela de crianças (pegar data de nascimento)
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

        # Etapa 3: Calcular idade da criança no momento da visita
        .with_columns([
            (pl.col("dt_atendimento") - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("dias_de_vida")
        ])

        # Etapa 4: Filtrar visitas entre 31 e 183 dias de vida (1 a 6 meses)
        .filter(
            (pl.col("dias_de_vida") >= 31) &
            (pl.col("dias_de_vida") <= 183)
        )

        # Etapa 5: Agrupar por criança para contar visitas nesse intervalo
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.col("dt_atendimento").max().alias("dt_ultima_visita"),
            pl.len().alias("total_visitas_31a183dias"),
            pl.col("dt_nasc_cidadao").last().alias("dt_nasc_cidadao")
        ])

        # Etapa 6: Calcular idade atual
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias")
        )

        # Etapa 7: Criar indicador com regra de exceção para < 6 meses
        .with_columns(
            pl.when(pl.col("total_visitas_31a183dias") >= 1)
            .then(pl.lit(1))
            .when((pl.col("idade_em_dias") < 183) & (pl.col("total_visitas_31a183dias") == 0))
            .then(pl.lit(99))
            .otherwise(pl.lit(0))
            .alias("agg_visita_acs_ate_6m")
        )

        # Etapa 8: Indicadores adicionais (dashboard e lista nominal)
        .with_columns([
            pl.when(
                (pl.col("dt_ultima_visita") >= dt_24meses) &
                (pl.col("agg_visita_acs_ate_6m") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_visita_acs_ate_6m"),

            pl.when(
                (pl.col("dt_ultima_visita") >= dt_36meses) &
                (pl.col("agg_visita_acs_ate_6m") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_card_visita_acs_ate_6m")
        ])
        .select([
            "co_fat_cidadao_pec",
            "total_visitas_31a183dias",
            "agg_dashboard_visita_acs_ate_6m",
            "agg_card_visita_acs_ate_6m"
        ])
    )


    # ## **Indicador VI** - Crianças com uma consulta odontológica até 12 meses de vida  - Dashboard - (% por categoria)
    # 
    # ### Lista Nominal: (Sim / Não / Não se aplica) - ALERTA: Não

    # In[25]:


    indicadorVI = (
        fao_v2

        # Etapa 1: Filtrar atendimentos odontológicos realizados por cirurgiões-dentistas
        .filter(
            (pl.col("co_dim_cbo_1").is_in(cirurgioes_dentistas_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(cirurgioes_dentistas_codigos))
        )

        # Etapa 2: Juntar com a base de crianças (sem select)
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

        # Etapa 3: Calcular idade no atendimento
        .with_columns([
            (pl.col("dt_atendimento") - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias")
        ])

        # Etapa 4: Filtrar atendimentos com menos de 12 meses de idade (< 365 dias)
        .filter(pl.col("idade_em_dias") < 365)

        # Etapa 5: Agrupar por criança e contar atendimentos + obter última data
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.len().alias("qtd_consultas_odont_ate_12m"),
            pl.col("dt_atendimento").max().alias("dt_ultima_consulta_odonto_ate_12m"),
            pl.col("dt_nasc_cidadao").last().alias("dt_nasc_cidadao")
        ])

        # Etapa 6: Calcular idade atual
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao")).dt.total_days().alias("idade_em_dias")
        )

        # Etapa 7: Criar indicador com tratamento para < 12 meses
        .with_columns(
            pl.when(pl.col("qtd_consultas_odont_ate_12m") >= 1)
            .then(pl.lit(1))
            .when((pl.col("idade_em_dias") < 365) & (pl.col("qtd_consultas_odont_ate_12m") == 0))
            .then(pl.lit(99))
            .otherwise(pl.lit(0))
            .alias("agg_odonto_ate_12m")
        )

        # Etapa 8: Indicadores adicionais (dashboard e lista nominal com base na data da última consulta)
        .with_columns([
            pl.when(
                (pl.col("dt_ultima_consulta_odonto_ate_12m") >= dt_24meses) &
                (pl.col("agg_odonto_ate_12m") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_odonto_ate_12m"),

            pl.when(
                (pl.col("dt_ultima_consulta_odonto_ate_12m") >= dt_36meses) &
                (pl.col("agg_odonto_ate_12m") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_card_odonto_ate_12m")
        ])

        # Etapa 9: Selecionar colunas finais
        .select([
            "co_fat_cidadao_pec",
            "agg_dashboard_odonto_ate_12m",
            "agg_card_odonto_ate_12m"
        ])
    )


    # In[26]:


    #indicadorVI.head(10)


    # ## **Indicador VII** - Crianças com consulta odontológica entre 12 e 24 meses de vida - Dashboard
    # 
    # ### Lista Nominal: Sim / Não / Não se aplica (crianças com menos de 12 meses de vida)
    # 

    # In[27]:


    indicadorVII = (
        fao_v2

        # Etapa 1: Filtrar atendimentos realizados por cirurgiões-dentistas
        .filter(
            (pl.col("co_dim_cbo_1").is_in(cirurgioes_dentistas_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(cirurgioes_dentistas_codigos))
        )

        # Etapa 2: Juntar com base de crianças para obter data de nascimento
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

        # Etapa 3: Calcular idade da criança no atendimento
        .with_columns([
            (pl.col("dt_atendimento") - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias")
        ])

        # Etapa 4: Filtrar atendimentos entre 12 e 24 meses (365–730 dias)
        .filter(
            (pl.col("idade_em_dias") >= 365) &
            (pl.col("idade_em_dias") <= 730)
        )

        # Etapa 5: Agrupar por criança e contar atendimentos
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.col("dt_atendimento").max().alias("dt_ultima_consulta_odonto"),
            pl.len().alias("num_odonto_ate24m"),
            pl.col("dt_nasc_cidadao").last().alias("dt_nasc_cidadao")
        ])

        # Etapa 6: Calcular idade atual
        .with_columns(
            (pl.lit(today) - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_em_dias")
        )


        # Etapa 8: Indicador com tratamento para crianças com menos de 12 meses
        .with_columns(
        pl.when(pl.col("num_odonto_ate24m") >= 1)
            .then(pl.lit(1))
            .when((pl.col("idade_em_dias") < 365) & (pl.col("num_odonto_ate24m") == 0))
            .then(pl.lit(99))
            .otherwise(pl.lit(0))
            .alias("agg_odonto_12a24m")
        )

        # Etapa 9: Indicadores adicionais (dashboard e lista nominal com base no indicador anterior + datas)
        .with_columns([
            pl.when(
                (pl.col("dt_ultima_consulta_odonto") >= dt_24meses) &
                (pl.col("agg_odonto_12a24m") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_odonto_12a24m"),

            pl.when(
                (pl.col("dt_ultima_consulta_odonto") >= dt_36meses) &
                (pl.col("agg_odonto_12a24m") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_card_odonto_12a24m")
        ])

            # Etapa 10: Selecionar colunas finais
        .select([
            "co_fat_cidadao_pec",
            "num_odonto_ate24m",
            "agg_dashboard_odonto_12a24m",
            "agg_card_odonto_12a24m"
        ])
    )


    # ## **Indicador VIII** - Crianças com marcos do desenvolvimento avaliados  - Dashboard - (% por categoria)
    # 
    # ### Lista Nominal: (Sim / Não) - ALERTA: Não

    # In[28]:


    indicadorVIII = (
        fai_v2
        # Etapa 1: Filtrar apenas avaliações de marcos do desenvolvimento
        .filter(pl.col("ds_filtro_proced_avaliados").str.contains("0301010277") )
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

        # Etapa 4: Agrupar por criança
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.len().alias("qtd_avaliacoes_desenvolvimento"),
            pl.col("dt_atendimento").max().alias("dt_ultima_avaliacao_desenvolvimento")
        ])

        # Etapa 5: Criar indicador principal (1 ou 0)
        .with_columns(
            pl.when(pl.col("qtd_avaliacoes_desenvolvimento") >= 1)
            .then(pl.lit(1))
            .otherwise(pl.lit(0))
            .alias("agg_marco_desenvolvimento")
        )

        # Etapa 6: Indicadores adicionais (dashboard e lista nominal)
        .with_columns([
            pl.when(
                (pl.col("dt_ultima_avaliacao_desenvolvimento") >= dt_24meses) &
                (pl.col("agg_marco_desenvolvimento") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_dashboard_marco_desenvolvimento"),

            pl.when(
                (pl.col("dt_ultima_avaliacao_desenvolvimento") >= dt_36meses) &
                (pl.col("agg_marco_desenvolvimento") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_card_marco_desenvolvimento")
        ])

        # Etapa 7: Selecionar colunas finais
        .select([
            "co_fat_cidadao_pec",
            "agg_dashboard_marco_desenvolvimento",
            "agg_card_marco_desenvolvimento"
        ])
    )


    # ## **Indicador IX** - Crianças com consumo alimentar avaliado (na data das consultas de puericultura) - Dashboard
    # 
    # ### Lista Nominal: Sim / Não

    # In[29]:


    # Etapa 1: Filtrar apenas puericultura em fai_v2
    fai_puericultura = (
        fai_v2
        .filter(pl.col("ds_filtro_proced_avaliados").str.contains(regex_puericultura))
        .select(["co_fat_cidadao_pec", "dt_atendimento"])
        .unique()
    )

    # Etapa 2: Cruzar fichas de consumo com puericultura na mesma data
    consumo_puericultura = (
        mca_v2
        .join(
            fai_puericultura,
            on=["co_fat_cidadao_pec", "dt_atendimento"],
            how="inner"  # mantém apenas quando tem ficha E puericultura na mesma data
        )
    )

    # Etapa 3: Juntar com base de crianças (com data de nascimento)
    indicadorIX = (
        consumo_puericultura
        .join(
            crianca_dt_nasc,
            on="co_fat_cidadao_pec",
            how="inner"
        )

    # Etapa 4: Agrupar por criança — contar fichas e pegar data mais recente
    .group_by("co_fat_cidadao_pec")
    .agg([
        pl.len().alias("qtd_fichas_consumo"),
        pl.col("dt_atendimento").max().alias("dt_ultima_ficha_consumo")
    ])

    # Etapa 5: Indicador principal
    .with_columns(
        pl.when(pl.col("qtd_fichas_consumo") >= 1)
        .then(pl.lit(1))
        .otherwise(pl.lit(0))
        .alias("agg_consumo_alimentar")
    )

    # Etapa 6: Indicadores adicionais (dashboard e lista nominal)
    .with_columns([
        pl.when(
            (pl.col("dt_ultima_ficha_consumo") >= dt_24meses) &
            (pl.col("agg_consumo_alimentar") == 1)
        ).then(1)
        .otherwise(0)
        .alias("agg_dashboard_consumo_alimentar"),

        pl.when(
            (pl.col("dt_ultima_ficha_consumo") >= dt_36meses) &
            (pl.col("agg_consumo_alimentar") == 1)
        ).then(1)
        .otherwise(0)
        .alias("agg_card_consumo_alimentar")
    ])

    # Etapa 7: Selecionar colunas finais
    .select([
        "co_fat_cidadao_pec",
        "qtd_fichas_consumo",
        "dt_ultima_ficha_consumo",
        "agg_consumo_alimentar",
        "agg_dashboard_consumo_alimentar",
        "agg_card_consumo_alimentar"
    ])
    )


    # ## Passo 9. Criar tabela pessoa final com todas as variáveis necessárias para próximas etapas de desenvolvimento do Painel

    # In[30]:


    # arrumando variáveis de unidade de saúde e equipe

    tb_dim_und_saude_v2 = (
        tb_dim_und_saude
        .select([
            'co_seq_dim_unidade_saude',
            'nu_cnes',
            'no_unidade_saude',
            'st_registro_valido'
        ]).rename({
            'nu_cnes': 'codigo_unidade_saude',
            'co_seq_dim_unidade_saude': 'co_dim_unidade_saude',
            'st_registro_valido': 'st_registro_valido_und_saude',
            'no_unidade_saude': 'nome_unidade_saude',
        }) .with_columns([

            pl.when(
                (pl.col("codigo_unidade_saude") == "-")
            )
            .then(None)
            .otherwise(pl.col("codigo_unidade_saude"))
            .alias("codigo_unidade_saude"),
        ])
    )

    tb_dim_und_saude_v3 = tb_dim_und_saude_v2.select('codigo_unidade_saude','nome_unidade_saude','st_registro_valido_und_saude','co_dim_unidade_saude')



    tb_dim_equipe_v2 = (
        tb_dim_equipe
        .select([
            'nu_ine',
            'no_equipe',
            'co_seq_dim_equipe',
            'st_registro_valido'
        ]).rename({
            'co_seq_dim_equipe': 'codigo_equipe',
            'st_registro_valido': 'st_registro_valido_equipe',
            'no_equipe': 'nome_equipe',
        })

        .with_columns([

            pl.when(
                (pl.col("nu_ine") == "-")
            )
            .then(None)
            .otherwise(pl.col("nu_ine"))
            .alias("nu_ine"),
        ]).filter(pl.col("st_registro_valido_equipe") == 1)
    )


    # In[31]:


    # adicionando informações cidadaos conforme prioridades entre tabelas

    tabela_crianca_final = (crianca
        .with_columns([
            pl.coalesce(['nu_telefone_celular','nu_telefone_contato']).alias("telefone")
        ]).drop(['nu_telefone_celular','nu_telefone_contato']).join(
            tb_dim_equipe_v2,
            left_on="nu_ine_vinc_equipe",
            right_on= "nu_ine",
            how="left"
        ).join(
            tb_dim_und_saude_v3,
            left_on="nu_cnes_vinc_equipe",
            right_on= "codigo_unidade_saude",
            how="left"
        ).with_columns(
            pl.when(
                    (pl.col("ds_tipo_localizacao_domicilio").is_null() )  )
            .then(pl.lit("Não Informado"))
            .otherwise(pl.col("ds_tipo_localizacao_domicilio"))
            .alias("ds_tipo_localizacao_domicilio"),

            pl.coalesce([
                pl.col("nu_micro_area_domicilio"),
                pl.col("nu_micro_area_fci"),
                pl.col("nu_micro_area_tb_cidadao"),
            ]).alias("nu_micro_area")
        )
        .join(
            indicadorI,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicador_II,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorIII,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorIV,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorV,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorVI,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorVII,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorVIII,
            on="co_fat_cidadao_pec",
            how='left'
        )
        .join(
            indicadorIX,
            on="co_fat_cidadao_pec",
            how='left'
        )

    ).drop("nu_micro_area_domicilio","nu_micro_area_fci","nu_micro_area_tb_cidadao")


    
    # In[32]:

    colunas_do_schema = tabela_crianca_final.collect_schema().names()


    tabela_crianca_final = (
        tabela_crianca_final.with_columns([
            pl.col(col).fill_null(0)#.alias(col)
            for col in colunas_do_schema
            if col.startswith("agg_")
        ]).with_columns(
            pl.col("num_consultas_puericultura").fill_null(0),
            pl.col("total_peso_altura").fill_null(0),
        )
    )




    # In[33]:


    #padronizando informações de endereço
    #endereço prioridade: domilicio -> cidadao
    colunas_cidadao = [
        'no_tipo_logradouro_tb_cidadao',
        'ds_logradouro_tb_cidadao',
        'nu_numero_tb_cidadao',
        'no_bairro_tb_cidadao',
        'ds_complemento_tb_cidadao',
        'ds_cep_tb_cidadao',
        'no_municipio_tb_cidadao'
    ]

    # Gerar automaticamente os nomes das colunas de domicílio correspondentes
    colunas_domicilio = [col.replace("_tb_cidadao", "_domicilio") for col in colunas_cidadao]
    colunas_nomes = [col.replace("_tb_cidadao", "") for col in colunas_cidadao]


    condicao = (
        pl.col("ds_logradouro_domicilio").is_not_null() &
        (pl.col("ds_logradouro_domicilio") != "")
    )


    expressoes = [
        pl.when(condicao)
        .then(pl.col(domicilio))
        .otherwise(pl.col(cidadao))
        .alias(nomes)  # Mantém o nome original da coluna do cidadão
        for cidadao, domicilio, nomes in zip(colunas_cidadao, colunas_domicilio,colunas_nomes)
    ]
    tabela_crianca_final = tabela_crianca_final.with_columns(expressoes)


    # In[34]:


    tabela_crianca_final = tabela_crianca_final.rename({
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
        'faixa_etaria_0_3_anos': 'faixa_etaria',


            # Novas renomeações adicionadas
        'st_registro_valido_equipe': 'status_registro_valido_equipe',
        'st_registro_valido_und_saude': 'status_registro_valido_unidade_saude',
        'co_dim_unidade_saude': 'codigo_unidade_saude',
        'co_fat_cidadao_pec': 'cidadao_pec',
        'co_unico_ultima_ficha': 'codigo_unico_ultima_ficha',
        'dt_nasc_cidadao': 'data_nascimento',
        'dt_ultima_fci': 'data_ultima_fci'
    })



    tabela_crianca_final = (tabela_crianca_final
                        .select(
                                'agg_dashboard_puericultura_ate_8_dias',
                                'agg_card_puericultura_ate_8_dias',
                                'agg_dashboard_puericultura_9_consultas_ate_2_anos',
                                'agg_card_puericultura_9_consultas_ate_2_anos',
                                'agg_dashboard_9_peso_altura',
                                'agg_card_9_peso_altura',
                                'agg_dashboard_visita_acs_ate_30d',
                                'agg_card_visita_acs_ate_30d',
                                'agg_dashboard_visita_acs_ate_6m',
                                'agg_card_visita_acs_ate_6m',
                                'agg_dashboard_odonto_ate_12m',
                                'agg_card_odonto_ate_12m',
                                'agg_dashboard_marco_desenvolvimento',
                                'agg_card_marco_desenvolvimento',
                                'agg_dashboard_consumo_alimentar',
                                'agg_card_consumo_alimentar',
                                'agg_dashboard_odonto_12a24m',
                                'agg_card_odonto_12a24m',
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
                                'num_consultas_puericultura',
                                'nu_peso_recentes',
                                'nu_altura_recentes',
                                'total_peso_altura',
                                'idade_em_dias',
                            #   'num_odonto_ate24m',
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
                                #'total_visitas_domiciliares_acs',
                                'crianca_atendida_12_meses'

                            )
                        )

    #tabela_crianca_final.write_parquet("../output/crianca.parquet")
    escrever_dados_raw(tabela_crianca_final,"crianca.parquet")

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Tempo total de execução: {execution_time:.2f} segundos")




