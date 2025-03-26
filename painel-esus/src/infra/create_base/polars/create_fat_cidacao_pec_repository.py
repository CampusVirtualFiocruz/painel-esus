import pandas as pd
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase

class CreateCidacaoPecBaseRepository(AbstractGenerateBase):
    _base = 'tb_fat_cidadao_pec'
    _sql = "select * from tb_fat_cidadao_pec order by co_seq_fat_cidadao_pec"

    def __init__(self):
        dtype={
            'co_seq_fat_cidadao_pec': pd.Int64Dtype(),
            'co_cidadao': pd.Int64Dtype(),
            'nu_cns': pd.StringDtype(),
            'no_cidadao': pd.StringDtype(),
            'no_social_cidadao': pd.StringDtype(),
            'co_dim_tempo_nascimento': pd.Int64Dtype(),
            'co_dim_sexo': pd.Int64Dtype(),
            'co_dim_identidade_genero': pd.Int64Dtype(),
            'nu_telefone_celular': pd.StringDtype(),
            'st_faleceu': pd.Int64Dtype(),
            'st_lookup_etl': pd.Int64Dtype(),
            'st_deletar': pd.Int64Dtype(),
            'nu_cpf_cidadao': pd.StringDtype(),
            'co_dim_unidade_saude_vinc': pd.Int64Dtype(),
            'co_dim_equipe_vinc': pd.Int64Dtype(),
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base

