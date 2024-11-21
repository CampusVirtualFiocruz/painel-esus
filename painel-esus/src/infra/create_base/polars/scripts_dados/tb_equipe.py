#!/usr/bin/env python
# coding: utf-8
# In[1]:
import time

start_time = time.time()


# In[2]:


# import glob
import os
from datetime import date, datetime
from pathlib import Path

import polars as pl

pl.Config.set_tbl_cols(100)
pl.Config.set_tbl_rows(1000)

working_directory  = os.getcwd()


input_path = os.path.join(working_directory, "dados", "input",os.sep) 
output_path = os.path.join(working_directory,"dados","output", os.sep) 


# ## ler dados

# In[4]:


fat_cidadao_pec = pl.read_parquet(input_path+"tb_fat_cidadao_pec.parquet")

fat_cad_ind = pl.read_parquet(input_path+"tb_fat_cad_individual.parquet")

fat_atd_ind = pl.read_parquet(input_path+"tb_fat_atendimento_individual.parquet")

fat_vis_dom = pl.read_parquet(input_path+"tb_fat_visita_domiciliar.parquet")

fat_atd_ind_odonto = pl.read_parquet(input_path+"tb_fat_atendimento_odonto.parquet")

fat_acomp_vinc = pl.read_parquet(input_path+"tb_acomp_cidadaos_vinculados.parquet")

fat_fam_terr = pl.read_parquet(input_path+"tb_fat_familia_territorio.parquet")

tb_dim_equipe = pl.read_parquet(input_path+"tb_dim_equipe.parquet")

tb_dim_und_saude = pl.read_parquet(input_path+"tb_dim_unidade_saude.parquet")

fat_vac = pl.read_parquet(input_path+"tb_fat_vacinacao.parquet")

fcdt = pl.read_parquet(input_path+"tb_fat_cad_domiciliar.parquet")

tb_pessoa = pl.read_csv( input_path+"pessoas.csv"),separator=";",ignore_errors=True)
tb_pessoa = tb_pessoa.with_columns(pl.col("cidadao_pec").cast(pl.Int64))

# ## Transformações

# ### tb unidade de saude

# In[5]:


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
            "co_seq_dim_unidade_saude": "codigo_unidade_saude",
            "co_seq_dim_unidade_saude": "co_dim_unidade_saude",
            "st_registro_valido": "st_registro_valido_und_saude",
            "no_unidade_saude": "nome_unidade_saude",
        }
    )
    .with_columns(
        [
            pl.col("codigo_unidade_saude")
            .str.replace_all("-", "")
            .cast(pl.Int32, strict=False)
            .alias("codigo_unidade_saude")
        ]
    )
)

tb_dim_und_saude_v3 = tb_dim_und_saude_v2.select('codigo_unidade_saude','nome_unidade_saude','st_registro_valido_und_saude','co_dim_unidade_saude')


# ### tb dim equipes

# In[6]:


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
        pl.col("nu_ine")
        .str.replace_all('-', "") 
        .cast(pl.Int32,strict=False).alias("nu_ine")
    ]).filter(pl.col("st_registro_valido_equipe") == 1)
)


# ### fci

# In[7]:


equipe_fci = (
    fat_cad_ind
    .filter(pl.col('co_fat_cidadao_pec').is_not_null())
    .select([
        'co_fat_cidadao_pec',
        'co_dim_equipe',
        'co_dim_unidade_saude',
        'co_dim_tempo',
        'nu_micro_area'
    ]).with_columns([
        pl.lit("fcp").alias('tabela'),
        pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d").alias("dt_last"),
    ]) .rename({
        'co_dim_equipe': 'codigo_equipe',
    })
     .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
     .join(tb_dim_equipe_v2,on="codigo_equipe",how='left') 
    .rename({
        'nu_micro_area': 'micro_area',
    })
     .unique(subset=['co_fat_cidadao_pec','codigo_equipe'],keep='last')
     .select(['co_fat_cidadao_pec',
             'codigo_equipe',
             'codigo_unidade_saude',
             'micro_area',
             'tabela',
             'nome_unidade_saude',
             'nome_equipe',
             'dt_last',
              'nu_ine',
             'co_dim_unidade_saude',
    ])
)


# ### fcp

# In[8]:


