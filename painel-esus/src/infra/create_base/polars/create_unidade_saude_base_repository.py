import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase
class CreateUnidadesSaudeBaseRepository(AbstractGenerateBase):
    _base = 'tb_dim_unidade_saude'
    _sql = "select * from tb_dim_unidade_saude order by co_seq_dim_unidade_saude"

    def __init__(self):
        dtype={
            'co_seq_dim_unidade_saude': pd.Int64Dtype(),
            'nu_cnes': pd.StringDtype(),
            'no_unidade_saude': pd.StringDtype(),
            'no_bairro': pd.StringDtype(),
            'st_registro_valido': pd.Int64Dtype(),
            'ds_filtro': pd.StringDtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
