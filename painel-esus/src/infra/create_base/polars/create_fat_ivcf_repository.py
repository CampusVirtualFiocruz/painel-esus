from src.infra.db.settings.connection import DBConnectionHandler
import pandas as pd
from sqlalchemy import text
import pyarrow as pa
import pyarrow.parquet as pq
from src.env.conf import getenv

lista_vars = ['co_seq_fat_ivcf','co_fat_cidadao_pec','co_dim_tempo']
lista_vars_str = ', '.join(lista_vars)

SQL = f"SELECT {lista_vars_str} FROM tb_fat_ivcf order by co_seq_fat_ivcf"

class CreatIvcfBaseRepository:
    _base = 'tb_fat_ivcf'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:

            schema_fixo =  self.get_schema() 
            _next = True
            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 2500000)
            parquet_file = f"{self._base}.parquet"
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

                    if not df.empty:
                        table = pa.Table.from_pandas(df,schema = schema_fixo,preserve_index = False)

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
            pa.field('co_seq_fat_ivcf', pa.int64(), nullable=False),
            pa.field('co_dim_tempo', pa.int64(), nullable=True),
            pa.field('co_fat_cidadao_pec', pa.int64(), nullable=True),

        ])
        return schema


