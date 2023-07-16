import pandas as pd
from datetime import datetime
import json
import numpy as np
from dateutil.relativedelta import relativedelta
import math 



def extractLastYearDate(_data):
  _lastDate = _data["co_dim_tempo"]
  lastDate = _lastDate.max()  
  lastYear = lastDate - relativedelta(years=1)
  return ( lastYear, lastDate )

def filterLastYear( data):
    (lastYear, lastDate) = extractLastYearDate(data)
    data = data[ (data['co_dim_tempo'] >= lastYear) & (data['co_dim_tempo'] <= lastDate) ]
    return data


class PreNatalIndicator:
    def __init__(self):
        pass
    def fn_12_semana( self, _data) :
        return {
            "com_consulta" :round(_data[ (_data["nu_idade_gestacional"] > 1) & (_data["nu_idade_gestacional"] <=12)].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" : 100 - (round(_data[ (_data["nu_idade_gestacional"] > 1) & (_data["nu_idade_gestacional"] <=12)].shape[0]/_data.shape[0],4)*100)
            }

    def fn_6_mais_consulta( self, _data) :
        return {
            "com_consulta" :round(_data[ (_data['consultas_6_prenatal'] == 1)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['consultas_6_prenatal'] != 1)  ].shape[0]/_data.shape[0],4)*100 
            }

    def fn_atendimento_odontologico( self, _data) :
        _data['com_atendimento_odontologico_razoavel'] = _data['com_atendimento_odontologico_razoavel'].fillna(0)
        return {
            "com_consulta" :round(_data[ (_data['com_atendimento_odontologico_razoavel'] == 1)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['com_atendimento_odontologico_razoavel'] != 1)  ].shape[0]/_data.shape[0],4)*100 
            }

    def fn_st_vacinacao_em_dia( self, _data) :
        _data.loc[_data['st_vacinacao_em_dia'] == '', 'st_vacinacao_em_dia'] = '0.0'
        _data['st_vacinacao_em_dia'] = _data['st_vacinacao_em_dia'].astype(str).astype(float)
        return {
            "com_consulta" :round(_data[ (_data['st_vacinacao_em_dia'] == 1)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['st_vacinacao_em_dia'] != 1)  ].shape[0]/_data.shape[0],4)*100 
            }

    def fn_sifilis_hiv( self, _data) :
        _data['exames_para_sifilis_hiv']  = _data['exames_para_sifilis_hiv'].astype(bool)
        return {
            "com_consulta" :round(_data[ (_data['exames_para_sifilis_hiv'] == True)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['exames_para_sifilis_hiv'] != np.True_)  ].shape[0]/_data.shape[0],4)*100 
            }

class ObstetricFactors:

    def __init__(self):
        pass
    def fn_gestacoes_previas( self,_data) :
        _data['N_gestacoes'] = _data['N_gestacoes'].fillna(0)
        _data['N_gestacoes'] = _data['N_gestacoes'].astype(str).astype(float).astype(int)
        return {
            "com_consulta" :round(_data[ (_data['N_gestacoes'] > 1)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['N_gestacoes'] <= 1)  ].shape[0]/_data.shape[0],4)*100 
            }

    def fn_gravidez_planejada( self,_data) :
        print( _data['st_gravidez_planejada'].unique() )
        _data['st_gravidez_planejada'] = _data['st_gravidez_planejada'].fillna(0)
        _data['st_gravidez_planejada'] = _data['st_gravidez_planejada'].astype(str).astype(float).astype(int)
        return {
            "com_consulta" :round(_data[ (_data['st_gravidez_planejada'] == 1)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['st_gravidez_planejada'] != 1)  ].shape[0]/_data.shape[0],4)*100 
            }

    def fn_hipertensao( self,_data) :
        
        return {
            "com_consulta" :round(_data[ (_data['isContained_HIPERTENSAO'] == True)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['isContained_HIPERTENSAO'] != True)  ].shape[0]/_data.shape[0],4)*100 
            }

    def fn_diabete( self,_data) :
        return {
            "com_consulta" :round(_data[ (_data['isContained_DIABETE'] == True)  ].shape[0]/_data.shape[0],4)*100,
            "sem_consulta" :round(_data[ (_data['isContained_DIABETE'] != True)  ].shape[0]/_data.shape[0],4)*100 
            }    

