# pylint: disable=E0401,C0301,W0612,W0611
import os
from pathlib import Path

from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.env import env
from src.errors.logging import logging
from src.infra.create_base.polars import (
    CreateAcompCidadaosVinculadosBaseRepository,
    CreateAtendIndivBaseRepository,
    CreateAtendOdontoBaseRepository,
    CreateAtvddColetivaBaseRepository,
    CreateCadIndividualBaseRepository,
    CreateCidCiapExplodeAtendimentosRepository,
    CreateDimEquipesBaseRepository,
    CreateDimRacaCorBaseRepository,
    CreateEquipeBaseRepository,
    CreateIndicadoresCadastroRepository,
    CreateIndicadoresDiabetesRepository,
    CreateIndicadoresHipertensaoRepository,
    CreateMarcaConsumoBaseRepository,
    CreateProcedAtendBaseRepository,
    CreateTbDimCboRepository,
    CreateUnidadesSaudeBaseRepository,
    CreateVacinacaoBaseRepository,
    CreateVisistaDomiciliarBaseRepository,
)


class CreateBasesController:

    def create_bases(self):
        working_directory  = os.getcwd()
        input_path = os.path.join(working_directory, "dados") 

        try:
            os.removedirs(input_path)
        except:
            ...
        try:
            os.makedirs(input_path,exist_ok=False)
            os.makedirs(input_path + os.sep + 'input', exist_ok=False)
            os.makedirs(input_path + os.sep + "output", exist_ok=False)
        except:
            ...
        
        if "GENERATE_BASE" not in env or env["GENERATE_BASE"] == "True":
            logging.info("Starting base generation")
            _list = [
                [
                    CreateCadIndividualBaseRepository(),
                    CreateProcedAtendBaseRepository(),
                    CreateDimEquipesBaseRepository(),
                    CreateEquipeBaseRepository(),
                    CreateVacinacaoBaseRepository(),
                    CreateVisistaDomiciliarBaseRepository(),
                    CreateMarcaConsumoBaseRepository(),
                    CreateAtvddColetivaBaseRepository(),
                    CreateUnidadesSaudeBaseRepository(),
                    CreateDimRacaCorBaseRepository(),
                    CreateAtendIndivBaseRepository(),
                    CreateAcompCidadaosVinculadosBaseRepository(),
                    CreateAtendOdontoBaseRepository(),
                    CreateTbDimCboRepository(),
                    CreateCidCiapExplodeAtendimentosRepository(),
                ],
                [
                    CreateIndicadoresCadastroRepository(),
                    CreateIndicadoresHipertensaoRepository(),
                    CreateIndicadoresDiabetesRepository()
                ]
            ]

            usecase = CreateBasesUseCase(bases_generators=_list)
            usecase.create_bases()

        else:
            logging.info("Skipping base generation")
