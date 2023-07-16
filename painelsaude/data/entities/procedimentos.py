from .pessoa import Pessoa

import re
import math, random
from typing import List


class ExamStatus:
  def __init__(self):
     self.evaluated = 0
     self.requested = 0

  def checkPresence(self, row):
    
 
    pattern = r'\W+'
    evaluatedProcedures = set(re.split(pattern, row['ds_filtro_proced_avaliados']))
    requestedProcedures = set(re.split(pattern, row['ds_filtro_proced_solicitados'])) 
    print(evaluatedProcedures)
    print(requestedProcedures)
    print(self.exams)
    
    evaluatedProceduresPresence = self.exams & evaluatedProcedures
    
    requestedProceduresPresence = self.exams & requestedProcedures
    
    print(evaluatedProceduresPresence)
    print(requestedProceduresPresence)
    """
    - se o código do exame não estiver nas colunas solicitado e avaliado, 
    soma 1 solicitação pendente para o exame;
    """
    if len(requestedProceduresPresence) == 0 and len(evaluatedProceduresPresence) == 0:
      print('00')
      self.requested += 1
    else:
      """
      - se o código do exame  estiver nas coluna solicitado, mas não na coluna avaliado,
      conta pendente nos avaliados do exame; 
      """
      if len(requestedProceduresPresence) > 0 and len(evaluatedProceduresPresence) == 0:
        self.evaluated += 1

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
    self.exams = set(['0202010017' ,'ABEX027'])
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
    
    
def set_all_arterial_hipertension_procedures(pessoa: Pessoa):
    exams_list = ArterialHypertensionExamsList()
    for atendimento in pessoa.atendimentos.atendimento_list:
        for exam in exams_list.list:
            exam_code = list(exam.exams)[0]
            atendimento.ds_filtro_proced_avaliados.append(exam_code.strip())
            atendimento.ds_filtro_proced_solicitados.append(exam_code.strip())
    pessoa.atendimentos.update()

  
def set_data_arterial_hipertension_procedures(pessoa: Pessoa, number_cases: List[List[int]]):
    exams_list = ArterialHypertensionExamsList()
    for atendimento in pessoa.atendimentos.atendimento_list:
        for i, exam in enumerate(exams_list.list):
            take = random.randint(1,100)
            take2 = random.randint(1,100)
            exam_code = list(exam.exams)[0]
            if take <=5:
              atendimento.ds_filtro_proced_solicitados.append(exam_code.strip())
            elif take2 <= 5:
              pass
            else:
              atendimento.ds_filtro_proced_solicitados.append(exam_code.strip())
              atendimento.ds_filtro_proced_avaliados.append(exam_code.strip())
              
    pessoa.atendimentos.update()
    
    
def set_all_diabetes_procedures(pessoa: Pessoa):
    exams_list = DiabetesExamsList()
    for atendimento in pessoa.atendimentos.atendimento_list:
        for exam in exams_list.list:
            exam_code = list(exam.exams)[0]
            atendimento.ds_filtro_proced_avaliados.append(exam_code.strip())
            atendimento.ds_filtro_proced_solicitados.append(exam_code.strip())    
    pessoa.atendimentos.update()
    
def set_data_diabetes_procedures(pessoa: Pessoa):
    exams_list = DiabetesExamsList()
    for atendimento in pessoa.atendimentos.atendimento_list:
        for exam in exams_list.list:
            take = random.randint(1,100)
            take2 = random.randint(1,100)
            exam_code = list(exam.exams)[0]
            if take <=5:
              atendimento.ds_filtro_proced_solicitados.append(exam_code.strip())
            elif take2 <= 5:
              pass
            else:
              atendimento.ds_filtro_proced_avaliados.append(exam_code.strip())
              atendimento.ds_filtro_proced_solicitados.append(exam_code.strip())    
    pessoa.atendimentos.update()