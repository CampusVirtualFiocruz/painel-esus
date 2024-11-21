#!/usr/bin/env python
# coding: utf-8
# In[1]:
import os
import time

start_time = time.time()


# In[2]:


from datetime import datetime

import polars as pl
from dateutil.relativedelta import relativedelta

def gerar_banco():
    working_directory  = os.getcwd()
    input_path = os.path.join(working_directory, "dados", "input") 
    output_path = os.path.join(working_directory, "dados", "output")  
    print(os.path.join(working_directory, "dados", "input"))
    tb_pessoa = pl.read_csv(input_path + os.sep + "pessoas.csv", separator=";", ignore_errors=True)
    tb_pessoa = tb_pessoa.with_columns(pl.col("cidadao_pec").cast(pl.Int64))

    fai = pl.read_parquet(input_path + os.sep +"tb_fat_atendimento_individual.parquet")
    fai = fai.with_columns(pl.col("co_fat_cidadao_pec").cast(pl.Int64) )

    fao = pl.read_parquet(input_path + os.sep +"tb_fat_atendimento_odonto.parquet")


    faip = pl.read_parquet(input_path + os.sep +"fat_atd_ind_cod.parquet")

    fat_vis_dom = pl.read_parquet(input_path + os.sep +"tb_fat_visita_domiciliar.parquet")


    fat_vac = pl.read_parquet(input_path + os.sep +"tb_fat_vacinacao.parquet")

    fat_acomp_vinc = pl.read_parquet(input_path + os.sep +"tb_acomp_cidadaos_vinculados.parquet")


    faip = pl.read_parquet(input_path + os.sep +"fat_atd_ind_cod.parquet")
    faip = faip.with_columns(pl.col("co_seq_fat_atd_ind").cast(pl.Int64) )

    dt_12meses = datetime.today() - relativedelta(months=12)
    dt_hoje = datetime.today()

    medico_codigos = [476, 484, *range(636, 699), *range(785, 789)] # Códigos de médicos
    enfermeiro_codigos = [475, 479, 487, *range(627, 636), *range(782, 785)] # Códigos de enfermeiros

    pezinho = ['0201020050','ABEX021']

    codigos_dentista = [485, 599, *range(699, 720)] # Códigos de cirurgião dentista

    acs_crianca = [483, 488, 489,526, 557, 589, 606, 617, 618, 620, 621, 780, 781, *range(522, 525), *range(623, 626)] 


    cod_assistente_social = [477]
    cod_farma = [*range(721, 727)]
    fisio_cod = [482,*range(727, 732),*range(796, 799)]
    prof_edu_fisic_cod = [738,776]
    cod_terap_ocup = [749]
    cod_nutri = [481]
    fonod_cod = [480,*range(732, 735),*range(799, 803)]

    cod_psicologo = [478,499,545,736,*range(740, 747)]
    cirur_den_cod = [485,599,*range(699, 720)]

    todos_codigos = (
        medico_codigos +
        enfermeiro_codigos +
        fonod_cod +
        cod_psicologo +
        prof_edu_fisic_cod +
        cod_assistente_social +
        cod_terap_ocup +
        cod_farma +
        fisio_cod +
        cirur_den_cod +
        cod_nutri
    )


    crianca = tb_pessoa.filter(
        (pl.col("idade").cast(pl.Int32) <= 2)).rename({"cidadao_pec" : "co_fat_cidadao_pec"}).with_columns(pl.col("co_fat_cidadao_pec").cast(pl.Int64) ).select("co_fat_cidadao_pec")


    crianca_fai = fai.join(
        crianca.select('co_fat_cidadao_pec'),
        on="co_fat_cidadao_pec",
        how="inner"
    )


    indicador_I_e_II_III_V = crianca_fai.select(
            ["co_fat_cidadao_pec", "co_dim_tempo", "co_dim_cbo_1", "co_dim_cbo_2","dt_nascimento","nu_peso", "nu_altura","co_seq_fat_atd_ind"]
        ).with_columns(
            # Convert `co_dim_tempo` to datetime and create `dt_atendimento`
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
            pl.col("dt_nascimento").cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nascimento")
        ).filter(
        # (pl.col("dt_atendimento") >= dt_12meses) &
            (pl.col("co_fat_cidadao_pec").is_not_null())
        ).with_columns(
            (pl.col("dt_atendimento") - pl.col("dt_nascimento")).dt.total_days().alias("diff_dias"),
            pl.when(
                    (pl.col("co_dim_cbo_1").is_in(medico_codigos)) |
                    (pl.col("co_dim_cbo_2").is_in(medico_codigos)) |
                    (pl.col("co_dim_cbo_1").is_in(enfermeiro_codigos)) |
                    (pl.col("co_dim_cbo_2").is_in(enfermeiro_codigos))
            ).then(1).otherwise(0).alias("atd_med_enf"),

        
            pl.when( ( pl.col("nu_peso").is_not_null() ) & ( pl.col("nu_altura").is_not_null() ) )
            .then(1)
            .otherwise(0)
            .alias("medicoes_peso_altura")
        
        ).with_columns(
            pl.when( (pl.col("diff_dias") <= 8) & (pl.col("diff_dias") >= 0)  & (pl.col("atd_med_enf") == 1 ) )
            .then(1)
            .when( (pl.col("atd_med_enf").is_null() ) & (pl.col("diff_dias").is_null()) ) 
            .then(2)
            .otherwise(0)
            .alias("atd_8dias")
        )


    indicador_I = indicador_I_e_II_III_V.group_by(
            "co_fat_cidadao_pec"
        ).agg([
            pl.when( (pl.col("atd_8dias") == 1).any() )
            .then(1)
            .otherwise(0)
            .alias("indicador_atendimentos_medicos_enfermeiros"),
            pl.col("dt_atendimento"),
        
            pl.col("dt_atendimento")  
            .filter(pl.col("atd_8dias") >= 1)              
            .max()                                           
            .alias("data_ultimo_atendimento_medico_enfermeiro"),
            pl.col("atd_8dias").sum().alias("atendimentos_medicos_enfermeiros_8d_vida")
        ]).drop("dt_atendimento")

    indicador_II_III = (indicador_I_e_II_III_V
        .filter(pl.col("diff_dias") <= 729)
        )


    indicador_II =  ( indicador_II_III.group_by(
            "co_fat_cidadao_pec"
        ).agg([
        # pl.len().alias("num_atendimentos"),
            pl.col("atd_med_enf").sum().alias("atendimentos_medicos_enfermeiros_puericult"),
            pl.col("dt_atendimento")  
            .filter( (pl.col("atd_med_enf").sum() >= 9 ) )              
            .max()                                           
            .alias("data_ultimo_atendimento_medicos_enfermeiros_puericult")
        ]).with_columns(
            pl.when((pl.col("atendimentos_medicos_enfermeiros_puericult") >= 9 ) )
            .then(1)
            .otherwise(0)
            .alias("indicador_atendimentos_medicos_enfermeiros_puericult"),

        )
    )


    indicador_III = (indicador_II_III
        .group_by(
            "co_fat_cidadao_pec"
        ).agg([
            #pl.len().alias("num_atendimentos"),
            pl.col("medicoes_peso_altura").sum().alias("medicoes_peso_altura_ate2anos"),

            pl.col("dt_atendimento")  
            .filter( (pl.col("medicoes_peso_altura").sum() >= 9) & (pl.col("nu_peso").is_not_null() & pl.col("nu_altura").is_not_null() ) )               
            .max()                                           
            .alias("data_ultima_medicao_peso_altura_ate2anos"),
        ]).with_columns(
            pl.when( (pl.col("medicoes_peso_altura_ate2anos") >= 9)  )
            .then(1)
            .otherwise(0)
            .alias("indicador_medicoes_peso_altura_ate2anos")
        )
    )



    indicador_IV = (
        fat_vis_dom
        .select([
            "co_seq_fat_visita_domiciliar", "co_fat_cidadao_pec", "dt_nascimento", "co_dim_tempo", "co_dim_cbo"
        ])
        .with_columns(
            # Converter `co_dim_tempo` para datetime e criar `dt_atendimento`
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
            pl.col("dt_nascimento").cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nascimento")
        )
        .filter(
            (pl.col("co_dim_cbo").is_in(acs_crianca)) &  # Filtrar pelos códigos de ACS Criança
            (pl.col("co_fat_cidadao_pec").is_not_null())  # Garantir que `co_fat_cidadao_pec` não seja nulo
        )
        .group_by("co_fat_cidadao_pec")
        .agg([
            # Ordenar `dt_atendimento` para facilitar o processamento das datas
            pl.col("dt_atendimento").sort().alias("sorted_dt_atendimento"),
            # Manter `dt_nascimento` para cada grupo
            pl.col("dt_nascimento").first().alias("dt_nascimento")
        ])
        .explode("sorted_dt_atendimento")  # Explodir as datas ordenadas para calcular as condições das visitas
        .with_columns(
            # Calcular as condições para a primeira e segunda visitas
            primeira_visita=pl.when(
                ((pl.col("sorted_dt_atendimento") - pl.col("dt_nascimento")).dt.total_days() >= 0) &
                ((pl.col("sorted_dt_atendimento") - pl.col("dt_nascimento")).dt.total_days() <= 30)
            ).then(1).otherwise(0).alias("primeira_visita"),

            segunda_visita=pl.when(
                ((pl.col("sorted_dt_atendimento") - pl.col("dt_nascimento")).dt.total_days() > 30) &
                ((pl.col("sorted_dt_atendimento") - pl.col("dt_nascimento")).dt.total_days() <= 180)
            ).then(1).otherwise(0).alias("segunda_visita")
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            # Incluir apenas `data_ultima_visita_domiciliar_acs` e o indicador na saída final
            pl.col("sorted_dt_atendimento").max().alias("data_ultima_visita_domiciliar_acs"),

            # Criar a coluna `indicador_visitas_domiciliares_acs` com base nas condições
            indicador_visitas_domiciliares_acs=pl.when(
                (pl.col("primeira_visita").sum() >= 1) &  # Pelo menos duas primeiras visitas
                (pl.col("segunda_visita").sum() >= 1)     # Pelo menos duas segundas visitas
            ).then(1).otherwise(0),

            # Criar a coluna `visitas_domiciliares_acs` como a soma de `primeira_visita` e `segunda_visita`
            visitas_domiciliares_acs=(pl.col("primeira_visita").sum() + pl.col("segunda_visita").sum()).alias("visitas_domiciliares_acs")
        )
    )

    faip_pezinho = (
        faip.filter(pl.col("tipo") == "Procedimentos Avaliados").filter(pl.col("codigo").is_in(pezinho))
            .unique(subset=["co_seq_fat_atd_ind"])  # Remove duplicates based on `co_seq_fat_atd_ind`
    )

    indicador_V = (indicador_I_e_II_III_V
        .select("co_seq_fat_atd_ind","dt_atendimento","dt_nascimento","co_fat_cidadao_pec","diff_dias")
        .join(faip_pezinho, on="co_seq_fat_atd_ind", how="left")
        .filter( 
            pl.col("codigo").is_in(pezinho)   
        )
        .with_columns(
            pl.when( (pl.col("diff_dias") <= 5 ) )
            .then(1)
            .otherwise(0)
            .alias("bool_teste_pezinho")
        ).group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("bool_teste_pezinho").sum().alias("teste_pezinho"), 
            pl.when( (pl.col("bool_teste_pezinho") == 1).any() )
            .then(1)
            .otherwise(0)
            .alias("indicador_teste_pezinho"),

            pl.col("dt_atendimento")  
            .filter( pl.col("bool_teste_pezinho") == 1 )               
            .max()                                           
            .alias("data_ultimo_teste_pezinho"),
        )
    )


    indicador_vac = (
        fat_vac
        .select("co_fat_cidadao_pec","ds_filtro_imunobiologico","co_dim_tempo","dt_nascimento","co_seq_fat_vacinacao")
        .filter(pl.col("co_fat_cidadao_pec").is_not_null())
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento2"),
            pl.col("dt_nascimento").cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nascimento2"),
        )
        .with_columns(
            (pl.col("dt_atendimento2") - pl.col("dt_nascimento2")).dt.total_days().alias("diff_dias") 
        )
        .filter(pl.col("diff_dias") <= 729)
        .with_columns(
            #Difteria/Tétano/Coqueluche/Hepatite B/Influenza B
            pl.when(pl.col("ds_filtro_imunobiologico").str.contains("42|43"))
            .then(1)
            .when(
                pl.col("ds_filtro_imunobiologico").str.contains("9") &
                pl.col("ds_filtro_imunobiologico").str.contains("39") &
                pl.col("diff_dias") >= 30 
            )
            .then(1)
            .when(
                pl.col("ds_filtro_imunobiologico").str.contains("9") &
                pl.col("ds_filtro_imunobiologico").str.contains("29") &
                pl.col("diff_dias") >= 30 
            )
            .then(1)
            .when(
                pl.col("ds_filtro_imunobiologico").str.contains("9") &
                pl.col("ds_filtro_imunobiologico").str.contains("17") &
                pl.col("ds_filtro_imunobiologico").str.contains("46") &
                pl.col("diff_dias") >= 30 
            )
            .then(1)
            .when(
                pl.col("ds_filtro_imunobiologico").str.contains("9") &
                pl.col("ds_filtro_imunobiologico").str.contains("17") &
                pl.col("ds_filtro_imunobiologico").str.contains("47") &
                pl.col("diff_dias") >= 30 
            )
            .then(1)
            .when(
                pl.col("ds_filtro_imunobiologico").str.contains("9") &
                pl.col("ds_filtro_imunobiologico").str.contains("17") &
                pl.col("ds_filtro_imunobiologico").str.contains("58") &
                pl.col("diff_dias") >= 30 
            )
            .then(1)
            .otherwise(0)
            .alias("vacina_1"),

            #Poliomielite
            pl.when(pl.col("ds_filtro_imunobiologico").str.contains("22"))
            .then(1)
            .when(pl.col("ds_filtro_imunobiologico").str.contains("29"))
            .then(1)
            .when(pl.col("ds_filtro_imunobiologico").str.contains("43"))
            .then(1)
            .when(pl.col("ds_filtro_imunobiologico").str.contains("58"))
            .then(1)
            .otherwise(0)
            .alias("vacina_2"),

            #Sarampo/Caxumba/Rubéola/Varicela
            pl.when(
                (
                    pl.col("ds_filtro_imunobiologico").str.contains("24") |
                    pl.col("ds_filtro_imunobiologico").str.contains("56")
                ) &
                (
                pl.col("diff_dias") >= 366
                )
            )
            .then(1)
            .otherwise(0)
            .alias("vacina_3")
        )
    )


    indicador_VI = (
        indicador_vac
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("vacina_1").sum().alias("n_vacina_1"), 
            pl.col("vacina_2").sum().alias("n_vacina_2"), 
            pl.col("vacina_3").sum().alias("n_vacina_3"), 
            
            pl.col("dt_atendimento2")  
            .filter( (pl.col("vacina_1").sum() >= 3)  & (pl.col("vacina_1") == 1 )   )
            .max()                                           
            .alias("data_ultima_vacina_penta"),

            pl.col("dt_atendimento2")  
            .filter( (pl.col("vacina_2").sum() >= 3 ) & (pl.col("vacina_2") == 1 )   )                
            .max()                                           
            .alias("data_ultima_vacina_polio"),

            pl.col("dt_atendimento2")  
            .filter( (pl.col("vacina_3").sum() >= 2)  & (pl.col("vacina_3") == 1 )   )               
            .max()                                           
            .alias("data_ultima_vacina_triplici")
        )
        .with_columns(
            pl.when(
                (pl.col("n_vacina_1") >= 3) &
                (pl.col("n_vacina_2") >= 3) &
                (pl.col("n_vacina_3") >= 2) 
            )
            .then(1)
            .otherwise(0)
            .alias("indicador_vacinas_penta_polio_triplici")
        )
    ).rename({
        "n_vacina_1": "n_penta",
        "n_vacina_2": "n_polio",
        "n_vacina_3": "n__triplici"
    })

    crianca_fao = fao.join(
        crianca.select('co_fat_cidadao_pec'),
        on="co_fat_cidadao_pec",
        how="inner"
    )

    indicador_VII = crianca_fao.select(
            ["co_fat_cidadao_pec", "co_dim_tempo", "co_dim_cbo_1", "co_dim_cbo_2","dt_nascimento"]
        ).with_columns(
            # Convert `co_dim_tempo` to datetime and create `dt_atendimento`
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
            pl.col("dt_nascimento").cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nascimento")
        
        ).filter(
            (pl.col("co_fat_cidadao_pec").is_not_null() )

        ).with_columns(
            (pl.col("dt_atendimento") - pl.col("dt_nascimento")).dt.total_days().alias("diff_dias"),
            
        ).with_columns(
            (pl.col("diff_dias") / 365.25).alias("diff_anos"),
        ).filter(
            (pl.col("co_dim_cbo_1").is_in(codigos_dentista)) |
            (pl.col("co_dim_cbo_2").is_in(codigos_dentista))
        ).with_columns(
            pl.when(pl.col("diff_anos") <= 1)
            .then(1)
            .otherwise(0)
            .alias("atendimento_ultimo_ano")
            
        ).group_by("co_fat_cidadao_pec").agg([
            pl.len().alias("atendimentos_odontologicos"),
            pl.max("atendimento_ultimo_ano").alias("atendimento_ultimo_ano"),

            pl.col("dt_atendimento")
            .filter(  (pl.col("atendimento_ultimo_ano") == 1 )  & (pl.len() >= 2) )
            .max()                                           
            .alias("data_ultimo_atendimento_odontologico"),
    ]).with_columns(
            pl.when(
                (pl.col("atendimento_ultimo_ano") == 1) &
                (pl.col("atendimentos_odontologicos") >= 2)
            
            )
            .then(1)
            .otherwise(0)
            .alias("indicador_atendimentos_odontologicos")
            
        ).drop("atendimento_ultimo_ano")

    crianca_fai = (
        fai.join(
            crianca.select('co_fat_cidadao_pec'),
            on="co_fat_cidadao_pec",
            how="inner"
        ).select("co_dim_cbo_1","co_dim_cbo_2","co_fat_cidadao_pec")
    )

    crianca_fao = fao.join(
        crianca.select('co_fat_cidadao_pec'),
        on="co_fat_cidadao_pec",
        how="inner"
    ).select("co_dim_cbo_1","co_dim_cbo_2","co_fat_cidadao_pec")


    crianca_fai_fao = pl.concat([crianca_fai, crianca_fao])

    crianca_plot_proffis = (
        crianca_fai_fao
        .with_columns(
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(medico_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(medico_codigos)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_medico"),
            
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(enfermeiro_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(enfermeiro_codigos)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_enfer"),

            pl.when(
                (pl.col("co_dim_cbo_1").is_in(fonod_cod)) |
                (pl.col("co_dim_cbo_2").is_in(fonod_cod)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_fono"),

            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cirur_den_cod)) |
                (pl.col("co_dim_cbo_2").is_in(cirur_den_cod)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_ciru_dent"),
            

            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cod_psicologo)) |
                (pl.col("co_dim_cbo_2").is_in(cod_psicologo)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_psicol"),

            pl.when(
                (pl.col("co_dim_cbo_1").is_in(prof_edu_fisic_cod)) |
                (pl.col("co_dim_cbo_2").is_in(prof_edu_fisic_cod)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_educ_fisica"),
            
            
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cod_assistente_social)) |
                (pl.col("co_dim_cbo_2").is_in(cod_assistente_social)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_assist_social"),
            
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cod_terap_ocup)) |
                (pl.col("co_dim_cbo_2").is_in(cod_terap_ocup)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_tera_ocup"),
            
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cod_farma)) |
                (pl.col("co_dim_cbo_2").is_in(cod_farma)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_farmac"),

            pl.when(
                (pl.col("co_dim_cbo_1").is_in(fisio_cod)) |
                (pl.col("co_dim_cbo_2").is_in(fisio_cod)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_fisio"),
            
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cod_nutri)) |
                (pl.col("co_dim_cbo_2").is_in(cod_nutri)) 
            )
            .then(1)
            .otherwise(0)
            .alias("bin_nutric"),

            pl.when(
            (~pl.col("co_dim_cbo_1").is_in(todos_codigos)) &
            (~pl.col("co_dim_cbo_2").is_in(todos_codigos))
        ).then(1).otherwise(0).alias("bin_outros")
            
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("bin_medico").sum().alias("n_medicos"),
            pl.col("bin_enfer").sum().alias("n_enfer"),
            pl.col("bin_fono").sum().alias("n_fono"),
            pl.col("bin_psicol").sum().alias("n_psicol"),
            pl.col("bin_educ_fisica").sum().alias("n_educ_fisica"),
            pl.col("bin_assist_social").sum().alias("n_assist_social"),
            pl.col("bin_tera_ocup").sum().alias("n_tera_ocup"),
            pl.col("bin_farmac").sum().alias("n_farmac"),
            pl.col("bin_fisio").sum().alias("n_fisio"),
            pl.col("bin_nutric").sum().alias("n_nutric"),
            pl.col("bin_ciru_dent").sum().alias("n_ciru_dent"),
            pl.col("bin_outros").sum().alias("n_outros"),
            pl.len().alias("total"),
        )

    )



    mapeamento_renomeacao = {
        "co_fat_cidadao_pec": "cidadao_pec",
    }


    crianca_updated = (crianca
                    .join(indicador_I , on ="co_fat_cidadao_pec",how="left" )
                    .with_columns([
                            pl.col("indicador_atendimentos_medicos_enfermeiros").fill_null(2),  
                    ])
                    .join(indicador_II , on ="co_fat_cidadao_pec",how="left" )
                    .with_columns([
                            pl.col("indicador_atendimentos_medicos_enfermeiros_puericult").fill_null(2),  
                    ])
                    .join(indicador_III , on ="co_fat_cidadao_pec",how="left" )
                    .with_columns([
                            pl.col("indicador_medicoes_peso_altura_ate2anos").fill_null(2),  
                    ])
                    .join(indicador_IV , on ="co_fat_cidadao_pec",how="left" )
                    .with_columns([
                            pl.col("indicador_visitas_domiciliares_acs").fill_null(0),  
                    ])
                    .join(indicador_V , on ="co_fat_cidadao_pec",how="left" )
                    .with_columns([
                            pl.col("indicador_teste_pezinho").fill_null(2),  
                    ])
                    .join(indicador_VI , on ="co_fat_cidadao_pec",how="left" )
                    .with_columns([
                            pl.col("indicador_vacinas_penta_polio_triplici").fill_null(0),  
                    ])
                    .join(indicador_VII , on ="co_fat_cidadao_pec",how="left" )
                    .join(crianca_plot_proffis , on ="co_fat_cidadao_pec",how="left" )
                    .rename(mapeamento_renomeacao)

    )
    crianca_updated.write_parquet(output_path+os.sep+"crianca.parquet")

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Tempo total de execução: {execution_time:.2f} segundos")
