#import pandas as pd
#from sqlalchemy import text
#import pyarrow as pa
#import pyarrow.parquet as pq
import logging
import os
import subprocess

import polars
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)


class CreateIndicadoresIdososRepository(CreateBasesRepositoryInterface):


    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
             current_dir = os.path.dirname(os.path.abspath(__file__))

             script_path = os.path.join(current_dir, 'scripts_dados', 'Indicadores_Idoso_Polars.py')

            # print(script_path)

             resultado = subprocess.run(
                    ['python', script_path],
                    check=True,             # Levanta uma exceção se o comando falhar
                    stdout=subprocess.PIPE, # Captura a saída padrão
                    stderr=subprocess.PIPE, # Captura a saída de erro
                    text=True               # Retorna a saída como string
                )
             print("Script idoso executado com sucesso:")
             print(resultado.stdout)
         
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
