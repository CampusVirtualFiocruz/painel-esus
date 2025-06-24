# pylint: disable=E0401,W0012,R0915, R0914
# pylint: disable=E0501
# pylint: disable=E0401,C0301,W0612,W0611,R0912
import os
from collections import OrderedDict
from pathlib import Path
from typing import Dict

import duckdb
import pandas as pd
from sqlalchemy import text
from src.data.interfaces.demographics_info import (
    DemographicsInfoRepository as DemographicsInfoRepositoryInterface,
)
from src.env.conf import env
from src.errors import InvalidArgument
from src.errors.logging import logging
from src.infra.db.repositories.children.children_repository import ChildrenRepository
from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository
from src.infra.db.repositories.oral_health.oral_health_repository import (
    OralHealthRepository,
)
from src.infra.db.repositories.sqls.demographics import (
    filter_by_gender_age,
    filter_by_localidade,
    filter_by_sexo,
)
from src.infra.db.repositories.sqls.disease.auto_referidos import (
    filter_diabetes_by_localidade,
    filter_hypertension_by_localidade,
)
from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas
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
        return OrderedDict(reversed(body.items())).copy()

    def __create_age_groups(self, response) -> Dict:
        body = {
            "Feminino": self.__create_age_groups_items(),
            "Masculino": self.__create_age_groups_items(),
        }

        for resp in response:
            if resp[0] in body:
                if all(item is not None for item in resp):
                    body[resp[0]][resp[1]][resp[2]] = resp[3]
        return body

    def get_total_people(self, cnes: int = None, equipe: int = None):
        sql_pessoas = get_pessoas(cnes=cnes,equipe=equipe)

        sql = f"""
                with pessoas as ({sql_pessoas})
                select count(*) total 
                from pessoas    
            """
        db_response = duckdb.sql(sql).fetchone()
        # print(db_response[0])
        return db_response[0] if len(db_response) > 0 else 0

    def get_ibge_total(self):
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
        return ibge_population

    def get_age_groups(self, cnes: int = None, equipe: int = None):
        age_gender = filter_by_gender_age(cnes, equipe)
        result_age_gender = duckdb.sql(age_gender).fetchall()
        age_groups = self.__create_age_groups(result_age_gender)
        return age_groups

    def get_by_place(self, cnes: int = None, equipe: int = None):
        location_area_sql = filter_by_localidade(cnes, equipe)
        result_location_area_sql = duckdb.sql(location_area_sql).fetchall()

        location_body = {"rural": 0, "urbano": 0, "nao_definido": 0}
        for resp in result_location_area_sql:
            location_body[resp[0]] = int(resp[1])
        return location_body

    def get_by_gender(self, cnes: int = None, equipe: int = None):
        gender = {"feminino": 0, "masculino": 0}
        gender_sql = filter_by_sexo(cnes, equipe)
        result_gender = duckdb.sql(gender_sql).fetchall()
        for resp in result_gender:
            gender[str(resp[0]).lower()] = int(resp[1])
        return gender

    def get_diabetes_location(self, cnes: int = None, equipe: int = None):
        location_area_sql = filter_diabetes_by_localidade(cnes, equipe)
        result_location_area_sql = duckdb.sql(location_area_sql).fetchall()

        location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        for resp in result_location_area_sql:
            if resp[0] is None:
                location_body["nao_informado"] = int(resp[1])
            else:
                location_body[resp[0]] = int(resp[1])
        return location_body

    def get_hypertension_location(self, cnes: int = None, equipe: int = None):
        location_area_sql = filter_hypertension_by_localidade(cnes, equipe)
        result_location_area_sql = duckdb.sql(location_area_sql).fetchall()

        location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        for resp in result_location_area_sql:
            if resp[0] is None:
                location_body["nao_informado"] = int(resp[1])
            else:
                location_body[resp[0]] = int(resp[1])
        return location_body

    def get_elderly_total(self, cnes: int = None, equipe: int = None):
        repo = ElderlyRepository()
        result_location_area_sql = repo.total_card(cnes, equipe)

        location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        location_map = {
            'rural':'rural',
            'urbana':'urbano'
        }
        for resp in result_location_area_sql:
            if resp[0] is None:
                location_body["nao_informado"] = int(resp[1])
            else:
                key = str(resp[0]).lower()
                if key in location_map:
                    key = location_map[key]
                else:
                    key = 'nao_informado'
                location_body[key] = int(resp[1])
        return location_body

    def get_children_total(self, cnes: int = None, equipe: int = None):
        repo = ChildrenRepository()
        result_location_area_sql = repo.total_card(cnes, equipe)

        location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        location_map = {
            'rural':'rural',
            'urbana':'urbano'
        }
        for resp in result_location_area_sql:
            if resp[0] is None:
                location_body["nao_informado"] = int(resp[1])
            else:
                key = str(resp[0]).lower()
                if key in location_map:
                    key = location_map[key]
                else:
                    key = 'nao_informado'
                location_body[key] = int(resp[1])
        return location_body
    
    def get_oral_health_total(self, cnes: int = None, equipe: int = None):
        repo = OralHealthRepository()
        result_location_area_sql = repo.total_card(cnes, equipe, 'atendidas')

        location_body = {"rural": 0, "urbano": 0, "nao_informado": 0}
        location_map = {
            'rural':'rural',
            'urbana':'urbano'
        }
        for resp in result_location_area_sql:
            if resp[0] is None:
                location_body["nao_informado"] = int(resp[1])
            else:
                key = str(resp[0]).lower()
                if key in location_map:
                    key = location_map[key]
                else:
                    key = 'nao_informado'
                location_body[key] = int(resp[1])
        return location_body

    def get_demographics_info(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")

        total_people = self.get_total_people(cnes, equipe)
        ibge_population = self.get_ibge_total()
        age_groups = self.get_age_groups(cnes, equipe)
        location_body = self.get_by_place(cnes, equipe)
        gender = self.get_by_gender(cnes, equipe)
        diabetes = self.get_diabetes_location(cnes,equipe)
        hypertension = self.get_hypertension_location(cnes, equipe)
        elderly = self.get_elderly_total(cnes, equipe)
        oral_health = self.get_oral_health_total(cnes, equipe)
        children = self.get_children_total(cnes, equipe)
        idicators_body = {
            "diabetes": diabetes,
            "hipertensao": hypertension,
            "crianca": children,
            "idosa": elderly,
            "saude_bucal": oral_health,
            "qualidade": {
                "rural": location_body["rural"],
                "urbano": location_body["urbano"],
                "nao_informado": location_body['nao_definido'],
            },
        }
        # with LocalDBConnectionHandler().get_engine().connect() as local_con:
        #     indicator_diabetes_sql = get_indicators_diabetes_plus_autorreferidos(
        #         cnes, equipe
        #     )
        #     result_diabetes = local_con.execute(
        #         text(indicator_diabetes_sql),
        #     )
        #     for resp in result_diabetes:
        #         idicators_body["diabetes"][resp[0]] = int(resp[1])

        #     indicator_hipertensao_sql = get_indicators_hipertensao_plus_autorreferidos(
        #         cnes, equipe
        #     )
        #     result_hipertensao = local_con.execute(
        #         text(indicator_hipertensao_sql),
        #     )
        #     for resp in result_hipertensao:
        #         idicators_body["hipertensao"][resp[0]] = int(resp[1])

        # indicator_idoso_sql = get_indicators_idoso(
        #     cnes, equipe
        # )
        # result_idoso = local_con.execute(
        #     text(indicator_idoso_sql),
        # )
        # for resp in result_idoso:
        #     key = (
        #         resp[0]
        #         .lower()
        #         .replace("zona ", "")
        #         .replace("n/i", "nao_informado")
        #         .replace("urbana", "urbano")
        #     )
        #     idicators_body["idosa"][key] = int(resp[1])

        # indicator_crianca_sql = get_indicators_crianca(cnes, equipe)
        # result_crianca = local_con.execute(
        #     text(indicator_crianca_sql),
        # )
        # for resp in result_crianca:
        #     key = (
        #         resp[0].lower().replace("zona ", "").replace("n/i", "nao_informado").replace("urbana", "urbano")
        #     )
        #     idicators_body["crianca"][key] = int(resp[1])
        return {
            "total": total_people,
            "ibgePopulation": ibge_population,
            "ageGroups": age_groups,
            "locationArea": location_body,
            "gender": gender,
            "indicators": idicators_body,
        }
