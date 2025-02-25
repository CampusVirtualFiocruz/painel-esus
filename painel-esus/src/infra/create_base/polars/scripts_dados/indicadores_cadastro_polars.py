import os
import time
from datetime import date, datetime

import pandas as pd
import polars as pl
from dateutil.relativedelta import relativedelta
from src.infra.db.settings.connection_local import DBConnectionHandler

start_time = time.time()


# In[2]:



def gerar_banco():
    working_directory  = os.getcwd()
    input_path = os.path.join(working_directory, "dados", "input") 
    output_path = os.path.join(working_directory, "dados", "output")  
    

    # Define a data de 12 meses atrás
    dt_12meses = datetime.today() - relativedelta(months=12)


    # In[190]:


    coluns_acv = ['co_unico_ultima_ficha','st_usar_cadastro_individual',
                'st_possui_fci','st_possui_fcdt','dt_ultima_atualizacao_cidadao','co_cidadao',
                'nu_cnes_vinc_equipe','dt_atualizacao_fcd','nu_ine_vinc_equipe','dt_nascimento_cidadao','nu_cpf_cidadao',
                'nu_cns_cidadao','no_tipo_logradouro_tb_cidadao','ds_logradouro_tb_cidadao',
                'nu_numero_tb_cidadao','no_bairro_tb_cidadao','ds_complemento_tb_cidadao',
                'ds_cep_tb_cidadao','nu_telefone_celular','nu_telefone_contato',"no_cidadao",
                'no_sexo_cidadao','nu_micro_area_domicilio','ds_tipo_localizacao_domicilio']


    tb_pessoa = pl.read_parquet(input_path + os.sep +"tb_acomp_cidadaos_vinculados.parquet",columns=coluns_acv)


    #tabelas para indicador de acompnhamento

    coluns_vac = ['co_seq_fat_vacinacao','co_fat_cidadao_pec','co_dim_tempo'] 

    vac = pl.read_parquet(input_path + os.sep +"tb_fat_vacinacao.parquet",columns=coluns_vac)

    columns_proced = ['co_seq_fat_proced_atend','co_fat_cidadao_pec','co_dim_tempo']

    proced_atend = pl.read_parquet(input_path + os.sep +"tb_fat_proced_atend.parquet",columns=columns_proced)

    fai_vars = ['co_fat_cidadao_pec','co_dim_tempo']

    fai = pl.read_parquet(input_path + os.sep +"tb_fat_atendimento_individual.parquet",columns =fai_vars)

    fao_vars = ['co_fat_cidadao_pec','co_dim_tempo']

    fao = pl.read_parquet(input_path + os.sep +"tb_fat_atendimento_odonto.parquet",columns =fao_vars)

    marc_cons_alim_vars = ['co_seq_fat_marca_con_almnt','co_fat_cidadao_pec','co_dim_tempo']

    marc_cons_alim = pl.read_parquet(input_path + os.sep +"tb_fat_marca_consumo_alimnt.parquet",columns =marc_cons_alim_vars)

    atv_colet_vars= ['co_seq_fat_atvdd_cltv_part','co_fat_cidadao_pec','co_dim_tempo']

    atv_colet = pl.read_parquet(input_path + os.sep +"tb_fat_atvdd_coletiva_part.parquet",columns =atv_colet_vars)

    selected_columns_cad = ["co_fat_cidadao_pec","co_dim_tempo","nu_uuid_ficha","co_dim_raca_cor"]
    fci = pl.read_parquet(input_path + os.sep +"tb_fat_cad_individual.parquet", columns=selected_columns_cad)
    fci = fci.rename({"co_dim_tempo" : "co_dim_tempo_fci"})


    tb_dim_equipe = pl.read_parquet(input_path + os.sep +"tb_dim_equipe.parquet")

    tb_dim_und_saude = pl.read_parquet(input_path + os.sep +"tb_dim_unidade_saude.parquet")




    dim_raca_cor = pl.read_parquet(input_path + os.sep +"tb_dim_raca_cor.parquet")
    dim_raca_cor = dim_raca_cor.rename({"co_seq_dim_raca_cor" : "co_dim_raca_cor"}).select("co_dim_raca_cor","ds_raca_cor")

    fci = fci.join(dim_raca_cor,on="co_dim_raca_cor",how='left')

    vis_dom_vars = ['co_seq_fat_visita_domiciliar','co_fat_cidadao_pec','co_dim_tempo']

    fat_vis_dom = pl.read_parquet(input_path + os.sep +"tb_fat_visita_domiciliar.parquet", columns=vis_dom_vars)



    tb_pessoa_v2 = tb_pessoa.join(
        fci,
        left_on="co_unico_ultima_ficha",
        right_on="nu_uuid_ficha",
        how="left"
    )


    # In[40]:


    today = date.today()

    dt_24meses = datetime.today() - relativedelta(months=24)

    tb_pessoa_v3 = (
        tb_pessoa_v2
            .with_columns(
                pl.col("co_dim_tempo_fci").cast(pl.Utf8).str.strptime(pl.Date, format="%Y%m%d").alias("dt_update_fci"),
                pl.when(
                    ( pl.col("st_possui_fci") == 1 ) & ( pl.col("st_possui_fcdt") == 1 ) 
                )
                .then(pl.lit("cadastro_completo")) # cadastro completo
                .when(  
                    ( pl.col("st_possui_fci") == 1 ) & ( pl.col("st_possui_fcdt") == 0 )
                )
                .then(pl.lit("cadastro_incompleto")) # cadastro incompleto
                .when(  
                    ( pl.col("st_possui_fci") == 0 ) & ( pl.col("st_possui_fcdt") == 0 )
                )
                .then(pl.lit("pessoa_ident_nao_cadastrada")) # pessoa identificada e não cadastrada
                .when(  
                    ( pl.col("st_possui_fci") == 0 ) & ( pl.col("st_possui_fcdt") == 1 )
                )
                .then(pl.lit("outro")) # outros
                .otherwise(pl.lit("outro"))
                .alias("status_cadastro"),
                
                pl.col("dt_nascimento_cidadao").str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nasc_cidadao"),
            # pl.col("dt_ultima_atualizacao_cidadao").str.strptime(pl.Date, "%Y-%m-%d").alias("dt_ultima_atualizacao_cidadao"),
                pl.col("dt_atualizacao_fcd").str.strptime(pl.Date, "%Y-%m-%d").alias("dt_atualizacao_fcd")

            ).with_columns(
                pl.when(
                    pl.date(pl.col("dt_nasc_cidadao").dt.year(), today.month, today.day) >= pl.col("dt_nasc_cidadao")
                )
                .then(today.year - pl.col("dt_nasc_cidadao").dt.year())
                .otherwise(today.year - pl.col("dt_nasc_cidadao").dt.year() - 1).cast(pl.Float32).alias("idade"),


                pl.when(
                    (pl.col("dt_atualizacao_fcd") >= dt_24meses) # (pl.col("status_cadastro") >= 0) &
                )
                .then(1)
                .otherwise(0)
                .alias("fcdt_att_2anos"),
            

                pl.when(
                    (pl.col("status_cadastro") != "cadastro_completo")
                )
                .then(1)
                .otherwise(0)
                .alias("alerta_status_cadastro"),

                pl.when(
                    (pl.col("nu_cpf_cidadao").is_null() ) & (pl.col("nu_cns_cidadao").is_null() )
                )
                .then(0)
                .otherwise(1)
                .alias("tipo_ident_cpf_cns")
                
            ).with_columns(
                pl.when(
                    (pl.col("dt_update_fci") >= dt_24meses) # (pl.col("status_cadastro") >= 0) &
                )
                .then(1)
                .otherwise(0)
                .alias("fci_att_2anos"),
                
                pl.when((pl.col("idade") >= 1) & (pl.col("idade") <= 4)).then(pl.lit("1a4"))
                .when((pl.col("idade") >= 5) & (pl.col("idade") <= 9)).then(pl.lit("5a9"))
                .when((pl.col("idade") >= 10) & (pl.col("idade") <= 14)).then(pl.lit("10a14"))
                .when((pl.col("idade") >= 15) & (pl.col("idade") <= 19)).then(pl.lit("15a19"))
                .when((pl.col("idade") >= 20) & (pl.col("idade") <= 29)).then(pl.lit("20a29"))
                .when((pl.col("idade") >= 30) & (pl.col("idade") <= 39)).then(pl.lit("30a39"))
                .when((pl.col("idade") >= 40) & (pl.col("idade") <= 49)).then(pl.lit("40a49"))
                .when((pl.col("idade") >= 50) & (pl.col("idade") <= 59)).then(pl.lit("50a59"))
                .when((pl.col("idade") >= 60) & (pl.col("idade") <= 69)).then(pl.lit("60a69"))
                .when((pl.col("idade") >= 70) & (pl.col("idade") <= 79)).then(pl.lit("70a79"))
                .when(pl.col("idade") >= 80).then(pl.lit("80mais"))
                .otherwise(pl.lit("idade_invalida"))
                .alias("faixa_etaria")
            )
    )


    # ### criar dados sobre acompanhamneto

    # #### procedimento

    # In[41]:




    vac_v2 = (
        vac
        .with_columns(
            pl.lit("vac").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
    )

    proced_atend_v2 = (
        proced_atend
        .with_columns(
            pl.lit("proced_atend").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
    )

    procedimento  = pl.concat([vac_v2,proced_atend_v2])

    procedimento_grouped = (
        procedimento
        .group_by('co_fat_cidadao_pec')
        .agg(
            pl.len().alias("n_procedimentos") 
        )
        .with_columns(
            pl.when(
                    (pl.col("n_procedimentos") >= 1)  
                    )
            .then(1)
            .otherwise(0)
            .alias("procedimento"),
        )
    )


    # #### atendimento

    # In[42]:


    fai_v2 = (
        fai
        .with_columns(
            pl.lit("fai").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
    )


    fao_v2 = (
        fao
        .with_columns(
            pl.lit("fao").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
    )

    marc_cons_alim_v2 = (
        marc_cons_alim
        .with_columns(
            pl.lit("cons_alim").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
    )

    atv_colet_v2 = (
        atv_colet
        .with_columns(
            pl.lit("atv_coletiva").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
            pl.col("co_fat_cidadao_pec").cast(pl.Int64).alias("co_fat_cidadao_pec")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
    )

    fat_vis_dom_v2 = (
        fat_vis_dom
        .with_columns(
            pl.lit("vis_dom").alias("tabela"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
            pl.col("co_fat_cidadao_pec").cast(pl.Int64).alias("co_fat_cidadao_pec")
        )
        .filter(
            (pl.col("dt_atendimento") >= pl.lit(dt_12meses) ) &
            (pl.col("co_fat_cidadao_pec").is_not_null() ) 
        ) 
        .select("co_fat_cidadao_pec","tabela")
)




    atendimento =  pl.concat([fai_v2,fao_v2,marc_cons_alim_v2,atv_colet_v2,fat_vis_dom_v2])


    atendimento_grouped = (
        atendimento
        .group_by('co_fat_cidadao_pec')
        .agg(
            pl.len().alias("n_atendimentos") 
        )
        .with_columns(
            pl.when(
                    (pl.col("n_atendimentos") >= 1)  
                    )
            .then(1)
            .otherwise(0)
            .alias("atendimentos"),
        )
    )


    # #### indicador acompnhamento

    # In[43]:


    tb_pessoa_v4  = (
        tb_pessoa_v3.join(atendimento_grouped, on="co_fat_cidadao_pec", how="left")
    )

    tb_pessoa_v5  = (
        tb_pessoa_v4.join(procedimento_grouped, on="co_fat_cidadao_pec", how="left")
    ).with_columns(
        # Replace missing values with 2 in `indicador_medicoes_peso_altura`
        pl.col("n_atendimentos").fill_null(0),
        pl.col("n_procedimentos").fill_null(0),
        pl.col("atendimentos").fill_null(0),
        pl.col("procedimento").fill_null(0)
    )


    # In[44]:


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
        # pl.col("codigo_unidade_saude")
        # .str.replace_all('-', "") 
        # .cast(pl.Int32,strict=False).alias("codigo_unidade_saude")
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
        # pl.col("nu_ine")
        # .str.replace_all('-', "") 
        # .cast(pl.Int32,strict=False).alias("nu_ine2")
        ]).filter(pl.col("st_registro_valido_equipe") == 1)
    )


    # In[45]:


    tb_pessoa_v6 = tb_pessoa_v5.join(
        tb_dim_equipe_v2,
        left_on="nu_ine_vinc_equipe",
        right_on= "nu_ine",
        how="left"
    ).join(
        tb_dim_und_saude_v3,
        left_on="nu_cnes_vinc_equipe",
        right_on= "codigo_unidade_saude",
        how="left"
    )


    # In[46]:


    tb_pessoa_v7 = (
        tb_pessoa_v6
        .with_columns(
            pl.when(
                ( (pl.col("procedimento") == 1 ) &  (pl.col("atendimentos") == 1)  )
            
            )
            .then(1)
            .when(pl.col("n_atendimentos") >= 2)
            .then(1)
            .otherwise(0)
            .alias("acompanhamento"),

            pl.coalesce(['nu_telefone_celular','nu_telefone_contato']).alias("telefone"),
            
            pl.when(
            (   (pl.col("fci_att_2anos") == 0 )  |  ( pl.col("alerta_status_cadastro") == 1)  |  ( pl.col("fcdt_att_2anos") == 0) )
            
            )
            .then(1)
            .otherwise(0)
            .alias("alerta")
        )
    ).select("co_fat_cidadao_pec","co_cidadao","nu_cnes_vinc_equipe","nu_ine_vinc_equipe","dt_nasc_cidadao","nu_cpf_cidadao","nu_cns_cidadao","acompanhamento",'status_cadastro',
        'idade','tipo_ident_cpf_cns',"faixa_etaria","ds_raca_cor",'no_tipo_logradouro_tb_cidadao','ds_logradouro_tb_cidadao',
         'nu_numero_tb_cidadao','no_bairro_tb_cidadao','ds_complemento_tb_cidadao','ds_cep_tb_cidadao','ds_tipo_localizacao_domicilio','telefone',
         "no_cidadao","no_sexo_cidadao","nu_micro_area_domicilio","nome_equipe","nome_unidade_saude","fci_att_2anos","fcdt_att_2anos","alerta_status_cadastro","alerta",
        "co_dim_unidade_saude","codigo_equipe","dt_update_fci","dt_atualizacao_fcd")


    tb_pessoa_v7.write_parquet(output_path+os.sep+"cadastro_db.parquet")
