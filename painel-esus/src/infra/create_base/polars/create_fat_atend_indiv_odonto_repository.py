import pandas as pd
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase
from src.infra.db.settings.connection import DBConnectionHandler


class CreateAtendOdontoBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_atendimento_odonto'
    _sql = ""

    def __init__(self):
        fao_vars = [
            "co_seq_fat_atd_odnt",
            "co_fat_cidadao_pec",
            "co_dim_tempo",
            "co_dim_cbo_1",
            "co_dim_cbo_2",
            "ds_filtro_cids",
            "ds_filtro_ciaps",
            "ds_filtro_procedimentos",
            "nu_peso",
            "nu_altura",
            "co_dim_tipo_consulta",
            "st_conduta_tratamento_concluid",
            "st_paciente_necessidades_espec",
            "st_gestante",
        ]
        dtype = {
            "co_seq_fat_atd_odnt": pd.Int64Dtype(),
            "co_fat_cidadao_pec": pd.Int64Dtype(),
            "co_dim_tempo": pd.Int64Dtype(),
            "co_dim_cbo_1": pd.Int64Dtype(),
            "co_dim_cbo_2": pd.Int64Dtype(),
            "ds_filtro_cids": pd.StringDtype(),
            "ds_filtro_ciaps": pd.StringDtype(),
            "ds_filtro_procedimentos": pd.StringDtype(),
            "nu_peso": pd.Float64Dtype(),
            "nu_altura": pd.Float64Dtype(),
            "co_dim_tipo_consulta": pd.Int64Dtype(),
            "st_conduta_tratamento_concluid": pd.Int64Dtype(),
            "st_paciente_necessidades_espec": pd.StringDtype(),
            "st_gestante": pd.StringDtype(),
        }
        self._sql = "SELECT {} FROM tb_fat_atendimento_odonto order by co_seq_fat_atd_odnt".format(", ".join(fao_vars))
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
