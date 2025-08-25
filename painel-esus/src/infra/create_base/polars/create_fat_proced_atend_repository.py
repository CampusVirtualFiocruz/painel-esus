import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateProcedAtendBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_proced_atend'
    _sql = ""

    def __init__(self):
        lista_vars = [
            "co_seq_fat_proced_atend",
            "co_dim_cbo",
            "co_dim_tempo",
            "ds_filtro_procedimento",
            "co_fat_cidadao_pec",
            "nu_altura",
            "nu_peso",
        ]
        self._sql = "SELECT {} FROM tb_fat_proced_atend order by co_seq_fat_proced_atend".format(", ".join(lista_vars))
        
        dtype = {
            "co_seq_fat_proced_atend": pd.Int64Dtype(),
            "co_dim_cbo": pd.Int64Dtype(),
            "co_dim_tempo": pd.Int64Dtype(),
            "ds_filtro_procedimento": pd.StringDtype(),
            "co_fat_cidadao_pec": pd.Int64Dtype(),
            "nu_peso": pd.Float64Dtype(),
            "nu_altura": pd.Float64Dtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
