import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateEquipeBaseRepository(AbstractGenerateBase):
    _base = "tb_equipe"
    _sql = "select * from tb_equipe"

    def __init__(self):
        dtype={
            'co_seq_equipe': pd.Int64Dtype(),
            'nu_ine': pd.StringDtype(),
            'st_ativo': pd.Int64Dtype(),
            'co_unidade_saude': pd.Int64Dtype(),
            'qt_referencia': pd.Int64Dtype(),
            'tp_equipe': pd.Int64Dtype(),
            'ds_area': pd.Int64Dtype(),
            'no_equipe': pd.StringDtype(),
            'no_equipe_filtro': pd.StringDtype(),
            'co_unico_equipe': pd.StringDtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
