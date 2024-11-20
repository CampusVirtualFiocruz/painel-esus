import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)

SQL = "select * from tb_fat_proced_atend"

class CreateProcedAtendBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_proced_atend'

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
            chunk_size = 30000
            parquet_file = f"{self._base}.parquet"
            os.remove("dados/input/" + parquet_file)
            writer = None 
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    print(text(f"{SQL}  LIMIT {chunk_size} OFFSET {offset};"))
                    df = pd.read_sql_query(
                        text(f'{SQL}  LIMIT {chunk_size} OFFSET {offset};'), con=engine,dtype_backend='pyarrow')

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                                if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(df,preserve_index = False,schema = schema_fixo)

                        if writer is None:

                            writer = pq.ParquetWriter("dados/input/"+parquet_file,schema_fixo) #, schema=schema_fixo


                        writer.write_table(table)

            if writer:
                writer.close()  
        except Exception as e:
            print(e)
            print(f'Erro {self._base} already destroyed!')



    def get_schema(self):
            # Definindo o schema fixo
        schema = pa.schema([
            pa.field('co_seq_fat_proced_atend', pa.int64(), nullable=False),
            pa.field('co_fat_procedimento', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_ficha', pa.int64(), nullable=True),
            pa.field('co_dim_municipio', pa.int64(), nullable=True),
            pa.field('co_dim_unidade_saude', pa.int64(), nullable=True),
            pa.field('co_dim_equipe', pa.int64(), nullable=True),
            pa.field('co_dim_profissional', pa.int64(), nullable=True),
            pa.field('co_dim_cbo', pa.int64(), nullable=True),
            pa.field('co_dim_tempo', pa.int64(), nullable=True),
            pa.field('co_dim_sexo', pa.int64(), nullable=True),
            pa.field('co_dim_turno', pa.int64(), nullable=True),
            pa.field('co_dim_local_atendimento', pa.int64(), nullable=True),
            pa.field('co_dim_faixa_etaria', pa.int64(), nullable=True),
            pa.field('st_escuta_inicial', pa.int32(), nullable=True),
            pa.field('nu_uuid_ficha', pa.string(), nullable=True),
            pa.field('nu_atendimento', pa.int32(), nullable=True),
            pa.field('nu_cns', pa.string(), nullable=True),
            pa.field('dt_nascimento', pa.date32(), nullable=True),
            pa.field('ds_filtro_procedimento', pa.string(), nullable=True),
            pa.field('nu_uuid_dado_transp', pa.string(), nullable=True),
            pa.field('nu_prontuario', pa.string(), nullable=True),
            pa.field('co_dim_tipo_origem_dado_transp', pa.int64(), nullable=True),
            pa.field('co_dim_cds_tipo_origem', pa.int64(), nullable=True),
            pa.field('co_fat_cidadao_pec', pa.int64(), nullable=True),
            pa.field('dt_inicial_atendimento', pa.string(), nullable=True),
            pa.field('dt_final_atendimento', pa.string(), nullable=True),
            pa.field('nu_cpf_cidadao', pa.string(), nullable=True),
            pa.field('nu_peso', pa.float64(), nullable=True),
            pa.field('nu_altura', pa.float64(), nullable=True),
])

        return schema
