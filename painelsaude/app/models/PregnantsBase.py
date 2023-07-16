import logging
import pandas as pd
import numpy as np
import collections
from ..helpers.str import treatNames, strToData
from app.models.load_bases import load_gestantes_base
logging.basicConfig(level=logging.DEBUG)

def singleton(cls):
    instances = {}

    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance
    
@singleton
class PregnantsBase:
  _instance = {}
  _base = None

  def __init__(self):
    self._instance = None

  def getBase(self):
    if self._base is None:
      logging.info('Loading the pregnants final data base')
      self._base = load_gestantes_base()
      logging.info('Base loaded')
    # print(self._base)
    return self._base

  def getNameByIds(self, con, ids, page):
    #print( ''' select * from tb_fat_cidadao_pec p where p.co_seq_fat_cidadao_pec in  ({})  '''.format( ids) )
    
    result = con.consultar(''' select 
        tfc.no_cidadao,
        tfc.no_social_cidadao,
        tfc.co_seq_fat_cidadao_pec
        from 
        tb_fat_cidadao_pec tfc 
        where tfc.co_seq_fat_cidadao_pec in  ({})
        '''.format( ids, (20*(page-1))))

    results = []
    for i in result:
      result = dict()
      result['nome'] = treatNames(i[0])
      result['nomeSocial'] = treatNames(i[1])
      result['co_fat_cidadao_pec'] = int(str(i[2]))
      
      results.append(result)
    return pd.DataFrame(results)
    
  def getByIds(self, con, ids):
    result = con.consultar(''' select 
        distinct tfc.nu_cns,
        tfc.co_dim_tempo_nascimento ,
        tfc.no_cidadao,
        tfc.no_social_cidadao ,
        tfc.co_dim_sexo,
        tfc.co_dim_identidade_genero ,
        tfc.co_dim_unidade_saude_vinc ,
        ts.no_unidade_saude,
        tb.nu_telefone_celular,
        tb.nu_telefone_residencial,
        tb.nu_telefone_contato ,
        tb.ds_logradouro ,
        tb.ds_complemento ,
        tb.ds_ponto_referencia ,
        tb.ds_cep ,
        tb.ds_email, 
        tfc.co_seq_fat_cidadao_pec as co_fat_cidadao_pec,
        tfc.nu_cpf_cidadao 
        from 
        tb_fat_cidadao_pec tfc 
        left join tb_cidadao tb on tfc.nu_cns = tb.nu_cns
        left join tb_dim_unidade_saude ts on ts.co_seq_dim_unidade_saude = tfc.co_dim_unidade_saude_vinc 
        where tfc.co_seq_fat_cidadao_pec in  ({})
        '''.format( ids))
    results = []
    for i in result:
      result = collections.OrderedDict()
      result['cns'] = treatNames(i[0])
      result['dataNascimento'] = strToData( str(i[1]) )
      result['nome'] = treatNames(i[2])
      result['nomeSocial'] = treatNames(i[3])
      result['sexo'] = i[4]
      result['identidadeGenero'] = i[5]
      result['unidadeSaude'] = {
        "id": i[6],
        "nome": i[7]
      }
      result['celular'] = treatNames(i[8])
      result['telefoneResidencial'] = treatNames(i[9])
      result['telefoneConato'] = treatNames(i[10])
      result['logradouro'] = i[11]
      result['complemento'] = i[12]
      result['pontoReferencia'] = i[13]
      result['cep'] = i[14]
      result['email'] = treatNames(i[15])
      result['co_fat_cidadao_pec'] = i[16]
      result['cpf'] = treatNames(i[17])
      results.append(result)
    return results

  def pregnantsByPec( self, con, pec):
    result = self.getByIds( con, f'\'{pec}\'')
    return result[0]