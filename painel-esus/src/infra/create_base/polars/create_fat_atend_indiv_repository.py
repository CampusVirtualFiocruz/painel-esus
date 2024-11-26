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

EQUIPES = "select * from tb_fat_atendimento_individual"

class CreateAtendIndivBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_atendimento_individual'

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
                    # print(text(f"{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};"))
                    df = pd.read_sql_query(
                        text(f'{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};'), con=engine,dtype_backend='pyarrow')

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    #      df.to_sql(name=self._base, con=local_engine,
                    #                  if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(df,schema=schema_fixo,preserve_index = False,)

                        if writer is None:
                            working_directory  = os.getcwd()
                            input_path = os.path.join(working_directory, "dados", "input") 
                            writer = pq.ParquetWriter(input_path+os.sep+parquet_file, schema_fixo)

                        writer.write_table(table)

            if writer:
                writer.close()  
        except Exception as e:
            print(str(e))
            print(f'Erro {self._base} already destroyed!')

    def get_schema(self):
        # Definindo o schema fixo
        schema = pa.schema([
            pa.field('co_seq_fat_atd_ind', pa.int64()),
            pa.field('co_dim_municipio', pa.int64()),
            pa.field('co_dim_tipo_ficha', pa.int64()),
            pa.field('co_dim_profissional_1', pa.int64()),
            pa.field('co_dim_profissional_2', pa.int64()),
            pa.field('co_dim_cbo_1', pa.int64()),
            pa.field('co_dim_cbo_2', pa.int64()),
            pa.field('co_dim_unidade_saude_1', pa.int64()),
            pa.field('co_dim_unidade_saude_2', pa.int64()),
            pa.field('co_dim_equipe_1', pa.int64()),
            pa.field('co_dim_equipe_2', pa.int64()),
            pa.field('co_dim_tempo', pa.int64()),
            pa.field('co_dim_racionalidade_saude', pa.int64()),
            pa.field('nu_uuid_ficha', pa.string()),
            pa.field('nu_atendimento', pa.int64()),
            pa.field('nu_cns', pa.string()),
            pa.field('dt_nascimento', pa.date32()),
            pa.field('co_dim_faixa_etaria', pa.int64()),
            pa.field('co_dim_sexo', pa.int64()),
            pa.field('co_dim_turno', pa.int64()),
            pa.field('co_dim_local_atendimento', pa.int64()),
            pa.field('co_dim_tipo_atendimento', pa.int64()),
            pa.field('nu_peso', pa.float64()),
            pa.field('nu_altura', pa.float64()),
            pa.field('nu_perimetro_cefalico', pa.float64()),
            pa.field('st_vacinacao_em_dia', pa.float64()),
            pa.field('co_dim_aleitamento', pa.int64()),
            pa.field('co_dim_tempo_dum', pa.int64()),
            pa.field('st_gravidez_planejada', pa.float64()),
            pa.field('nu_idade_gestacional_semanas', pa.float64()),
            pa.field('nu_gestas_previas', pa.float64()),
            pa.field('nu_partos', pa.float64()),
            pa.field('co_dim_modalidade_ad', pa.int64()),
            pa.field('st_ficou_em_observacao', pa.float64()),
            pa.field('st_nasf_avaliacao_diagnostico', pa.int64()),
            pa.field('st_nasf_proce_clin_terapeutico', pa.int64()),
            pa.field('st_nasf_prescricao_terapeutica', pa.int64()),
            pa.field('st_conduta_consulta_agendada', pa.int64()),
            pa.field('st_conduta_cuidd_conti_program', pa.int64()),
            pa.field('st_conduta_agendamento_grupos', pa.int64()),
            pa.field('st_conduta_agendamento_nasf', pa.int64()),
            pa.field('st_conduta_alta_episodio', pa.int64()),
            pa.field('st_encaminhamento_interno_dia', pa.int64()),
            pa.field('st_encaminhamento_serv_special', pa.int64()),
            pa.field('st_encaminhamento_caps', pa.int64()),
            pa.field('st_encaminhamento_intern_hospi', pa.int64()),
            pa.field('st_encaminhamento_urgencia', pa.int64()),
            pa.field('st_encaminhamento_servico_ad', pa.int64()),
            pa.field('st_encaminhamento_intersetoria', pa.int64()),
            pa.field('ds_filtro_cids', pa.string()),
            pa.field('ds_filtro_ciaps', pa.string()),
            pa.field('ds_filtro_proced_avaliados', pa.string()),
            pa.field('ds_filtro_proced_solicitados', pa.string()),
            pa.field('nu_prontuario', pa.string()),
            pa.field('nu_uuid_dado_transp', pa.string()),
            pa.field('co_dim_tipo_origem_dado_transp', pa.int64()),
            pa.field('co_dim_cds_tipo_origem', pa.int64()),
            pa.field('co_fat_cidadao_pec', pa.int64()),
            pa.field('dt_inicial_atendimento', pa.string() ),
            pa.field('dt_final_atendimento', pa.string() ),
            pa.field('nu_cpf_cidadao', pa.string()),  # Mudança de null para string
            pa.field('st_conduta_manter_observacao', pa.int64()),
            pa.field('co_dim_prof_finalizador_obs', pa.int64()),
            pa.field('co_dim_cbo_finalizador_obs', pa.int64()),
            pa.field('co_dim_ubs_finalizador_obs', pa.int64()),
            pa.field('co_dim_equipe_finalizador_obs', pa.int64()),
            pa.field('co_dim_tp_particip_cidadao', pa.int64()),
            pa.field('co_dim_tp_particip_prof_conv', pa.int64()),
            pa.field('st_conduta_agendamento_emulti', pa.string()),  # Mudança de null para string
            pa.field('st_nasf', pa.int64()),
            pa.field('nu_circ_abdominal', pa.float64()),  # Mudança de null para string
            pa.field('nu_perim_panturrilha', pa.float64()),  # Mudança de null para string
            pa.field('nu_pressao_sistolica', pa.int32()),  # Mudança de null para string
            pa.field('nu_pressao_diastolica', pa.int32()),  # Mudança de null para string
            pa.field('nu_freq_respiratoria', pa.string()),  # Mudança de null para string
            pa.field('nu_freq_cardiaca', pa.int32()),  # Mudança de null para string
            pa.field('nu_temperatura', pa.float64()),  # Mudança de null para string
            pa.field('nu_saturacao_o2', pa.int32()),  # Mudança de null para string
            pa.field('nu_glicemia', pa.int32()),  # Mudança de null para string
            pa.field('co_dim_tipo_glicemia', pa.int64())  # Mudança de null para string
        ])
        return schema
