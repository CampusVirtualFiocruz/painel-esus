# 1. Importando as bibliotecas ----

library(readr)
library(tidyverse)
library(openssl)
library(arrow)

# 2. Importando Dataset ----
setwd("~/Code/Cidade_X")
df <- read.csv2("tb_fat_atendimento_individual.csv")

# Preparar o código que conectaria no banco local (ou na nuvem), tratando
# dados restritos como IP, nome do banco, user, pass como variável de ambiente

# 3. Inspecionando e selecionando as colunas ----

View(df)
str(df)

atendimentos <- df %>% 
  select(co_seq_fat_atd_ind,
         co_dim_profissional_1,
         co_dim_cbo_1,
         co_dim_unidade_saude_1,
         co_dim_tempo,
         co_dim_faixa_etaria,
         co_dim_sexo,
         co_dim_local_atendimento,
         co_dim_tipo_atendimento,
         nu_peso,
         nu_altura,
         ds_filtro_cids,
         ds_filtro_ciaps,
         ds_filtro_proced_avaliados,
         ds_filtro_proced_solicitados,
         co_fat_cidadao_pec)

rm(df)

# 4. Ajustando data de atendimentos ----

glimpse(atendimentos)

atendimentos$co_dim_tempo <- as.character(atendimentos$co_dim_tempo)

atendimentos$data <- ymd(atendimentos$co_dim_tempo)

# Criei nova variável correspondendo a data do atendimento. Avaliar se mantemos
# o nome como co_dim_tempo

salto = year(Sys.Date()) - year(max(atendimentos$data))

atendimentos$data <- atendimentos$data %m+% years(salto)  

(max(atendimentos$data))

# Agora as datas estão ajustadas adicionando anos para atingir o atual

atendimentos <- atendimentos |> filter (data < Sys.Date())

(max(atendimentos$data))

atendimentos$co_dim_tempo <- atendimentos$data

atendimentos$data <- NULL

# E agora não existemNULL# E agora não existem datas no futuro no banco

# 5. Anonimizando com MD5 ----

atendimentos$co_fat_cidadao_pec <- as.character(atendimentos$co_fat_cidadao_pec)
atendimentos$paciente_id <- md5(atendimentos$co_fat_cidadao_pec)
atendimentos$co_fat_cidadao_pec <- NULL

# agora nosso banco é pseudonimizado!

# 6. Salvando como CSV e testando importação ----

str(atendimentos)

# Conferindo Datatypes

write_csv2(atendimentos, file="atendimentos.csv")

# CSV com só com as colunas essenciais 74,5 MB

atendimentos_final <- read.csv2(file="atendimentos.csv")

# Grande descoberta do ano - csv2 já lê no formato europeu, com delimitador ; 
# e separador decimal ,

str(atendimentos_final)

# Reconheceu os datatypes todos corretos, inteiros, numéricos e char

# write_feather(atendimentos_final, "atendimentos.feather", compression = "lz4")
# Feather 50 MB. Compensa quebrar o padrão que vimos usando
# pelo teórico ganho de velocidade? Até o momento, não.

# 7. Salvando o arquivo em Parquet ----

write_parquet(atendimentos_final, "atendimentos.parquet")

# Parquet 26,7 MB. Arquivo pequeno, está abrindo super-rápido, e ficou acima do 
# tamanho mínimo recomendado pela Apache (20 MB)
