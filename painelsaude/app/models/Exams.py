from .CheckPresense import CheckPresence, PipelineModel
import re

class ExamStatus:
  def __init__(self):
     self.evaluated = 0
     self.requested = 0

  def checkPresence(self, row):
    
    if len(self.exams) == 0:
      return
    pattern = r'\W+'
    evaluatedProcedures = set(re.split(pattern, row['ds_filtro_proced_avaliados']))
    requestedProcedures = set(re.split(pattern, row['ds_filtro_proced_solicitados'])) 

    evaluatedProceduresPresence = self.exams & evaluatedProcedures
    # print(evaluatedProceduresPresence)
    requestedProceduresPresence = self.exams & requestedProcedures
    """
    - se o código do exame não estiver nas colunas solicitado e avaliado, 
    soma 1 solicitação pendente para o exame;
    """
    if len(requestedProceduresPresence) == 0 and len(evaluatedProceduresPresence) == 0:
      self.requested += 1
    else:
      """
      - se o código do exame  estiver nas coluna solicitado, mas não na coluna avaliado,
      conta pendente nos avaliados do exame; 
      """
      if len(requestedProceduresPresence) > 0 and len(evaluatedProceduresPresence) == 0:
        self.evaluated += 1


  def toJson(self):
    return {
        "avaliados": self.evaluated,
        "solicitados":self.requested,
        "tipo":self.label
    }

class BloodPressure(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0301100039'])
    self.label = 'Aferição de PA'

class BloodGlucose(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202010473', '0202010295','ABEX026'])
    self.label = 'Glicemia'

class Creatinine(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202010317','ABEX003'])
    self.label = 'Creatinina'

class Urine(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202010017','ABEX027'])
    self.label = 'EAS/EQU (urina rotina)' 

class SodiumPotassium(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202010635','0202010600'])
    self.label = 'Sódio e potássio' 

class TotalCholesterol(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202010295'])
    self.label = 'Colesterol total'  

class BloodCount(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202020380','ABEX028'])
    self.label = 'Hemograma'  

class ECG(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0211020036'])
    self.label = 'Eletrocardiograma'  

class Retinography(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0211060178','ABEX013'])
    self.label = 'Retinografia'  

class GlycatedHemoglobin(ExamStatus):
  def __init__(self):
    super().__init__()
    self.exams = set(['0202010503','ABEX008'])
    self.label = 'Hemoglobina glicada' 

    
class ArterialHypertensionExamsList():
  def __init__(self):
    self.list = [
        BloodPressure(),
        BloodGlucose(),
        Creatinine(),
        Urine(),
        SodiumPotassium(),
        TotalCholesterol(),
        BloodCount(),
        ECG()
    ]

  def pipelineFn(self, row):
    for i in self.list:
      i.checkPresence(row)
  
  def getResponse(self):
    result =[]
    for i in self.list:
      result.append( i.toJson() )

    return result

class DiabetesExamsList():
  def __init__(self):
    self.list = [
      BloodGlucose(),
      GlycatedHemoglobin(),
      Retinography(),
      Creatinine(),
      Urine(),
      BloodCount(),
      BloodPressure(),
      TotalCholesterol()

    ]

  def pipelineFn(self, row):
    for i in self.list:
      i.checkPresence(row)
  
  def getResponse(self):
    result =[]
    for i in self.list:
      result.append( i.toJson() )

    return result