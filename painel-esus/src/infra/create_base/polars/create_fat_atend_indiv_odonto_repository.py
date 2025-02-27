import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.env.conf import getenv
from src.errors.logging import logging
from src.infra.db.settings.connection import DBConnectionHandler

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
]
fao_vars_str = ", ".join(fao_vars)


SQL = (
    f"SELECT {fao_vars_str} FROM tb_fat_atendimento_odonto order by co_seq_fat_atd_odnt"
)

class CreateAtendOdontoBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_atendimento_odonto'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
            _next = True
            schema_fixo =  self.get_schema() 

            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 2500000)
            parquet_file = f"{self._base}.parquet"
            writer = None 
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    df = pd.read_sql_query(
                        text(f'{SQL}  LIMIT {chunk_size} OFFSET {offset};'), con=engine,dtype_backend='pyarrow')

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    if not df.empty:

                        table = pa.Table.from_pandas(df,preserve_index = False,schema=schema_fixo)

                        if writer is None:

                            writer = pq.ParquetWriter("dados/input/"+parquet_file,schema=schema_fixo) #, schema=schema_fixo

                        writer.write_table(table)

            if writer:
                writer.close()  
        except Exception as e:
            logging.exception(e)

    def get_schema(self):
        # Definindo o schema fixo
        schema = pa.schema([
            pa.field('co_seq_fat_atd_odnt', pa.int64()),
            pa.field('co_fat_cidadao_pec', pa.int64()),
            pa.field('co_dim_tempo', pa.int64()),
            pa.field('co_dim_cbo_1', pa.int64()),
            pa.field('co_dim_cbo_2', pa.int64()),
            pa.field('ds_filtro_cids', pa.string()),
            pa.field('ds_filtro_ciaps', pa.string()),
            pa.field('ds_filtro_procedimentos', pa.string()),
            pa.field('nu_peso', pa.float64()),
            pa.field('nu_altura', pa.float64()),
        ])
        return schema
