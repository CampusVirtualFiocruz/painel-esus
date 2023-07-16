from .CheckPresense import CheckPresence, PipelineModel

"""
0 a 17 anos
18 a 29 anos
30 a 44 anos
45 a 59 anos
60 + anos
"""

class AgeGroup:
  def __init__(self):
    self.faixas = {
        "Faixa 1": "0 a 17 anos",
        "Faixa 2": "18 a 29 anos",
        "Faixa 3": "30 a 44 anos",
        "Faixa 4": "45 a 59 anos",
        "Faixa 5": "60 + anos",
    }
    self.count = {
        "Faixa 1": 0,
        "Faixa 2": 0,
        "Faixa 3": 0,
        "Faixa 4": 0,
        "Faixa 5": 0,
    }
  def findAgeGroup( self, ageRule ):
    return self.faixas[ageRule]

  def increment( self, ageRule ):
    self.count[ageRule] += 1

class BaseGroupModel:
  def __init__(self):
    self.localizacao = {
        'Urbano': AgeGroup(),
        'Rural': AgeGroup()
    }
    self.gender = {
      "Masculino": AgeGroup(),
      "Feminino":  AgeGroup()
    }
  def countAgegroup( self, ageGroup, gender = False ):
    localizacao = str(ageGroup[self.localizacaoLabel])
    sexo = str(ageGroup[self.sexoLabel]).replace('nan', '').replace('NaN', '')
    faixa = str(ageGroup[self.faixaLabel]).replace('nan', '').replace('NaN', '')

    faixas = set()
    items = faixa.split(',')
    localizacoes = localizacao.split(',')
    sexos = sexo.split(',')
    tipoLocalizacao = localizacoes[0]
    sexo = sexos[0]
    
    if tipoLocalizacao == 'nan':
      tipoLocalizacao = 'Urbano'
    for i in range(len(items)):
      if i is not None:
        faixas.add( items[i] )

    faixas = list(faixas)

    if len(faixas) == 1 and faixas[0] == '' :
      return
    for i in range(len(faixas)):
      if gender:
        ageGroupObj = self.gender[sexo]
        ageGroupObj.increment( faixas[i] )
      else:
        ageGroupObj = self.localizacao[tipoLocalizacao]
        ageGroupObj.increment( faixas[i] )
    
    
  
  def getLocations(self):
    result = dict()
    for i in self.localizacao['Urbano'].count:
      result[self.localizacao['Urbano'].faixas[i] ] = {
              'Urbano': self.localizacao['Urbano'].count[i],
              'Rural': self.localizacao['Rural'].count[i]
            }
    return result
  
  def getLocationsByGender(self):
    result = dict()
    for i in self.gender['Masculino'].count:
      result[self.gender['Masculino'].faixas[i] ] = {
              'Masculino': self.gender['Masculino'].count[i],
              'Feminino': self.gender['Feminino'].count[i]
            }
    return result

  def pipelineFn(self, row):
    self.countAgegroup(row)
    self.countAgegroup(row,True)
  
class AgeGroupModelHipertensao(BaseGroupModel):
  def __init__(self):
    super().__init__()
    self.localizacaoLabel = 'ds_tipo_localizacao'
    self.sexoLabel = 'ds_sexo'
    self.faixaLabel = 'FAIXA_ETARIA_HIPERTENSO'
    
class AgeGroupModelDiabetes(BaseGroupModel):
  def __init__(self):
    super().__init__()
    self.localizacaoLabel = 'ds_tipo_localizacao'
    self.sexoLabel = 'ds_sexo'
    self.faixaLabel = 'FAIXA_ETARIA_DIABETICO'