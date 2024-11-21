# import pandas as pd
# from sqlalchemy import text
# import pyarrow as pa
# import pyarrow.parquet as pq
import logging
import os
import subprocess

import polars
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.infra.create_base.polars.scripts_dados.indicadores_crianca_polars import (
    gerar_banco,
)


class CreateIndicadoresCriancasRepository(CreateBasesRepositoryInterface):

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
            gerar_banco()

        except subprocess.CalledProcessError as e:
            # Log detalhado do erro
            logging.error("Erro ao executar o script idosos.py:")
            logging.error(e.stderr)
        except FileNotFoundError:
            # Trata o caso onde o interpretador Python não é encontrado
            logging.error("Python não encontrado. Verifique se o Python está instalado e no PATH.")
        except Exception as e:
            # Trata quaisquer outras exceções
            logging.error(f"Ocorreu um erro inesperado: {str(e)}")