equipe_fcp = (
    fat_cidadao_pec
    .filter(pl.col('co_seq_fat_cidadao_pec').is_not_null())
    .select([
        'co_seq_fat_cidadao_pec',
        'co_dim_equipe_vinc',
        'co_dim_unidade_saude_vinc',
    ]).with_columns([
        pl.lit("fcp").alias('tabela'),
        pl.lit(None).alias('micro_area'),
        pl.lit(None).alias("dt_last"),
    ]).rename({
        'co_seq_fat_cidadao_pec': 'co_fat_cidadao_pec',
        'co_dim_unidade_saude_vinc': 'co_dim_unidade_saude',
        'co_dim_equipe_vinc': 'codigo_equipe',
    })
    .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
    .join(tb_dim_equipe_v2,on="codigo_equipe",how='left') 
    .unique(subset=['co_fat_cidadao_pec','codigo_equipe'])
    .filter(pl.col('codigo_equipe').is_not_null())
    .select(['co_fat_cidadao_pec',
             'codigo_equipe',
             'codigo_unidade_saude',
             'micro_area',
             'tabela',
             'nome_unidade_saude',
             'nome_equipe',
             'dt_last',
              'nu_ine',
             'co_dim_unidade_saude',
    ])
)


# In[9]:


# equipe_fcp.glimpse() # 19246 apos remover equipe vazia foi para 7730


# ### fai

# In[9]:


equipe_fai_inter = (
    fat_atd_ind
    .select([
        'co_fat_cidadao_pec',
        'co_dim_equipe_1',
        'co_dim_equipe_2',
        'co_dim_tempo',
        'co_dim_unidade_saude_1',
        'co_dim_unidade_saude_2'
    ])
    .filter(pl.col('co_fat_cidadao_pec').is_not_null())
    .with_columns([
        pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d").alias("dt_last_fai"),
    ])
)


# equipe_fai_inter.filter(pl.col("co_dim_equipe_1") != 1)
# equipe_fai_inter.filter(pl.col("co_dim_equipe_2") != 1)

df_equipe_1_fai = equipe_fai_inter.select([
    pl.col("co_fat_cidadao_pec"),
    pl.col("co_dim_equipe_1").alias("co_dim_equipe"),
    pl.col("dt_last_fai"),
    pl.col("co_dim_unidade_saude_1").alias("co_dim_unidade_saude")
])

df_equipe_2_fai = equipe_fai_inter.select([
    pl.col("co_fat_cidadao_pec"),
    pl.col("co_dim_equipe_2").alias("co_dim_equipe"),
    pl.col("dt_last_fai"),
    pl.col("co_dim_unidade_saude_2").alias("co_dim_unidade_saude")
])

equipe_fai = (pl.concat([df_equipe_1_fai, df_equipe_2_fai])
    .unique(subset=['co_fat_cidadao_pec','co_dim_equipe'])
    .rename({
        'co_dim_equipe': 'codigo_equipe',
    })
    .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
    .join(tb_dim_equipe_v2,on="codigo_equipe",how='left') 
    .with_columns([
        pl.lit("fai").alias('tabela'),
        pl.lit(None).alias('micro_area'),
        pl.col("dt_last_fai").alias("dt_last"),
        pl.col("co_fat_cidadao_pec").cast(pl.Int64)
    ]).select([
        'co_fat_cidadao_pec',
         'codigo_equipe',
         'codigo_unidade_saude',
         'micro_area',
         'tabela',
         'nome_unidade_saude',
         'nome_equipe',
         'dt_last',
         'nu_ine',
         'co_dim_unidade_saude',
    ])
)


# ### visita domiciliar

# In[10]:


