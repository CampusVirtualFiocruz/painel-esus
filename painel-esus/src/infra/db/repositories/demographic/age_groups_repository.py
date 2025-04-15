# pylint: disable=W1202

from collections import OrderedDict
from typing import Dict

import duckdb
from src.data.interfaces.demographic_repository import DemographicAgeGroupsInterface
from src.errors.logging import logging
from src.infra.db.repositories.sqls.demographics import filter_by_gender_age


class AgeGroupsRepository(DemographicAgeGroupsInterface):

    def __init__(self, db_connection=duckdb):
        self.db = db_connection
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
                    logging.info(
                        "body[resp[0]][resp[1]][resp[2]] = int(resp[3]) => {}, {}, {}, {}".format(
                            resp[0], resp[1], resp[2], resp[3]
                        )
                    )
                    body[resp[0]][resp[1]][resp[2]] = resp[3]
        # print(body)
        return body

    def get_age_groups(self, cnes: int = None, equipe: int = None):
        age_gender = filter_by_gender_age(cnes, equipe)
        result_age_gender = self.db.sql(age_gender).fetchall()
        age_groups = self.__create_age_groups(result_age_gender)
        return age_groups
