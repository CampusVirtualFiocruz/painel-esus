from .CheckPresense import CheckPresence, PipelineModel
import re

class CBO:
  def __init__(self):
     self.total = 0
     self.totalCount = 0

  def checkPresence(self, row):
    pattern = r'\W+'
    profissional = set(re.split(pattern, row['CBO_PROFISSIONAL']))
    profissionalPresence = self.label & profissional
    if len(profissionalPresence) > 0 :
      # print(row['ds_filtro_cids'])
      self.total += 1

  def toJson(self):
    return {
        "profissao": self.text,
        "total": round( (self.total/self.totalCount)*100, 2),
        "totalCount": self.total
    }

class Doctors(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['MÉDICOS'])
    self.text = 'Médicos'

class Nurses(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['ENFERMEIROS'])
    self.text = 'Enfermeiros'    


class Dentists(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['CIRURGIÕES-DENTISTAS'])
    self.text = 'Dentistas'    

class Pharmacists(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['FARMACÊUTICOS'])
    self.text = 'Farmacêuticos'    

class PhysicalTherapists(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['FISIOTERAPEUTAS'])
    self.text = 'Fisioterapeutas'    

class Nutritionists(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['NUTRICIONISTAS'])
    self.text = 'Nutricionistas'    

class SpeechTherapists(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['FONOAUDIÓLOGOS'])
    self.text = 'Fonoaudiólogos'  

class OccupationalTherapists(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['TERAPEUTAS OCUPACIONAIS'])
    self.text = 'Terapeutas Ocupacionais' 

class PhysicalEducation(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['EDUCAÇÃO FÍSICA'])
    self.text = 'Educacao Física' 

class IntegrativeComplementary(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['INTEGRATIVA E COMPLEMENTAR'])
    self.text = 'Integrativa e Complementar' 

class Others(CBO):
  def __init__(self):
    super().__init__()
    self.label = set(['OUTRO'])
    self.text = 'Outros' 

class ProfessionalsList:
  def __init__(self):
    self.result = []
    self.list = [
        Doctors(),
        Nurses(),
        Dentists(),
        PhysicalTherapists(),
        OccupationalTherapists(),
        Pharmacists(),
        PhysicalEducation(),
        IntegrativeComplementary(),
        Others()
      ]
  def sortCriteria(self, row):
    return row.total
  
  def pipelineFn(self, row):

    for i in self.list:
      i.checkPresence(row)
    
  def sortResponse(self):
    if len(self.result) == 0:
      self.list.sort(reverse=True, key=self.sortCriteria)
      self.result=[]
      total = 0
      for i in self.list:
        total += i.total
      for i in self.list:
        i.totalCount = total
        self.result.append( i.toJson() )
    return self.result 
