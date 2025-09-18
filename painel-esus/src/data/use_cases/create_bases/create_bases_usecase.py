# pylint: disable=C0411
from typing import List

from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.domain.use_cases.create_bases.create_bases import CreateBasesUsecasesInterface
from src.errors import InvalidArgument
from src.presentations.controllers.create_bases.rich_progess import (
    InstallJobs,
    StartGeneration,
)


class CreateBasesUseCase(CreateBasesUsecasesInterface):

    def __init__(
        self, bases_generators: List[CreateBasesRepositoryInterface] = None
    ) -> None:
        self.__bases_generators = bases_generators

    def create_bases(self):
        if self.__bases_generators is None:
            raise InvalidArgument("No bases to generate was passed.")
        jobs = InstallJobs(
            creation=self.__bases_generators[0], 
            key_factors=self.__bases_generators[1],
        )

        generation = StartGeneration(jobs)
        generation.run()

    def destroy_bases(self):
        pass
