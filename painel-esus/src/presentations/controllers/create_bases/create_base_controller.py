# pylint: disable=E0401,C0301,W0612,W0611
import os
from pathlib import Path

from parquet_db import gerar_banco
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.env import env
from src.errors.logging import logging
from src.infra.create_base.create_autorreferido_base_repository import (
    CreateAutorreferidoBaseRepository,
)
from src.infra.create_base.create_diabetes_bases_repository import (
    CreateDiabetesBasesRepository,
)
from src.infra.create_base.create_equipes_base_repository import (
    CreateEquipesBaseRepository,
)
from src.infra.create_base.create_hypertension_bases_repository import (
    CreateHypertensionBasesRepository,
)
from src.infra.create_base.create_nominal_lists_bases_repository import (
    CreateDiabetesNominalListRepository,
    CreateHypertensionNominalListRepository,
)
from src.infra.create_base.create_pessoas_base_repository import (
    CreatePessoasBaseRepository,
    CreateStatusRecordsRepository,
)
from src.infra.create_base.create_structure_base_repository import (
    CreateStructureBaseRepository,
)
from src.infra.create_base.create_units_base_repository import CreateUnitsBaseRepository
from src.infra.create_base.polars import (
    CreateAcompCidadaosVinculadosBaseRepository,
    CreateAtendIndivBaseRepository,
    CreateAtendOdontoBaseRepository,
    CreateCadDomiciliarBaseRepository,
    CreateCadIndividualBaseRepository,
    CreateCidacaoPecBaseRepository,
    CreateCidadaoBaseRepository,
    CreateCidCiapExplodeAtendimentosRepository,
    CreateDimRacaCorBaseRepository,
    CreateFamiliaTerrBaseRepository,
    CreateIndicadoresCriancasRepository,
    CreateIndicadoresIdososRepository,
    CreateProcedAtendBaseRepository,
    CreateTbDimCboRepository,
    CreateTipoEquipeBaseRepository,
    CreateUnidadesSaudeBaseRepository,
    CreateVacinacaoBaseRepository,
    CreateVisistaDomiciliarBaseRepository,
)


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
                CreateStructureBaseRepository(),
                CreatePessoasBaseRepository(),
                CreateAtendIndivBaseRepository(),
                CreateEquipesBaseRepository(),
                CreateUnidadesSaudeBaseRepository(),
                CreateTbDimCboRepository(),
                CreateAtendOdontoBaseRepository(),
                CreateCadIndividualBaseRepository(),
                CreateVacinacaoBaseRepository(),
                CreateCidacaoPecBaseRepository(),
                CreateProcedAtendBaseRepository(),
                CreateFamiliaTerrBaseRepository(),
                CreateCidadaoBaseRepository(),
                CreateCadDomiciliarBaseRepository(),
                CreateDimRacaCorBaseRepository(),
                CreateTipoEquipeBaseRepository(),
                CreateAcompCidadaosVinculadosBaseRepository(),
                CreateVisistaDomiciliarBaseRepository(),
                CreateCidCiapExplodeAtendimentosRepository(),
                CreateUnitsBaseRepository(),
                CreateAutorreferidoBaseRepository(),
                CreateDiabetesBasesRepository(),
                CreateHypertensionBasesRepository(),
                CreateDiabetesNominalListRepository(),
                CreateHypertensionNominalListRepository(),
                CreateStatusRecordsRepository(),
                CreateIndicadoresIdososRepository(),
                CreateIndicadoresCriancasRepository(),
            ]
            usecase = CreateBasesUseCase(bases_generators=_list)
            usecase.create_bases()

            
        else:
            logging.info("Skipping base generation")
