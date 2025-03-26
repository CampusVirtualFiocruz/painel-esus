import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateAtvddColetivaBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_atvdd_coletiva_part'
    _sql = ""

    def __init__(self):
        lista_vars = [
            'co_seq_fat_atvdd_cltv_part',
            'co_fat_cidadao_pec',
            'co_dim_tempo',
            'nu_participante_peso',
            'nu_participante_altura',
            'co_dim_cbo'
            ]
        dtype = {
            'co_seq_fat_atvdd_cltv_part': pd.Int64Dtype(),
            'co_fat_cidadao_pec': pd.Int64Dtype(),
            'co_dim_tempo': pd.Int64Dtype(),
            'nu_participante_peso': pd.Float64Dtype(),
            'nu_participante_altura': pd.Float64Dtype(),
            'co_dim_cbo': pd.Int64Dtype()
            }
        self._sql = "SELECT {} FROM tb_fat_atvdd_coletiva_part order by co_seq_fat_atvdd_cltv_part".format(", ".join(lista_vars))
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base

