from .unidade_saude import UnidadeSaude
from .diseases import Diabetes, Hipertensao
from ..entities.atendimento_mestre import AtendimentoMestreCollection
from .atendimento_diabetes_hipertensao import DiabetesDictAdapter, HipertensaoDictAdapter
from enum import Enum

class PessoaEnums(Enum):
    URBANA = 1
    RURAL = 2

    MASCULINO = 3
    FEMININO = 4
    
    FAIXA_ETARIA_1 = 5
    FAIXA_ETARIA_2 = 6
    FAIXA_ETARIA_3 = 7
    FAIXA_ETARIA_4 = 8
    FAIXA_ETARIA_5 = 9
    FAIXA_ETARIA_6 = 10
    FAIXA_ETARIA_7 = 11
    
    def get_label(value):
        return {
            1: 'Urbano',
            2: 'Rural',
            3: 'Masculino',
            4: 'Feminino',
            5: 'Faixa 1',
            6: 'Faixa 2',
            7: 'Faixa 3',
            8: 'Faixa 4',
            9: 'Faixa 5',
            10: 'Faixa 6',
            11: 'Faixa 7',
        }[value]

class Pessoa:
    def __init__(
        self,
        co_fat_cidadao_pec,
        ds_tipo_localizacao,
        st_vacinacao_em_dia,
        st_hipertensao,
        st_diabetes,
        st_gestante,
        ds_sexo,
        dt_nascimento,
        nu_idade,
        ds_faixa_etaria,
        unidade_saude: UnidadeSaude,
        atendimentos: AtendimentoMestreCollection,
        nome: str = None
        ) -> None:
        self.co_fat_cidadao_pec = co_fat_cidadao_pec
        self.ds_tipo_localizacao = ds_tipo_localizacao
        self.st_vacinacao_em_dia = st_vacinacao_em_dia
        self.st_hipertensao = st_hipertensao
        self.st_diabetes = st_diabetes
        self.st_gestante = st_gestante
        self.ds_sexo = ds_sexo
        self.dt_nascimento = dt_nascimento
        self.nu_idade = nu_idade
        self.ds_faixa_etaria = ds_faixa_etaria
        self.unidade_saude = unidade_saude
        self.atendimentos = atendimentos
        self.nome = nome
        

    def update(self):
      if self.atendimentos is not None:
        hipertensao = Hipertensao()
        diabetes = Diabetes()
        atendimento_dict = self.atendimentos.to_dict()
        cids = atendimento_dict["cad_filtro_cids"].replace("|","").split(",")
        ciaps = atendimento_dict["cad_filtro_ciap"].replace("|","").split(",")
        self.st_hipertensao = (
            hipertensao.check(cids) or 
            hipertensao.check(ciaps)
          )
        self.st_diabetes = (
            diabetes.check(cids) or 
            diabetes.check(ciaps)
          ) 
        
    def to_dict(self):
      diabetes = Diabetes()
      hipertensao = Hipertensao()
      pessoa_dict = {
          "co_fat_cidadao_pec": self.co_fat_cidadao_pec,
          "ds_tipo_localizacao": PessoaEnums.get_label(self.ds_tipo_localizacao.value),
          "st_vacinacao_em_dia": self.st_vacinacao_em_dia,
          "st_hipertensao": None,
          "st_diabetes": None,
          "st_gestante": self.st_gestante,
          "ds_sexo": PessoaEnums.get_label(self.ds_sexo),
          "dt_nascimento": self.dt_nascimento.strftime("%Y-%m-%d"),
          "nu_idade": self.nu_idade,
          "ds_faixa_etaria": self.ds_faixa_etaria,
          "nome": self.nome
          } 
      pessoa_dict.update(self.unidade_saude.to_dict())

        
      return pessoa_dict

  
def parse_pessoa_cadatro_mestre(pessoa_dict, atendimentos):  
  hipertensao = Hipertensao()
  diabetes = Diabetes()
  pessoa_dict.pop("nome")
  if atendimentos is not None:
    atendimento_dict = atendimentos.to_dict()
    pessoa_dict.update(atendimento_dict)
    
    cids = pessoa_dict["cad_filtro_cids"].replace("|","").split(",")
    ciaps = pessoa_dict["cad_filtro_ciap"].replace("|","").split(",")
    pessoa_dict["st_hipertensao"] = (
        hipertensao.check(cids) or 
        hipertensao.check(ciaps)
      )
    pessoa_dict["st_diabetes"] = (
        diabetes.check(cids) or 
        diabetes.check(ciaps)
      )  
    return pessoa_dict  
  
def parse_pessoa_atendimento_model(pessoa_dict, atendimentos, type='hipertensao'):
  if atendimentos is not None:
    if type == 'diabetes':
      atendimentos_adapter = DiabetesDictAdapter(atendimentos=atendimentos)
      pessoa_dict["st_diabetes"] = 1
    else:
      atendimentos_adapter = HipertensaoDictAdapter(atendimentos=atendimentos)
      pessoa_dict["st_hipertensao"] = 1
      
    atendimento_dict = atendimentos_adapter.to_dict()
    pessoa_dict.update(atendimento_dict)
        
    pessoa_dict["IMC"] = pessoa_dict["IMC"][-1]
    pessoa_dict["IMC_FINAL"] = pessoa_dict["IMC_FINAL"][-1]
    
  return pessoa_dict  

# def age_group(age):
#    if age >= 0 and age <=5:
#      return "Faixa 1"
#    elif age >= 6 and age <=12:
#      return "Faixa 2"
#    elif age >= 13 and age <=17:
#      return "Faixa 3"
#    elif age >= 18 and age <=29:
#      return "Faixa 4"
#    elif age >= 30 and age <=44:
#      return "Faixa 5"
#    elif age >= 45 and age <=59:
#      return "Faixa 6"
#    elif age >= 60:
#      return "Faixa 7"
#    else:
#      return "NaN"
   
# def age_range_by_age_group(age: str):
#   return {
#     "Faixa 1": (0, 5),
#     "Faixa 2": (6, 12),
#     "Faixa 3": (13, 17),
#     "Faixa 4": (18, 29),
#     "Faixa 5": (30, 44),
#     "Faixa 6": (45, 59),
#     "Faixa 7": (60, 100),
#     }[age]

def age_group(age):
  if age >= 0 and age <=17:
    return "Faixa 1"
  elif age >= 18 and age <=29:
    return "Faixa 2"
  elif age >= 30 and age <=44:
    return "Faixa 3"
  elif age >= 45 and age <=59:
    return "Faixa 4"
  elif age >= 60:
    return "Faixa 5"
  else:
    return "NaN"

def age_range_by_age_group(age: str):
  return {
    "Faixa 1": (0, 17),
    "Faixa 2": (18, 29),
    "Faixa 3": (30, 44),
    "Faixa 4": (45, 59),
    "Faixa 5": (60, 100),
    }[age]