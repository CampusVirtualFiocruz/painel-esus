import logging
import pandas as pd
import numpy as np
import collections
from ..helpers.str import treatNames, strToData
logging.basicConfig(level=logging.DEBUG)
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .load_bases import load_hipertensao_base, load_diabetes_base
def singleton(cls):
    instances = {}

    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance


def extractLastYearDate(_data):
  _lastDate = _data["co_dim_tempo"]
  lastDate = _lastDate.max()  
  lastYear = lastDate - relativedelta(years=1)
  return ( lastYear, lastDate )

def filterLastYear( data):
    (lastYear, lastDate) = extractLastYearDate(data)
    return data[ (data['co_dim_tempo'] >= lastYear) & (data['co_dim_tempo'] <= lastDate) ]


class BaseEntity:

  def findByCnes(self, nu_cnes = None):
    _data = self.getBase()
    if nu_cnes is not None:
      nu_cnes = int(nu_cnes.strip())
      mask = _data['nu_cnes'] == nu_cnes
      _data =  _data[mask]
      print(_data.shape)
    return _data

@singleton
class ArterialHypertensionBase(BaseEntity):
  _instance = {}
  _base = None

  def __init__(self):
    super().__init__()
    self._instance = None

  def getBase(self):
    if self._base is None:
      logging.info('Loading the pregnants final data base')
      self._base = load_hipertensao_base()
      logging.info('Base loaded')
    # print(self._base)
    return self._base


@singleton
class DiabetesBase(BaseEntity):
  _instance = {}
  _base = None

  def __init__(self):
    super().__init__()
    self._instance = None

  def getBase(self):
    if self._base is None:
      logging.info('Loading the pregnants final data base')
      self._base = load_diabetes_base()
      logging.info('Base loaded')
    # print(self._base)
    return self._base