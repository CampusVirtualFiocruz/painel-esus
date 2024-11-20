from typing import List

from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.domain.use_cases.create_bases.create_bases import CreateBasesUsecasesInterface
from src.errors import InvalidArgument
from src.errors import NoSuchTableError
from src.errors.logging import logging


class CreateBasesUseCase(CreateBasesUsecasesInterface):

    def __init__(
        self,
        bases_generators: List[CreateBasesRepositoryInterface] = None
    ) -> None:
        self.__bases_generators = bases_generators

    def create_bases(self):
        if self.__bases_generators is None:
            raise InvalidArgument('No bases to generate was passed.')
        for base in self.__bases_generators:
            if isinstance(base, CreateBasesRepositoryInterface):
                # try:
                #     base.destroy_base()
                # except NoSuchTableError:
                #     logging.info("Base already destroyed!")
                base.create_base()
            else:
                raise InvalidArgument(
                    'Base is no instance of CreateBasesRepositoryInterface.')

    def destroy_bases(self):
        pass
