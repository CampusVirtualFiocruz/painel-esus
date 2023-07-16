from .CheckPresense import CheckPresence, PipelineModel

class IMC():
  def __init__(self, totalRegistro): 
    self.total = 0
    self.totalRegistro = totalRegistro

  def checkPresence(self, row):
    imc = row['IMC_FINAL']
    if self.imc == imc:
      self.total += 1
  def calcPercent(self):
      percent = round( (self.total/self.totalRegistro)*100, 2)
      return [ percent, 100-percent ]

  def toJson(self):
    percent = self.calcPercent()
    return [self.imc, {
            "limite": self.label,
            "com_consulta": percent[0],
            "com_consulta_abs": self.total,
            "sem_consulta": percent[1],
            "sem_consulta_abs": self.totalRegistro,

            }]

class BaixoPeso(IMC):
  def __init__(self, totalRegistros):
    super().__init__(totalRegistros)
    self.imc = 'Baixo Peso'
    self.label = '< 18,5'

class ExcessoPeso(IMC):
  def __init__(self, totalRegistros):
    super().__init__(totalRegistros)
    self.imc = 'Excesso de Peso'
    self.label = '25 a 29,9'
  
class Obesidade(IMC):
  def __init__(self, totalRegistros):
    super().__init__(totalRegistros)
    self.imc = 'Obesidade'  
    self.label = '> 30'

class ImcOutros(IMC):
  def __init__(self, totalRegistros):
    super().__init__(totalRegistros)
    self.imc = 'OUTROS'
    self.label = 'OUTROS'


class ImcNormal(IMC):
  def __init__(self, totalRegistros):
    super().__init__(totalRegistros)
    self.imc = 'Normal'
    self.label = '18,5 a 24,9'

class ImcModel(PipelineModel):

  def __init__(self, totalRegistros):
    self.list = [
       BaixoPeso(totalRegistros),
       ImcNormal(totalRegistros),
       ExcessoPeso(totalRegistros),  
       Obesidade(totalRegistros),
       ImcOutros(totalRegistros)    
    ]

