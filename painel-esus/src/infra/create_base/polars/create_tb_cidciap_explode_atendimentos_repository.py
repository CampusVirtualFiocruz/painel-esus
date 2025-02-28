import logging

# import pandas as pd
# from sqlalchemy import text
# import pyarrow as pa
# import pyarrow.parquet as pq
# import polars
# import subprocess
import os
from datetime import datetime

# import sys
import polars as pl
from dateutil.relativedelta import relativedelta
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)

# from src.infra.create_base.polars.scripts_dados.gerar_cid_ciap_atendimentos_individuais import (
#     gerar_banco,
# )


# class CreateCidCiapExplodeAtendimentosRepository(CreateBasesRepositoryInterface):

#     def __init__(self):
#         ...

#     def get_base(self):
#         return self._base

#     def create_base(self):
#         try:
#             gerar_banco()

#         except FileNotFoundError as e:
#             # Trata o caso onde o interpretador Python não é encontrado
#             logging.error(str(e))
#         except Exception as e:
#             # Trata quaisquer outras exceções
#             logging.error(f"Ocorreu um erro inesperado: {str(e)}")





class CreateCidCiapExplodeAtendimentosRepository(CreateBasesRepositoryInterface):

    def __init__(self): ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:

            current_dir = os.path.dirname(os.path.abspath(__file__))

            current_dir = os.getcwd()

            input_path = os.path.join(current_dir, "dados", "input", "")

            output_path = os.path.join(current_dir, "dados", "output", "")

            # fai = pl.read_parquet(input_path+"tb_fat_atendimento_individual.parquet")
            fai_lazy = pl.scan_parquet(
                input_path + "tb_fat_atendimento_individual.parquet"
            )


            fai_lazy = fai_lazy.select(
                "co_seq_fat_atd_ind",
                "ds_filtro_cids",
                "ds_filtro_ciaps",
                "ds_filtro_proced_avaliados",
                "ds_filtro_proced_solicitados",
            )

            # Função genérica para processamento das colunas
            def processar_coluna(
                lf: pl.LazyFrame, coluna: str, tipo: str
            ) -> pl.LazyFrame:
                return (
                    lf.select(
                        [pl.col("co_seq_fat_atd_ind"), pl.col(coluna).str.split("|")]
                    )
                    .explode(coluna)
                    .filter(pl.col(coluna) != "")
                    .rename({coluna: "codigo"})
                    .with_columns(tipo=pl.lit(tipo))
                )

            transformacoes = [
                ("ds_filtro_cids", "CIDS"),
                ("ds_filtro_ciaps", "CIAPS"),
                ("ds_filtro_proced_avaliados", "Procedimentos Avaliados"),
                ("ds_filtro_proced_solicitados", "Procedimentos Solicitados"),
            ]

            # Processa todas as colunas paralelamente usando threading
            processed_frames = [
                processar_coluna(fai_lazy, col, tipo) for col, tipo in transformacoes
            ]

            # Combina todos os resultados
            final_lazy = (
                pl.concat(processed_frames).select(
                    ["co_seq_fat_atd_ind", "codigo", "tipo"]
                )
                # Ordenação final única se necessária
                # .sort(by=["co_seq_fat_atd_ind"], descending=False)
            )

            # Executa o pipeline e salva otimizando
            final_lazy.sink_parquet(
                input_path + "fat_atd_ind_cod.parquet",
                compression="zstd",  # Compactação mais eficiente
                statistics=True,  # Habilita estatísticas para query
                row_group_size=8192,  # Tamanho ideal para maioria dos casos
            )

            # final_df.write_parquet(input_path+"fat_atd_ind_cod.parquet")
        except Exception as e:
            # Trata quaisquer outras exceções
            logging.error(f"Ocorreu um erro inesperado em fat atd ind cods: {str(e)}")
