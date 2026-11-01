# pylint: disable=E0401,C0301,W0612,W0611
import os
import shutil
from pathlib import Path

from sqlalchemy import text
from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.env import env
from src.errors.logging import logging
from src.infra.db.settings.connection import DBConnectionHandler
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
    CreateIndicadoresCriancasRepository,
    CreateIndicadoresDiabetesRepository,
    CreateIndicadoresHipertensaoRepository,
    CreateIndicadoresIdososRepository,
    CreateIndicadoresSaudeBucalRepository,
    CreateMarcaConsumoBaseRepository,
    CreateProcedAtendBaseRepository,
    CreateTbDimCboRepository,
    CreateUnidadesSaudeBaseRepository,
    CreateVacinacaoBaseRepository,
    CreateVisistaDomiciliarBaseRepository,
    CreatIvcfBaseRepository,
)


class CreateBasesController:

    def create_bases(self):
        working_directory  = os.getcwd()
        input_path = os.path.join(working_directory, "dados") 

        if "GENERATE_BASE" not in env or env["GENERATE_BASE"] == "True":
            # Sem banco, mantem a base anterior: apagar antes deixaria o painel sem dados ate a proxima geracao
            try:
                with DBConnectionHandler().get_engine().connect() as conn:
                    conn.execute(text("select 1"))
            except Exception as e:
                logging.error("Banco indisponivel, base atual mantida: %s", type(e).__name__)
                return
            try:
                shutil.rmtree(input_path)
            except Exception as e:
                ...
            try:
                os.makedirs(input_path,exist_ok=False)
                os.makedirs(input_path + os.sep + 'input', exist_ok=False)
                os.makedirs(input_path + os.sep + "output", exist_ok=False)
            except:
                ...

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
                    CreatIvcfBaseRepository()
                ],
                [
                    CreateIndicadoresCadastroRepository(),
                    CreateIndicadoresHipertensaoRepository(),
                    CreateIndicadoresDiabetesRepository(),
                    CreateIndicadoresIdososRepository(),
                    CreateIndicadoresSaudeBucalRepository(),
                    CreateIndicadoresCriancasRepository()
                ]
            ]

            usecase = CreateBasesUseCase(bases_generators=_list)
            usecase.create_bases()

        else:
            logging.info("Skipping base generation")
