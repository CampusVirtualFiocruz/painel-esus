import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateVacinacaoBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_vacinacao'
    _sql = ""

    def __init__(self):
        vac_vars = [
            'co_seq_fat_vacinacao',
            'co_fat_cidadao_pec',
            'ds_filtro_imunobiologico',
            'co_dim_tempo',
            'dt_nascimento'
            ]
        dtype={
            'co_seq_fat_vacinacao': pd.Int64Dtype(),
            'co_fat_cidadao_pec': pd.Int64Dtype(),
            'ds_filtro_imunobiologico': pd.StringDtype(),
            'co_dim_tempo': pd.Int64Dtype(),
            'dt_nascimento': pd.StringDtype(),
            }
        self._sql = "SELECT {} FROM tb_fat_vacinacao order by co_seq_fat_vacinacao".format(", ".join(vac_vars))
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
