# pylint: disable=E0401,W0012,R0915, R0914
# pylint: disable=E0501
# pylint: disable=E0401,C0301,W0612,W0611,R0912
import os
from collections import OrderedDict
from pathlib import Path
from typing import Dict

import pandas as pd
from sqlalchemy import text
from src.data.interfaces.demographics_info import (
    DemographicsInfoRepository as DemographicsInfoRepositoryInterface,
)
from src.env.conf import env
from src.errors import InvalidArgument
from src.errors.logging import logging
from src.infra.db.repositories.sqls.demographics import filter_by_gender_age
from src.infra.db.repositories.sqls.demographics import filter_by_localidade
from src.infra.db.repositories.sqls.demographics import filter_by_sexo
from src.infra.db.repositories.sqls.demographics import get_indicators_diabetes
from src.infra.db.repositories.sqls.demographics import get_indicators_hipertensao
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


class DemographicsInfoV2Repository(DemographicsInfoRepositoryInterface):

    def __init__(self):
        self.indicators = None
        self.faixas_dict = {
            "1": "0 a 4 anos",
            "2": "5 a 9 anos",
            "3": "10 a 14 anos",
            "4": "15 a 19 anos",
            "5": "20 a 24 anos",
            "6": "25 a 29 anos",
            "7": "30 a 34 anos",
            "8": "35 a 39 anos",
            "9": "40 a 44 anos",
            "10": "45 a 49 anos",
            "11": "50 a 54 anos",
            "12": "55 a 59 anos",
            "13": "60 a 64 anos",
            "14": "65 a 69 anos",
            "15": "70 a 74 anos",
            "16": "75 a 79 anos",
            "17": "80 a 84 anos",
            "18": "85 a 89 anos",
            "19": "90 a 94 anos",
            "20": "95 a 99 anos",
            "21": "100 ou mais",
        }

    def __create_age_groups_items(self) -> Dict:
        body = {
            "0 a 4 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "5 a 9 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "10 a 14 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "15 a 19 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "20 a 24 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "25 a 29 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "30 a 34 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "35 a 39 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "40 a 44 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "45 a 49 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "50 a 54 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "55 a 59 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "60 a 64 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "65 a 69 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "70 a 74 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "75 a 79 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "80 a 84 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "85 a 89 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "90 a 94 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "95 a 99 anos": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
            "100 ou mais": {"Rural": 0, "Urbano": 0, "Nao Informado": 0},
        }
        return OrderedDict(reversed(body.items()))

    def __create_age_groups(self, response) -> Dict:
        body = {
            "Feminino": self.__create_age_groups_items(),
            "Masculino": self.__create_age_groups_items(),
        }

        for resp in response:
            body[resp[0]][resp[1]][resp[2]] = int(resp[3])
        return body

    def get_demographics_info(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        with DBConnectionHandler().get_engine().connect() as con:

            sql = "select count(tus.*) total  from tb_acomp_cidadaos_vinculados tacv join tb_dim_unidade_saude tus on tus.nu_cnes = tacv.nu_cnes_vinc_equipe "
            if cnes is not None:
                statement = text(
                    f"{sql} where tus.co_seq_dim_unidade_saude  = {cnes} ;"
                )
            else:
                statement = text(f"{sql};")
            result = con.execute(
                statement,
            )
            db_response = next(result)

            path = os.getcwd()
            path = Path(path)
            path = os.path.join(path, "ibge.csv")
            df = pd.read_csv(path, sep=";")

            ibge = int(env.get("CIDADE_IBGE", 0))
            if ibge == "-":
                ibge_population = 0
            else:
                try:
                    df_ibge = df[df["IBGE"] == ibge]
                    ibge_population = df_ibge["POPULACAO"].iloc[0]
                    ibge_population = f"{ibge_population:_.0f}".replace("_", ".")
                except Exception as exc:
                    logging.exception(exc)
                    ibge_population = 0
            age_gender = filter_by_gender_age(cnes)
            statement = text(age_gender)
            result_age_gender = con.execute(
                statement,
            )
            age_groups = self.__create_age_groups(result_age_gender)
            location_area_sql = filter_by_localidade(cnes)
            statement = text(location_area_sql)
            result_location_area_sql = con.execute(
                statement,
            )
            location_body = {"rural": 0, "urbano": 0, "nao_definido": 0}
            for resp in result_location_area_sql:
                location_body[resp[0]] = int(resp[1])

            gender = {"feminino": 0, "masculino": 0}
            gender_sql = filter_by_sexo(cnes)
            statement = text(gender_sql)
            result_gender = con.execute(
                statement,
            )
            for resp in result_gender:
                gender[resp[0]] = int(resp[1])

            idicators_body = {
                "diabetes": {"rural": 0, "urbano": 0, "nao_informado": 0},
                "hipertensao": {"rural": 0, "urbano": 0, "nao_informado": 0},
            }
            with LocalDBConnectionHandler().get_engine().connect() as local_con:
                indicator_diabetes_sql = get_indicators_diabetes(cnes)
                result_diabetes = local_con.execute(
                    text(indicator_diabetes_sql),
                )
                for resp in result_diabetes:
                    idicators_body["diabetes"][resp[0]] = int(resp[1])

                indicator_hipertensao_sql = get_indicators_hipertensao(cnes)
                result_hipertensao = local_con.execute(
                    text(indicator_hipertensao_sql),
                )
                for resp in result_hipertensao:
                    idicators_body["hipertensao"][resp[0]] = int(resp[1])

            return {
                "total": db_response[0],
                "ibgePopulation": ibge_population,
                "ageGroups": age_groups,
                "locationArea": location_body,
                "gender": gender,
                "indicators": idicators_body,
            }
