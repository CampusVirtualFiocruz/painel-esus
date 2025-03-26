from datetime import date
import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase



class CreateAtendIndivBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_atendimento_individual'
    _sql = ""

    def __init__(self):
        fai_vars = [
            "co_seq_fat_atd_ind",
            "co_fat_cidadao_pec",
            "co_dim_tempo",
            "co_dim_cbo_1",
            "co_dim_cbo_2",
            "nu_peso",
            "nu_altura",
            "dt_nascimento",
            "ds_filtro_cids",
            "ds_filtro_ciaps",
            "ds_filtro_proced_avaliados",
            "ds_filtro_proced_solicitados",
        ]
        dtype = {
            "co_seq_fat_atd_ind": pd.Int64Dtype(),
            "co_fat_cidadao_pec": pd.Int64Dtype(),
            "co_dim_tempo": pd.Int64Dtype(),
            "co_dim_cbo_1": pd.Int64Dtype(),
            "co_dim_cbo_2": pd.Int64Dtype(),
            "nu_peso": pd.Float64Dtype(),
            "nu_altura": pd.Float64Dtype(),
            "dt_nascimento": pd.StringDtype(),
            "ds_filtro_cids": pd.StringDtype(),
            "ds_filtro_ciaps": pd.StringDtype(),
            "ds_filtro_proced_avaliados": pd.StringDtype(),
            "ds_filtro_proced_solicitados": pd.StringDtype(),
        }
        
        self._sql = "SELECT {} FROM tb_fat_atendimento_individual order by co_seq_fat_atd_ind".format(", ".join(fai_vars))
        # ['dt_nascimento', 'co_dim_tempo']
        super().__init__( DBConnectionHandler(), self._sql, dtype )

    def get_base(self):
        return self._base