### equipe visita domiciliar
equipe_vis_dom = (
    fat_vis_dom
    .filter(pl.col('co_fat_cidadao_pec').is_not_null())
    .select([
        'co_fat_cidadao_pec',
        'co_dim_equipe',
        'nu_micro_area',
        'co_dim_tempo',
        'co_dim_unidade_saude'
    ]).with_columns([
        pl.when(pl.col("nu_micro_area") == "--")
            .then(None)  # Substitui por null
            .otherwise(pl.col("nu_micro_area"))
            .alias("nu_micro_area"),
        pl.lit("vis_dom").alias('tabela'),
        pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d").alias("dt_last"),
        
    ]).rename({
        'co_dim_equipe': 'codigo_equipe',
        'nu_micro_area' : 'micro_area',
    }).unique(subset=['co_fat_cidadao_pec','codigo_equipe'])
    .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
    .join(tb_dim_equipe_v2,on="codigo_equipe",how='left') 
    .select([
        'co_fat_cidadao_pec',
         'codigo_equipe',
         'codigo_unidade_saude',
         'micro_area',
         'tabela',
         'nome_unidade_saude',
         'nome_equipe',
         'dt_last',
         'nu_ine',
         'co_dim_unidade_saude',
    ])
)


# ### atend odonto

# In[11]:


# atendimento indivi odonto

equipe_faio_inter = (
    fat_atd_ind_odonto
    .select([
        'co_fat_cidadao_pec',
        'co_dim_equipe_1',
        'co_dim_equipe_2',
        'co_dim_tempo',
        'co_dim_unidade_saude_1',
        'co_dim_unidade_saude_2'
    ])
    .filter(pl.col('co_fat_cidadao_pec').is_not_null())
    .with_columns([
        pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d").alias("dt_last"),
    ])
)

df_equipe_1_faio = equipe_faio_inter.filter(pl.col("co_dim_equipe_1") != 1).select([
    pl.col("co_fat_cidadao_pec"),
    pl.col("co_dim_equipe_1").alias("co_dim_equipe"),
    pl.col("dt_last"),
    pl.col("co_dim_unidade_saude_1").alias("co_dim_unidade_saude")
])

df_equipe_2_faio = equipe_faio_inter.filter(pl.col("co_dim_equipe_2") != 1).select([
    pl.col("co_fat_cidadao_pec"),
    pl.col("co_dim_equipe_2").alias("co_dim_equipe"),
    pl.col("dt_last"),
    pl.col("co_dim_unidade_saude_2").alias("co_dim_unidade_saude")
])

equipe_faio = (pl.concat([df_equipe_1_faio, df_equipe_2_faio])
    .unique(subset=['co_fat_cidadao_pec','co_dim_equipe'])
    .rename({
        'co_dim_equipe': 'codigo_equipe',
    })
    .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
    .join(tb_dim_equipe_v2,on="codigo_equipe",how='left')  
    .with_columns([
        pl.lit("faio").alias('tabela'),
        pl.lit(None).alias('micro_area'),
      #  pl.lit(None).alias('nome_equipe'),
        pl.lit(5).alias('prioridade'),
      #  pl.lit(None).alias('nome_unidade_saude')
                
    ])
    .select([
         'co_fat_cidadao_pec',
         'codigo_equipe',
         'codigo_unidade_saude',
         'micro_area',
         'tabela',
         'nome_unidade_saude',
         'nome_equipe',
         'dt_last',
         'nu_ine',
         'co_dim_unidade_saude',
    ])
)


# In[12]:


equipe_fam_terr = (
    fat_fam_terr
    .filter(pl.col('co_fat_cidadao_pec').is_not_null())
    .select([
        'co_fat_cidadao_pec',
        'co_dim_equipe',
        'nu_micro_area',
        'co_dim_tempo_fcd',
        'co_dim_unidade_saude'
    ]).with_columns([
        pl.when(pl.col("nu_micro_area") == "--")
            .then(None)  # Substitui por null
            .otherwise(pl.col("nu_micro_area"))
            .alias("nu_micro_area"),
        pl.lit("fam_terr").alias('tabela'),
        pl.col("co_dim_tempo_fcd").cast(pl.String).str.to_date("%Y%m%d").alias("dt_last"),
        
    ]).rename({
        'co_dim_equipe': 'codigo_equipe',
        'nu_micro_area' : 'micro_area',
        
    })
    .sort(['co_fat_cidadao_pec', 'dt_last'])
    .unique(subset=['co_fat_cidadao_pec','codigo_equipe'],keep='last')
    .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
    .join(tb_dim_equipe_v2,on="codigo_equipe",how='left') 
    .select([
        'co_fat_cidadao_pec',
         'codigo_equipe',
         'codigo_unidade_saude',
         'micro_area',
         'tabela',
         'nome_unidade_saude',
         'nome_equipe',
         'dt_last',
         'nu_ine',
         'co_dim_unidade_saude',
    ])
)


