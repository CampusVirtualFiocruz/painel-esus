# pylint: disable=C0411
from typing import List

from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.domain.use_cases.create_bases.create_bases import CreateBasesUsecasesInterface
from src.errors import InvalidArgument
from tqdm import tqdm


class CreateBasesUseCase(CreateBasesUsecasesInterface):

    def __init__(
        self, bases_generators: List[CreateBasesRepositoryInterface] = None
    ) -> None:
        self.__bases_generators = bases_generators

    def create_bases(self):
        if self.__bases_generators is None:
            raise InvalidArgument("No bases to generate was passed.")
        for base in tqdm(
            self.__bases_generators,
            ascii="░▒█",
            desc="Geração das Bases: ",
            colour="blue",
            leave=False,
        ):
            if isinstance(base, CreateBasesRepositoryInterface):
                base.create_base()
            else:
                raise InvalidArgument(
                    "Base is no instance of CreateBasesRepositoryInterface."
                )

    def destroy_bases(self):
        pass
