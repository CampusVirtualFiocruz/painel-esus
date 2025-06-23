import logging
import os
import subprocess

import polars

from src.infra.create_base.polars.scripts_dados.indicadores_crianca_polars import (
    gerar_banco,
)


class CreateIndicadoresCriancasRepository():

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
            gerar_banco()

        except subprocess.CalledProcessError as e:
            # Log detalhado do erro
            logging.error("Erro ao executar o script criança:")
            logging.error(e.stderr)
        except FileNotFoundError as e:
            # Trata o caso onde o interpretador Python não é encontrado
            logging.error(e)
        except Exception as e:
            # Trata quaisquer outras exceções
            logging.error(f"Ocorreu um erro inesperado no script de criança: {str(e)}")