class PregnantsByTimeRange:
    def __init__(self):
        pass


    def getDataBetweenWeeks( self,data,  start, end):
        _data = data.copy()
        ndata = _data[ (_data["nu_idade_gestacional"] >= start) & (_data["nu_idade_gestacional"] <= end)  ]
        ndata = ndata.drop_duplicates('co_fat_cidadao_pec', keep='last')
        return ndata.shape[0]

    def getDataBetweenWeeksDf( self,data,  start, end):
        _data = data.copy()
        ndata = _data[ (_data["nu_idade_gestacional"] >= start) & (_data["nu_idade_gestacional"] <= end)  ]
        ndata = ndata.drop_duplicates('co_fat_cidadao_pec', keep='last')
        return ndata


    def groupByTriMonths(self,data):
        _data = data.copy()
        return {
            "1º Trimestre": _data[ _data['nu_idade_gestacional_trimestre'] == "1º Trimestre"].drop_duplicates('co_fat_cidadao_pec', keep='last').shape[0],
            "2º Trimestre": _data[ (_data['nu_idade_gestacional'] >= 13) & (_data['nu_idade_gestacional'] <= 24) ].shape[0] ,
            "3º Trimestre": _data[ _data['nu_idade_gestacional_trimestre'] == "3º Trimestre"].drop_duplicates('co_fat_cidadao_pec', keep='last').shape[0]
        }


    def groupByWeek( self,_data) :
        mask = _data['nu_idade_gestacional'] < 0
        _data.loc[mask, 'nu_idade_gestacional'] = 1
        return {
            "1 a 12 semanas" : self.getDataBetweenWeeks(_data, 0,12),
            "13 a 16 semanas" :self.getDataBetweenWeeks(_data, 13,16),
            "17 a 20 semanas": self.getDataBetweenWeeks(_data, 17,20),
            "21 a 24 semanas": self.getDataBetweenWeeks(_data, 21,24),
            "25 a 28 semanas": self.getDataBetweenWeeks(_data, 25,28),
            "29 a 32 semanas": self.getDataBetweenWeeks(_data, 29, 32),
            "33 a 36 semanas": self.getDataBetweenWeeks(_data, 33,36),
            "37 a 41 semanas": self.getDataBetweenWeeks(_data, 37,41)
        }

    def pregnantWomenByTrimester(self,_data):
        mask = _data['nu_idade_gestacional'] < 0
        _data.loc[mask, 'nu_idade_gestacional'] = 1
        
        return {
            "groupByTrimester": self.groupByTriMonths(_data),
            "groupByWeeks": self.groupByWeek( _data )
        }

    def filterPregnantsByTrimester(self,_data, trimester):
        trimesterStr  = {
            '1': '1º Trimestre',
            '2': '2º Trimestre',
            '3': '3º Trimestre'
        }
        
        return  _data[ _data["nu_idade_gestacional_trimestre"] == trimesterStr[str(trimester)]  ]



    def convertColumnToText( self,dataColumn ):
        return dataColumn.astype(str).values.flatten().tolist()

