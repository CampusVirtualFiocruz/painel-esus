# pylint: disable=E0401,C0301,W0612,W0611
import os
from pathlib import Path

from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.env import env
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
from src.infra.create_base.local.create_base_factory import CreateLocalDatabaseFactory


class CreateBasesController:

    def create_bases(self):
        if os.getenv("ENV") == "instalador":
            path = "painel_esus.db"
        else:
            path = os.getcwd()
            path = Path(path.split("/painel-esus")[0])
            path = os.path.join(path, "painel_esus.db")
            path = os.path.relpath(path)
        # os.remove(path)
        if "GENERATE_BASE" not in env or env["GENERATE_BASE"] == "True":
            logging.info("Starting base generation")
            _list = [
                CreateLocalDatabaseFactory.demographics_factory(),
                CreateLocalDatabaseFactory.atendimento_individual_filtro_factory(),
                CreateLocalDatabaseFactory.units(),
                CreateDiabetesBasesRepository(),
                CreateHypertensionBasesRepository(),
                CreateOralHealthBasesRepository(),
            ]
            usecase = CreateBasesUseCase(bases_generators=_list)
            usecase.create_bases()
        else:
            logging.info("Skipping base generation")
