import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateMarcaConsumoBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_marca_consumo_alimnt'
    _sql = ""

    def __init__(self):
        lista_vars = ["co_seq_fat_marca_con_almnt", "co_fat_cidadao_pec", "co_dim_tempo"]
        
        self._sql = "SELECT {} FROM tb_fat_marca_consumo_alimnt order by co_seq_fat_marca_con_almnt".format(", ".join(lista_vars))
        
        dtype= {
            "co_seq_fat_marca_con_almnt": pd.Int64Dtype(),
            "co_fat_cidadao_pec": pd.Int64Dtype(),
            "co_dim_tempo": pd.Int64Dtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base