# ### fat vacinacao


equipe_vac = (
    fat_vac
    .filter(pl.col('co_fat_cidadao_pec').is_not_null())
    .select([
        'co_fat_cidadao_pec',
        'co_dim_equipe',
        #'nu_micro_area',
        'co_dim_tempo',
        'co_dim_unidade_saude'
    ]).with_columns([
        pl.lit("vac").alias('tabela'),
        pl.lit(None).alias('micro_area'),
        pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d").alias("dt_last"),
        
    ]).rename({
        'co_dim_equipe': 'codigo_equipe',
       # 'nu_micro_area' : 'micro_area',
        
    })
    .sort(['co_fat_cidadao_pec', 'dt_last'])
    .unique(subset=['co_fat_cidadao_pec','codigo_equipe'],keep='last')
    .join(tb_dim_und_saude_v3,on="co_dim_unidade_saude",how='left') 
    .join(tb_dim_equipe_v2,on="codigo_equipe",how='left') 
    .select([
        'co_fat_cidadao_pec',
         'codigo_equipe',
         'codigo_unidade_saude',
         'micro_area',
         'tabela',
         'nome_unidade_saude',
         'nome_equipe',
         'dt_last',
         'nu_ine',
         'co_dim_unidade_saude',
    ])
)


# ### acomp. vinculo

# In[15]:


# rename coluns

coluna_excluir = "co_seq_fat_cidadao_pec"


rename_dict = {col: (f"{col}_fat_cidacao_pec" if col != coluna_excluir else col) for col in fat_cidadao_pec.columns}

fat_cidadao_pec_renamed = fat_cidadao_pec.rename(rename_dict).select("co_cidadao_fat_cidacao_pec","co_seq_fat_cidadao_pec")


# In[16]:


fat_acomp_vinc_v2 = fat_acomp_vinc.join(
    fat_cidadao_pec_renamed,
    left_on='co_cidadao',
    right_on='co_cidadao_fat_cidacao_pec',
    how='inner'
).unique(subset="co_seq_fat_cidadao_pec").rename({"co_seq_fat_cidadao_pec" : "co_fat_cidadao_pec"}).with_columns(
    pl.col("nu_ine_vinc_equipe").cast(pl.Int32),
    pl.col("nu_cnes_vinc_equipe").cast(pl.Int32),
)


# In[17]:


equipe_acomp_vinc_inter = (
    fat_acomp_vinc_v2
    .select([
        'co_fat_cidadao_pec',
        'nu_cnes_vinc_equipe',
       # 'no_equipe_vinc_equipe',
        'nu_micro_area_tb_cidadao',
        'nu_micro_area_domicilio',
        'nu_ine_vinc_equipe',
        'st_usar_cadastro_individual',
        'dt_ultima_atualizacao_cidadao',
    ]).with_columns([
       # pl.lit("nu_ine_vinc_equipe").cast(pl.Int64).alias('nu_ine'),
        pl.col("dt_ultima_atualizacao_cidadao").cast(pl.String).str.to_date("%Y-%m-%d").alias("dt_last"),
        pl.col('nu_micro_area_tb_cidadao').cast(pl.String).alias('nu_micro_area_tb_cidadao'),
        pl.lit("acom_vinc").alias('tabela')
        
    ]).rename({
        'nu_ine_vinc_equipe' : 'nu_ine',
        'nu_micro_area_tb_cidadao': 'micro_area',
       # 'dt_ultima_atualizacao_cidadao': 'dt_last',
        'nu_cnes_vinc_equipe': 'codigo_unidade_saude',
    }).join(tb_dim_equipe_v2,on="nu_ine",how='left') 
    .join(tb_dim_und_saude_v2,on="codigo_unidade_saude",how='left') 
    .select([
         'co_fat_cidadao_pec',
         'codigo_equipe',
         'codigo_unidade_saude',
         'micro_area',
         'tabela',
         'nome_unidade_saude',
         'nome_equipe',
         'dt_last',
         'nu_ine',
         'co_dim_unidade_saude',
    ])
)


# In[18]:


