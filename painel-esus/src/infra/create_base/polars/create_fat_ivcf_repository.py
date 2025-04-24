from src.infra.db.settings.connection import DBConnectionHandler
from src.env.conf import getenv
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase
import pandas as pd
class CreatIvcfBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_ivcf'


    def __init__(self):
        lista_vars = ['co_seq_fat_ivcf','co_fat_cidadao_pec','co_dim_tempo']
        
        dtype = {
            'co_seq_fat_ivcf': pd.Int64Dtype(),
            'co_fat_cidadao_pec': pd.Int64Dtype(),
            'co_dim_tempo': pd.Int64Dtype()
        }
        self._sql = "SELECT {} FROM tb_fat_ivcf order by co_seq_fat_ivcf".format(", ".join(lista_vars))
        super().__init__( DBConnectionHandler(), self._sql, dtype)
        

    def get_base(self):
        return self._base

    