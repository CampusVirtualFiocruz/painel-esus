#!/usr/bin/env python
# coding: utf-8


import os
import time
from datetime import date, datetime

import pandas as pd
import polars as pl
from codigos_cbo import *
from dateutil.relativedelta import relativedelta
from src.env.conf import getenv


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
         print(output_path + os.sep + nome_parquet)
         #df.collect().sink_parquet(output_path + os.sep + nome_parquet,compression='snappy',lazy=True)
         df.collect().write_parquet(output_path + os.sep +nome_parquet)

    else:
        df.write_parquet(output_path + os.sep +nome_parquet)


def gerar_banco():
    # ACV
    coluns_acv_geral = ['co_unico_ultima_ficha','dt_nascimento_cidadao','no_sexo_cidadao','nu_cpf_cidadao',
                'nu_cns_cidadao','nu_telefone_celular','nu_telefone_contato','no_cidadao'
                ,'nu_micro_area_domicilio','nu_micro_area_tb_cidadao','nu_ine_vinc_equipe','nu_cnes_vinc_equipe',
                'ds_tipo_localizacao_domicilio','dt_ultima_atualizacao_cidadao','co_seq_acomp_cidadaos_vinc','tp_identidade_genero_cidadao']


    coluns_acv_end = ['no_tipo_logradouro_tb_cidadao','ds_logradouro_tb_cidadao',
                'nu_numero_tb_cidadao','no_bairro_tb_cidadao','ds_complemento_tb_cidadao',
                'ds_cep_tb_cidadao','no_municipio_tb_cidadao','no_tipo_logradouro_domicilio',
                'ds_logradouro_domicilio','nu_numero_domicilio',
                'ds_complemento_domicilio','no_bairro_domicilio','no_municipio_domicilio','ds_cep_domicilio']

    columns_acv = coluns_acv_geral + coluns_acv_end

    # FCI
    selected_columns_fci = ["co_fat_cidadao_pec","co_dim_tempo","nu_uuid_ficha","co_dim_raca_cor","nu_micro_area",'st_comunidade_tradicional']


    # FAOI
    columns_fao = ['co_fat_cidadao_pec','co_dim_tempo',"nu_altura","nu_peso",'co_dim_cbo_1','co_dim_cbo_2',
                'co_seq_fat_atd_odnt','ds_filtro_procedimentos','co_dim_tipo_consulta', 'st_conduta_tratamento_concluid','st_paciente_necessidades_espec','st_gestante']



    tb_pessoa = ler_dados_raw("tb_acomp_cidadaos_vinculados.parquet",columns_acv)

    #fci = pl.read_parquet(caminho_pasta+"tb_fat_cad_individual.parquet", columns=selected_columns_fci)
    fci = ler_dados_raw("tb_fat_cad_individual.parquet",selected_columns_fci)
    fci = fci.rename({"nu_micro_area" : "nu_micro_area_fci"})

    fao = ler_dados_raw("tb_fat_atendimento_odonto.parquet", columns_fao)

    tb_dim_equipe = ler_dados_raw("tb_dim_equipe.parquet")

    tb_dim_und_saude = ler_dados_raw("tb_dim_unidade_saude.parquet")


    dim_raca_cor = ler_dados_raw("tb_dim_raca_cor.parquet")
    dim_raca_cor = dim_raca_cor.rename({"co_seq_dim_raca_cor" : "co_dim_raca_cor"}).select("co_dim_raca_cor","ds_raca_cor")

    fci = fci.join(dim_raca_cor,on="co_dim_raca_cor",how='left')


    coluns_cbo = ['nu_cbo','co_seq_dim_cbo']

    dim_cbo = ler_dados_raw("tb_dim_cbo.parquet", coluns_cbo)


    dim_cbo = dim_cbo.with_columns(pl.col("co_seq_dim_cbo").cast(pl.Int64))



    fci = (
        fci
        .with_columns(
            pl.when(pl.col("st_comunidade_tradicional") == 1)
                .then(pl.lit("Sim"))
                .when(pl.col("st_comunidade_tradicional") == 0)
                .then(pl.lit("Não"))
                .otherwise(pl.lit(None))
                .alias("st_comunidade_tradicional")
        )

    )


    tb_pessoa = (
        tb_pessoa
        .with_columns(
            pl.when(pl.col("tp_identidade_genero_cidadao") == "HOMEM_CIS").then(pl.lit("Homem cisgênero"))
            .when(pl.col("tp_identidade_genero_cidadao") == "MULHER_CIS").then(pl.lit("Mulher cisgênero"))
            .when(pl.col("tp_identidade_genero_cidadao") == "HOMEM_TRANS").then(pl.lit("Homem transgênero"))
            .when(pl.col("tp_identidade_genero_cidadao") == "MULHER_TRANS").then(pl.lit("Mulher transgênero"))
            .when(pl.col("tp_identidade_genero_cidadao") == "TRAVESTI").then(pl.lit("Travesti"))
            .when(pl.col("tp_identidade_genero_cidadao") == "NAO_BINARIO").then(pl.lit("Não-binário"))
            .when(pl.col("tp_identidade_genero_cidadao") == "OUTRO_IDENTIDADE_GENERO").then(pl.lit("Outra"))
            .otherwise(pl.lit(None))  
            .alias("tp_identidade_genero_cidadao")
        )  
    )


    # ## Passo 5. Criar variáveis de tempo de acordo com Indicadores

    # In[78]:


    dt_24meses = datetime.today() - relativedelta(months=24)
    dt_30meses = datetime.today() - relativedelta(months=30)

    def calcular_data(meses: int):
        return datetime.today() - relativedelta(months=meses)


    # ## Passo 6. Filtrar os códigos de profissionais, exames ou condições de saúde dos Indicadores


    # AJUSTE de CBO

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


    # ## Passo 7. Manipular dados conforme necessidades dos Indicadores

    # ### Manipulando dados comuns aos indicadores

    # In[81]:


    fao_v2 = (
        fao
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))


    fao_vars = (
        fao_v2
        .filter(pl.col("dt_atendimento") >= dt_30meses)
        .select("co_fat_cidadao_pec", "st_paciente_necessidades_espec", "st_gestante", "dt_atendimento")
        .sort("dt_atendimento", descending=True)
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("st_paciente_necessidades_espec").first().alias("st_paciente_necessidades_espec"),
            pl.col("st_gestante").first().alias("st_gestante"),
        )
        .with_columns(
            pl.when(pl.col("st_gestante") == 1)
                .then(pl.lit("Sim"))
                .when(pl.col("st_gestante") == 0)
                .then(pl.lit("Não"))
                .otherwise(pl.lit("Sem Informação"))
                .alias("st_gestante"),

            pl.when(pl.col("st_paciente_necessidades_espec") == 1)
                .then(pl.lit("Sim"))
                .when(pl.col("st_paciente_necessidades_espec") == 0)
                .then(pl.lit("Não"))
                .otherwise(pl.lit("Sem Informação"))
                .alias("st_paciente_necessidades_espec"),
        )
    )


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
            pl.col("ds_raca_cor").first().alias("ds_raca_cor"),
        ])
    )


    fci_v2 = fci.select("co_fat_cidadao_pec","nu_uuid_ficha","nu_micro_area_fci","st_comunidade_tradicional")


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
    ).join(
        fao_vars, #capturar st_paciente_necessidades_espec e st_gestante
        on="co_fat_cidadao_pec",
        how="left"
    )



    # removendo co_fat_cidadao_pec duplicados priorizando chave, depois data, depois variável inteira

    tb_pessoa_v2 = tb_pessoa_v2.sort(
        by=["co_fat_cidadao_pec", "dt_ultima_atualizacao_cidadao", "co_seq_acomp_cidadaos_vinc"],  
        descending=[False, True, True]             
    ).unique(
        subset="co_fat_cidadao_pec",                            
        keep="first"                              
    )

    # criando dt_atendimento para FAO, usada em mais de um indicador, e filtrando cidadaos não nulos





    # In[82]:


    today = date.today()

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
                pl.date(pl.col("dt_nasc_cidadao").dt.year(), today.month, today.day) >= pl.col("dt_nasc_cidadao")
            )
            .then(today.year - pl.col("dt_nasc_cidadao").dt.year())
            .otherwise(today.year - pl.col("dt_nasc_cidadao").dt.year() - 1).alias("idade_anos_int"),


            # Cálculo da idade em dias
            (pl.lit(today) - pl.col("dt_nasc_cidadao"))
            .dt.total_days()
            .alias("idade_dias"),

            # Cálculo da idade em meses (total aproximado, levando em conta o dia do mês)
            pl.when(pl.col("dt_nasc_cidadao").dt.day() > today.day)
            .then(
                (today.year - pl.col("dt_nasc_cidadao").dt.year()) * 12
                + today.month
                - pl.col("dt_nasc_cidadao").dt.month()
                - 1
            )
            .otherwise(
                (today.year - pl.col("dt_nasc_cidadao").dt.year()) * 12
                + today.month
                - pl.col("dt_nasc_cidadao").dt.month()
            )
            .alias("idade_meses_completos"), # Meses completos considerando o dia

            # Cálculo da idade em anos (total completo)
            pl.when(
                pl.date(pl.col("dt_nasc_cidadao").dt.year(), today.month, today.day)
                >= pl.col("dt_nasc_cidadao")
            )
            .then(today.year - pl.col("dt_nasc_cidadao").dt.year())
            .otherwise(today.year - pl.col("dt_nasc_cidadao").dt.year() - 1)
            .alias("idade_anos_completos"),
        )
        .with_columns(
            # Coluna final 'idade', incluindo todas as possibilidades
            pl.when(pl.col("idade_dias") < 30) # Aproximadamente 1 mês
                .then(
                    pl.format("{} dias", pl.col("idade_dias"))
                )
            .when(pl.col("idade_anos_completos") < 1) # Menor de 1 ano completo
                .then(
                    pl.format("{} meses", pl.col("idade_meses_completos"))
                )
            .otherwise( # A partir de 1 ano completo
                pl.format("{} ano(s)", pl.col("idade_anos_completos"))
            )
            .alias("idade")
        )
        #.drop("idade_dias", "idade_meses_completos", "idade_anos_completos","idade_aux")
    )
    #print(tb_pessoa_v2["idade"].head(4))


    # In[83]:


    tb_pessoa_odonto = (
        tb_pessoa_v2
        .join(
            fao_v2
            .filter(pl.col("dt_atendimento") >= dt_30meses)
            .group_by("co_fat_cidadao_pec")
            .agg(
                pl.col("dt_atendimento").max().alias("dt_ultimo_atendimento"),
            ),
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.when((pl.col("dt_ultimo_atendimento") >= dt_30meses) & pl.col("dt_ultimo_atendimento").is_not_null())
            .then(1).otherwise(0).cast(pl.Int8).alias("atendimento_odonto"),
            pl.when((pl.col("dt_ultima_fci") >= dt_30meses) & pl.col("dt_ultima_fci").is_not_null())
            .then(1).otherwise(0).cast(pl.Int8).alias("cadastradas_odonto")
        )
    ).filter(  (pl.col("atendimento_odonto") == 1) |  (pl.col("cadastradas_odonto") == 1  ) )
    #.select("co_fat_cidadao_pec","cadastradas_odonto","atendimento_odonto")

    # OBS.: populações de cidadãos presentes na tabela de acompanhamento e vínculo e que são:

    # pessoas atendidas de interesse = pessoas atendidas nos últimos 2 anos (aqui ainda 30 meses): atendimento_odonto == 1
    # pessoas cadastradas de interesse = pessoas cadastradas com cadastro atualizado nos últimos 2 anos (aqui ainda 30 meses): 
    # cadastradas_odonto == 1


    # In[84]:


    tb_pessoa_odonto_populacao = tb_pessoa_odonto.select("co_fat_cidadao_pec","cadastradas_odonto","atendimento_odonto")


    fao_v3 = (
        fao_v2
        .join(
            tb_pessoa_odonto_populacao,
            on="co_fat_cidadao_pec",
            how="left"
        )
    ).with_columns(
        pl.col("cadastradas_odonto").fill_null(0),
        pl.col("atendimento_odonto").fill_null(0),
    )


    # ## PARTE I: PESSOAS ATENDIDAS

    # #### Total de pessoas atendidas - Dashboard

    # In[85]:


    # pessoas atendidas nos últimos 2 anos: atendimento_odonto == 1

    atendidas = (
            tb_pessoa_odonto
            .filter(pl.col("atendimento_odonto") == 1)
            .filter(pl.col("dt_ultimo_atendimento") >= dt_24meses)
            .group_by("co_fat_cidadao_pec")
            .agg()
            )
    #print(atendidas)
    #atendidas.height


    # #### Total de pessoas atendidas segundo sexo - Dashboard

    # In[86]:


    categorias_validas_sexo = ["MASCULINO", "FEMININO", "INDETERMINADO"]

    tb_pessoa_odonto = tb_pessoa_odonto.with_columns(
        pl.when(pl.col("no_sexo_cidadao").str.to_uppercase().is_in(categorias_validas_sexo))
        .then(pl.col("no_sexo_cidadao").str.to_uppercase())  # Mantém e padroniza para maiúsculas
        .otherwise(pl.lit("NÃO INFORMADO"))  # Substitui valores inválidos
        .alias("no_sexo_cidadao")  # Atualiza a coluna original
    )


    # #### Total de pessoas atendidas segundo raça/cor - Dashboard

    # In[87]:


    categorias_validas = ["Branca", "Preta", "Amarela", "Parda", "Indígena"]

    tb_pessoa_odonto = tb_pessoa_odonto.with_columns(
        pl.when(pl.col("ds_raca_cor").is_in(categorias_validas))
            .then(pl.col("ds_raca_cor"))  # Mantém o valor original se for válido
            .otherwise(pl.lit("NÃO INFORMADO"))  # Substitui valores inválidos
            .alias("ds_raca_cor")  # Atualiza a coluna original
    )


    # #### Total de pessoas atendidas segundo faixa etária - Dashboard

    # In[88]:


    tb_pessoa_odonto = (tb_pessoa_odonto
        .with_columns(
        pl.when((pl.col("idade_anos_completos") >= 0) & (pl.col("idade_anos_completos") <= 1)).then(pl.lit("0a1"))
        .when((pl.col("idade_anos_completos") >= 1) & (pl.col("idade_anos_completos") <= 4)).then(pl.lit("1a4"))
        .when((pl.col("idade_anos_completos") >= 5) & (pl.col("idade_anos_completos") <= 9)).then(pl.lit("5a9"))
        .when((pl.col("idade_anos_completos") >= 10) & (pl.col("idade_anos_completos") <= 14)).then(pl.lit("10a14"))
        .when((pl.col("idade_anos_completos") >= 15) & (pl.col("idade_anos_completos") <= 19)).then(pl.lit("15a19"))
        .when((pl.col("idade_anos_completos") >= 20) & (pl.col("idade_anos_completos") <= 29)).then(pl.lit("20a29"))
        .when((pl.col("idade_anos_completos") >= 30) & (pl.col("idade_anos_completos") <= 39)).then(pl.lit("30a39"))
        .when((pl.col("idade_anos_completos") >= 40) & (pl.col("idade_anos_completos") <= 49)).then(pl.lit("40a49"))
        .when((pl.col("idade_anos_completos") >= 50) & (pl.col("idade_anos_completos") <= 59)).then(pl.lit("50a59"))
        .when((pl.col("idade_anos_completos") >= 60) & (pl.col("idade_anos_completos") <= 69)).then(pl.lit("60a69"))
        .when((pl.col("idade_anos_completos") >= 70) & (pl.col("idade_anos_completos") <= 79)).then(pl.lit("70a79"))
        .when(pl.col("idade_anos_completos") >= 80).then(pl.lit("80mais"))
        .otherwise(pl.lit("idade_invalida"))
        .alias("faixa_etaria")
    )
    )


    # #### **Indicador I** - Pessoas atendidas que realizaram a primeira consulta odontológica programática
    # 
    # 
    # #### Card da Lista Nominal: Exibir a data da 1ª consulta ou se não tiver realizado nenhuma consulta colocar um hífen
    # 

    # In[89]:


    indicador_primeira_consulta_at = (
        fao_v3
        .filter(
            (pl.col("atendimento_odonto") == 1) &
            (pl.col("co_dim_tipo_consulta") == 1) &
            (pl.col("dt_atendimento") >= dt_30meses) & 
            (
                (pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V) | 
                (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V)))
            )
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento")
            .max().alias("dt_primeira_consulta_programatica")
        )
        .with_columns(
            # Cria o indicador binário (1 = tem primeira consulta, 0 = não tem = alerta)
            pl.when(
                pl.col("dt_primeira_consulta_programatica").is_not_null() & 
                (pl.col("dt_primeira_consulta_programatica")>= dt_24meses))
                .then(1)
                .otherwise(0)
                .cast(pl.Int8)
                .alias("agg_primeira_consulta_atendidas"),

            # Formata a data ou coloca "-" se não existir
            pl.when(
                pl.col("dt_primeira_consulta_programatica").is_not_null() &
                (pl.col("dt_primeira_consulta_programatica")>= dt_30meses)
                )   
                .then(pl.col("dt_primeira_consulta_programatica"))
                .otherwise(pl.lit(None))
                .alias("dt_primeira_consulta_atendidas"),
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_primeira_consulta_atendidas",
            "dt_primeira_consulta_atendidas"
        ])
    )


    # #### Indicador I e Itens da **Lista nominal** do Indicador I no df **"tb_pessoa_odonto_final"**:  
    # #### *A saber:*
    # ##### Número de cidadãos atendidos pela Equipe de Saúde Bucal que realizaram a primeira consulta odontológica nos últimos 2 anos: **'agg_primeira_consulta'= 1**
    # ##### - data da primeira consulta odontológica programática (**"dt_primeira_consulta_atendidas"**) ou "-" se ausente

    # In[90]:


    atendidas = (
        atendidas
        .join(
            indicador_primeira_consulta_at,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_primeira_consulta_atendidas").fill_null(0),
            #pl.col("dt_primeira_consulta_atendidas").fill_null("-")
        )
    )


    # In[91]:


    #print(atendidas["agg_primeira_consulta_atendidas"].value_counts())


    # ### **Indicador II** -  Pessoas atendidas que concluíram o tratamento odontológico - Dashboard
    # 
    # ### Card da Lista Nominal: Exibir a data da conclusão do tratamento ou se não tiver finalizado colocar um hífen

    # In[92]:


    tratamento_odontologico_concluido_at = (
        fao_v3
        .filter(
            ((pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V)) |
            (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V))) &
            (pl.col("atendimento_odonto") == 1) &
            (pl.col("dt_atendimento") >= dt_30meses) & 
            (pl.col("st_conduta_tratamento_concluid") == 1)
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento")
            .max().alias("dt_tratamento_concluido_atendidas")
        )
        .with_columns(
            pl.when(
                (pl.col("dt_tratamento_concluido_atendidas") >= dt_24meses)
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("agg_tratamento_odonto_concluido_atendidas"),

        # pl.coalesce(
        #     pl.col("dt_tratamento_concluido_atendidas"),
        #     pl.lit("-")
        # ).alias("dt_tratamento_concluido_atendidas")
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_tratamento_odonto_concluido_atendidas",
            "dt_tratamento_concluido_atendidas"
        ])
    )


    # In[93]:


    #tratamento_odontologico_concluido_at["dt_tratamento_concluido_atendidas"].describe()


    # #### **Indicador II** e Itens da **Lista nominal** do Indicador II no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber:*
    # ##### Número de cidadãos atendidos pela Equipe de Saúde Bucal que tiveram o tratamento concluído nos últimos 2 anos **"agg_tratamento_odonto_concluido_atendidas" = 1**
    # 
    # ##### - Exibir a data da conclusão do tratamento ou se não tiver finalizado colocar um hífen: **"dt_tratamento_concluido_atendidas**

    # In[94]:


    atendidas = (
        atendidas
        .join(
            tratamento_odontologico_concluido_at,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_tratamento_odonto_concluido_atendidas").fill_null(0)
        )
    )


    # In[95]:


    #atendidas["agg_tratamento_odonto_concluido_atendidas"].value_counts()


    # ### **Indicador III** - Proporção de pessoas atendidas que realizaram exodontia - Dashboard
    # 
    # ### Card da Nominal: Exibir quantidade de exodontias realizadas

    # In[96]:


    import re
    codigos_procurados = ["0414020138", "0414020146"]

    codigos_escaped = [re.escape(codigo) for codigo in codigos_procurados]
    regex_pattern = rf"\|({'|'.join(codigos_procurados)})\|"


    # In[97]:


    tb_pessoa_odonto_exodontia_at = (
        fao_v3
        .filter(
            ((pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V)) |
            (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V))) &
            (pl.col("atendimento_odonto") == 1) & 
            (pl.col("dt_atendimento") >= dt_30meses) & 
            (pl.col("ds_filtro_procedimentos").str.contains(r"\|0414020138|0414020146\|")    )
        )
        .with_columns(

            pl.lit(1).alias("total_exodontia_atendidas_30"),

            pl.when(
                    (pl.col("dt_atendimento") >= dt_24meses)  
            )
            .then(1)
            .otherwise(0)
            .alias("agg_realizaram_exodontia_atendidas_aux")

        )
        .group_by("co_fat_cidadao_pec")
        .agg(

            pl.col("dt_atendimento").max().alias("dt_max_exodontia"),

            pl.col("total_exodontia_atendidas_30").sum().alias("total_exodontia_atendidas"),

            pl.max("agg_realizaram_exodontia_atendidas_aux").alias("agg_realizaram_exodontia_atendidas")
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_realizaram_exodontia_atendidas",

            "total_exodontia_atendidas" # 30meses
        ])
    )


    # In[98]:


    #tb_pessoa_odonto_exodontia_at["agg_realizaram_exodontia_atendidas"].value_counts()


    # In[99]:


    #tb_pessoa_odonto_exodontia_at["total_exodontia_atendidas"].value_counts()


    # In[100]:


    #tb_pessoa_odonto_exodontia_at["agg_realizaram_exodontia_atendidas"].value_counts()


    # #### **Indicador III** e Itens da **Lista nominal** do Indicador III no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de  cidadãos atendidos pela Equipe de Saúde Bucal que realizaram exodontia nos últimos 2 anos: **"agg_realizaram_exodontia_atendidas" = 1**
    # 
    # ##### Exibir a quantidade de exodontias realizadas: **"total_exodontia_atendidas"**

    # In[101]:


    atendidas = (
        atendidas
        .join(
            tb_pessoa_odonto_exodontia_at,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_realizaram_exodontia_atendidas").fill_null(0),
            pl.col("total_exodontia_atendidas").fill_null(0)
        )
    )


    # ### **Indicador IV** - Pessoas atendidas que realizaram procedimentos preventivos - Dashboard
    # 
    # ### Card Lista Nominal:  Exibir a descrição do procedimento realizado conforme o SIGTAP ou se não tiver realizado nenhum procedimento colocar um hífen

    # In[102]:


    # Dicionário de códigos para descrições
    dict_procedimentos = {
        '0101020058': 'Aplicação de cariostático (por dente)',
        '0101020066': 'Aplicação de selante (por dente)',
        '0101020074': 'Aplicação tópica de flúor (individual por sessão)',
        '0101020082': 'Evidenciação de placa bacteriana',
        '0101020090': 'Selamento',
        '0101020104': 'Orientação de higiene bucal'
    }

    procedimentos_preventivos_regex = r"\|(" + "|".join(dict_procedimentos.keys()) + r")\|"

    def extrair_procedimentos(texto: str, substituir_por_descricao: bool = False) -> str | None:

        #import re
        codigos = re.findall(procedimentos_preventivos_regex, texto)

        if not codigos:
            return None

        if substituir_por_descricao:
            descricoes = {dict_procedimentos.get(codigo, codigo) for codigo in codigos}
            return "|".join(descricoes)
        else:
            codigos_unicos = set(codigos)
            return "|".join(codigos_unicos)

    def extrair_codigos(texto: str) -> str | None:
        return extrair_procedimentos(texto, substituir_por_descricao=False)

    def extrair_descricoes(texto: str) -> str | None:
        return extrair_procedimentos(texto, substituir_por_descricao=True)



    indicador_procedimentos_preventivos_at = (
        fao_v3
        .filter(
            (pl.col("atendimento_odonto") == 1) &
            (pl.col("dt_atendimento") >= dt_30meses) &
            (pl.col("ds_filtro_procedimentos").str.contains(procedimentos_preventivos_regex)) &
            (
                (pl.col("co_dim_cbo_1").is_in(cbos_odonto_IV_VI) | 
                (pl.col("co_dim_cbo_2").is_in(cbos_odonto_IV_VI))
            )
        ))
        .with_columns(
            ((pl.col("dt_atendimento") >= dt_24meses)
            ).cast(pl.Int8).alias("agg_procedimentos_preventivos_atendidas")
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("agg_procedimentos_preventivos_atendidas").alias("agg_procedimentos_preventivos_atendidas"),
            pl.col("ds_filtro_procedimentos").str.concat("|").alias("todos_procedimentos")
        )
        .with_columns(
            pl.col("todos_procedimentos")
            .map_elements(extrair_codigos, return_dtype=pl.Utf8)
            .alias("codigos_procedimentos_preventivos_atendidas"),
        )
        .with_columns(
            pl.col("todos_procedimentos")
            .map_elements(extrair_descricoes, return_dtype=pl.Utf8)
            .alias("descricao_procedimentos_preventivos_atendidas"),
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_procedimentos_preventivos_atendidas",
            "codigos_procedimentos_preventivos_atendidas",
            "descricao_procedimentos_preventivos_atendidas"
        ])
    )


    # In[103]:


    #print(indicador_procedimentos_preventivos_at["agg_procedimentos_preventivos_atendidas"].value_counts())


    # In[104]:


    #print(indicador_procedimentos_preventivos_at["codigos_procedimentos_preventivos_atendidas"].value_counts())


    # In[105]:


    #print(indicador_procedimentos_preventivos_at["descricao_procedimentos_preventivos_atendidas"].value_counts())


    # #### **Indicador IV** e Itens da **Lista nominal** do Indicador IV no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de cidadãos atendidos pela Equipe de Saúde Bucal que realizaram procedimentos preventivos nos últimos 2 anos : **"agg_procedimentos_preventivos_atendidas" = 1**
    # 
    # ##### - Exibir a descrição (e código) do procedimento realizado conforme o SIGTAP ou se não tiver realizado nenhum procedimento colocar um hífen **"codigos_preventivos_atendidas"**, **"procedimentos_preventivos_atendidas"**

    # In[106]:


    atendidas = (
        atendidas
        .join(
            indicador_procedimentos_preventivos_at,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_procedimentos_preventivos_atendidas").fill_null(0),
            pl.col("codigos_procedimentos_preventivos_atendidas").fill_null(0),
            pl.col("descricao_procedimentos_preventivos_atendidas").fill_null(0)
        )
    )


    # In[107]:


   # print(atendidas["codigos_procedimentos_preventivos_atendidas"].len())


    # In[108]:


    #print(atendidas["descricao_procedimentos_preventivos_atendidas"].len())


    # In[109]:


    #print(atendidas["agg_procedimentos_preventivos_atendidas"].value_counts())


    # ### **Indicador V** - Pessoas atendidas que realizaram tratamento restaurador atraumático (TRA) - Dashboard
    # 
    # ### Lista Nominal: Exibir a data do último procedimento ou se não tiver realizado colocar um hífen

    # In[110]:


    tb_pessoa_odonto_TRA_at = (
        fao_v3
        .filter(
            ((pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V)) |
            (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V))) &
            (pl.col("atendimento_odonto") == 1) & 
        ( pl.col("ds_filtro_procedimentos").str.contains("0307010074") ) &
            (pl.col("dt_atendimento") >= dt_30meses)
        )
        .with_columns(

            pl.when(
                    (pl.col("ds_filtro_procedimentos").str.contains("0307010074")) &
                    (pl.col("dt_atendimento") >= dt_24meses) 
            )
            .then(1)
            .otherwise(0)
            .alias("n_TRA_atendidas")


        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento").max().alias("dt_TRA_atendidas"),
            pl.col("n_TRA_atendidas").sum().alias("sum_TRA_atendidas")
        )
        .with_columns(

        )
        .with_columns(
            pl.when(
                (pl.col("sum_TRA_atendidas") >= 0 )
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("agg_TRA_atendidas")
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_TRA_atendidas",
            "dt_TRA_atendidas"
        ])
    )


    # In[111]:


    #print(tb_pessoa_odonto_TRA_at["agg_TRA_atendidas"].value_counts())


    # In[112]:


    #print(tb_pessoa_odonto_TRA_at["dt_TRA_atendidas"].value_counts())


    # #### **Indicador V** e Itens da **Lista nominal** do Indicador V no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de cidadãos atendidos pela Equipe de Saúde Bucal que realizaram tratamento restaurador atraumático (TRA) nos últimos 2 anos: **"agg_tratamento_restaurador_atendidas" = 1**
    # 
    # ##### - Exibir a data do último procedimento ou se não tiver realizado colocar um hífen: **dt_tratamento_restaurador_atendidas**

    # In[113]:


    atendidas = (
        atendidas
        .join(
            tb_pessoa_odonto_TRA_at,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_TRA_atendidas").fill_null(0),
        )
    )


    # In[114]:


    #print(atendidas["agg_TRA_atendidas"].value_counts())


    # ### **Indicador VI** - Pessoas atendidas que realizaram escovação supervisionada em atividade coletiva - Dashboard
    # 
    # ### Card Lista Nominal: Exibir a data da realização ou se não tiver realizado colocar um hífen

    # In[115]:


    # ESTE INDICADOR NÃO SERÁ APRESENTADO NA PRIMEIRA VERSÃO, POIS NÃO USAREMOS A TABELA DE ATIVIDADE COLETIVA


    # #### **Indicador VI** e Itens da **Lista nominal** do Indicador VI no df **"pessoa_atendida_saude_bucal"**:
    # ##### *A saber*
    # #### Número de cidadãos atendidos pela Equipe de Saúde Bucal que realizaram escovação supervisionada em atividade coletiva nos últimos 2 anos: **"agg_escovacao_supervisionada_atendidas" = 1**
    # 
    # ##### - Exibir a data da realização ou se não tiver realizado colocar um hífen: **"dt_escovacao_supervisionada_atendidas"**

    # In[116]:


    # ESTE INDICADOR NÃO SERÁ APRESENTADO NA PRIMEIRA VERSÃO, POIS NÃO USAREMOS A TABELA DE ATIVIDADE COLETIVA


    # ## PARTE II - PESSOAS CADASTRADAS

    # ### Total de pessoas cadastradas

    # In[117]:


    #  pessoas cadastradas com cadastro atualizado nos últimos 2 anos: 
    # cadastradas_odonto == 1

    cadastradas = (
            tb_pessoa_odonto
            .filter(pl.col("cadastradas_odonto") == 1)
            .filter(pl.col("dt_ultima_fci") >= dt_24meses)
            .group_by("co_fat_cidadao_pec")
            .agg()
            ) 
    #print(atendidas)
    #cadastradas.height #4328


    # ### Total de pessoas cadastradas segundo sexo / raça cor / faixa etária

    # In[118]:


    cadastradas = (
        cadastradas
        .join(
            tb_pessoa_odonto.select("co_fat_cidadao_pec","no_sexo_cidadao","ds_raca_cor","faixa_etaria"),
            on="co_fat_cidadao_pec",
            how="left"
        )
    )


    # In[119]:


    #print(cadastradas["no_sexo_cidadao"].value_counts())


    # In[120]:


    #print(cadastradas["ds_raca_cor"].value_counts())


    # ### **Indicador I** - Pessoas cadastradas que realizaram a primeira consulta odontológica programática
    # 
    # 
    # ### Card da Lista Nominal: Exibir a data da 1ª consulta ou se não tiver realizado nenhuma consulta colocar um hífen

    # In[121]:


    indicador_primeira_consulta_cad = (
        fao_v3
        .filter(
            (pl.col("cadastradas_odonto") == 1) &
            (pl.col("co_dim_tipo_consulta") == 1) &
            (pl.col("dt_atendimento") >= dt_30meses) & 
            (
                (pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V) | 
                (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V)))
            )
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento")
            .max().alias("dt_primeira_consulta_programatica")
        )
        .with_columns(
            # Cria o indicador binário (1 = tem primeira consulta, 0 = não tem = alerta)
            pl.when(
                pl.col("dt_primeira_consulta_programatica").is_not_null() & 
                (pl.col("dt_primeira_consulta_programatica")>= dt_24meses))
                .then(1)
                .otherwise(0)
                .cast(pl.Int8)
                .alias("agg_primeira_consulta_cadastradas"),

            # Formata a data ou coloca "-" se não existir
            pl.when(
                pl.col("dt_primeira_consulta_programatica").is_not_null() &
                (pl.col("dt_primeira_consulta_programatica")>= dt_30meses)
                )   
                .then(pl.col("dt_primeira_consulta_programatica"))
                .otherwise(pl.lit(None))
                .alias("dt_primeira_consulta_cadastradas"),
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_primeira_consulta_cadastradas",
            "dt_primeira_consulta_cadastradas"
        ])
    )


    # In[122]:


    #indicador_primeira_consulta_cad.filter(pl.col("co_fat_cidadao_pec") == 281)


    # In[123]:


    #print(indicador_primeira_consulta_cad["dt_primeira_consulta_cadastradas"].describe())


    # #### Indicador I e Itens da **Lista nominal** do Indicador I no df **"tb_pessoa_odonto_final"**:  
    # #### *A saber:*
    # ##### Número de cidadãos cadastrados pela Equipe de Saúde Bucal que realizaram a primeira consulta odontológica nos últimos 2 anos: **'agg_cidadaos_cadastrados'= 1**
    # ##### - data da primeira consulta odontológica programática (**"dt_primeira_consulta_cadastradas"**) ou "-" se ausente

    # In[124]:


    cadastradas = (
        cadastradas
        .join(
            indicador_primeira_consulta_cad,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_primeira_consulta_cadastradas").fill_null(0),
        )
    )


    # In[125]:


    #cadastradas["agg_primeira_consulta_cadastradas"].value_counts()


    # ### **Indicador II** -  Pessoas cadastradas que concluíram o tratamento odontológico - Dashboard
    # 
    # ### Card da Lista Nominal: Exibir a data da conclusão do tratamento ou se não tiver finalizado colocar um hífen

    # In[126]:


    tratamento_odontologico_concluido_cad = (
        fao_v3
        .filter(
            ((pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V)) |
            (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V))) &
            (pl.col("dt_atendimento") >= dt_30meses) & 
            (pl.col("cadastradas_odonto") == 1) &
            (pl.col("st_conduta_tratamento_concluid") == 1)
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento")
            .max().alias("dt_tratamento_concluido_cadastradas")
        )
        .with_columns(
            pl.when(
                (pl.col("dt_tratamento_concluido_cadastradas") >= dt_24meses)
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("agg_tratamento_odonto_concluido_cadastradas"),

        )
        .select([
            "co_fat_cidadao_pec",
            "agg_tratamento_odonto_concluido_cadastradas",
            "dt_tratamento_concluido_cadastradas"
        ])
    )


    # In[127]:


    #tratamento_odontologico_concluido_cad["agg_tratamento_odonto_concluido_cadastradas"].value_counts()


    # In[128]:


    #tratamento_odontologico_concluido_cad["dt_tratamento_concluido_cadastradas"].describe()


    # #### **Indicador II** e Itens da **Lista nominal** do Indicador II no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber:*
    # ##### Número de cidadãos cadastrados pela Equipe de Saúde Bucal que tiveram o tratamento concluído nos últimos 2 anos **"agg_tratamento_concluido_cadastradas" = 1**
    # 
    # ##### - Exibir a data da conclusão do tratamento ou se não tiver finalizado colocar um hífen: **"dt_tratamento_concluido_cadastradas**

    # In[129]:


    cadastradas = (
        cadastradas
        .join(
            tratamento_odontologico_concluido_cad,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_tratamento_odonto_concluido_cadastradas").fill_null(0),
        )
    )


    # In[130]:


    #cadastradas["agg_tratamento_odonto_concluido_cadastradas"].value_counts()


    # ### **Indicador III** - Proporção de pessoas cadastradas que realizaram exodontia - Dashboard
    # 
    # ### Card da Nominal: Exibir quantidade de exodontias realizadas

    # In[131]:


    import re
    codigos_procurados = ["0414020138", "0414020146"]

    codigos_escaped = [re.escape(codigo) for codigo in codigos_procurados]
    regex_pattern = rf"\|({'|'.join(codigos_procurados)})\|"


    # In[132]:


    tb_pessoa_odonto_exodontia_cad = (
        fao_v3
        .filter(
            ((pl.col("co_dim_cbo_1").is_in(cbos_odonto_I_II_III_V)) |
            (pl.col("co_dim_cbo_2").is_in(cbos_odonto_I_II_III_V))) &
            (pl.col("cadastradas_odonto") == 1) & 
            (pl.col("dt_atendimento") >= dt_30meses) & 
            (pl.col("ds_filtro_procedimentos").str.contains(regex_pattern)    )
        )
        .with_columns(
            pl.when(
                pl.col("ds_filtro_procedimentos").str.contains(regex_pattern)
            )
            .then(1)
            .otherwise(0)
            .alias("total_exodontia_cadastradas_30"),

            pl.when(
                    (pl.col("ds_filtro_procedimentos").str.contains(regex_pattern)) &
                    (pl.col("dt_atendimento") >= dt_24meses)  
            )
            .then(1)
            .otherwise(0)
            .alias("total_exodontia_cadastradas_24")

        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("total_exodontia_cadastradas_30").sum().alias("total_exodontia_cadastradas"),
            pl.col("total_exodontia_cadastradas_24").sum().alias("sum_total_exodontia_cadastradas_24")
        )
        .with_columns(
            pl.when(
                (pl.col("sum_total_exodontia_cadastradas_24") > 0)
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("agg_realizaram_exodontia_cadastradas")
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_realizaram_exodontia_cadastradas",
            "total_exodontia_cadastradas" # 30meses
        ])
    )


    # #### **Indicador III** e Itens da **Lista nominal** do Indicador III no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de  cidadãos cadastrados pela Equipe de Saúde Bucal que realizaram exodontia nos últimos 2 anos: **"agg_exodontia_cadastradas" = 1**
    # 
    # ##### Exibir a quantidade de exodontias realizadas: **"dt_exodontia_cadastradas"**

    # In[133]:


    cadastradas = (
        cadastradas
        .join(
            tb_pessoa_odonto_exodontia_cad,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            pl.col("agg_realizaram_exodontia_cadastradas").fill_null(0),
            pl.col("total_exodontia_cadastradas").fill_null(0)
        )
    )


    # In[134]:


    #cadastradas["agg_realizaram_exodontia_cadastradas"].value_counts()


    # ### **Indicador IV** - Pessoas cadastradas que realizaram procedimentos preventivos - Dashboard
    # 
    # ### Card Lista Nominal:  Exibir a descrição do procedimento realizado conforme o SIGTAP ou se não tiver realizado nenhum procedimento colocar um hífen

    # In[135]:


    ### dicionário de procedimentos e funções na etapa de "atendidas"

    indicador_procedimentos_preventivos_cad = (
        fao_v3
        .filter(
            (pl.col("cadastradas_odonto") == 1) &
            (pl.col("dt_atendimento") >= dt_30meses) &
            (pl.col("ds_filtro_procedimentos").str.contains(procedimentos_preventivos_regex)) &
            (
                (pl.col("co_dim_cbo_1").is_in(cbos_odonto_IV_VI) | 
                (pl.col("co_dim_cbo_2").is_in(cbos_odonto_IV_VI))
            )
        ))
        .with_columns(
            ((pl.col("dt_atendimento") >= dt_24meses)
            ).cast(pl.Int8).alias("agg_procedimentos_preventivos_cadastradas")
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("agg_procedimentos_preventivos_cadastradas").alias("agg_procedimentos_preventivos_cadastradas"),
            pl.col("ds_filtro_procedimentos").str.concat("|").alias("todos_procedimentos")
        )
        .with_columns(
            pl.col("todos_procedimentos")
            .map_elements(extrair_codigos, return_dtype=pl.Utf8)
            .alias("codigos_procedimentos_preventivos_cadastradas"),
        )
        .with_columns(
            pl.col("todos_procedimentos")
            .map_elements(extrair_descricoes, return_dtype=pl.Utf8)
            .alias("descricao_procedimentos_preventivos_cadastradas"),
        )
        .select([
            "co_fat_cidadao_pec",
            "agg_procedimentos_preventivos_cadastradas",
            "codigos_procedimentos_preventivos_cadastradas",
            "descricao_procedimentos_preventivos_cadastradas"
        ])
    )


    # In[136]:


    #print(indicador_procedimentos_preventivos_cad["codigos_procedimentos_preventivos_cadastradas"].value_counts())


    # In[137]:


    #print(indicador_procedimentos_preventivos_cad["descricao_procedimentos_preventivos_cadastradas"].value_counts())


    # In[138]:


    #print(indicador_procedimentos_preventivos_cad["agg_procedimentos_preventivos_cadastradas"].value_counts())


    # #### **Indicador IV** e Itens da **Lista nominal** do Indicador IV no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de cidadãos cadastrados pela Equipe de Saúde Bucal que realizaram procedimentos preventivos nos últimos 2 anos : **"agg_procedimentos_preventivos_cadastradas" = 1**
    # 
    # ##### - Exibir a descrição do procedimento realizado conforme o SIGTAP ou se não tiver realizado nenhum procedimento colocar um hífen **"procedimentos_preventivos_cadastradas**

    # In[139]:


    cadastradas = (
        cadastradas
        .join(
            indicador_procedimentos_preventivos_cad,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            #pl.col("agg_procedimentos_preventivos_cadastradas").fill_null(0),
            #pl.col("codigos_procedimentos_preventivos_cadastradas").fill_null(0),
            #pl.col("descricao_procedimentos_preventivos_cadastradas").fill_null(0)
        )
    )


    # ### **Indicador V** - Pessoas cadastradas que realizaram tratamento restaurador atraumático (TRA) - Dashboard
    # 
    # ### Lista Nominal: Exibir a data do último procedimento ou se não tiver realizado colocar um hífen

    # In[ ]:





    # In[140]:


    tb_pessoa_odonto_TRA_cad = (
        fao_v3
        .filter(
            ((pl.col("co_dim_cbo_1").cast(pl.Utf8).is_in(cbos_odonto_I_II_III_V)) |
            (pl.col("co_dim_cbo_2").cast(pl.Utf8).is_in(cbos_odonto_I_II_III_V))) &
            (pl.col("cadastradas_odonto") == 1) &
            ( pl.col("ds_filtro_procedimentos").str.contains("0307010074") ) &
            (pl.col("dt_atendimento") >= dt_30meses)
        )
        .with_columns(

            pl.when(
                    (pl.col("dt_atendimento") >= dt_24meses) 
            )
            .then(1)
            .otherwise(0)
            .alias("n_TRA_atendidas"),

        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("dt_atendimento").max().alias("dt_TRA_cadastradas"),
            pl.col("n_TRA_atendidas").sum().alias("sum_TRA_cad")
        )
        .with_columns(

            pl.when(
                (pl.col("sum_TRA_cad") >= 0 )
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("agg_TRA_cadastradas")

        )
        .select([
            "co_fat_cidadao_pec",
            "agg_TRA_cadastradas",
            "dt_TRA_cadastradas"
        ])
    )


    # #### **Indicador V** e Itens da **Lista nominal** do Indicador V no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de cidadãos cadastrados pela Equipe de Saúde Bucal que realizaram tratamento restaurador atraumático (TRA) nos últimos 2 anos: **"agg_tratamento_restaurador_cadastradas" = 1**
    # 
    # ##### - Exibir a data do último procedimento ou se não tiver realizado colocar um hífen: **dt_tratamento_restaurador_cadastradas**

    # In[141]:


    cadastradas = (
        cadastradas
        .join(
            tb_pessoa_odonto_TRA_cad,
            on="co_fat_cidadao_pec",
            how="left"
        )
        .with_columns(
            #pl.col("agg_TRA_cadastradas").fill_null(0),
        )
    )




    # In[142]:


    #cadastradas["agg_TRA_cadastradas"].value_counts()


    # ### **Indicador VI** - Pessoas cadastradas que realizaram escovação supervisionada em atividade coletiva - Dashboard
    # 
    # ### Card Lista Nominal: Exibir a data da realização ou se não tiver realizado colocar um hífen

    # In[143]:


    # ESTE INDICADOR NÃO SERÁ APRESENTADO NA PRIMEIRA VERSÃO, POIS NÃO USAREMOS A TABELA DE ATIVIDADE COLETIVA


    # #### **Indicador VI** e Itens da **Lista nominal** do Indicador VI no df **"tabela_pessoa_odonto_final"**:
    # ##### *A saber*
    # #### Número de cidadãos cadastrados pela Equipe de Saúde Bucal que realizaram escovação supervisionada em atividade coletiva nos últimos 2 anos: **"agg_escovacao_supervisionada_cadastradas" = 1**
    # 
    # ##### - Exibir a data da realização ou se não tiver realizado colocar um hífen: **"dt_escovacao_supervisionada_cadastradas"**

    # In[144]:


    # ESTE INDICADOR NÃO SERÁ APRESENTADO NA PRIMEIRA VERSÃO, POIS NÃO USAREMOS A TABELA DE ATIVIDADE COLETIVA


    # ## Passo 8. Criar tabela pessoa final com todas as variáveis necessárias para próximas etapas de desenvolvimento do Painel

    # In[145]:


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


    # In[146]:


    # adicionando informações cidadaos conforme prioridades entre tabelas

    tb_pessoa_odonto_final = (tb_pessoa_odonto
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
    )


    # In[147]:


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
    tb_pessoa_odonto_final = tb_pessoa_odonto_final.with_columns(expressoes)


    # In[148]:


    tb_pessoa_odonto_final = (
        tb_pessoa_odonto_final.join(
            cadastradas,
            on="co_fat_cidadao_pec",
            how="left"        
        )
        .join(
            atendidas,
            on="co_fat_cidadao_pec",
            how="left"        
        )
        .with_columns(
            pl.col("agg_primeira_consulta_atendidas").fill_null(0),
            pl.col("agg_tratamento_odonto_concluido_atendidas").fill_null(0),
            pl.col("agg_realizaram_exodontia_atendidas").fill_null(0),
            pl.col("total_exodontia_atendidas").fill_null(0),
            pl.col("agg_procedimentos_preventivos_atendidas").fill_null(0),
            #pl.col("codigos_procedimentos_preventivos_atendidas").fill_null(None),
            #pl.col("descricao_procedimentos_preventivos_atendidas").fill_null(None),
            pl.col("agg_TRA_atendidas").fill_null(0),
            pl.col("agg_primeira_consulta_cadastradas").fill_null(0),
            pl.col("agg_tratamento_odonto_concluido_cadastradas").fill_null(0),
            pl.col("agg_realizaram_exodontia_cadastradas").fill_null(0),
            pl.col("total_exodontia_cadastradas").fill_null(0),
            pl.col("agg_procedimentos_preventivos_cadastradas").fill_null(0),
            #pl.col("codigos_procedimentos_preventivos_cadastradas").fill_null(None),
            #pl.col("descricao_procedimentos_preventivos_cadastradas").fill_null(None),
            pl.col("agg_TRA_cadastradas").fill_null(0),        
        )

    )


    # In[149]:


    tb_pessoa_odonto_final = tb_pessoa_odonto_final.rename({
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
        'no_cidadao': 'cidadao',
        'no_sexo_cidadao': 'sexo',
        'no_municipio': 'municipio',
        'no_tipo_logradouro': 'tipo_logradouro',
        'no_bairro': 'bairro',

        # Novas renomeações adicionadas
        'st_registro_valido_equipe': 'status_registro_valido_equipe',
        'st_registro_valido_und_saude': 'status_registro_valido_unidade_saude',
        'co_dim_unidade_saude': 'codigo_unidade_saude',
        'co_fat_cidadao_pec': 'cidadao_pec',
        'co_unico_ultima_ficha': 'codigo_unico_ultima_ficha',
        'dt_nasc_cidadao': 'data_nascimento',
        'dt_ultima_atualizacao_cidadao': 'data_ultima_atualizacao_cidadao',
        'dt_ultima_fci': 'data_ultima_fci',
        'dt_tratamento_concluido_atendidas':'data_tratamento_concluido_atendidas',
        'dt_tratamento_concluido_cadastradas':'data_tratamento_concluido_cadastradas',
        'dt_primeira_consulta_atendidas': 'data_primeira_consulta_atendidas',
        'dt_primeira_consulta_cadastradas': 'data_primeira_consulta_cadastradas',
        'dt_TRA_atendidas':'data_TRA_atendidas',
        'dt_TRA_cadastradas':'data_TRA_cadastradas',
        'dt_ultimo_atendimento':'data_ultimo_atendimento'
    })


    # In[150]:


    # deixando variáveis em ordem alfabética
    #tabela_pessoa_odonto_final = tb_pessoa_odonto_final.select((tb_pessoa_odonto_final.columns))


    # In[151]:


    tabela_pessoa_odonto_final = (tb_pessoa_odonto_final
                        .select('agg_TRA_atendidas',
                                'agg_TRA_cadastradas',
                                'agg_primeira_consulta_atendidas',
                                'agg_primeira_consulta_cadastradas',
                                'agg_procedimentos_preventivos_atendidas',
                                'agg_procedimentos_preventivos_cadastradas',
                                'agg_realizaram_exodontia_atendidas',
                                'agg_realizaram_exodontia_cadastradas',
                                'agg_tratamento_odonto_concluido_atendidas',
                                'agg_tratamento_odonto_concluido_cadastradas',
                                'atendimento_odonto',
                                'bairro',
                                'cadastradas_odonto',
                                'cep',
                                'cidadao_pec',
                                'cns',
                                'cnes_equipe',
                                'codigo_unidade_saude',
                                'codigos_procedimentos_preventivos_atendidas',
                                'codigos_procedimentos_preventivos_cadastradas',
                                'co_seq_acomp_cidadaos_vinc',
                                'codigo_unico_ultima_ficha',
                                'codigo_equipe',
                                'complemento',
                                'cpf',
                                'data_TRA_atendidas',
                                'data_TRA_cadastradas',
                                'data_nascimento',
                                'data_primeira_consulta_atendidas',
                                'data_primeira_consulta_cadastradas',
                                'data_tratamento_concluido_atendidas',
                                'data_tratamento_concluido_cadastradas',
                                'data_ultima_atualizacao_cidadao',
                                'data_ultima_fci',
                                'data_ultimo_atendimento',
                                'descricao_procedimentos_preventivos_atendidas',
                                'descricao_procedimentos_preventivos_cadastradas',
                                'faixa_etaria',
                                'idade',
                                'ine_equipe',
                                'logradouro',
                                'micro_area',
                                'cidadao',
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
                                'total_exodontia_atendidas',
                                'total_exodontia_cadastradas',
                                'st_comunidade_tradicional',
                                'st_gestante',
                                'st_paciente_necessidades_espec',
                                'tp_identidade_genero_cidadao'
                            )
                        )


    escrever_dados_raw(tabela_pessoa_odonto_final,"saude_bucal.parquet")



