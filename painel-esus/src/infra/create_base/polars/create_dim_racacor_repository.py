import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase



class CreateDimRacaCorBaseRepository(AbstractGenerateBase):
    _base = 'tb_dim_raca_cor'
    _sql = "select * from tb_dim_raca_cor order by co_seq_dim_raca_cor"

    def __init__(self):
        dtype = {
            'co_seq_dim_raca_cor': pd.Int64Dtype(),
            'nu_identificador': pd.StringDtype(),
            'nu_ms': pd.StringDtype(),
            'ds_raca_cor': pd.StringDtype(),
            'co_ordem': pd.Int64Dtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
