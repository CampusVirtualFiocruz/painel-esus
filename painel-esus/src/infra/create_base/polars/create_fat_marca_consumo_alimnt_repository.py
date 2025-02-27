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

lista_vars = ["co_seq_fat_marca_con_almnt", "co_fat_cidadao_pec", "co_dim_tempo"]
lista_vars_str = ", ".join(lista_vars)

EQUIPES = f"SELECT {lista_vars_str} FROM tb_fat_marca_consumo_alimnt order by co_seq_fat_marca_con_almnt"


class CreateMarcaConsumoBaseRepository(
    CreateBasesRepositoryInterface
):
    _base = "tb_fat_marca_consumo_alimnt"

    def __init__(self): ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
            schema_fixo = self.get_schema()
            _next = True
            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 2500000)
            parquet_file = f"{self._base}.parquet"
            writer = None
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    df = pd.read_sql_query(
                        text(f"{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};"),
                        con=engine,
                        dtype_backend="pyarrow",
                    )

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    if not df.empty:

                        table = pa.Table.from_pandas(
                            df, preserve_index=False, schema=schema_fixo
                        )

                        if writer is None:

                            working_directory = os.getcwd()
                            input_path = os.path.join(
                                working_directory, "dados", "input"
                            )
                            writer = pq.ParquetWriter(
                                input_path + os.sep + parquet_file, schema_fixo
                            )

                        writer.write_table(table)

            if writer:
                writer.close()
        except Exception as e:
            logging.exception(e)

    def get_schema(self):
        # Definindo o schema fixo

        schema = pa.schema(
            [
                pa.field("co_seq_fat_marca_con_almnt", pa.int64()),
                pa.field("co_fat_cidadao_pec", pa.int64()),
                pa.field("co_dim_tempo", pa.int64()),
            ]
        )

        return schema
