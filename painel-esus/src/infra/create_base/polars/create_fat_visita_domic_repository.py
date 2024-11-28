import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.env.conf import getenv
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)

EQUIPES = "select * from tb_fat_visita_domiciliar order by co_seq_fat_visita_domiciliar"

class CreateVisistaDomiciliarBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_visita_domiciliar'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:

            schema_fixo =  self.get_schema() 

            local_db = LocalDBConnectionHandler()
            local_engine = local_db.get_engine()
            _next = True
            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 25000)
            parquet_file = f"{self._base}.parquet"
            # os.remove("dados/input/" + parquet_file)
            writer = None 
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    #print(text(f"{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};"))
                    df = pd.read_sql_query(
                        text(f'{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};'), con=engine,dtype_backend='pyarrow')

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                                if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(df,schema = schema_fixo,preserve_index = False)

                        if writer is None:

                            working_directory  = os.getcwd()
                            input_path = os.path.join(working_directory, "dados", "input") 
                            writer = pq.ParquetWriter(input_path+os.sep+parquet_file,schema_fixo) #, schema=schema_fixo

                        writer.write_table(table)

            if writer:
                writer.close()  
        except Exception as e:
            print(e)
            print(f'Erro {self._base} already destroyed!')

    def get_schema(self):
        # Definindo o schema fixo
        schema = pa.schema([
            pa.field('co_seq_fat_visita_domiciliar', pa.int64(), nullable=False),
            pa.field('nu_uuid_ficha', pa.string(), nullable=True),
            pa.field('co_dim_tipo_ficha', pa.int64(), nullable=True),
            pa.field('co_dim_municipio', pa.int64(), nullable=True),
            pa.field('co_dim_profissional', pa.int64(), nullable=True),
            pa.field('co_dim_cbo', pa.int64(), nullable=True),
            pa.field('co_dim_unidade_saude', pa.int64(), nullable=True),
            pa.field('co_dim_equipe', pa.int64(), nullable=True),
            pa.field('co_dim_tempo', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_imovel', pa.int64(), nullable=True),
            pa.field('co_dim_turno', pa.int64(), nullable=True),
            pa.field('co_dim_sexo', pa.int64(), nullable=True),
            pa.field('nu_micro_area', pa.string(), nullable=True),
            pa.field('nu_peso', pa.float64(), nullable=True),
            pa.field('nu_altura', pa.float64(), nullable=True),
            pa.field('nu_cns', pa.string(), nullable=True),
            pa.field('dt_nascimento', pa.string(), nullable=True),
            pa.field('co_dim_faixa_etaria', pa.int64(), nullable=True),
            pa.field('st_visita_compartilhada', pa.int32(), nullable=True),
            pa.field('st_mot_vis_cad_att', pa.int32(), nullable=True),
            pa.field('st_mot_vis_visita_periodica', pa.int32(), nullable=True),
            pa.field('st_mot_vis_busca_ativa', pa.int32(), nullable=True),
            pa.field('st_mot_vis_acompanhamento', pa.int32(), nullable=True),
            pa.field('st_mot_vis_egresso_internacao', pa.int32(), nullable=True),
            pa.field('st_mot_vis_ctrl_ambnte_vetor', pa.int32(), nullable=True),
            pa.field('st_mot_vis_convte_atvidd_cltva', pa.int32(), nullable=True),
            pa.field('st_mot_vis_orintacao_prevncao', pa.int32(), nullable=True),
            pa.field('st_mot_vis_outros', pa.int32(), nullable=True),
            pa.field('st_busca_ativa_consulta', pa.int32(), nullable=True),
            pa.field('st_busca_ativa_exame', pa.int32(), nullable=True),
            pa.field('st_busca_ativa_vacina', pa.int32(), nullable=True),
            pa.field('st_busca_ativa_bolsa_familia', pa.int32(), nullable=True),
            pa.field('st_acomp_gestante', pa.int32(), nullable=True),
            pa.field('st_acomp_puerpera', pa.int32(), nullable=True),
            pa.field('st_acomp_recem_nascido', pa.int32(), nullable=True),
            pa.field('st_acomp_crianca', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_desnutricao', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_reabil_deficie', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_hipertensao', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_diabetes', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_asma', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_dpoc_enfisema', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_cancer', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_doenca_cronica', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_hanseniase', pa.int32(), nullable=True),
            pa.field('st_acomp_pessoa_tuberculose', pa.int32(), nullable=True),
            pa.field('st_acomp_sintomaticos_respirat', pa.int32(), nullable=True),
            pa.field('st_acomp_tabagista', pa.int32(), nullable=True),
            pa.field('st_acomp_domiciliados_acamados', pa.int32(), nullable=True),
            pa.field('st_acomp_condi_vulnerab_social', pa.int32(), nullable=True),
            pa.field('st_acomp_condi_bolsa_familia', pa.int32(), nullable=True),
            pa.field('st_acomp_saude_mental', pa.int32(), nullable=True),
            pa.field('st_acomp_usuario_alcool', pa.int32(), nullable=True),
            pa.field('st_acomp_usuario_outras_drogra', pa.int32(), nullable=True),
            pa.field('st_ctrl_amb_vet_acao_educativa', pa.int32(), nullable=True),
            pa.field('st_ctrl_amb_vet_imovel_foco', pa.int32(), nullable=True),
            pa.field('st_ctrl_amb_vet_acao_mecanica', pa.int32(), nullable=True),
            pa.field('st_ctrl_amb_vet_tratamnt_focal', pa.int32(), nullable=True),
            pa.field('co_dim_desfecho_visita', pa.int64(), nullable=True),
            pa.field('nu_uuid_dado_transp', pa.string(), nullable=True),
            pa.field('nu_prontuario', pa.string(), nullable=True),
            pa.field('co_dim_tipo_origem_dado_transp', pa.int64(), nullable=True),
            pa.field('co_dim_cds_tipo_origem', pa.int64(), nullable=True),
            pa.field('co_fat_cidadao_pec', pa.int64(), nullable=True),
            pa.field('nu_cpf_cidadao', pa.string(), nullable=True),
            pa.field('co_dim_tipo_glicemia', pa.int64(), nullable=True),
            pa.field('nu_medicao_pressao_arterial', pa.string(), nullable=True),
            pa.field('nu_medicao_temperatura', pa.string(), nullable=True),
            pa.field('nu_medicao_glicemia', pa.string(), nullable=True),
            pa.field('nu_latitude', pa.float64(), nullable=True),
            pa.field('nu_longitude', pa.float64(), nullable=True),
            pa.field('co_uuid_origem_fcd', pa.string(), nullable=True),
            pa.field('st_processado_origem_fcd', pa.int32(), nullable=True),
        ])
        return schema
