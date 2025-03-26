import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateDimEquipesBaseRepository(AbstractGenerateBase):
    _base = 'tb_dim_equipe'
    _sql = "select * from tb_dim_equipe order by co_seq_dim_equipe"

    def __init__(self):
        dtype={
            'co_seq_dim_equipe': pd.Int64Dtype(),
            'nu_ine': pd.StringDtype(),
            'no_equipe': pd.StringDtype(),
            'st_registro_valido': pd.Int64Dtype(),
            'ds_filtro': pd.StringDtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
