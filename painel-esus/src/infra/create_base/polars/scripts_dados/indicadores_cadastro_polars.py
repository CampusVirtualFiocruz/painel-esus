import os
import time
from datetime import date, datetime

import pandas as pd
import polars as pl
from dateutil.relativedelta import relativedelta
from src.infra.db.settings.connection_local import DBConnectionHandler

start_time = time.time()





def gerar_banco():
    working_directory  = os.getcwd()
    input_path = os.path.join(working_directory, "dados", "input") 
    output_path = os.path.join(working_directory, "dados", "output")  
    

    # Define a data de 12 meses atrás
    dt_12meses = datetime.today() - relativedelta(months=12)




    coluns_acv_geral = ['co_seq_acomp_cidadaos_vinc','st_usar_cadastro_individual','co_unico_ultima_ficha','dt_nascimento_cidadao','no_sexo_cidadao','nu_cpf_cidadao','st_possui_fci','st_possui_fcdt','co_cidadao',''
                'nu_cns_cidadao','nu_telefone_celular','nu_telefone_contato','no_cidadao'
                ,'nu_micro_area_domicilio','nu_micro_area_tb_cidadao','nu_ine_vinc_equipe','nu_cnes_vinc_equipe',
                'ds_tipo_localizacao_domicilio','dt_ultima_atualizacao_cidadao','dt_atualizacao_fcd']


    coluns_acv_end = ['no_tipo_logradouro_tb_cidadao','ds_logradouro_tb_cidadao',
                'nu_numero_tb_cidadao','no_bairro_tb_cidadao','ds_complemento_tb_cidadao',
                'ds_cep_tb_cidadao','no_municipio_tb_cidadao','no_tipo_logradouro_domicilio',
                'ds_logradouro_domicilio','nu_numero_domicilio',
                'ds_complemento_domicilio','no_bairro_domicilio','no_municipio_domicilio','ds_cep_domicilio']


    tb_pessoa = pl.scan_parquet(input_path + os.sep +"tb_acomp_cidadaos_vinculados.parquet")


    

    vac = pl.scan_parquet(input_path + os.sep +"tb_fat_vacinacao.parquet")

    columns_proced = ['co_seq_fat_proced_atend','co_fat_cidadao_pec','co_dim_tempo']

    proced_atend = pl.scan_parquet(input_path + os.sep +"tb_fat_proced_atend.parquet")

    fai_vars = ['co_fat_cidadao_pec','co_dim_tempo']

    fai = pl.scan_parquet(input_path + os.sep +"tb_fat_atendimento_individual.parquet")

    fao_vars = ['co_fat_cidadao_pec','co_dim_tempo']

    fao = pl.scan_parquet(input_path + os.sep +"tb_fat_atendimento_odonto.parquet")

    marc_cons_alim_vars = ['co_seq_fat_marca_con_almnt','co_fat_cidadao_pec','co_dim_tempo']

    marc_cons_alim = pl.scan_parquet(input_path + os.sep +"tb_fat_marca_consumo_alimnt.parquet")

    atv_colet_vars= ['co_seq_fat_atvdd_cltv_part','co_fat_cidadao_pec','co_dim_tempo']

    atv_colet = pl.scan_parquet(input_path + os.sep +"tb_fat_atvdd_coletiva_part.parquet")

    selected_columns_cad = ["co_fat_cidadao_pec","co_dim_tempo","nu_uuid_ficha","co_dim_raca_cor"]
    fci = pl.scan_parquet(input_path + os.sep +"tb_fat_cad_individual.parquet")
    fci = fci.rename({"co_dim_tempo" : "co_dim_tempo_fci"})
    fci = fci.rename({"nu_micro_area" : "nu_micro_area_fci"})


    tb_dim_equipe = pl.scan_parquet(input_path + os.sep +"tb_dim_equipe.parquet")

    tb_dim_und_saude = pl.scan_parquet(input_path + os.sep +"tb_dim_unidade_saude.parquet")




    dim_raca_cor = pl.scan_parquet(input_path + os.sep +"tb_dim_raca_cor.parquet")
    dim_raca_cor = dim_raca_cor.rename({"co_seq_dim_raca_cor" : "co_dim_raca_cor"}).select("co_dim_raca_cor","ds_raca_cor")

    fci = fci.join(dim_raca_cor,on="co_dim_raca_cor",how='left')

    vis_dom_vars = ['co_seq_fat_visita_domiciliar','co_fat_cidadao_pec','co_dim_tempo']

    fat_vis_dom = pl.scan_parquet(input_path + os.sep +"tb_fat_visita_domiciliar.parquet")



    tb_pessoa_v2 = tb_pessoa.join(
        fci,
        left_on="co_unico_ultima_ficha",
        right_on="nu_uuid_ficha",
        how="left"
    ).with_columns(
        pl.col("dt_ultima_atualizacao_cidadao").cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d").alias("dt_ultima_atualizacao_cidadao")
    ).sort(
        by=["co_fat_cidadao_pec", "dt_ultima_atualizacao_cidadao", "co_seq_acomp_cidadaos_vinc"],  # Prioriza chave, depois data, depois variável inteira
        descending=[False, True, True]             # Ordena data e variável inteira em ordem decrescente
    ).unique(
        subset="co_fat_cidadao_pec",                            # Remove duplicatas pela chave
        keep="first"                               # Mantém a primeira ocorrência após a ordenação
    )




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
    tb_pessoa_v6 = tb_pessoa_v6.with_columns(expressoes)





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
            .alias("alerta"),

        pl.coalesce([
            pl.col("nu_micro_area_domicilio"), 
            pl.col("nu_micro_area_fci"),
            pl.col("nu_micro_area_tb_cidadao"),
        ]).alias("nu_micro_area")

        ).select("co_fat_cidadao_pec",
            "co_cidadao",
            "nu_cnes_vinc_equipe",
            "nu_ine_vinc_equipe",
            "dt_nasc_cidadao",
            "nu_cpf_cidadao",
            "nu_cns_cidadao",
            "acompanhamento",
            "status_cadastro",
            "idade",
            "tipo_ident_cpf_cns",
            "faixa_etaria",
            "ds_raca_cor",
            "no_tipo_logradouro",
            "ds_logradouro",
            "nu_numero",
            "no_bairro",
            "ds_complemento",
            "ds_cep",
            "ds_tipo_localizacao_domicilio",
            "telefone",
            "no_cidadao",
            "no_sexo_cidadao",
            "nu_micro_area",
            "nome_equipe",
            "nome_unidade_saude",
            "fci_att_2anos",
            "fcdt_att_2anos",
            "alerta_status_cadastro",
            "alerta",
            "co_dim_unidade_saude",
            "codigo_equipe",
            "dt_update_fci",
            "dt_atualizacao_fcd",
            "st_usar_cadastro_individual"
        )
    )


    tb_pessoa_v7.sink_parquet(output_path+os.sep+"cadastro_db.parquet", row_group_size=8192 )

