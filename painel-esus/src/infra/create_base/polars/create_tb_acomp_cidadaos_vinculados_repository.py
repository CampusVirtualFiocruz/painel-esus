
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.create_base.polars.abstract_generate_base import AbstractGenerateBase
import pandas as pd

class CreateAcompCidadaosVinculadosBaseRepository(AbstractGenerateBase):
    _base = "tb_acomp_cidadaos_vinculados"
    _sql = "select * from tb_acomp_cidadaos_vinculados order by co_seq_acomp_cidadaos_vinc"

    def __init__(self):
        dtype = {
            'co_cds_domicilio': pd.Int64Dtype(),
            'co_cidadao': pd.Int64Dtype(),
            'co_seq_acomp_cidadaos_vinc': pd.Int64Dtype(),
            'co_unico_ultima_ficha': pd.StringDtype(),
            'ds_cep_domicilio': pd.StringDtype(),
            'ds_cep_tb_cidadao': pd.StringDtype(),
            'ds_complemento_domicilio': pd.StringDtype(),
            'ds_complemento_tb_cidadao': pd.StringDtype(),
            'ds_logradouro_domicilio': pd.StringDtype(),
            'ds_logradouro_domicilio_filtro': pd.StringDtype(),
            'ds_logradouro_tb_cidadao': pd.StringDtype(),
            'ds_logradouro_tb_cidadao_filtr': pd.StringDtype(),
            'ds_tipo_localizacao_domicilio': pd.StringDtype(),
            'no_bairro_domicilio': pd.StringDtype(),
            'no_bairro_domicilio_filtro': pd.StringDtype(),
            'no_bairro_tb_cidadao': pd.StringDtype(),
            'no_bairro_tb_cidadao_filtro': pd.StringDtype(),
            'no_cidadao': pd.StringDtype(),
            'no_equipe_vinc_equipe': pd.StringDtype(),
            'no_municipio_domicilio': pd.StringDtype(),
            'no_municipio_tb_cidadao': pd.StringDtype(),
            'no_raca_cor': pd.StringDtype(),
            'no_responsavel': pd.StringDtype(),
            'no_sexo_cidadao': pd.StringDtype(),
            'no_social_cidadao': pd.StringDtype(),
            'no_tipo_logradouro_domicilio': pd.StringDtype(),
            'no_tipo_logradouro_tb_cidadao': pd.StringDtype(),
            'nu_cnes_vinc_equipe': pd.StringDtype(),
            'nu_cns_cidadao': pd.StringDtype(),
            'nu_cpf_cidadao': pd.StringDtype(),
            'nu_fone_residencial': pd.StringDtype(),
            'nu_ine_vinc_equipe': pd.StringDtype(),
            'nu_micro_area_domicilio': pd.StringDtype(),
            'nu_micro_area_tb_cidadao': pd.StringDtype(),
            'nu_numero_domicilio': pd.StringDtype(),
            'nu_numero_tb_cidadao': pd.StringDtype(),
            'nu_telefone_celular': pd.StringDtype(),
            'nu_telefone_contato': pd.StringDtype(),
            'sg_uf_domicilio': pd.StringDtype(),
            'sg_uf_tb_cidadao': pd.StringDtype(),
            'st_possui_fcdt': pd.Int64Dtype(),
            'st_possui_fci': pd.Int64Dtype(),
            'st_sem_numero_domicilio': pd.Int64Dtype(),
            'st_sem_numero_tb_cidadao': pd.Int64Dtype(),
            'st_usar_cadastro_individual': pd.Int64Dtype(),
            'tp_identidade_genero_cidadao': pd.StringDtype(),
            'dt_nascimento_cidadao': pd.StringDtype(),
            'dt_ultima_atualizacao_cidadao': pd.StringDtype(),
            'dt_atualizacao_fcd': pd.StringDtype()
        }
        super().__init__( DBConnectionHandler(), self._sql, dtype)

    def get_base(self):
        return self._base

