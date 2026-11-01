# pylint: disable=E0401,C0301,W0612,W0611
import os
import shutil
from pathlib import Path

from sqlalchemy import text
from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.env import env
from src.errors.logging import logging
from src.infra.db.settings.connection import DBConnectionHandler
from src.presentations.controllers.create_bases.instalation_status import InstalationStatus
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


INDICADORES = ("cadastro_db", "crianca", "diabetes", "hipertensao", "idoso", "saude_bucal")


def _base_completa(pasta):
    for nome in INDICADORES:
        arquivo = os.path.join(pasta, "output", f"{nome}.parquet")
        if not os.path.isfile(arquivo) or os.path.getsize(arquivo) == 0:
            return False
    return True


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
            # A base atual so sai de cena depois que a nova estiver completa
            anterior = input_path + ".anterior"
            if _base_completa(input_path) or not os.path.isdir(anterior):
                shutil.rmtree(anterior, ignore_errors=True)
                if os.path.isdir(input_path):
                    os.replace(input_path, anterior)
            else:
                shutil.rmtree(input_path, ignore_errors=True)
            os.makedirs(input_path + os.sep + "input", exist_ok=True)
            os.makedirs(input_path + os.sep + "output", exist_ok=True)

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

            try:
                usecase = CreateBasesUseCase(bases_generators=_list)
                usecase.create_bases()
                if not _base_completa(input_path):
                    raise RuntimeError("Base gerada incompleta")
            except Exception as e:
                logging.exception(e)
                logging.error("Geracao falhou: base anterior restaurada")
                if os.path.isdir(anterior):
                    shutil.rmtree(input_path, ignore_errors=True)
                    os.replace(anterior, input_path)
                InstalationStatus().cancel()
                return
            if os.path.isdir(anterior + os.sep + "settings"):
                shutil.copytree(anterior + os.sep + "settings", input_path + os.sep + "settings", dirs_exist_ok=True)
            shutil.rmtree(anterior, ignore_errors=True)

        else:
            logging.info("Skipping base generation")
