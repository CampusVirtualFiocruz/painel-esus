import logging
from src.infra.create_base.polars.scripts_dados.indicadores_crianca_polars import (
    gerar_banco,
)


class CreateIndicadoresCriancasRepository():
    _base = 'indicadores_crianca'
    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:
            gerar_banco()

        except FileNotFoundError as e:
            # Trata o caso onde o interpretador Python não é encontrado
            logging.error(e)
        except Exception as e:
            # Trata quaisquer outras exceções
            error = f"Ocorreu um erro inesperado no script de criança: {str(e)}"
            logging.error(error)
            