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

EQUIPES = "select * from tb_fat_vacinacao order by co_seq_fat_vacinacao"

class CreateVacinacaoBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_vacinacao'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
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
                        text(f'{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};'),  con=engine,dtype_backend='pyarrow')

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                              if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(df,preserve_index = False)

                        if writer is None:

                            working_directory  = os.getcwd()
                            input_path = os.path.join(working_directory, "dados", "input") 
                            writer = pq.ParquetWriter(input_path+os.sep+parquet_file, table.schema)

                        writer.write_table(table)

            if writer:
                writer.close()  
        except:
            print(f'Erro {self._base} already destroyed!')
