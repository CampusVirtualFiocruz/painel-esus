import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateVisistaDomiciliarBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_visita_domiciliar'
    _sql = ""

    def __init__(self):
        lista_vars = [
                "co_seq_fat_visita_domiciliar",
                "co_dim_cbo",
                "co_dim_tempo",
                "co_fat_cidadao_pec",
                "nu_peso",
                "nu_altura"

            ]
        self._sql = "SELECT {} FROM tb_fat_visita_domiciliar order by co_seq_fat_visita_domiciliar".format(", ".join(lista_vars))
        
        dtype={
            "co_seq_fat_visita_domiciliar": pd.Int64Dtype(),
            "co_dim_cbo": pd.Int64Dtype(),
            "co_dim_tempo": pd.Int64Dtype(),
            "co_fat_cidadao_pec": pd.Int64Dtype(),
            "nu_peso": pd.Float64Dtype(),
            "nu_altura": pd.Float64Dtype()
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
