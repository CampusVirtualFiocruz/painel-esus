import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateCadIndividualBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_cad_individual'
    _sql = ""

    def __init__(self):
        fci_vars = [
            "co_seq_fat_cad_individual",
            "co_fat_cidadao_pec",
            "co_dim_equipe",
            "co_dim_tempo",
            "nu_micro_area",
            "st_hipertensao_arterial",
            "st_diabete",
            "nu_uuid_ficha",
            "co_dim_raca_cor",
        ]
        dtype = {
            "co_seq_fat_cad_individual": pd.Int64Dtype(),
            "co_fat_cidadao_pec": pd.Int64Dtype(),
            "co_dim_equipe": pd.Int64Dtype(),
            "co_dim_tempo": pd.Int64Dtype(),
            "nu_micro_area": pd.StringDtype(),
            "st_hipertensao_arterial": pd.Int64Dtype(),
            "st_diabete": pd.Int64Dtype(),
            "nu_uuid_ficha": pd.StringDtype(),
            "co_dim_raca_cor": pd.Int64Dtype(),
        }
        self._sql = "SELECT {} FROM tb_fat_cad_individual order by co_seq_fat_cad_individual".format(", ".join(fci_vars))
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
