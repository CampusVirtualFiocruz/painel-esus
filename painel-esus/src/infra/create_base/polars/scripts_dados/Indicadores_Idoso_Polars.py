#!/usr/bin/env python
# coding: utf-8
# # Indicadores Idosos
#
# A tabela pessoa foi gerada a partir da tabela de acompanhamento do cidadão vinculado.O script realiza o cálculo de diversos indicadores baseados em nas fichas de atendimento individual e odontológico de população idosa. O processo inclui a leitura de dados, criação de filtros temporais e categóricos, cálculo de frequências de atendimentos e procedimentos (como creatinina e peso/altura), e geração de colunas de indicadores binários (1 ou 0). Esses indicadores são então integrados ao conjunto de dados final de idosos para análise posterior.
#
# usando a tabela pessoa gerada via sql do tales, script adaptado
# In[27]:
import time

from src.infra.db.settings.connection_local import DBConnectionHandler

start_time = time.time()


# In[28]:


import os
from datetime import datetime

import polars as pl
from dateutil.relativedelta import relativedelta


def gerar_banco():
    working_directory  = os.getcwd()
    input_path = os.path.join(working_directory, "dados", "input") 
    output_path = os.path.join(working_directory, "dados", "output")  


    tb_pessoa = pl.read_csv(input_path+os.sep+"pessoas.csv",separator=";",ignore_errors=True)
    tb_pessoa = tb_pessoa.with_columns(pl.col("cidadao_pec").cast(pl.Int64))

    fai = pl.read_parquet(input_path+os.sep+"tb_fat_atendimento_individual.parquet")

    fai = fai.with_columns(pl.col("co_fat_cidadao_pec").cast(pl.Int64) )

    fao = pl.read_parquet(input_path+os.sep+"tb_fat_atendimento_odonto.parquet")

    fat_vis_dom = pl.read_parquet(input_path+os.sep+"tb_fat_visita_domiciliar.parquet")

    faip = pl.read_parquet(input_path+os.sep+"fat_atd_ind_cod.parquet")

    tb_fat_vac = pl.read_parquet(input_path+os.sep+"tb_fat_vacinacao.parquet")


    dt_12meses = datetime.today() - relativedelta(months=12)
    # Define a data de hoje
    dt_hoje = datetime.today()

    ## Definir códigos para identificar médicos, enfermeiros e outros procedimentos
    medico_codigos = [476, 484, *range(636, 699), *range(785, 789)] # Códigos de médicos
    enfermeiro_codigos = [475, 479, 487, *range(627, 636), *range(782, 785)] # Códigos de enfermeiros
    creatinina = ["ABEX003", "0202010317"] # Códigos para creatinina
    cirurgiao_dentista = [485, 599] # Códigos de cirurgiões-dentistas


    # indicador 2 registro peso e altura
    # reusar o medicos_codigos e enfemerio_codigo do indicador 1
    tec_aux_enferm_cod = [483,*range(522, 525),*range(620, 626)]
    tec_age_comun_cod = [780]
    asc_cod = [488]
    cirur_den_cod = [485,599,*range(699, 720)]
    farma_cod = [*range(721, 727)]
    fisio_cod = [482,*range(727, 732),*range(796, 799)]
    prof_edu_fisic_cod = [738,776]
    terap_ocup_codi = [749]
    nutri_cod = [481]
    fonod_cod = [480,*range(732, 735),*range(799, 803)]
    antropometrica = ['0101040024']

    cods_ind_peso_altura = tec_aux_enferm_cod + tec_age_comun_cod+asc_cod+cirur_den_cod+farma_cod+fisio_cod + prof_edu_fisic_cod+terap_ocup_codi+nutri_cod+fonod_cod+medico_codigos+enfermeiro_codigos

    acs_tacs = [488, 780]

    idoso = tb_pessoa.filter(
        (pl.col("idade").cast(pl.Int32) >= 60)).rename({"cidadao_pec" : "co_fat_cidadao_pec"}).with_columns(pl.col("co_fat_cidadao_pec").cast(pl.Int64) ).select("co_fat_cidadao_pec")

    # Original operations with updated column names
    indicador_atendimentos_medicos = fai.select(
        ["co_fat_cidadao_pec", "co_dim_tempo", "co_dim_cbo_1", "co_dim_cbo_2"]
    ).with_columns(
        # Convert `co_dim_tempo` to datetime and create `dt_atendimento`
        pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
    ).with_columns(
        # Create `atd_med_enf` to check if atendimento is by doctors or nurses
        pl.when(
            (pl.col("co_dim_cbo_1").is_in(medico_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(medico_codigos)) |
            (pl.col("co_dim_cbo_1").is_in(enfermeiro_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(enfermeiro_codigos))
        ).then(1).otherwise(0).alias("atd_med_enf")
    ).filter(
        (pl.col("dt_atendimento") >= dt_12meses) &
        (pl.col("co_fat_cidadao_pec").is_not_null())
    ).group_by(
        "co_fat_cidadao_pec"
    ).agg([
        pl.len().alias("atendimentos"),  
        pl.col("atd_med_enf").sum().alias("num_med_enf_medicos"),  
        pl.col("dt_atendimento")                                      
        .filter(pl.col("atd_med_enf").sum() >= 2)              
        .max()                                           
        .alias("data_ultimo_atendimento_medicos"),
        
    ]).with_columns(
        pl.when(
                pl.col("atendimentos") < 2)
                .then(0)
                .when(
                    (pl.col("num_med_enf_medicos") >= 2)
                )
                .then(1)
                .otherwise(0)
                .alias("indicador_atendimentos_medicos")
    )

    # Step 4: Left join `idoso` with `indicador_atendimentos_medicos` and replace NA values
    idoso = idoso.join(
        indicador_atendimentos_medicos,
        on="co_fat_cidadao_pec",
        how="left"
    ).with_columns(
        # Replace missing values with 2 in `indicador_atendimentos_medicos`
        pl.col("indicador_atendimentos_medicos").fill_null(2),
    )



    faip_peso_altura = (
        faip.filter(pl.col("tipo") == "Procedimentos Avaliados").filter(pl.col("codigo").is_in(antropometrica))
            .unique(subset=["co_seq_fat_atd_ind"]) 
    )


    # Step 1: Process `fai` to create `indicador_medicoes_peso_altura`
    indicador_medicoes_peso_altura = fai.select(
        ["co_fat_cidadao_pec", "co_dim_tempo", "nu_peso", "nu_altura","co_dim_cbo_1","co_dim_cbo_2"]
    ).with_columns(
        # Convert `co_dim_tempo` to datetime and create `dt_atendimento`
        pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
    ).filter(
        # Filter to keep records within the last 12 months and valid citizen IDs
        (pl.col("dt_atendimento") >= dt_12meses) &
        (pl.col("co_fat_cidadao_pec").is_not_null()) & 
        (pl.col("co_dim_cbo_1").is_in(cods_ind_peso_altura)) | (pl.col("co_dim_cbo_2").is_in(cods_ind_peso_altura))
    ).group_by(
        "co_fat_cidadao_pec"
    ).agg([
        # Count where both `nu_peso` and `nu_altura` are not null
        (pl.col("nu_peso").is_not_null() & pl.col("nu_altura").is_not_null()).cast(pl.Int64).sum().alias("medicoes_peso_altura"),
        # Get the latest date of measurement
        pl.col("dt_atendimento")                                      
        .filter(pl.col("nu_peso").is_not_null() & pl.col("nu_altura").is_not_null())              
        .max()                                           
        .alias("data_ultima_medicao_peso_altura"),
    ]).with_columns(
        # Create `indicador_medicoes_peso_altura` column based on the count
        pl.when(pl.col("medicoes_peso_altura") >= 1).then(1).otherwise(0).alias("indicador_medicoes_peso_altura")
    )


    last_peso_altura = fai.select(
        ["co_fat_cidadao_pec", "co_dim_tempo", "nu_peso", "nu_altura","co_dim_cbo_1","co_dim_cbo_2"]
    ).with_columns(
        # Convert `co_dim_tempo` to datetime and create `dt_atendimento`
        pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
    ).filter(
        # Filter to keep records within the last 12 months and valid citizen IDs
        (pl.col("dt_atendimento") >= dt_12meses) &
        (pl.col("co_fat_cidadao_pec").is_not_null()) & 
        (pl.col("co_dim_cbo_1").is_in(cods_ind_peso_altura)) | (pl.col("co_dim_cbo_2").is_in(cods_ind_peso_altura)) &
        (pl.col("nu_peso").is_not_null() & pl.col("nu_altura").is_not_null() )
    ).sort("dt_atendimento",descending = True).group_by(
        "co_fat_cidadao_pec",maintain_order = True
    ).agg([
        pl.all().first()
    ]).with_columns(
        (pl.col("nu_peso") /  ( ( pl.col("nu_altura") / 100 ) ** 2) ).alias("imc")
    ).with_columns(
        pl.when(pl.col("nu_peso").is_null() | pl.col("nu_altura").is_null())
        .then(pl.lit("não informado"))
        .when(pl.col("imc") <= 22)
        .then(pl.lit("baixo peso"))
        .when((pl.col("imc") > 22) & (pl.col("imc") < 27))
        .then(pl.lit("normal"))
        .when(pl.col("imc") >= 27)
        .then(pl.lit("excesso de peso"))
        .otherwise(pl.lit("erro"))
        .alias("categoria_imc")
    ).select("co_fat_cidadao_pec","imc","categoria_imc")

    indicador_medicoes_peso_altura_v2 =  indicador_medicoes_peso_altura.join(
        last_peso_altura,
        on="co_fat_cidadao_pec",
        how ="left"
    )


    # Step 4: Left join `idoso` with `indicador_medicoes_peso_altura` and replace NA values
    idoso = idoso.join(
        indicador_medicoes_peso_altura_v2,
        on="co_fat_cidadao_pec",
        how="left"
    ).with_columns(
        # Replace missing values with 2 in `indicador_medicoes_peso_altura`
        pl.col("indicador_medicoes_peso_altura").fill_null(2),
        pl.col("categoria_imc").fill_null(pl.lit("não informado")),
    )


    filtro_prof_ind_3 = medico_codigos + enfermeiro_codigos + nutri_cod + farma_cod


    # Filter for rows where `codigo` is in `creatinina` and remove duplicates
    faip_creatina = (
        faip.filter(pl.col("codigo").is_in(creatinina))
            .unique(subset=["co_seq_fat_atd_ind"])  # Remove duplicates based on `co_seq_fat_atd_ind`
    )


    indicador_III = (
        fai.select(["co_seq_fat_atd_ind", "co_fat_cidadao_pec", "co_dim_tempo","co_dim_cbo_1","co_dim_cbo_2"])
        .with_columns([
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, format="%Y%m%d").alias("dt_atendimento")
        ])
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) & 
            (pl.col("co_dim_cbo_1").is_in(filtro_prof_ind_3)) | (pl.col("co_dim_cbo_2").is_in(filtro_prof_ind_3))  )
        .join(faip_creatina, on="co_seq_fat_atd_ind", how="left")
        .group_by("co_fat_cidadao_pec")
        .agg([
            # Calculate num_creatina_III
            (pl.col("codigo").is_not_null() & (pl.col("tipo") == "Procedimentos Avaliados")).sum().alias("num_creatina_III"),
            
            pl.col("dt_atendimento")                                      
            .filter( (pl.col("codigo").is_not_null() ) & (pl.col("tipo") == "Procedimentos Avaliados")  )              
            .max()                                           
            .alias("data_ultimo_registro_creatinina")
        ])
        # Now calculate indicador_III based on num_creatina_III
        .with_columns([
            pl.when(pl.col("num_creatina_III") >= 1).then(1).otherwise(0).alias("indicador_III")
        ])
    )


    # Final join with the `idoso` DataFrame
    idoso = (
        idoso.join(indicador_III, on="co_fat_cidadao_pec", how="left")
            .with_columns(pl.col("indicador_III").fill_null(2))  # Fill NA values with 2
    )



    indicador_IV = (
        fat_vis_dom
        .select([
            "co_seq_fat_visita_domiciliar", "co_fat_cidadao_pec", "dt_nascimento", "co_dim_tempo", "co_dim_cbo"
        ])
        .with_columns(
            # Converter `co_dim_tempo` para datetime e criar `dt_atendimento`
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("dt_atendimento") >= dt_12meses) &  # Filtrar atendimentos nos últimos 12 meses
            (pl.col("co_fat_cidadao_pec").is_not_null()) &  # Garantir que `co_fat_cidadao_pec` não seja nulo
            (pl.col("co_dim_cbo").is_in(acs_tacs))  # Filtrar pelos códigos ACS/TACS
        )
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.col("dt_atendimento").count().alias("n_atendimentos"),
            pl.col("dt_atendimento").sort().alias("sorted_dt_atendimento") , # Ordenar as datas de atendimento
            pl.min("dt_atendimento").alias("min_date"),
            pl.max("dt_atendimento").alias("max_date"),
            
            pl.col("dt_atendimento")                                      
            .filter( (pl.col("dt_atendimento").count() >= 2 ) & ( (pl.max("dt_atendimento") - pl.min("dt_atendimento") ).dt.total_days() >= 30 ) )              
            .max()                                           
            .alias("data_ultima_visita_domiciliar_acs")
            
        ])
        .with_columns(
            (pl.col("max_date") - pl.col("min_date")).dt.total_days().alias("diff_dias")
        )
        .with_columns(
            pl.when(
                (pl.col("n_atendimentos") >= 2) & 
                (pl.col("diff_dias") >= 30)
            )
            .then(1)
            .otherwise(0)
            .alias("indicador_visitas_domiciliares_acs"),
        )
        .with_columns(
            pl.when(
                (pl.col("indicador_visitas_domiciliares_acs") == 1)
            )
            .then("n_atendimentos")
            .otherwise(None)
            .alias("visitas_domiciliares_acs")
        )        

    ).select("co_fat_cidadao_pec","indicador_visitas_domiciliares_acs","visitas_domiciliares_acs","data_ultima_visita_domiciliar_acs")

    # Final join with the `idoso` DataFrame
    idoso = (
        idoso.join(indicador_IV, on="co_fat_cidadao_pec", how="left")
            .with_columns(pl.col("indicador_visitas_domiciliares_acs").fill_null(2))  # Fill NA values with 2
    )


    # Step 1: Select relevant columns and filter based on `ds_filtro_imunobiologico`
    fai_vac = (
        tb_fat_vac
        .select(["co_fat_cidadao_pec", "co_dim_tempo", "ds_filtro_imunobiologico"])
        .filter(
            pl.col("ds_filtro_imunobiologico").str.contains("33|77")  # Filter for codes "33" or "77"
        )
    )


    indicador_vacinas_influenza = (
        fai_vac
        .with_columns([
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("data_vacina")  # Cast to string and parse to date
        ])
        .filter(
            (pl.col("data_vacina") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) ) 
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.len().alias("vacinas_influenza"),  
            pl.col("data_vacina")                                      
            .filter(pl.len().alias("vacinas_influenza") >= 1)              
            .max()                                           
            .alias("data_ultima_vacina_influenza"),
        ]).with_columns(
            pl.when(
            ( pl.col("vacinas_influenza") >=  1)
            )
            .then(1)
            .otherwise(0)
            .alias("indicador_vacinas_influenza")
        )
    )

    idoso = (
        idoso
        .join(indicador_vacinas_influenza, on="co_fat_cidadao_pec", how="left")  # Left join with `idoso`
        .with_columns(
            pl.col("indicador_vacinas_influenza").fill_null(2)  # Set missing `indicador_vacinas_influenza` values to 2
        )
    )

    indicador_atendimento_odontologico = (
        fao
        .with_columns(  # Cast `co_fat_cidadao_pec` to String
            pl.col("co_fat_cidadao_pec").cast(pl.Utf8)
        )
        .select([
            "co_fat_cidadao_pec", "co_dim_tempo", "co_dim_cbo_1", "co_dim_cbo_2"
        ])
    .with_columns([
            # Cast `co_dim_tempo` to string and parse it to Date
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, format="%Y%m%d").alias("dt_atendimento")
        ])
        .filter(
            (pl.col("dt_atendimento") >= dt_12meses) &  # Filter by date
            pl.col("co_fat_cidadao_pec").is_not_null()  # Remove missing `co_fat_cidadao_pec`
        )
        .with_columns([
            # Indicate if the service was provided by a dentist
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cirur_den_cod)) |
                (pl.col("co_dim_cbo_2").is_in(cirur_den_cod))
            )
            .then(1)
            .otherwise(0)
            .alias("atd_cirurgiao_dentista")
        ])
        .group_by("co_fat_cidadao_pec")
        .agg([
            # Summarize the number of dentist visits
            pl.col("atd_cirurgiao_dentista").sum().alias("atendimentos_odontologicos"),
            
            # Get the latest date of dentist visits
            pl.col("dt_atendimento")                                      
            .filter(pl.col("atd_cirurgiao_dentista") >= 1)              
            .max()                                           
            .alias("data_ultimo_atendimento_odontologico")
            
        ])
        .with_columns([
            # Define `indicador_atendimento_odontologico` based on dentist visits
            pl.when(pl.col("atendimentos_odontologicos") >= 1).then(1).otherwise(0).alias("indicador_atendimento_odontologico")
        ])
    )


    # Step 4: Join with idoso DataFrame and replace NAs with 2
    idoso_updated = (
        idoso
        .with_columns([
            pl.col("co_fat_cidadao_pec").cast(pl.Utf8)  # Ensure idoso has String type for join
        ])
        .join(indicador_atendimento_odontologico, on="co_fat_cidadao_pec", how="left")  # Left join with idoso
        .with_columns([
            pl.col("indicador_atendimento_odontologico").fill_null(2),  # Replace NAs with 2
        ])
    )


    colunas_para_remover = ["atendimentos"]



    mapeamento_renomeacao = {
        "co_fat_cidadao_pec": "cidadao_pec",
        "num_med_enf_medicos": "atendimentos_medicos", #enfermeiros tbm esta aqui
        "num_creatina_III": "registros_creatinina",
        #"num_creatina_III": "registros_creatinina",
        "indicador_III": "indicador_registros_creatinina",
    }


    idoso_updated_v2 = (idoso_updated
                        .drop(colunas_para_remover)
                        .rename(mapeamento_renomeacao)
    )



    idoso_updated_v2.write_parquet(output_path + os.sep + "idoso.parquet")
    with DBConnectionHandler() as con:
        engine = con.get_engine()
        idoso_updated_v2.to_sql(name='idoso', con=engine, if_exists="append")
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Tempo total de execução idoso: {execution_time:.2f} segundos")

