#!/usr/bin/env python
# coding: utf-8

import os
import time
from datetime import date, datetime

import polars as pl
from dateutil.relativedelta import relativedelta

from .codigos_cbo import *


def gerar_banco():
    start_time = time.time()
    working_directory  = os.getcwd()
    input_path = os.path.join(working_directory, "dados", "input") 
    output_path = os.path.join(working_directory, "dados", "output")  


    coluns_acv_geral = ['co_seq_acomp_cidadaos_vinc','co_unico_ultima_ficha','dt_nascimento_cidadao','no_sexo_cidadao','nu_cpf_cidadao',
                'nu_cns_cidadao','nu_telefone_celular','nu_telefone_contato','no_cidadao'
                ,'nu_micro_area_domicilio','nu_micro_area_tb_cidadao','nu_ine_vinc_equipe','nu_cnes_vinc_equipe',
                'ds_tipo_localizacao_domicilio','dt_ultima_atualizacao_cidadao']


    coluns_acv_end = ['no_tipo_logradouro_tb_cidadao','ds_logradouro_tb_cidadao',
                'nu_numero_tb_cidadao','no_bairro_tb_cidadao','ds_complemento_tb_cidadao',
                'ds_cep_tb_cidadao','no_municipio_tb_cidadao','no_tipo_logradouro_domicilio',
                'ds_logradouro_domicilio','nu_numero_domicilio',
                'ds_complemento_domicilio','no_bairro_domicilio','no_municipio_domicilio','ds_cep_domicilio']

    columns_acv = coluns_acv_geral + coluns_acv_end



    # FCI
    selected_columns_fci = ["co_fat_cidadao_pec","st_diabete","co_dim_tempo","nu_uuid_ficha",'co_dim_raca_cor','nu_micro_area']


    # FAI
    selected_columns_atd_ind = ["co_fat_cidadao_pec", "co_seq_fat_atd_ind","nu_altura","nu_peso","co_dim_tempo","co_dim_cbo_1", "co_dim_cbo_2", "dt_nascimento"]


    # PROCED / ATEND
    columns_proced = ['co_seq_fat_proced_atend','co_fat_cidadao_pec',"nu_altura","nu_peso",'co_dim_tempo','ds_filtro_procedimento','co_dim_cbo']




    # FAOI
    columns_fao = ['co_fat_cidadao_pec','co_dim_tempo',"nu_altura","nu_peso",'co_dim_cbo_1','co_dim_cbo_2','co_seq_fat_atd_odnt','ds_filtro_procedimentos']


    # FAC (atividade coletiva)
    columns_atvdd_coletiva = ['co_fat_cidadao_pec','co_dim_tempo',"nu_participante_altura","nu_participante_peso",'co_seq_fat_atvdd_cltv_part']


    # VIS_DOM (visita domiciliar)
    columns_vis_dom = ['co_seq_fat_visita_domiciliar','co_fat_cidadao_pec','co_dim_tempo','co_dim_cbo']

    coluns_cbo = ['nu_cbo','co_seq_dim_cbo']


    tb_pessoa = pl.read_parquet(input_path + os.sep +"tb_acomp_cidadaos_vinculados.parquet",columns = columns_acv)


    fci = pl.read_parquet(input_path + os.sep +"tb_fat_cad_individual.parquet", columns=selected_columns_fci)
    fci = fci.rename({"nu_micro_area" : "nu_micro_area_fci"})


    fai = pl.read_parquet(input_path + os.sep +"tb_fat_atendimento_individual.parquet",columns=selected_columns_atd_ind)



    fai_cods = pl.read_parquet(input_path + os.sep +"fat_atd_ind_cod.parquet")


    proced_atend = pl.read_parquet(input_path + os.sep +"tb_fat_proced_atend.parquet",columns = columns_proced)


    fao = pl.read_parquet(input_path + os.sep +"tb_fat_atendimento_odonto.parquet")#,columns = columns_fao)


    #fac = pl.read_parquet(input_path + os.sep +"tb_fat_atvdd_coletiva_part.parquet")

    tb_atv_coletv_part= pl.read_parquet(input_path + os.sep +"tb_fat_atvdd_coletiva_part.parquet")


    fat_vis_dom = pl.read_parquet(input_path + os.sep + "tb_fat_visita_domiciliar.parquet", columns=columns_vis_dom)

    # Dimensão UNIDADE DE SAUDE
    tb_dim_und_saude = pl.read_parquet(input_path + os.sep + "tb_dim_unidade_saude.parquet")

    # Dimensão EQUIPE
    tb_dim_equipe = pl.read_parquet(input_path + os.sep + "tb_dim_equipe.parquet")

    # Dimensão RAÇA/COR
    dim_raca_cor = pl.read_parquet(input_path + os.sep +"tb_dim_raca_cor.parquet")
    dim_raca_cor = dim_raca_cor.rename({"co_seq_dim_raca_cor" : "co_dim_raca_cor"}).select("co_dim_raca_cor","ds_raca_cor")


    dim_cbo = pl.read_parquet(input_path + os.sep +"tb_dim_cbo.parquet",columns=coluns_cbo)

    #Juntando raça/cor
    fci = fci.join(dim_raca_cor,on="co_dim_raca_cor",how='left')


    
    


    dim_cbo = dim_cbo.with_columns(pl.col("co_seq_dim_cbo").cast(pl.Int64))




    #fai
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


    fat_vis_dom = (
        fat_vis_dom
        .join(
            dim_cbo,
            left_on="co_dim_cbo",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo")
        .rename({"nu_cbo": "co_dim_cbo"})
    )

    proced_atend = (
        proced_atend
        .join(
            dim_cbo,
            left_on="co_dim_cbo",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo")
        .rename({"nu_cbo": "co_dim_cbo"})
    )

    tb_atv_coletv_part = (
        tb_atv_coletv_part
        .join(
            dim_cbo,
            left_on="co_dim_cbo",
            right_on="co_seq_dim_cbo",
            how="left"
        )
        .drop("co_dim_cbo")
        .rename({"nu_cbo": "co_dim_cbo"})
    )


    # Passo 5. Criar variáveis de tempo de acordo com Indicador, quando aplicável



    dt_12meses = datetime.today() - relativedelta(months=12)
    dt_6meses = datetime.today() - relativedelta(months=6)


    def calcular_data(meses: int):
        return datetime.today() - relativedelta(months=meses)


    # Passo 6. Filtrar os códigos de profissionais, exames ou condições de saúde dos Indicadores 5 a 8

    # Passo 7. Manipular dados conforme necessidades dos Indicadores




    # agrupa a tabela fci e captura se tem diabetes de forma autoreferida , 
    # usando todo o periodo de fci,captura a data da ultima fci usando co_dim_tempo

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
            pl.col("dt_atendimento").max().alias("last_dt_fci"),
            pl.col("st_diabete").max().alias("st_diabete"),
            pl.col("ds_raca_cor").first().alias("ds_raca_cor")  ,
        ])
        .filter(
            pl.col("st_diabete") >= 1
        )
    )

    #print(cad_grouped.glimpse() )




    # selecionando variáveis de interesse e juntando ACV e FCI agrupada por cidadão

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
    ).with_columns([
        pl.col("st_diabete").fill_null(0),
    ])

    #tb_pessoa_v2.height





    tb_pessoa_v2 = tb_pessoa_v2.sort(
        by=["co_fat_cidadao_pec", "dt_ultima_atualizacao_cidadao", "co_seq_acomp_cidadaos_vinc"],  # Prioriza chave, depois data, depois variável inteira
        descending=[False, True, True]             # Ordena data e variável inteira em ordem decrescente
    ).unique(
        subset="co_fat_cidadao_pec",                            # Remove duplicatas pela chave
        keep="first"                               # Mantém a primeira ocorrência após a ordenação
    )




    # criando coluna para indicar se contém diabetes

    faip_cods_diabetes = fai_cods.with_columns(
        pl.when(
            ((pl.col("tipo") == "CIDS") & pl.col("codigo").is_in(cid_codes_diabetes)) |
            ((pl.col("tipo") == "CIAPS") & pl.col("codigo").is_in(ciap_codes_diabetes)) |
            ((pl.col("tipo") == "CIDS") & pl.col("codigo").is_in(abp_codes_diabetes)) |  
            ((pl.col("tipo") == "CIAPS") & pl.col("codigo").is_in(abp_codes_diabetes))  
        )
        .then(1)
        .otherwise(0)
        .alias("isContained_DIABETES"),

    # Coluna com o código de diabetes, se houver

        pl.when(
            (
                (pl.col("tipo") == "CIDS") & pl.col("codigo").is_in(cid_codes_diabetes)
            ) |
            (
                (pl.col("tipo") == "CIAPS") & pl.col("codigo").is_in(ciap_codes_diabetes)
            ) |
            (
                (pl.col("tipo") == "CIDS") & pl.col("codigo").is_in(abp_codes_diabetes)
            ) |
            (
                (pl.col("tipo") == "CIAPS") & pl.col("codigo").is_in(abp_codes_diabetes)
            )
        )
        .then(pl.col("codigo"))
        .otherwise(None)
        .alias("diabetes_codigo")
    )




    faip_cods_diabetes = faip_cods_diabetes.filter(pl.col("isContained_DIABETES") == 1)




    # agrupando dados de diabetes, seus códigos e número de diagnósticos de diabetes por cidadão

    grouped_faip = (
        faip_cods_diabetes
        .group_by(
            "co_seq_fat_atd_ind"
        ).agg(
            pl.max("isContained_DIABETES").alias("isContained_DIABETES"),
            pl.col("diabetes_codigo")
            .filter(pl.col("diabetes_codigo").is_not_null())
            .unique()
            .alias("diabetes_codigos_unicos"),
            pl.len().alias("n_diabetes_diag")
        )   
    )

    #grouped_faip.height




    #grouped_faip  # co se fat ate ind com 2 cids 308989 - verificar lista nominal final




    # formatando variável de tempo e filtrando cidadãos não nulos

    fai_v2 = (
        fai
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))


    # versao 3 = filtrando por atendimentos dentro dos últimos 12 meses

    fai_v3 = (
        fai_v2
        .filter(
            pl.col("dt_atendimento") >= dt_12meses
        )
        .select("co_fat_cidadao_pec","co_seq_fat_atd_ind","dt_atendimento","co_dim_cbo_1","co_dim_cbo_2")
    )
    #fai_v3.height







    # Passo 7.1
    # Total de pessoas com diabetes



    # cruzamento entre atendimento e cid/ciaps de diabetes já agrupados por atendimentos únicos

    fai_diabetes_atd_unico = fai_v2.join(
        grouped_faip,
        on="co_seq_fat_atd_ind",
        how="inner"
    )

    # agrupando por cidadão, incluindo data primeiro registro diabetes

    grouped_fai_diabetes_atd_unico = (
        fai_diabetes_atd_unico
        .group_by("co_fat_cidadao_pec")
        #.sort("dt_atendimento")
        .agg(
            pl.max("isContained_DIABETES").alias("diabetes"),
            pl.min("dt_atendimento").alias("dt_primeiro_reg_condicao") ,
            pl.col("diabetes_codigos_unicos").first().alias("diabetes_codigos_1atend"),
            pl.len().alias("n"),
            pl.col("diabetes_codigos_unicos").list.len().alias("x")
        )
        
    )
    #grouped_fai_diabetes_atd_unico.height




    # filtrando pessoas da ACV com diabetes

    pessoas_diabetes = tb_pessoa_v2.join(
        grouped_fai_diabetes_atd_unico,
        on="co_fat_cidadao_pec",
        how="left"
    ).with_columns([
        pl.col("diabetes").fill_null(0),  
    ]).filter(
    (pl.col("st_diabete") == 1 ) | (pl.col("diabetes") == 1 )
    )

    # criando coluna indicando autoreferidos

    pessoas_diabetes = (
        pessoas_diabetes
        .with_columns(
            pl.when(
                (pl.col("st_diabete") == 1) &
                (pl.col("diabetes") == 0 )
            )
            .then(1)
            .otherwise(0)
            .alias("autoreferido")
            
        )
    )

    #pessoas_diabetes.height


    # ### Calculo Agravos





    for column_name, codes in agravos_dict.items():
        fai_cods = fai_cods.with_columns(
            pl.when( (pl.col("codigo").is_in(codes)) & (pl.col("tipo") == "CIDS") )
            .then(1)
            .otherwise(0)
            .alias(column_name)
        )

    fai_cods = fai_cods.with_columns(
        pl.when( (pl.col("codigo").is_in(isContained_Doença_renal_ciap)) & (pl.col("tipo") == "CIAPS") |
                (pl.col("codigo").is_in(isContained_Doença_renal_cid)) & (pl.col("tipo") == "CIDS") )
        .then(1)
        .otherwise(0)
        .alias("isContained_Doença_renal")
    )


    #print(fai_cods.glimpse())


    #for column_name in agravos_dict.keys():
        #value_counts = fai_cods.group_by(column_name).len()
        #print(f"Value counts for {column_name}:")
        #print(value_counts)
        
    #value_counts = fai_cods.group_by("isContained_Doença_renal").len()




    grouped_complicacoes = (
        fai_cods
        .group_by("co_seq_fat_atd_ind")
        .agg(
            pl.sum("isContained_Infarto_Agudo").alias("n_infarto_agudo_aux"),
            pl.sum("isContained_Acidente_Vascular").alias("n_acidente_vascular_aux"),
            pl.sum("isContained_Doença_Coronariana").alias("n_coronariana_aux"),
            pl.sum("isContained_Doença_Cerebrovascular").alias("n_cerebrovascular_aux"),
            pl.sum("isContained_Doença_renal").alias("n_renal_aux")
        )
        .with_columns(
            pl.when(pl.col("n_infarto_agudo_aux") >= 1).then(1).otherwise(0).alias("n_infarto_agudo"),
            pl.when(pl.col("n_acidente_vascular_aux") >= 1).then(1).otherwise(0).alias("n_acidente_vascular"),
            pl.when(pl.col("n_coronariana_aux") >= 1).then(1).otherwise(0).alias("n_coronariana"),
            pl.when(pl.col("n_cerebrovascular_aux") >= 1).then(1).otherwise(0).alias("n_cerebrovascular"),
            pl.when(pl.col("n_renal_aux") >= 1).then(1).otherwise(0).alias("n_renal")
        )
    )



    ## add complicacoes aos atendimentos  
    fai_agravo  =  fai_v2.join(
        grouped_complicacoes,
        on="co_seq_fat_atd_ind",
        how="inner"
    )
    #fai_agravo.height  # o resultado não deveria ser 100%? ja que fai e grouped_complicacoes partem da mesma fonte? verificar com novos dados




    ## agrupar os atendimentos dos agravos em pessoas
    fai_pessoas_agravo = (
        fai_agravo
        .group_by("co_fat_cidadao_pec")
        .agg(
            (pl.sum("n_infarto_agudo") >= 1).cast(pl.Int8).alias("n_infarto_agudo"),
            (pl.sum("n_acidente_vascular") >= 1).cast(pl.Int8).alias("n_acidente_vascular"),
            (pl.sum("n_coronariana") >= 1).cast(pl.Int8).alias("n_coronariana"),
            (pl.sum("n_cerebrovascular") >= 1).cast(pl.Int8).alias("n_cerebrovascular"),
            (pl.sum("n_renal") >= 1).cast(pl.Int8).alias("n_renal")
        )
    )





    pessoas_diabetes_agravo  =  pessoas_diabetes.join(
        fai_pessoas_agravo,
        on="co_fat_cidadao_pec",
        how="left"
    ).with_columns(
        pl.col("n_infarto_agudo").fill_null(0), 
        pl.col("n_acidente_vascular").fill_null(0), 
        pl.col("n_coronariana").fill_null(0), 
        pl.col("n_cerebrovascular").fill_null(0), 
        pl.col("n_renal").fill_null(0)
    )


    #pessoas_diabetes_agravo.height


    # ### separando informações de interesse exames - sem ciaps e cids, apenas procedimentos avaliados ou solicitados





    exames = (
        fai_cods
        .select("co_seq_fat_atd_ind","codigo","tipo")
        .filter(
            (pl.col('tipo') == "Procedimentos Avaliados") |  (pl.col('tipo') == "Procedimentos Solicitados")
        )
    )


    # ### Passo 7.2
    # 
    # 
    # obs.: Capturar a data do último atendimento identificado para compor a lista nominal



    fai_diabetes_6meses = (
        fai_v2
        .select("co_fat_cidadao_pec","co_seq_fat_atd_ind","dt_atendimento","co_dim_cbo_1","co_dim_cbo_2")
        .filter(
            (pl.col("co_dim_cbo_1").is_in(medicos_codigos) | pl.col("co_dim_cbo_2").is_in(medicos_codigos))  | (pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)) | (pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos))
        )
        .with_columns(

        (pl.col("co_dim_cbo_1").is_in(medicos_codigos) | pl.col("co_dim_cbo_2").is_in(medicos_codigos)).alias("is_medico"),
            
        (pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos) | pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos)).alias("is_enfermeiro")

        )
        .group_by("co_fat_cidadao_pec")
        .agg(

            pl.col("dt_atendimento").filter(pl.col("is_medico")).max().alias("data_ultimo_medico"),
            pl.col("dt_atendimento").filter(pl.col("is_enfermeiro")).max().alias("data_ultimo_enfermeiro"),
            
            ((pl.col("is_medico") & (pl.col("dt_atendimento") >= dt_6meses)).any()).alias("tem_medico_6m"),
            ((pl.col("is_enfermeiro") & (pl.col("dt_atendimento") >= dt_6meses)).any()).alias("tem_enfermeiro_6m"),
            
            pl.col("dt_atendimento").filter(
                (pl.col("is_medico") & (pl.col("dt_atendimento") >= dt_6meses)) |
                (pl.col("is_enfermeiro") & (pl.col("dt_atendimento") >= dt_6meses))
            ).count().alias("total_consulta_med_enferm")
        )
        .with_columns(
            
            (pl.col("tem_medico_6m") | pl.col("tem_enfermeiro_6m")).cast(pl.Int8).alias("agg_medicos_enfermeiros"),
            
            pl.max_horizontal("data_ultimo_medico", "data_ultimo_enfermeiro").alias("dt_ultima_consulta_med_enferm"),
        )
        .with_columns(    
            pl.when(pl.col("dt_ultima_consulta_med_enferm") == pl.col("data_ultimo_medico"))
            .then(pl.lit("medico"))
            .when(pl.col("dt_ultima_consulta_med_enferm") == pl.col("data_ultimo_enfermeiro"))
            .then(pl.lit("enfermeiro"))
            .otherwise(None)
            .alias("tipo_ultima_consulta"),
    )
    ).select("co_fat_cidadao_pec","agg_medicos_enfermeiros","dt_ultima_consulta_med_enferm","tipo_ultima_consulta",'total_consulta_med_enferm')


    # ### Passo 7.3
    # 
    # 
    # obs.: Capturar a data do último procedimento identificado para compor a lista nominal



    fao_filtrado = fao.filter(pl.col('ds_filtro_procedimentos').str.contains(r"\|0301100039\|"))
    fai_cods_filtrado = fai_cods.filter((pl.col('tipo')=='Procedimentos Avaliado') & (pl.col('codigo')=='0301100039'))
    proced_atend_filtrado = proced_atend.filter(pl.col('ds_filtro_procedimento').str.contains(r"\|0301100039\|")).rename({"ds_filtro_procedimento": "ds_filtro_procedimentos"})

    fai_filtrado = fai.join(fai_cods_filtrado, on='co_seq_fat_atd_ind', how="left")

    pa_concatenado = pl.concat([fao_filtrado, fai_filtrado, proced_atend_filtrado], how="diagonal")

    afericao_pa = (
        pa_concatenado
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null())
        )
        .filter(
            pl.col("co_dim_cbo").is_in(cbo_afericao_pa)
        )
        .with_columns(
            pl.when(
                pl.col("ds_filtro_procedimentos").str.contains(afericao_pa_codigos)
            )
            .then(1)
            .otherwise(0)
            .alias("afericao_pa")
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("afericao_pa").alias("agg_afericao_pa_semdata"),
            pl.col("dt_atendimento")
                .filter(pl.col("afericao_pa") == 1)
                .max()
                .alias("dt_ultima_afericao_pa")
        )
        .with_columns(

            pl.when(
                (pl.col("dt_ultima_afericao_pa") >= calcular_data(6) ) &
                (pl.col("agg_afericao_pa_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_afericao_pa"),
        )
    ).select("co_fat_cidadao_pec","agg_afericao_pa","dt_ultima_afericao_pa")

    #afericao_pa.head()


    # ### Passo 7.4.
    # 
    # 
    # obs.: Capturar a quantidade de visitas para compor a lista nominal



    visita_asc = (
        fat_vis_dom
        .select([
            "co_seq_fat_visita_domiciliar", "co_fat_cidadao_pec", "co_dim_tempo", "co_dim_cbo"
        ])
        .with_columns(
            # Converter `co_dim_tempo` para datetime e criar `dt_atendimento`
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null()) &
            (pl.col("co_dim_cbo").is_in(acs_tacs))
        )
        .group_by("co_fat_cidadao_pec")
        .agg([
            pl.col("dt_atendimento").len().alias("n_visitas_domiciliares_acs"),
            pl.min("dt_atendimento").alias("min_date"),
            pl.max("dt_atendimento").alias("max_date"),
            pl.col("dt_atendimento").max().alias("dt_ultima_visita_domiciliar_acs"),
        ])
        .with_columns(
            (pl.col("max_date") - pl.col("min_date")).dt.total_days().alias("diff_dias")
        )
        .with_columns(
                pl.when(
                (pl.col("n_visitas_domiciliares_acs") >= 2) &
                (pl.col("diff_dias") >= 30) &
                (pl.col("max_date") >= calcular_data(12))
            )
            .then(1)
            .otherwise(0)
            .alias("agg_visitas_domiciliares_acs"),
        )
    ).select("co_fat_cidadao_pec", "agg_visitas_domiciliares_acs", "dt_ultima_visita_domiciliar_acs", "n_visitas_domiciliares_acs")


    # ### Passo 7.5
    # 
    # 
    # obs.: Capturar a data do último registro identificado de cada tipo de colesterol (Total, HDL e LDL) para compor a lista nominal



    #### boas praticas colesterol



    fai_exames_colesterol = (
        fai_v2
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null())
        )
        .join(
            exames,
            on="co_seq_fat_atd_ind",
            how="left"  
        )
        .filter(
                (pl.col("co_dim_cbo_1").is_in(ex_cbo_colesterol) ) |
                (pl.col("co_dim_cbo_2").is_in(ex_cbo_colesterol) )
        )
        .with_columns(
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(colesterol_total) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("colesterol_total"),

            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(colesterol_hdl) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("colesterol_hdl"),

            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(colesterol_ldl) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("colesterol_ldl"),
            
        

            
        )
        
    )




    #### boas praticas colesterol
    fai_exames_colesterol_grouped = (
        fai_exames_colesterol
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("colesterol_total").alias("agg_colesterol_total_semdata"),
            pl.max("colesterol_hdl").alias("agg_colesterol_hdl_semdata"),
            pl.max("colesterol_ldl").alias("agg_colesterol_ldl_semdata"),

            pl.col("dt_atendimento")
                .filter(pl.col("colesterol_total") == 1)
                .max()
                .alias("dt_ultima_colesterol_total"),

            pl.col("dt_atendimento")
                .filter(pl.col("colesterol_hdl") == 1)
                .max()
                .alias("dt_ultima_colesterol_hdl"),

            pl.col("dt_atendimento")
                .filter(pl.col("colesterol_ldl") == 1)
                .max()
                .alias("dt_ultima_colesterol_ldl")
                
        
        )
        .with_columns(

            pl.when(
                (pl.col("dt_ultima_colesterol_ldl") >= calcular_data(12) ) &
                (pl.col("agg_colesterol_ldl_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_colesterol_ldl"),

            pl.when(
                (pl.col("dt_ultima_colesterol_hdl") >= calcular_data(12) ) &
                (pl.col("agg_colesterol_hdl_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_colesterol_hdl"),

            pl.when(
                (pl.col("dt_ultima_colesterol_total") >= calcular_data(12) ) &
                (pl.col("agg_colesterol_total_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_colesterol_total"),
        ).with_columns(
            
            pl.when(
                (pl.col("agg_colesterol_total") == 1 ) &
                (pl.col("agg_colesterol_hdl") == 1 ) &
                (pl.col("agg_colesterol_ldl") == 1 ) 
            )
            .then(1)
            .otherwise(0)
            .alias("agg_colesterol")
            
        )
        
    )


    # ### Passo. 7.6
    # 
    # 
    # obs.: Capturar a data do último registro identificado para compor a lista nominal



    fai_exames_creatinina_grouped = (
        fai_v2
        .join(
            exames,
            on="co_seq_fat_atd_ind",
            how="left"
        )
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null())
        )
        .filter(
                (pl.col("co_dim_cbo_1").is_in(creatina_cbo) ) |
                (pl.col("co_dim_cbo_2").is_in(creatina_cbo) )
        )
        .with_columns(
            pl.when(
                ((pl.col("tipo") == "Procedimentos Avaliados") &
                (pl.col("codigo").is_in(creatinina_codigos))
                )
            )
            .then(1)
            .otherwise(0)
            .alias("creatinina"),
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("creatinina").alias("agg_creatinina_semdata"),
            pl.col("dt_atendimento")
            .filter(pl.col("creatinina") == 1)
            .max()
            .alias("dt_ultimo_creatinina"),
        )
        .with_columns(

            pl.when(
                (pl.col("dt_ultimo_creatinina") >= calcular_data(12) ) &
                (pl.col("agg_creatinina_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_creatinina"),
        )
    ).select("co_fat_cidadao_pec","agg_creatinina","dt_ultimo_creatinina")


    # ### Passo 7.7
    # 
    # 
    # obs.: Capturar a data do último registro identificado para compor a lista nominal




    fai_hemo = fai_v2.join(fai_cods, on='co_seq_fat_atd_ind', how="left")
    hemoglobina_filtrada = (
    fai_hemo
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null())
        )
        .filter(
            (pl.col("co_dim_cbo_1").is_in(hemoglo_cbo)) |
            (pl.col("co_dim_cbo_2").is_in(hemoglo_cbo))
        )
    )
    reg_hemoglobina = (
        hemoglobina_filtrada
        .with_columns(
            pl.when(
                ((pl.col("tipo") == "Procedimentos Avaliados") &
                (pl.col("codigo").is_in(hemoglobina_codigos)))
            )
            .then(1)
            .otherwise(0)
            .alias("hemoglobina_avaliado"),
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("hemoglobina_avaliado").alias("agg_hemoglobina_avaliado_semdata"),
            pl.col("dt_atendimento")
            .filter(pl.col("hemoglobina_avaliado") == 1)
            .max()
            .alias("dt_ultima_hemoglobina_avaliado")
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultima_hemoglobina_avaliado") >= calcular_data(12) ) &
                (pl.col("agg_hemoglobina_avaliado_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_hemoglobina"),
        )
    ).select("co_fat_cidadao_pec","agg_hemoglobina","dt_ultima_hemoglobina_avaliado")


    # ### Passo 7.8
    # 
    # 
    # obs.: Capturar a data do último registro identificado para compor a lista nominal
    # 



    fai_cods_filtrado = fai_cods.filter((pl.col('tipo')=='Procedimentos Avaliado') & (pl.col('codigo').is_in(pe_diabetico_codigos) ) ).select("co_seq_fat_atd_ind","tipo","codigo")

    proced_atend_filtrado = (proced_atend
                            .filter(pl.col('ds_filtro_procedimento').str.contains(r"\|0301040095\|"))
                            .rename({"ds_filtro_procedimento": "codigo","co_dim_cbo": "co_dim_cbo_1"})
                            .with_columns(
                                pl.lit("proced").alias("tb"),
                                pl.lit("Procedimentos Avaliados").alias("tipo"),
                                pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
                            )
                            ).select("co_fat_cidadao_pec","codigo","tipo","co_dim_cbo_1","tb","dt_atendimento")

    fai_filtrado = (fai_v2
                    .join(fai_cods_filtrado, on='co_seq_fat_atd_ind', how="left")
                    .with_columns(pl.lit("fai").alias("tb"))
                    .select("co_fat_cidadao_pec","co_dim_cbo_1","co_dim_cbo_2","dt_atendimento","tipo","codigo","tb")
                )

    pa_pe = pl.concat([fai_filtrado, proced_atend_filtrado], how="diagonal")







    grouped_pe = (
        pa_pe
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null())
        )
        .filter(
            (pl.col("co_dim_cbo_1").is_in(pe_cbo)) |
            (pl.col("co_dim_cbo_2").is_in(pe_cbo))
        )
        .with_columns(
            pl.when(
                ((pl.col("tipo") == "Procedimentos Avaliados") &
                (pl.col("codigo").is_in(pe_diabetico_codigos))
                )
            )
            .then(1)
            .otherwise(0)
            .alias("exame_pe")
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("exame_pe").alias("agg_exame_pe"),
            pl.col("dt_atendimento")
            .filter(pl.col("exame_pe") == 1)
            .max()
            .alias("dt_ultimo_pe"),
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultimo_pe") >= calcular_data(12)) &
                (pl.col("agg_exame_pe") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_exame_pe"),
        )
    ).select("co_fat_cidadao_pec","agg_exame_pe","dt_ultimo_pe")


    # ### Passo 7.9
    # 
    # 
    # obs.: Capturar a data do último atendimento odontológico identificado para compor a lista nominal



    fao_v2 = (
        fao
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            pl.col("co_fat_cidadao_pec").is_not_null()
        ))

    #fao_v2.height
        




    fao_atend_odonto = (
        fao_v2
        .with_columns(
            pl.when(
                (pl.col("co_dim_cbo_1").is_in(cirurgioes_dentistas_codigos)) |
                (pl.col("co_dim_cbo_2").is_in(cirurgioes_dentistas_codigos))
            )
            .then(1)
            .otherwise(0)
            .alias("cirurgiao_dentista"),
        )
        .sort("dt_atendimento", descending=True)
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("cirurgiao_dentista")
            .filter(pl.col("dt_atendimento") >= calcular_data(12))
            .max()
            .alias("agg_cirurgiao_dentista"),

            # Ultima data de atendimento sem restrigir o tempo
            pl.col("dt_atendimento")
            .max()
            .alias("dt_ultimo_atend_odonto"),

            pl.len().alias("n_atend_odonto")
        )
    )


    # ### dados plot exames



    #opcao 1
    #para o grafico de exames a creatinina deve ser feita dessa forma? igual ao indicador da lista nominal?

    fai_exames = (
        fai_v3  #fai v3 ja tem filtro de 12 meses
        .join(
            exames,
            on="co_seq_fat_atd_ind",
            how="left"  
        )
        .with_columns(
            #creatinina
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(creatinina_codigos) ) &  (  (pl.col("co_dim_cbo_1").is_in(creatina_cbo) ) | (pl.col("co_dim_cbo_2").is_in(creatina_cbo) )    )  )
            )
            .then(1)
            .otherwise(0)
            .alias("creatinina_solicitada"),

            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(creatinina_codigos) ) &  (  (pl.col("co_dim_cbo_1").is_in(creatina_cbo) ) | (pl.col("co_dim_cbo_2").is_in(creatina_cbo) )    )  )
            )
            .then(1)
            .otherwise(0)
            .alias("creatinina_avaliada"),
    

            #hemograma
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(hemograma_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("hemograma_solicitada"),
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(hemograma_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("hemograma_avaliada") ,

            #hemoglobina glicada
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(hemoglobina_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("hemob_glica_solicitada"),
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(hemoglobina_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("hemob_glica_avaliada"),

            #eas equ
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(eas_equ_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("eas_equ_solicitada"),
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(eas_equ_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("eas_equ_avaliada"),

            #glicemia
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(glicemia_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("glicemia_solicitada"),
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(glicemia_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("glicemia_avaliada"),
            

            #retinografia 
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(retinografia_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("retino_solicitada"),
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(retinografia_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("retino_avaliada"),


            #colesterol
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Solicitados") & ( pl.col("codigo").is_in(colesterol_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("colesterol_solicitada"),
            
            pl.when(
                (  (pl.col("tipo") == "Procedimentos Avaliados") & ( pl.col("codigo").is_in(colesterol_codigos) ) )
            )
            .then(1)
            .otherwise(0)
            .alias("colesterol_avaliada"),  

            
        )
        
    )




    ### plot situação dos exames 12 meses

    fai_plot_exames_grouped = (
        fai_exames
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("creatinina_solicitada").alias("agg_creatinina_solicitada"),
            pl.max("creatinina_avaliada").alias("agg_creatinina_avaliada"),
            
            pl.max("colesterol_solicitada").alias("agg_colesterol_solicitada"),
            pl.max("colesterol_avaliada").alias("agg_colesterol_avaliada"),
            
            pl.max("hemograma_solicitada").alias("agg_hemograma_solicitada"),
            pl.max("hemograma_avaliada").alias("agg_hemograma_avaliada"),
            
            pl.max("hemob_glica_solicitada").alias("agg_hemob_glica_solicitada"),
            pl.max("hemob_glica_avaliada").alias("agg_hemob_glica_avaliada"),
            
            pl.max("eas_equ_solicitada").alias("agg_eas_equ_solicitada"),
            pl.max("eas_equ_avaliada").alias("agg_eas_equ_avaliada"),

            pl.max("glicemia_solicitada").alias("agg_glicemia_solicitada"),
            pl.max("glicemia_avaliada").alias("agg_glicemia_avaliada"),

            pl.max("retino_solicitada").alias("agg_retino_solicitada"),
            pl.max("retino_avaliada").alias("agg_retino_avaliada"),
        )
        .with_columns(
            pl.when(
                    (pl.col("agg_creatinina_solicitada") == 1) & (pl.col("agg_creatinina_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_creatinina_solicitada") == 0) & (pl.col("agg_creatinina_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_creatinina_solicitada") == 1) & (pl.col("agg_creatinina_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)  # Para o caso onde ambos são 0
                .alias("creatinina"),
            
            pl.when(
                    (pl.col("agg_colesterol_solicitada") == 1) & (pl.col("agg_colesterol_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_colesterol_solicitada") == 0) & (pl.col("agg_colesterol_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_colesterol_solicitada") == 1) & (pl.col("agg_colesterol_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)  
                .alias("colesterol"),

            pl.when(
                    (pl.col("agg_hemograma_solicitada") == 1) & (pl.col("agg_hemograma_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_hemograma_solicitada") == 0) & (pl.col("agg_hemograma_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_hemograma_solicitada") == 1) & (pl.col("agg_hemograma_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)  
                .alias("hemograma")  ,

            pl.when(
                    (pl.col("agg_hemob_glica_solicitada") == 1) & (pl.col("agg_hemob_glica_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_hemob_glica_solicitada") == 0) & (pl.col("agg_hemob_glica_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_hemob_glica_solicitada") == 1) & (pl.col("agg_hemob_glica_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)
                .alias("hemob_glica")  ,


            pl.when(
                    (pl.col("agg_eas_equ_solicitada") == 1) & (pl.col("agg_eas_equ_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_eas_equ_solicitada") == 0) & (pl.col("agg_eas_equ_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_eas_equ_solicitada") == 1) & (pl.col("agg_eas_equ_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)
                .alias("eas_equ")  ,

            pl.when(
                    (pl.col("agg_glicemia_solicitada") == 1) & (pl.col("agg_glicemia_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_glicemia_solicitada") == 0) & (pl.col("agg_glicemia_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_glicemia_solicitada") == 1) & (pl.col("agg_glicemia_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)
                .alias("glicemia"),

            pl.when(
                    (pl.col("agg_retino_solicitada") == 1) & (pl.col("agg_retino_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_retino_solicitada") == 0) & (pl.col("agg_retino_avaliada") == 1)
                )
                .then(3)
                .when(
                    (pl.col("agg_retino_solicitada") == 1) & (pl.col("agg_retino_avaliada") == 0)
                )
                .then(2)
                .otherwise(1)
                .alias("retino"),


            
        )
        
    )


    # ### dados plot profissional 






    fai_prof = fai_v2.select(
        [
            "co_fat_cidadao_pec", "co_dim_tempo",
            "co_dim_cbo_1", "co_dim_cbo_2", 
            "dt_nascimento", "nu_peso","nu_altura"
        ]
    ).with_columns(
        pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
        ).filter(
            pl.col("dt_atendimento") >= dt_12meses
        ).with_columns(
        pl.when(
            (pl.col("co_dim_cbo_1").is_in(medicos_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(medicos_codigos))
        ).then(1).otherwise(0).alias("medicos"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(cirurgioes_dentistas_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(cirurgioes_dentistas_codigos))
        ).then(1).otherwise(0).alias("cirug_dentista"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(farmaceuticos_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(farmaceuticos_codigos))
        ).then(1).otherwise(0).alias("farmaceuticos"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(fisioterapeutas_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(fisioterapeutas_codigos))
        ).then(1).otherwise(0).alias("fisioterapeutas"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(nutricionistas_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(nutricionistas_codigos))
        ).then(1).otherwise(0).alias("nutricionistas"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(fonoaudiologos_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(fonoaudiologos_codigos))
        ).then(1).otherwise(0).alias("fonoaudiologos"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(terapeutas_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(terapeutas_codigos))
        ).then(1).otherwise(0).alias("terapeutas_ocupacionais"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(educacao_fisica_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(educacao_fisica_codigos))
        ).then(1).otherwise(0).alias("educação_fisica"),

    ## pl.when(
    ##     (pl.col("co_dim_cbo_1").is_in(integrativa_complementar_codigos)) |
    #     (pl.col("co_dim_cbo_2").is_in(integrativa_complementar_codigos))
    # ).then(1).otherwise(0).alias("INTEGRATIVA E COMPLEMENTAR"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(psicologos_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(psicologos_codigos))
        ).then(1).otherwise(0).alias("psicologos"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(assistentes_sociais_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(assistentes_sociais_codigos))
        ).then(1).otherwise(0).alias("assist_sociais"),

        pl.when(
            (pl.col("co_dim_cbo_1").is_in(enfermeiros_codigos)) |
            (pl.col("co_dim_cbo_2").is_in(enfermeiros_codigos))
        ).then(1).otherwise(0).alias("enfermeiros"),

        pl.when(
            (~pl.col("co_dim_cbo_1").is_in(todos_codigos)) &
            (~pl.col("co_dim_cbo_2").is_in(todos_codigos))
        ).then(1).otherwise(0).alias("bin_outros")
    )




    # dados plot estratificação por profissional agregados


    grouped_fai_estratif = fai_prof.group_by("co_fat_cidadao_pec").agg([

        pl.sum("medicos").alias("total_medicos"),
        pl.sum("cirug_dentista").alias("total_cirug_dentista"),
        pl.sum("farmaceuticos").alias("total_farmaceuticos"),
        pl.sum("fisioterapeutas").alias("total_fisioterapeutas"),
        pl.sum("nutricionistas").alias("total_nutricionistas"),
        pl.sum("fonoaudiologos").alias("total_fonoaudiologos"),
        pl.sum("terapeutas_ocupacionais").alias("total_terapeutas_ocupacionais"),
        pl.sum("educação_fisica").alias("total_educação_fisica"),
        #pl.sum("INTEGRATIVA E COMPLEMENTAR").alias("Total_INTEGRATIVA_COMPLEMENTAR"),
        pl.sum("psicologos").alias("total_psicologos"),
        pl.sum("assist_sociais").alias("total_assist_sociais"),
        pl.sum("enfermeiros").alias("total_enfermeiros"),
        pl.sum("bin_outros").alias("total_outros"),
        pl.len().alias("n_atendimentos_12_meses")
    ])


    # ### criando idade e faixa etaria - joins e select final



    # criar idade e faixa etaria

    today = date.today()

    pessoas_diabetes_agravo_v2 = pessoas_diabetes_agravo.join(
        grouped_fai_estratif,
        on="co_fat_cidadao_pec",
        how="left"  
    ).with_columns(
        pl.col("dt_nascimento_cidadao").str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nasc_cidadao"),
        pl.when(
            pl.col("n_atendimentos_12_meses") >= 1
        )
        .then(1)
        .otherwise(0)
        .alias("atendida_12_meses")
    ).with_columns(
                pl.when(
                    pl.date(pl.col("dt_nasc_cidadao").dt.year(), today.month, today.day) >= pl.col("dt_nasc_cidadao")
                )
                .then(today.year - pl.col("dt_nasc_cidadao").dt.year())
                .otherwise(today.year - pl.col("dt_nasc_cidadao").dt.year() - 1).cast(pl.Float32).alias("idade"),
    ).with_columns(
        pl.when((pl.col("idade") >= 0) & (pl.col("idade") <= 19)).then(pl.lit("0a19"))
        .when((pl.col("idade") >= 20) & (pl.col("idade") <= 29)).then(pl.lit("20a29"))
        .when((pl.col("idade") >= 30) & (pl.col("idade") <= 39)).then(pl.lit("30a39"))
        .when((pl.col("idade") >= 40) & (pl.col("idade") <= 49)).then(pl.lit("40a49"))
        .when((pl.col("idade") >= 50) & (pl.col("idade") <= 59)).then(pl.lit("50a59"))
        .when(pl.col("idade") >= 60).then(pl.lit("60mais"))
        .otherwise(pl.lit("idade_invalida"))
        .alias("faixa_etaria")
    )


    pessoas_diabetes_agravo_v2.height 


    # ### Passo 7.10
    # 
    # 
    # 
    # obs.: Capturar a data do último registro identificado para compor a lista nominal
    # 



    fao_select = fao.select("co_fat_cidadao_pec","co_dim_tempo","co_dim_cbo_1","co_dim_cbo_2","nu_peso","nu_altura").with_columns(pl.lit("fao").alias("tb"))

    fai_select = fai_v2.select("co_fat_cidadao_pec","co_dim_tempo","co_dim_cbo_1","co_dim_cbo_2","nu_peso","nu_altura").with_columns(pl.lit("fai").alias("tb"))

    proced_atend_select = (proced_atend
                        .select("co_fat_cidadao_pec","co_dim_tempo","co_dim_cbo","nu_peso","nu_altura")
                        .rename({"co_dim_cbo": "co_dim_cbo_1"})
                        .with_columns(pl.lit("proced").alias("tb"))
                        )
                        

    fac_select = (
        tb_atv_coletv_part
        .rename({"co_dim_cbo": "co_dim_cbo_1",'nu_participante_peso': 'nu_peso', 'nu_participante_altura': 'nu_altura'})
        .select("co_fat_cidadao_pec","co_dim_tempo","nu_peso","nu_altura","co_dim_cbo_1")
        .with_columns(pl.lit("fac").alias("tb"),
                    pl.col("co_dim_cbo_1").cast(pl.Utf8).alias("co_dim_cbo_1"))
    )





    peso_altura = pl.concat([proced_atend_select,fao_select,fai_select,fac_select  ], how="diagonal") 

    idade_pessoas = pessoas_diabetes_agravo_v2.select("dt_nascimento_cidadao","co_fat_cidadao_pec")


    peso_altura_imc = peso_altura.join(
        idade_pessoas,
        on="co_fat_cidadao_pec",
        how="inner" 
    )

    reg_peso_altura = (
        peso_altura
        .with_columns(
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento")
        )
        .filter(
            (pl.col("co_fat_cidadao_pec").is_not_null())
        )
        .filter(
            (pl.col('nu_peso').is_not_null()) &
            (pl.col('nu_altura').is_not_null())
        )
        .filter(
            (pl.col("co_dim_cbo_1").is_in(peso_altura_cbo)) |
            (pl.col("co_dim_cbo_2").is_in(peso_altura_cbo))
        )
        .with_columns(
            pl.lit(1).alias("peso_altura"),
        )
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.max("peso_altura").alias("agg_peso_altura_semdata"),
            
            pl.col("dt_atendimento")
            .filter(pl.col("peso_altura") == 1)
            .max()
            .alias("dt_ultima_peso_altura")
        )
        .with_columns(
            pl.when(
                (pl.col("dt_ultima_peso_altura") >= calcular_data(12) ) &
                (pl.col("agg_peso_altura_semdata") == 1)
            )
            .then(1)
            .otherwise(0)
            .alias("agg_peso_altura"),
        )
    ).select("co_fat_cidadao_pec","dt_ultima_peso_altura","agg_peso_altura")






    imc_grouped = (
        peso_altura_imc
        .with_columns(
            pl.col("dt_nascimento_cidadao").str.strptime(pl.Date, "%Y-%m-%d").alias("dt_nasc_cidadao"),
            pl.col("co_dim_tempo").cast(pl.Utf8).str.strptime(pl.Date, "%Y%m%d").alias("dt_atendimento"),
        )
        .with_columns(
            
            pl.when(
                        pl.col("dt_atendimento") >= pl.date(
                            pl.col("dt_atendimento").dt.year(),
                            pl.col("dt_nasc_cidadao").dt.month(),
                            pl.col("dt_nasc_cidadao").dt.day()
                        )
                    )
                    .then(pl.col("dt_atendimento").dt.year() - pl.col("dt_nasc_cidadao").dt.year())
                    .otherwise(pl.col("dt_atendimento").dt.year() - pl.col("dt_nasc_cidadao").dt.year() - 1)
                    .cast(pl.Float32)
                    .alias("idade")
        )
        .filter(
            pl.col("dt_atendimento") >= dt_12meses
        )
        .filter(
            (pl.col("nu_peso").is_not_null() ) & ( pl.col("nu_altura").is_not_null() )
        )

        .filter(
            (pl.col("idade") >= 20 ) & ( pl.col("idade") <= 60 )
        )
        .sort("dt_atendimento",descending = True)
        .group_by("co_fat_cidadao_pec")
        .agg(
            pl.col("nu_peso").first().alias("nu_peso_mais_recente_quilos"),
            pl.col("nu_altura").first().alias("nu_altura_mais_recente"),
        )
        .with_columns(
            (pl.col("nu_altura_mais_recente") / 100).alias("nu_altura_mais_recente_metros")
        )
        .with_columns(
            (pl.col("nu_peso_mais_recente_quilos") / (pl.col("nu_altura_mais_recente_metros") ) ** 2).round(1).alias("imc")
        )
        .with_columns(
            pl.when(pl.col("imc") < 18.5).then(pl.lit("baixo_peso"))
            .when((pl.col("imc") >= 18.5) & (pl.col("imc") <= 24.9)).then(pl.lit("peso_adequado"))
            .when((pl.col("imc") >= 25) & (pl.col("imc") <= 29.9)).then(pl.lit("excesso_peso"))
            .when((pl.col("imc") >= 30) ).then(pl.lit("obesidade"))
            .otherwise(pl.lit("na_outros"))
            .alias("imc_categoria") 
        ).select("imc_categoria","co_fat_cidadao_pec")
    )


    # Passo 8. Criar tabela pessoa final com todas as variáveis necessárias para próximas etapas de desenvolvimento do Painel



    # Juntando informações Unidade de Saúde e Equipe

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




    pessoas_diabetes_agravo_v3 = pessoas_diabetes_agravo_v2.join(
        fao_atend_odonto,
        on="co_fat_cidadao_pec",
        how="left"     
    ).join(
        fai_plot_exames_grouped,
        on="co_fat_cidadao_pec",
        how="left"     
    ).join(
        visita_asc,
        on="co_fat_cidadao_pec",
        how="left"     

    ).join(
        fai_exames_colesterol_grouped,
        on="co_fat_cidadao_pec",
        how="left"   
    ).join(
        reg_peso_altura,
        on="co_fat_cidadao_pec",
        how="left"   

    ).join(
        fai_exames_creatinina_grouped,
        on="co_fat_cidadao_pec",
        how="left"     

    ).join(
        grouped_pe,
        on="co_fat_cidadao_pec",
        how="left"
    ).join(
        afericao_pa,
        on="co_fat_cidadao_pec",
        how="left"
    ).join(
        fai_diabetes_6meses,
        on="co_fat_cidadao_pec",
        how="left"   
    ).join(
        reg_hemoglobina,
        on="co_fat_cidadao_pec",
        how="left"  
    ).join(
        imc_grouped,
        on="co_fat_cidadao_pec",
        how="left" 
    ).with_columns([
        pl.col("imc_categoria").fill_null("na_outros"),  
        pl.col("n_atend_odonto").fill_null(0), 
        
        pl.col("agg_afericao_pa").fill_null(0), 
        pl.col("agg_medicos_enfermeiros").fill_null(0), 
        pl.col("agg_visitas_domiciliares_acs").fill_null(0),
        pl.col("agg_cirurgiao_dentista").fill_null(0),
        pl.col("agg_colesterol_total").fill_null(0),
        pl.col("agg_colesterol_hdl").fill_null(0),
        pl.col("agg_colesterol_ldl").fill_null(0),
        pl.col("agg_peso_altura").fill_null(0),
        pl.col("agg_hemoglobina").fill_null(0),
        pl.col("agg_creatinina").fill_null(0),
        pl.col("agg_exame_pe").fill_null(0),


        pl.col("creatinina").fill_null(1),
        pl.col("colesterol").fill_null(1),
        pl.col("hemograma").fill_null(1),
        pl.col("hemob_glica").fill_null(1),
        pl.col("eas_equ").fill_null(1),
        pl.col("glicemia").fill_null(1),
        pl.col("retino").fill_null(1),
    

        
        pl.col("n_atendimentos_12_meses").fill_null(0), 
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
    pessoas_diabetes_agravo_v3 = pessoas_diabetes_agravo_v3.with_columns(expressoes)




    lista_vars_final = ['co_fat_cidadao_pec',
                        'nu_cns_cidadao',
                        'nu_cpf_cidadao',
                        'no_sexo_cidadao',
                        'dt_nasc_cidadao',
                        'no_tipo_logradouro',
                        'ds_logradouro',
                        'nu_numero',
                        'ds_cep',
                        'ds_complemento',
                        'no_bairro',
                        'diabetes',
                        'autoreferido',
                        'telefone',
                        'no_cidadao',
                        'nu_micro_area',
                        'co_dim_unidade_saude',
                        'nome_unidade_saude',
                        'codigo_equipe',
                        'nome_equipe',
                        'ds_raca_cor',
                        'ds_tipo_localizacao_domicilio',
                        'agg_afericao_pa',
                        'dt_ultima_afericao_pa',
                        'agg_visitas_domiciliares_acs',
                        'dt_ultima_visita_domiciliar_acs',
                        'dt_ultimo_atend_odonto',
                        'agg_cirurgiao_dentista',
                        'agg_colesterol_total',
                        'dt_ultima_colesterol_total',
                        'agg_colesterol_hdl',
                        'dt_ultima_colesterol_hdl',
                        'agg_colesterol_ldl',
                        'dt_ultima_colesterol_ldl',
                        'agg_colesterol',
                        'agg_medicos_enfermeiros',
                        'tipo_ultima_consulta',
                        'dt_ultima_consulta_med_enferm',
                        'total_consulta_med_enferm',
                        'dt_primeiro_reg_condicao',
                        'diabetes_codigos_1atend',
                        'idade',
                        'faixa_etaria',
                        'imc_categoria',
                        'n_infarto_agudo',
                        'n_acidente_vascular',
                        'n_coronariana',
                        'n_cerebrovascular',
                        'n_renal',
                        'total_medicos',
                        'total_cirug_dentista',
                        'total_farmaceuticos',
                        'total_fisioterapeutas',
                        'total_nutricionistas',
                        'total_fonoaudiologos',
                        'total_terapeutas_ocupacionais',
                        'total_educação_fisica',
                        'total_psicologos',
                        'total_assist_sociais',
                        'total_enfermeiros',
                        'total_outros',
                        'creatinina',
                        'colesterol',
                        'hemograma',
                        'eas_equ',
                        'glicemia',
                        'retino',
                        'hemob_glica',
                        'dt_ultima_peso_altura',
                        'agg_peso_altura',
                        'agg_hemoglobina',
                        'dt_ultima_hemoglobina_avaliado',
                        'agg_creatinina',
                        'dt_ultimo_creatinina',
                        'dt_ultimo_pe',
                        'agg_exame_pe',
                        'n_atendimentos_12_meses',
                        ]

    pessoas_diabetes_v3 = pessoas_diabetes_agravo_v3.select(lista_vars_final)
    pessoas_diabetes_v3.write_parquet(output_path+os.sep+"diabetes.parquet")
