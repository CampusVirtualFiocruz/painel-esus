import logging
import pandas as pd
import numpy as np
from app.models.load_bases import load_cadastro_mestre
import os
logging.basicConfig(level=logging.DEBUG)


def singleton(cls):
    instances = {}

    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance


@singleton
class IreceBase:
  _instance = {}
  _base = None

  def __init__(self):
    self._instance = None

  def getBase(self):
    if self._base is None:
      logging.info('Loading the final data base')
      self._base = load_cadastro_mestre()
    return self._base

  def gender(self, __data,  nu_cnes=None):
    _data = __data.copy()
    if nu_cnes is not None:
      _data =  _data.query( 'nu_cnes == {}'.format(nu_cnes) )

    gender = {
        "masculino": _data[_data['ds_sexo'] == 'Masculino'].shape[0],
        "feminino": _data[_data['ds_sexo'] == 'Feminino'].shape[0]
      }
    return gender


  def indicators(self, __data,  nu_cnes=None):
    _data = __data.copy()
    if nu_cnes is not None:
        _data = _data.query( 'nu_cnes == {}'.format(nu_cnes) ) #[(_data['nu_cnes'] == nu_cnes)]

    return {
        "hipertensao": {
            "rural": _data[(_data['st_hipertensao'] == 1) & (_data['ds_tipo_localizacao'] == 'Rural')].shape[0],
            "urbano": _data[(_data['st_hipertensao'] == 1) & (_data['ds_tipo_localizacao'] == 'Urbano')].shape[0]
          },
        "diabetes": {
            "rural": _data[(_data['st_diabetes'] == 1) & (_data['ds_tipo_localizacao'] == 'Rural')].shape[0],
            "urbano": _data[(_data['st_diabetes'] == 1) & (_data['ds_tipo_localizacao'] == 'Urbano')].shape[0]
        },
        "gestantes": {
            "rural": _data[(_data['st_gestante'] == 1) & (_data['ds_tipo_localizacao'] == 'Rural')].shape[0],
            "urbano": _data[(_data['st_gestante'] == 1) & (_data['ds_tipo_localizacao'] == 'Urbano')].shape[0]
        }
    }


  def locationArea(self, __data, nu_cnes=None):
    _data = __data.copy()
    if nu_cnes is not None:
        _data =  _data.query( 'nu_cnes == {}'.format(nu_cnes) )
  
    _data['ds_tipo_localizacao'] = _data['ds_tipo_localizacao'].str.lower()
    return _data.groupby(['ds_tipo_localizacao']).size().to_dict()

  def getTotalCnes( self, __data, nu_cnes=None):
    _data = __data.copy()
    if nu_cnes is not None:
      _data =  _data.query( 'nu_cnes == {}'.format(int(nu_cnes)) )
      return _data.shape[0]
    return _data.shape[0]

  def ageGroup(self, __data,  nu_cnes=None):
      _data = __data.copy()
      if nu_cnes is not None:
        _data =  _data.query( 'nu_cnes == {}'.format(nu_cnes) )
  
      faixaEtaria = {
          "Faixa 1": "Faixa etária 0 a 17 anos",
          "Faixa 2": "Faixa etária 18 a 29 anos",
          "Faixa 3": "Faixa etária 30 a 44 anos",
          "Faixa 4": "Faixa etária 45 a 59 anos",
          "Faixa 5": "Faixa etária 60 + anos",
          "nan": "nan"
      }
      _data['ds_faixa_etaria'] = _data['ds_faixa_etaria'].map(faixaEtaria)
      print( _data['ds_faixa_etaria'].unique())
      print(_data.groupby(
          ["ds_sexo", "ds_tipo_localizacao"]).size())

      piramide = pd.DataFrame({'count': _data.groupby(
          ["ds_sexo", "ds_faixa_etaria", "ds_tipo_localizacao"]).size()}).reset_index()

      result = piramide \
                .groupby('ds_sexo')\
                  .apply(lambda x:
                          [
                          x.groupby('ds_faixa_etaria').
                            apply(lambda y:
                                    dict(
                                        zip(y['ds_tipo_localizacao'], y['count']))
                                  ).to_dict()
                          ]
                        ) \
                .to_dict()
      return result

  def getDemographicInfo(self, nu_cnes = None):
    if nu_cnes is not None:
      nu_cnes = int(nu_cnes.strip())
    return  {
    "ibgePopulation": os.getenv('POPULATION', 72512),
    "total": self.getTotalCnes(self._base, nu_cnes),
    "gender":self.gender(self._base, nu_cnes),
    "locationArea": self.locationArea(self._base, nu_cnes),
    "ageGroups": self.ageGroup(self._base, nu_cnes),
    "indicators": self.indicators(self._base, nu_cnes)
    }


