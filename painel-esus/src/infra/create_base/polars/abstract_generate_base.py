import os
from src.env.conf import getenv
from src.errors.logging import logging
import pandas as pd
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)

class AbstractGenerateBase(CreateBasesRepositoryInterface):
    def __init__(self, connection_handler, base_sql, dtype=None, parse_date=None):
        self.connection_handler = connection_handler
        self.base_sql = base_sql
        self.dtype = dtype
        self.parse_date=parse_date
    
    def create_base(self):
        try:
            parquet_file = f"{self._base}.parquet"
            # os.remove("dados/input/" + parquet_file)
            chunk_size = getenv("CHUNK_SIZE", 3000)
            
            working_directory  = os.getcwd()
            input_path = os.path.join(working_directory, "dados", "input") 
            
            with self.connection_handler as db:
                engine = db.get_engine()
                for chunk_dataframe in pd.read_sql(
                    sql= text(self.base_sql), 
                    con=engine, 
                    chunksize=chunk_size,
                    dtype=self.dtype,
                    parse_dates=self.parse_date
                    ):
                    
                    chunk_dataframe.to_parquet(
                        path=input_path+os.sep+parquet_file,
                        engine='fastparquet',
                        append=False,
                    )

        except Exception as e:
            logging.error("BASE: {} \n {}".format(self._base, __name__))
            logging.exception(e)