class ExamsAndRequests:

  def __init__(self):
    self.notFound = set()
    """
    Mapeamento de procedimentos dessa forma o procedimento fica padronizado

    PS:
    ABEX026 = ABP de procedimento
    0202010473 = SIGTAP

    """
    self.conditionMap = {
        '0202010473' : '0202010473',
        'ABEX026' : '0202010473',
        '0202020371': '0202020380',
        '0202020380' : '0202020380',
        '0202020304': '0202020380',
        'ABEX028' : '0202020380' ,
        '0202120023':'0202120023', 
        '0202120031':'0202120023',
        '0213010517':'0213010517',
        '0202060217':'0213010517',
        'ABEX023': '0213010517',
        '0205020143':'0205020143',
        'ABEX024':'0205020143',
        '0202031110':'0202031110',
        'ABEX019':'0202031110',
        '0202030300':'0202030300' ,
        'ABEX018':'0202030300',
        '0202050017':'0202050017',
        'ABEX027':'0202050017',
        '0202080080':'0202080080',
        'ABEX029':'0202080080'
        }
    self.glicemia = { '0202010473', 'ABEX026' }
    self.hemograma = { '0202020380', 'ABEX028' }
    self.tipo_sanguineo = { '0202120023', '0202120031'}
    self.taxa_igm_igg = { '0213010517', '0202060217', 'ABEX023'}
    self.us_obstetrica = { '0205020143','ABEX024'}
    self.teste_rapido_sifilis = {'0202031110','ABEX019'}
    self.hiv = { '0202030300' ,'ABEX018'}
    self.urina =  {'0202050017', 'ABEX027'}
    self.urocultura = { '0202080080', 'ABEX029' }
    self.listaExamesStr = [ "glicemia", "hemograma", "tipo_sanguineo", "taxa_igm_igg", "us_obstetrica", "teste_rapido_sifilis", "hiv", "urina", "urocultura"]
    self.listaExames = [ self.glicemia, self.hemograma, self.tipo_sanguineo, self.taxa_igm_igg, self.us_obstetrica, self.teste_rapido_sifilis, self.hiv, self.urina, self.urocultura]
    self.listExams = self.resetExames()

  def resetExames(self):
    return {
        "hemograma": {
            "avaliados": 0,
            "solicitados": 0
        },
        "tipo_sanguineo": {
            "avaliados": 0,
            "solicitados": 0
        },
        "taxa_igm_igg": {
            "avaliados": 0,
            "solicitados": 0
        },
        "glicemia": {
            "avaliados": 0,
            "solicitados": 0
        },
        "us_obstetrica": {
            "avaliados": 0,
            "solicitados": 0
        },
        "teste_rapido_sifilis": {
            "avaliados": 0,
            "solicitados": 0
        },
        "hiv": {
            "avaliados": 0,
            "solicitados": 0
        },
        "urina": {
            "avaliados": 0,
            "solicitados": 0
        },
        "urocultura": {
            "avaliados": 0,
            "solicitados": 0
        },
        "antihbsag": {
            "avaliados": 0,
            "solicitados": 0
        }
    }

  def mapDto(self):
    return [
      {"tipo": "Hemograma", "solicitados": self.listExams['hemograma']['solicitados'], "avaliados": self.listExams['hemograma']['avaliados'] },
      {"tipo": "Tipo Sanguíneo/Rg", "solicitados": self.listExams['tipo_sanguineo']['solicitados'], "avaliados": self.listExams['tipo_sanguineo']['avaliados'] },
      {"tipo": "Taxa IgM e IgG", "solicitados": self.listExams['taxa_igm_igg']['solicitados'], "avaliados": self.listExams['taxa_igm_igg']['avaliados'] },
      {"tipo": "Anti HbsAg", "solicitados": self.listExams['antihbsag']['solicitados'], "avaliados": self.listExams['antihbsag']['avaliados'] },
      {"tipo": "US Obstetrícia", "solicitados": self.listExams['us_obstetrica']['solicitados'], "avaliados": self.listExams['us_obstetrica']['avaliados'] },
      {"tipo": "Glicemia Jejum", "solicitados": self.listExams['glicemia']['solicitados'], "avaliados": self.listExams['glicemia']['avaliados'] },
      {"tipo": "Teste rápido sífilis", "solicitados": self.listExams['teste_rapido_sifilis']['solicitados'], "avaliados": self.listExams['teste_rapido_sifilis']['avaliados'] },
      {"tipo": "Urina", "solicitados": self.listExams['urina']['solicitados'], "avaliados": self.listExams['urina']['avaliados'] },
      {"tipo": "Urocultura", "solicitados": self.listExams['urocultura']['solicitados'], "avaliados": self.listExams['urocultura']['avaliados'] },
            
    ]

    
  def computeExams(self, solicitados, avaliados):
    """ 
        - se o código do exame não estiver nas colunas solicitado e avaliado, soma 1 solicitação pendente para o exame; 
        - se o código do exame estiver nas colunas solicitado e avaliado, não conta como o exame como pendente solicitado e nem avaliado;
        - se o código do exame  estiver nas coluna solicitado, mas não na coluna avaliado, conta pendente nos avaliados do exame; 
        - se o código do exame  estiver nas coluna avaliado, não conta como o exame pendente solicitado e nem avaliado;
    """ 
    if len(solicitados) == 0 and len(avaliados)==0:
      for i in range(0, len(self.listaExames)-1):
          condition = self.listaExames[i]
          label = self.listaExamesStr[i]
        #   if condition:
          self.listExams[label]['solicitados'] = self.listExams[label]['solicitados']  +1
      return
    for i in range(0, len(self.listaExames)-1):
      condition = self.listaExames[i]
      label = self.listaExamesStr[i]
      if condition:
        code = condition.pop()
        currentExam = self.conditionMap[code]
        if currentExam not in solicitados and currentExam not in avaliados:
          self.listExams[label]['solicitados'] = self.listExams[label]['solicitados']  +1
        elif currentExam in solicitados and currentExam not in avaliados:
          # print(currentExam )
          self.listExams[label]['avaliados'] = self.listExams[label]['avaliados']  +1
      
      # else:
        # print( self.listaExamesStr[i] )

  def buildTable( self, solicitados, avaliados ):
    _solicitados = solicitados.split('|')
    # print( 'solicitado', _solicitados) 
    solicitados=set()
    notFound=set()
    for i in _solicitados:
      if i and i in self.conditionMap:
        solicitados.add(self.conditionMap[i])
      else:
        if i:
          self.notFound.add(i)
    _avaliados = avaliados.split('|')
    # print( 'avaliado', _avaliados)
    avaliados = set()
    for i in _avaliados:
      if i and i in self.conditionMap:
        avaliados.add(self.conditionMap[i])
      else:
        if i:
          self.notFound.add(i)
    self.computeExams(solicitados, avaliados)

  def prepareTable( self, solicitados, avaliados ):
    _solicitados=set()
    notFound=set()
    for i in solicitados:
      if i and i in self.conditionMap:
        _solicitados.add(self.conditionMap[i])
      else:
        if i:
          self.notFound.add(i)
    _avaliados = set()
    for i in avaliados:
      if i and i in self.conditionMap:
        _avaliados.add(self.conditionMap[i])
      else:
        if i:
          self.notFound.add(i)
    self.computeExams(_solicitados, _avaliados)

