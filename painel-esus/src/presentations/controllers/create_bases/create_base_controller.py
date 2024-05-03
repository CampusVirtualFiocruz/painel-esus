
from src.data.use_cases.create_bases.create_bases_usecase import \
    CreateBasesUseCase
from src.errors.logging import logging
from src.infra.create_base.create_diabetes_bases_repository import \
    CreateDiabetesBasesRepository
from src.infra.create_base.create_hypertension_bases_repository import \
    CreateHypertensionBasesRepository
from src.infra.create_base.create_oral_health_bases_repository import \
    CreateOralHealthBasesRepository


class CreateBasesController:

    def create_bases(self):
        logging.info('Starting base generation')
        _list = [
            CreateDiabetesBasesRepository(),
            CreateHypertensionBasesRepository(),
            CreateOralHealthBasesRepository()
        ]
        usecase = CreateBasesUseCase(bases_generators=_list)
        usecase.create_bases()
