import logging

from src.infra.create_base.polars.scripts_dados.indicadores_saude_bucal_polars import (
    gerar_banco,
)


class CreateIndicadoresSaudeBucalRepository():

    _base = "indicadores_saude_bucal"
    
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
            logging.error(f"Ocorreu um erro inesperado: {str(e)}")