class MergeTable:
  def __init__(self):
    self.mappedArray= dict()

  def buildTable(self,x):
    pec = x['co_fat_cidadao_pec']
    procedimento = x['ds_filtro_proced_solicitados']
    avaliacao = x['ds_filtro_proced_avaliados']
    if pec not in self.mappedArray:
      self.mappedArray[pec] = dict()
      self.mappedArray[pec]['ds_filtro_proced_solicitados']= set()
      self.mappedArray[pec]['ds_filtro_proced_avaliados']=set()

    _solicitados = procedimento.split('|')
    solicitados=set()
    for i in _solicitados:
      if i != '':
        solicitados.add(i)

    _avaliados = avaliacao.split('|')
    avaliados = set()
    for i in _avaliados:
      if i != '':
        avaliados.add(i)

    self.mappedArray[pec]['ds_filtro_proced_solicitados']= self.mappedArray[pec]['ds_filtro_proced_solicitados'].union(solicitados)
    self.mappedArray[pec]['ds_filtro_proced_avaliados']=self.mappedArray[pec]['ds_filtro_proced_avaliados'].union(avaliados)
    

class PregnatsTable:
  def __init__(self):
    self.result = dict()
    pass

  def mergeMestre( self, gestantes, mestre):
    gestantes['co_fat_cidadao_pec'] = gestantes['co_fat_cidadao_pec'].astype(str).astype(float).astype(int)
    mestre['co_fat_cidadao_pec'] = mestre['co_fat_cidadao_pec'].astype(str).astype(float).astype(int)
    # gestantes['co_fat_cidadao_pec'] = gestantes['co_fat_cidadao_pec'].str[:-2]
    mestre = mestre[['co_fat_cidadao_pec','ds_tipo_localizacao']]
    gestante = gestantes.merge(mestre, on='co_fat_cidadao_pec', how='left', indicator=True)
    
    gestante = gestante.drop(columns=['_merge'])
    if 'ds_tipo_localizacao' not in gestante:
        gestante['ds_tipo_localizacao'] = gestante['ds_tipo_localizacao_x']
    return gestante

  def proccessTableLine( self, x):
    cidadaoPec=x['co_fat_cidadao_pec']
    if x['co_fat_cidadao_pec'] in self.result:
      if self.result[cidadaoPec]['co_dim_tempo'] > x['co_dim_tempo']:
        self.result[cidadaoPec]['co_dim_tempo'] = x['co_dim_tempo']
        self.result[cidadaoPec]['igPrimeiraConsulta'] = x['nu_idade_gestacional']
      self.result[cidadaoPec]['totalConsultas'] += 1
    else:
        self.result[ cidadaoPec] = dict()
        self.result[cidadaoPec]['co_fat_cidadao_pec'] = cidadaoPec
        self.result[cidadaoPec]['igPrimeiraConsulta'] = int(float(x['nu_idade_gestacional']))
        self.result[cidadaoPec]['tipoResidencia'] =  x['ds_tipo_localizacao']
        self.result[cidadaoPec]['pendencia'] =  True if x['st_vacinacao_em_dia'] == 1.0 else False
        self.result[cidadaoPec]['idade'] = x['idade']
        self.result[cidadaoPec]['esquemaVacinal'] = 'SIM' if x['st_vacinacao_em_dia'] == 1.0 else 'NÃO'
        self.result[cidadaoPec]['temDiabetes'] = 'SIM' if x['isContained_DIABETE'] == True else 'NÃO'
        self.result[cidadaoPec]['temHas'] = 'SIM' if x['isContained_HIPERTENSAO'] == True else 'NÃO'
        self.result[cidadaoPec]['consultaOdonto'] = 'SIM' if x['com_atendimento_odontologico_razoavel'] == True else 'NÃO'
        self.result[cidadaoPec]['exameVdrlAntiHiv'] =  'SIM' if ( '0202030300' in x['ds_filtro_proced_avaliados'] or 'ABEX018' in x['ds_filtro_proced_avaliados'] ) else 'NÃO'
        self.result[cidadaoPec]['co_dim_tempo'] = x['co_dim_tempo']
        self.result[cidadaoPec]['totalConsultas'] = 1


