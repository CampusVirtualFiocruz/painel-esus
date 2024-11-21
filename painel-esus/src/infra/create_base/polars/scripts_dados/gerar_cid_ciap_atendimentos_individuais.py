#!/usr/bin/env python
# coding: utf-8
# In[20]:
import os
from datetime import datetime

import polars as pl
from dateutil.relativedelta import relativedelta

pl.Config.set_tbl_cols(100)
pl.Config.set_tbl_rows(5000)


working_directory  = os.getcwd()



input_path = os.path.join(working_directory, "dados", "input") 

output_path = os.path.join(working_directory, "dados", "output")  


fai = pl.read_parquet(input_path+os.sep+"tb_fat_atendimento_individual.parquet")


# In[22]:


fai_v2 = fai.select("co_seq_fat_atd_ind","ds_filtro_cids","ds_filtro_ciaps","ds_filtro_proced_avaliados","ds_filtro_proced_solicitados")


# In[23]:


cids_df = (
    fai_v2
    .select([
        pl.col("co_seq_fat_atd_ind"),
        pl.col("ds_filtro_cids")
            .str.split("|")  # Divide a string em lista
            .alias("codigo")
    ])
    .explode("codigo")  # Expande a lista em linhas separadas
    .filter(pl.col("codigo") != "")  # Remove possíveis strings vazias
    .with_columns(pl.lit("CIDS").alias("tipo"))  # Adiciona coluna tipo
).sort("co_seq_fat_atd_ind")

proced_avaliados_df = (
    fai_v2
    .select([
        pl.col("co_seq_fat_atd_ind"),
        pl.col("ds_filtro_proced_avaliados")
            .str.split("|")  # Divide a string em lista
            .alias("codigo")
    ])
    .explode("codigo")  # Expande a lista em linhas separadas
    .filter(pl.col("codigo") != "")  # Remove possíveis strings vazias
    .with_columns(pl.lit("Procedimentos Avaliados").alias("tipo"))  # Adiciona coluna tipo
).sort("co_seq_fat_atd_ind")

proced_solicitados_df = (
    fai_v2
    .select([
        pl.col("co_seq_fat_atd_ind"),
        pl.col("ds_filtro_proced_solicitados")
            .str.split("|")  # Divide a string em lista
            .alias("codigo")
    ])
    .explode("codigo")  # Expande a lista em linhas separadas
    .filter(pl.col("codigo") != "")  # Remove possíveis strings vazias
    .with_columns(pl.lit("Procedimentos Solicitados").alias("tipo"))  # Adiciona coluna tipo
).sort("co_seq_fat_atd_ind")


ciaps_df = (
    fai_v2
    .select([
        pl.col("co_seq_fat_atd_ind"),
        pl.col("ds_filtro_ciaps")
            .str.split("|")  # Divide a string em lista
            .alias("codigo")
    ])
    .explode("codigo")  # Expande a lista em linhas separadas
    .filter(pl.col("codigo") != "")  # Remove possíveis strings vazias
    .with_columns(pl.lit("CIAPS").alias("tipo"))  # Adiciona coluna tipo
).sort("co_seq_fat_atd_ind")


# In[24]:


final_df = pl.concat([cids_df, ciaps_df,proced_avaliados_df,proced_solicitados_df]).select([
    "co_seq_fat_atd_ind",
    "codigo",
    "tipo"
])


# In[25]:


final_df.write_parquet(input_path+os.sep+"fat_atd_ind_cod.parquet")
