import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateFamiliaTerrBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_familia_territorio'
    _sql = "select * from tb_fat_familia_territorio order by co_seq_fat_familia_territorio"

    def __init__(self):
        dtype={
            'co_seq_fat_familia_territorio': pd.Int64Dtype(),
            'co_dim_municipio': pd.Int64Dtype(),
            'co_dim_unidade_saude': pd.Int64Dtype(),
            'co_dim_equipe': pd.Int64Dtype(),
            'nu_uuid_ficha_origem': pd.StringDtype(),
            'co_fat_cidadao_pec': pd.Int64Dtype(),
            'co_fat_cad_domiciliar': pd.Int64Dtype(),
            'co_dim_tempo_fcd': pd.Int64Dtype(),
            'nu_prontuario': pd.StringDtype(),
            'nu_micro_area': pd.StringDtype(),
            'st_familia_fcd_mudouse': pd.Int64Dtype(),
            'st_resp_com_fci_no_territorio': pd.Int64Dtype(),
            'st_resp_declarado_no_fci': pd.Int64Dtype(),
            'st_resp_outro_fcd_mais_atual': pd.Int64Dtype(),
            'st_responsavel_ainda_reside': pd.Int64Dtype(),
            'st_responsavel_vivo': pd.Int64Dtype(),
            'st_familia_consistente': pd.Int64Dtype(),
            'st_processo_att_cidadao': pd.Int64Dtype(),
            'co_fat_cidadao_territorio': pd.Int64Dtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base