class PregnantsService:

    def __init__(self):
        pass

    def prenatalIndicators ( self, data, nu_cnes = None) :
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        if _data.shape[0] ==0:
            return   {
            "com 1ª consulta até 12 semanas" : 0,
            "com 6 ou mais consultas" : 0,
            "com atendimento odontológico" : 0,
            "esquema vacinal completo" : 0,
            "com exames VDRL e HIV" : 0
        }           
        indicators = PreNatalIndicator()
        return {
            "com 1ª consulta até 12 semanas" : indicators.fn_12_semana (_data),
            "com 6 ou mais consultas" : indicators.fn_6_mais_consulta (_data),
            "com atendimento odontológico" : indicators.fn_atendimento_odontologico (_data),
            "esquema vacinal completo" : indicators.fn_st_vacinacao_em_dia (_data),
            "com exames VDRL e HIV" : indicators.fn_sifilis_hiv (_data),
        }
    

    def obstetricFactors(self, data, nu_cnes = None) :
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        if _data.shape[0] == 0:
            return {
            "gestações prévias" : 0,
            "gravidez planejada" : 0,
            "hipertensão arterial" : 0,
            "diabetes mellitus" : 0
            }
        obstetrics = ObstetricFactors()    
        return {
            "gestações prévias" : obstetrics.fn_gestacoes_previas (_data),
            "gravidez planejada" : obstetrics.fn_gravidez_planejada (_data),
            "hipertensão arterial" : obstetrics.fn_hipertensao (_data),
            "diabetes mellitus" : obstetrics.fn_diabete (_data),
        }

    def age_group(self, row):
        if row['idade'] >= 12 and row['idade'] <=16:
            return "Faixa 1"
        elif row['idade'] >= 17 and row['idade'] <=20:
            return "Faixa 2"
        elif row['idade'] >= 21 and row['idade'] <=25:
            return "Faixa 3"
        elif row['idade'] >= 26 and row['idade'] <=30:
            return "Faixa 4"
        elif row['idade'] >= 31 and row['idade'] <=34:
            return "Faixa 5"
        elif row['idade'] >= 35:
            return "Faixa 6"
        else:
            return "NaN"

    def zeroPregnantsPerAges(self):
        return  {
            "12 a 16 anos": {
            "Rural": 0,
            "Urbano": 0
            },
            "17 a 20 anos": {
            "Rural": 0,
            "Urbano": 0
            },
            "21 a 25 anos": {
            "Rural": 0,
            "Urbano": 0
            },
            "26 a 30 anos": {
            "Rural": 0,
            "Urbano": 0
            },
            "31 a 33 anos": {
            "Rural": 0,
            "Urbano": 0
            },
            "35 + anos": {
            "Rural": 0,
            "Urbano": 0
            },
            "nan": {
            "Rural": 0,
            "Urbano": 0
            }
        }
    def pregnatsPerages(self,  data, nu_cnes = None) :
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        gestante_localiza = _data
        if _data.shape[0] == 0 :
            return self.zeroPregnantsPerAges()
        
        gestante_localiza['ds_faixa_etaria'] = gestante_localiza.apply (lambda row: self.age_group(row), axis=1)
        faixaEtaria ={
            "Faixa 1": "12 a 16 anos",
            "Faixa 2": "17 a 20 anos",
            "Faixa 3": "21 a 25 anos",
            "Faixa 4": "26 a 30 anos",
            "Faixa 5": "31 a 33 anos",
            "Faixa 6": "35 + anos",
            "nan":"nan",
            "NaN":"nan"
        }
        gestante_localiza['ds_faixa_etaria'] = gestante_localiza.apply (lambda row: faixaEtaria[row['ds_faixa_etaria']] ,axis=1)

        piramide = pd.DataFrame({'count' : gestante_localiza.groupby( ["ds_faixa_etaria", "ds_tipo_localizacao"] ).size()}).reset_index()
        result = piramide \
                .groupby('ds_faixa_etaria')\
                            .apply( lambda y:
                                    dict( zip(y['ds_tipo_localizacao'], y['count']))
                                    ).to_dict()
        return result

    def byTrimester(self,  data, nu_cnes = None) :
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        pregnants = PregnantsByTimeRange()
        return pregnants.pregnantWomenByTrimester(_data)
    
    def pregnantsByTrimester(self, data, trimester, page, pregnantsBase, con, nu_cnes = None) :
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  _data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        pregnants = PregnantsByTimeRange()
        if page < 0 or page is None:
            page = 1
        
        page = int(page)
        inicio = (page - 1) * 10
        fim = (page ) * 10
        ids = pregnants.filterPregnantsByTrimester(_data, trimester)
        listIds = ids.drop_duplicates('co_fat_cidadao_pec', keep='last')
        totalPages = listIds.shape[0]
        listIds = listIds[ inicio:fim]
        listIdsStr = ''
        for index, row in listIds['co_fat_cidadao_pec'].iteritems():
            index = row
            listIdsStr = listIdsStr + f'\'{index}\','
        result = pregnantsBase.getByIds(con, listIdsStr[:-1])
        return [result, totalPages]

    def pregnantsWeeklyRange(self, data, weekly, page, pregnantsBase, con, nu_cnes = None):
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  _data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        mask = _data['nu_idade_gestacional'] < 0
        _data.loc[mask, 'nu_idade_gestacional'] = 1
        
        pregnants = PregnantsByTimeRange()
        week = {    
            "1": [0,12 ], #"1 a 12 semanas" 
            "2": [13,16], #"13 a 16 semanas"
            "3": [17,20], #"17 a 20 semanas"
            "4": [21,24], #"21 a 24 semanas"
            "5": [25,28], #"25 a 28 semanas"
            "6": [29,32], #"29 a 32 semanas"
            "7": [33,36], #"33 a 36 semanas"
            "8": [37,41], #"37 a 41 semanas"
        }
        _data = pregnants.getDataBetweenWeeksDf(_data, week[weekly][0],week[weekly][1])
        if page < 0 or page is None:
            page = 1
        
        page = int(page)
        inicio = (page - 1) * 10
        fim = (page ) * 10
        ids = _data
        listIds = ids#.drop_duplicates('co_fat_cidadao_pec', keep='last')
        totalPages = math.ceil(listIds.shape[0])
        listIds = listIds[ inicio:fim]
        listIdsStr = ''
        for index, row in listIds['co_fat_cidadao_pec'].iteritems():
            index = row
            listIdsStr = listIdsStr + f'\'{index}\','
        result = pregnantsBase.getByIds(con, listIdsStr[:-1])
        return [result, totalPages]

    def examsAndResultsTable(self,  data, nu_cnes = None) :
        _data = data.copy()
        _data = filterLastYear(_data)
        if nu_cnes is not None:
            _data =  _data.query( 'nu_cnes == "{}"'.format(nu_cnes) )
        examsRequest = ExamsAndRequests()
        
        mergetable = MergeTable()

        """
        Cria uma tabale relacionando 
            pec_id -> ds_filtro_proced_solicitados
            pec_id -> ds_filtro_proced_avaliados
        """
        _data.apply( lambda x: mergetable.buildTable(x), axis=1)

        examsRequest = ExamsAndRequests()
        for i in mergetable.mappedArray:
            examsRequest.prepareTable( mergetable.mappedArray[i]['ds_filtro_proced_solicitados'], mergetable.mappedArray[i]['ds_filtro_proced_avaliados'] )


        return examsRequest.mapDto()


    def pregnantsTable(self, data, mestre, page, pregnantsBase, con, nu_cnes = None):
        _data = data.copy()
        _data = filterLastYear(_data)

        
        if nu_cnes is not None:
            _data =  data.query( 'nu_cnes == "{}"'.format(nu_cnes) )

        preg = PregnatsTable()
        if page < 0 or page is None:
            page = 1
        inicio = (page - 1) * 20
        fim = (page ) * 20
        gestantes = _data[ inicio:fim]
        
        _gestantes = preg.mergeMestre( gestantes, mestre)
        _gestantes.apply( lambda x : preg.proccessTableLine(x), axis=1)
        ids = ''
        total = _data['co_fat_cidadao_pec'].unique().shape[0]
       
        print(gestantes.shape)

        result= []
        for i in preg.result:
            ids = ids + f'\'{i}\', '
            result.append( preg.result[i])
        result = pd.DataFrame(result)
        print(result.shape)
        pregs = pregnantsBase.getNameByIds(con, ids[:-2], page)
        pregs = pregs[['co_fat_cidadao_pec','nome']]
        gestante = pd.merge(result, pregs, on='co_fat_cidadao_pec', how='left', indicator=True)
        print(gestante.shape)
        gestante['_merge'].value_counts()
        gestante = gestante.drop(columns=['_merge'])
        gestante = gestante.drop_duplicates()
        print(gestante.shape)
        return [gestante.to_dict('r'), total]

