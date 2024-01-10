import gc
import os
def cadIndividual(con):
  print('OW GETCWD: ',os.getcwd())
  return con.consultar_pd(''' SELECT distinct * FROM tb_fat_cad_individual tfci  ''', True).to_csv( path_or_buf=os.getcwd()+"/files/tb_fat_cad_individual.csv", sep=";", decimal = ',',header=True, index=False)

def cadDomiciliar(con):
  return con.consultar_pd(''' SELECT distinct * FROM tb_fat_cad_domiciliar  ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_fat_cad_domiciliar.csv", sep=";", decimal = ',',header=True, index=False)

def familiaTerritorio(con):
  return con.consultar_pd(''' SELECT distinct * FROM tb_fat_familia_territorio  ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_fat_familia_territorio.csv", sep=";", decimal = ',',header=True, index=False)

def cidadaoTerritorio(con):
  con.consultar_pd(''' SELECT distinct * FROM tb_fat_cidadao_territorio  ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_fat_cidadao_territorio.csv", sep=";", decimal = ',',header=True, index=False)
  
def cidadaoPec(con):
  return con.consultar_pd(''' SELECT distinct * FROM tb_fat_cidadao_pec  ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_fat_cidadao_pec.csv", sep=";", decimal = ',',header=True, index=False)

def atendimentoIndividual(con):
  return con.consultar_pd(''' select
	distinct *
from
	tb_fat_atendimento_individual
where
	co_dim_tempo >= cast( to_char(( (select
	to_date(co_dim_tempo::text, 'YYYYMMDD') 
from
	tb_fat_atendimento_individual order by 1 desc limit 1) - interval '12 months'), 'YYYYMMDD') as INTEGER);''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_fat_atendimento_individual.csv", sep=";", decimal = ',',header=True, index=False)

def municipio(con):
  return con.consultar_pd(''' SELECT distinct * FROM tb_dim_municipio  ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_dim_municipio.csv", sep=";", decimal = ',',header=True, index=False)

def unidades(con):
  return con.consultar_pd(''' select distinct co_seq_dim_unidade_saude, nu_cnes, no_unidade_saude from tb_dim_unidade_saude tdus    ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_dim_unidade_saude.csv", sep=";", decimal = ',',header=True, index=False)


def odonto(con):
  return con.consultar_pd(''' select distinct * from tb_fat_atendimento_odonto    ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_fat_atendimento_odonto.csv", sep=";", decimal = ',',header=True, index=False)

def cbo(con):
  return con.consultar_pd(''' select distinct * from tb_dim_cbo    ''', True).to_csv(path_or_buf=os.getcwd()+"/files/tb_dim_cbo.csv", sep=";", decimal = ',',header=True, index=False)


from tqdm import tqdm, tnrange
def generateAll(con):
  executions = {
    0: cadIndividual,
    1: cadDomiciliar,
    2: familiaTerritorio,
    3: cidadaoTerritorio,
    4: cidadaoPec,
    5: atendimentoIndividual,
    6: municipio,
    7: unidades,
    8: odonto,
    9: cbo,
  }
  for i in tqdm(range(0, len(executions)), desc="generating bases"):
    executions[i](con)
    gc.collect()