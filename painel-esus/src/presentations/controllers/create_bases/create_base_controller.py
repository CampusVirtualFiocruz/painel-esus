# pylint: disable=E0401,C0301,W0612,W0611
from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.errors.logging import logging
from src.infra.create_base.create_diabetes_bases_repository import (
    CreateDiabetesBasesRepository,
)
from src.infra.create_base.create_hypertension_bases_repository import (
    CreateHypertensionBasesRepository,
)
from src.infra.create_base.create_oral_health_bases_repository import (
    CreateOralHealthBasesRepository,
)
from src.infra.create_base.create_smoking_bases_repository import (
    CreateSmokingBasesRepository,
)


class CreateBasesController:

    def create_bases(self):
        logging.info("Starting base generation")
        _list = [
            # CreateDiabetesBasesRepository(),
            CreateHypertensionBasesRepository(),
            # CreateOralHealthBasesRepository(),
            # CreateSmokingBasesRepository()
        ]
        usecase = CreateBasesUseCase(bases_generators=_list)
        usecase.create_bases()
