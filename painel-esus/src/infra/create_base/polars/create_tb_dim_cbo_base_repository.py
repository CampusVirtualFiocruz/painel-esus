import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateTbDimCboRepository(AbstractGenerateBase):
    _base = 'tb_dim_cbo'
    _sql = "select * from tb_dim_cbo order by co_seq_dim_cbo"
    def __init__(self):
        dtype={
            'co_seq_dim_cbo': pd.Int64Dtype(),
            'nu_cbo': pd.StringDtype(),
            'no_cbo': pd.StringDtype(),
            'st_registro_valido': pd.Int64Dtype(),
            'ds_filtro': pd.StringDtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