tb_end = (
    fat_acomp_vinc_v2.
    select({
        'co_fat_cidadao_pec',
        'no_cidadao',
        'co_cidadao',
        'no_social_cidadao',
        'dt_nascimento_cidadao',
        'nu_cpf_cidadao',
        'nu_cns_cidadao',
        'dt_nascimento_cidadao',
        'no_sexo_cidadao',
        'tp_identidade_genero_cidadao',
        'nu_telefone_celular',
        'nu_telefone_contato',
        'nu_fone_residencial',
        'no_tipo_logradouro_tb_cidadao',
        'ds_logradouro_tb_cidadao',
        'nu_numero_tb_cidadao',
        'st_sem_numero_tb_cidadao',
        'ds_complemento_tb_cidadao',
        'no_municipio_tb_cidadao',
        'sg_uf_domicilio',
        'no_bairro_domicilio',
        'dt_ultima_atualizacao_cidadao',
        'ds_cep_tb_cidadao',
        'ds_cep_domicilio'
    }).with_columns(
        pl.concat_str(["no_tipo_logradouro_tb_cidadao", "ds_logradouro_tb_cidadao"], separator=" ").alias("endereco"),
        pl.coalesce(["nu_telefone_celular", "nu_telefone_contato","nu_fone_residencial"]).alias("telefone"),
        pl.coalesce(["ds_cep_tb_cidadao", "ds_cep_domicilio"]).alias("cep"),
        pl.col("no_bairro_domicilio")
          .str.replace_all(r'\s+', ' ')      # Substitui múltiplos espaços por um único espaço
         # .str.strip()                        # Remove espaços no início e no final
          .str.to_uppercase()                 # Converte para maiúsculas
          .alias("no_bairro_domicilio_clean"),
        
        
        pl.when(pl.col("no_bairro_domicilio").str.contains("ZONA RURAL"))
            .then(pl.lit("ZONA RURAL"))
            .when(
                (pl.col("no_bairro_domicilio").is_null() ) | 
                (pl.col("no_bairro_domicilio") == "" ))
            .then(None)
            .otherwise(pl.lit("ZONA URBANA")).alias("tipo_localidade")    
    )
)


# ## uniao e outras trasnformações

# In[20]:


equipe_inter = pl.concat([equipe_fci,equipe_fcp,equipe_fai,equipe_vis_dom,equipe_faio,equipe_acomp_vinc_inter,equipe_fam_terr,equipe_vac])


# ### criar contagens e last dt por pessoa-equipe-ficha , depois transformar em pessoa-equipe usando pivot

# In[21]:


contagens_p_e_f = (
     equipe_inter
    .group_by("co_fat_cidadao_pec","codigo_equipe","tabela")
    .agg([
        pl.len().alias("n"),
        pl.max("dt_last").alias("dt_last") 
    ])
)

pivot_contagem = contagens_p_e_f.pivot(
    values=['n','dt_last'],                  # Coluna com os valores a serem pivotados
    index=['co_fat_cidadao_pec', 'codigo_equipe'],# Colunas que serão usadas como índices
    on='tabela',            # Coluna cujos valores se tornarão novas colunas
    aggregate_function='first'   # Função de agregação (útil se houver duplicatas)
).fill_null(0)


# In[22]:


contagens_p_e_f.select(['co_fat_cidadao_pec', 'codigo_equipe']).unique().height


# In[23]:


equipe = (
    equipe_inter
    .unique(subset=["co_fat_cidadao_pec", "codigo_equipe"], keep="first") 
).join(pivot_contagem,on=['co_fat_cidadao_pec','codigo_equipe'] , how = 'left').rename({"co_fat_cidadao_pec":"cidadao_pec"}).with_columns(pl.col("cidadao_pec").cast(pl.Int64) )


# In[24]:


equipe_v2 = equipe.select("cidadao_pec","codigo_equipe","nome_equipe","codigo_unidade_saude","nome_unidade_saude","micro_area","nu_ine")


# In[27]:


equipe_pessoa = equipe_v2.join(tb_pessoa.select('cidadao_pec'),on ='cidadao_pec' , how ='inner')


equipe_pessoa.write_parquet(os.path.join(output_path, "equipe.parquet"))


end_time = time.time()
execution_time = end_time - start_time

print(f"Tempo total de execução equipe: {execution_time:.2f} segundos")


# In[31]:


# import os
# os.getcwd()
