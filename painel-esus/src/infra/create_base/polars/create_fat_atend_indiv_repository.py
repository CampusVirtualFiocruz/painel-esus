import os
import time

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

fai_vars = [
    "co_seq_fat_atd_ind",
    "co_fat_cidadao_pec",
    "co_dim_tempo",
    "co_dim_cbo_1",
    "co_dim_cbo_2",
    "nu_peso",
    "nu_altura",
    "dt_nascimento",
    "ds_filtro_cids",
    "ds_filtro_ciaps",
    "ds_filtro_proced_avaliados",
    "ds_filtro_proced_solicitados",
    ]
fai_vars_str = ", ".join(fai_vars)

EQUIPES = f"SELECT {fai_vars_str} FROM tb_fat_atendimento_individual order by co_seq_fat_atd_ind"

class CreateAtendIndivBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_atendimento_individual'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:

            start_time = time.time()
            # current_dir = os.getcwd()
            schema_fixo = self.get_schema()

            local_db = LocalDBConnectionHandler()
            local_engine = local_db.get_engine()
            _next = True
            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 25000)
            parquet_file = f"{self._base}.parquet"
            writer = None
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    # print(text(f"{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};"))
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

                    df.to_sql(name=self._base, con=local_engine,
                                if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(
                            df, schema=schema_fixo, preserve_index=False
                        )

                        if writer is None:
                            working_directory = os.getcwd()
                            input_path = os.path.join(
                                working_directory, "dados", "input"
                            )
                            print(input_path + os.sep + parquet_file)
                            writer = pq.ParquetWriter(
                                input_path + os.sep + parquet_file, schema=schema_fixo
                            )

                        writer.write_table(table)

            if writer:
                writer.close()
            end_time = time.time()
            execution_time = end_time - start_time
        except Exception as e:
            print(e)
            print(f"Erro {self._base} already destroyed!")

    def get_schema(self):
        # Definindo o schema fixo
        schema = pa.schema(
            [
                pa.field("co_seq_fat_atd_ind", pa.int64()),
                pa.field("co_fat_cidadao_pec", pa.int64()),
                pa.field("co_dim_tempo", pa.int64()),
                pa.field("co_dim_cbo_1", pa.int64()),
                pa.field("co_dim_cbo_2", pa.int64()),
                pa.field("nu_peso", pa.float64()),
                pa.field("nu_altura", pa.float64()),
                pa.field("dt_nascimento", pa.date32()),
                pa.field("ds_filtro_cids",pa.string()),
                pa.field("ds_filtro_ciaps",pa.string()),
                pa.field("ds_filtro_proced_avaliados",pa.string()),
                pa.field("ds_filtro_proced_solicitados",pa.string()),
            ]
        )
        return schema
