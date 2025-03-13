import logging

from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.infra.create_base.polars.scripts_dados.indicadores_diabetes_polars import (
    gerar_banco,
)


class CreateIndicadoresDiabetesRepository(CreateBasesRepositoryInterface):
    _base = "indicadores_diabetes"
    def __init__(self): ...

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
