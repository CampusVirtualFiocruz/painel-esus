import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateTipoEquipeBaseRepository(AbstractGenerateBase):
    _base = 'tb_tipo_equipe'
    _sql = "select * from tb_tipo_equipe order by co_seq_tipo_equipe"

    def __init__(self):
        dtype={
            'co_seq_tipo_equipe': pd.Int64Dtype(),
            'sg_tipo_equipe': pd.StringDtype(),
            'no_tipo_equipe': pd.StringDtype(),
            'sg_tipo_equipe_filtro': pd.StringDtype(),
            'no_tipo_equipe_filtro': pd.StringDtype(),
            'nu_ms': pd.StringDtype(),
            'ds_tp_equipe': pd.StringDtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
