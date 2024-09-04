# pylint: disable=E0401,W0012,R0915
# pylint: disable=E0501
# pylint: disable=E0401,C0301,W0612,W0611,R0912
import os
from datetime import date
from datetime import datetime
from pathlib import Path
from typing import Dict

import pandas as pd
from pandas import DataFrame
from pandas import Series
from src.data.interfaces.demographics_info import \
    DemographicsInfoRepository as DemographicsInfoRepositoryInterface
from src.domain.entities.diabetes import Diabetes
from src.domain.entities.hypertension import Hypertension
from src.domain.entities.pregnancy import Pregnants
from src.env.conf import env
from src.errors import InvalidArgument
from src.errors.logging import logging
from src.infra.db.repositories.enuns.individual_cares import IndividualCare
from src.infra.db.settings.connection import DBConnectionHandler

from .sqls import ATENDIMENTO_INDIVIDUAL_CID_CIAPS
from .sqls import LISTAGEM_FCI
from .sqls import MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL


class DemographicsInfoRepository(DemographicsInfoRepositoryInterface):

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

    def parse_date(self, data_frame: DataFrame) -> DataFrame:
        data_frame["idade"] = data_frame["co_dim_tempo_nascimento"].apply(
            lambda x: self.__calculate_age(
                datetime.strptime(str(x), "%Y-%m-%d").date())
        )
        return data_frame

    def __calculate_age(self, birth_date: str) -> int:
        today = date.today()
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age

    def __create_age_groups_items(self) -> Dict:
        return {
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

    def __create_age_groups(self) -> Dict:
        return {
            "Feminino": self.__create_age_groups_items(),
            "Masculino": self.__create_age_groups_items(),
        }

    def __hidrate_age_groups(self, row: Series, age_group: Dict) -> None:
        if row["faixas"]:
            key = self.faixas_dict[str(row["faixas"])]
            gender = row["co_dim_sexo"]
            location = row["co_dim_tipo_localizacao"]
            value = int(row["qtd"])
            age_group[gender][key][location] = value

    def __parse_age_group(self, data_frame: DataFrame) -> tuple([DataFrame, DataFrame]):
        data_frame["faixas"] = ""
        mask_faixa1 = (data_frame["idade"] >= 0) & (data_frame["idade"] <= 4)
        data_frame.loc[mask_faixa1, "faixas"] = "1"

        mask_faixa2 = (data_frame["idade"] >= 5) & (data_frame["idade"] <= 9)
        data_frame.loc[mask_faixa2, "faixas"] = "2"

        mask_faixa3 = (data_frame["idade"] >= 10) & (data_frame["idade"] <= 14)
        data_frame.loc[mask_faixa3, "faixas"] = "3"

        mask_faixa4 = (data_frame["idade"] >= 15) & (data_frame["idade"] <= 19)
        data_frame.loc[mask_faixa4, "faixas"] = "4"

        mask_faixa5 = (data_frame["idade"] >= 20) & (data_frame["idade"] <= 24)
        data_frame.loc[mask_faixa5, "faixas"] = "5"

        mask_faixa6 = (data_frame["idade"] >= 25) & (data_frame["idade"] <= 29)
        data_frame.loc[mask_faixa6, "faixas"] = "6"

        mask_faixa7 = (data_frame["idade"] >= 30) & (data_frame["idade"] <= 34)
        data_frame.loc[mask_faixa7, "faixas"] = "7"

        mask_faixa8 = (data_frame["idade"] >= 35) & (data_frame["idade"] <= 39)
        data_frame.loc[mask_faixa8, "faixas"] = "8"

        mask_faixa9 = (data_frame["idade"] >= 40) & (data_frame["idade"] <= 44)
        data_frame.loc[mask_faixa9, "faixas"] = "9"

        mask_faixa10 = (data_frame["idade"] >= 45) & (
            data_frame["idade"] <= 49)
        data_frame.loc[mask_faixa10, "faixas"] = "10"

        mask_faixa11 = (data_frame["idade"] >= 50) & (
            data_frame["idade"] <= 54)
        data_frame.loc[mask_faixa11, "faixas"] = "11"

        mask_faixa12 = (data_frame["idade"] >= 55) & (
            data_frame["idade"] <= 59)
        data_frame.loc[mask_faixa12, "faixas"] = "12"

        mask_faixa13 = (data_frame["idade"] >= 60) & (
            data_frame["idade"] <= 64)
        data_frame.loc[mask_faixa13, "faixas"] = "13"

        mask_faixa14 = (data_frame["idade"] >= 65) & (
            data_frame["idade"] <= 69)
        data_frame.loc[mask_faixa14, "faixas"] = "14"

        mask_faixa15 = (data_frame["idade"] >= 70) & (
            data_frame["idade"] <= 74)
        data_frame.loc[mask_faixa15, "faixas"] = "15"

        mask_faixa16 = (data_frame["idade"] >= 75) & (
            data_frame["idade"] <= 79)
        data_frame.loc[mask_faixa16, "faixas"] = "16"

        mask_faixa17 = (data_frame["idade"] >= 80) & (
            data_frame["idade"] <= 84)
        data_frame.loc[mask_faixa17, "faixas"] = "17"

        mask_faixa18 = (data_frame["idade"] >= 85) & (
            data_frame["idade"] <= 89)
        data_frame.loc[mask_faixa18, "faixas"] = "18"

        mask_faixa19 = (data_frame["idade"] >= 90) & (
            data_frame["idade"] <= 94)
        data_frame.loc[mask_faixa19, "faixas"] = "19"

        mask_faixa20 = (data_frame["idade"] >= 95) & (
            data_frame["idade"] <= 99)
        data_frame.loc[mask_faixa20, "faixas"] = "20"

        mask_faixa21 = data_frame["idade"] >= 100
        data_frame.loc[mask_faixa21, "faixas"] = "21"
        faixas = (
            data_frame.groupby(
                by=["co_dim_sexo", "co_dim_tipo_localizacao", "faixas"])
            .size()
            .reset_index(name="qtd")
        )

        urbano_value = IndividualCare.get_("urbano")
        rural_value = IndividualCare.get_("rural")
        nao_informado = 1

        masculino = IndividualCare.get_("Masculino")
        feminino = IndividualCare.get_("Feminino")

        faixas.loc[faixas["co_dim_sexo"] ==
                   masculino, "co_dim_sexo"] = "Masculino"
        faixas.loc[faixas["co_dim_sexo"] ==
                   feminino, "co_dim_sexo"] = "Feminino"
        faixas.loc[
            faixas["co_dim_tipo_localizacao"] == urbano_value, "co_dim_tipo_localizacao"
        ] = "Urbano"
        faixas.loc[
            faixas["co_dim_tipo_localizacao"] == rural_value, "co_dim_tipo_localizacao"
        ] = "Rural"
        faixas.loc[
            faixas["co_dim_tipo_localizacao"] == nao_informado,
            "co_dim_tipo_localizacao",
        ] = "Nao Informado"

        return tuple([data_frame, faixas])

    def retrieve_demographics_info(self, data_frame: DataFrame) -> Dict:
        if not isinstance(data_frame, DataFrame):
            raise InvalidArgument("df must be a DataFrame instance")
        data_frame = self.parse_date(data_frame)
        data_frame, faixas = self.__parse_age_group(data_frame)

        age_groups = self.__create_age_groups()
        faixas.apply(lambda x: self.__hidrate_age_groups(
            x, age_groups), axis=1)

        _age_groups = dict()
        gender = ["Masculino", "Feminino"]
        for gender_ in gender:
            _age_groups[gender_] = dict()
            for i in list(age_groups[gender_].keys())[-1::-1]:
                _age_groups[gender_][i] = age_groups[gender_][i]
        age_groups = _age_groups

        masculino = (
            data_frame[data_frame["co_dim_sexo"] == 1]
            .groupby(by=["co_dim_tipo_localizacao"])
            .size()
            .reset_index(name="qtd")
        )

        feminino = (
            data_frame[data_frame["co_dim_sexo"] == 2]
            .groupby(by=["co_dim_tipo_localizacao"])
            .size()
            .reset_index(name="qtd")
        )

        rural_value = IndividualCare.get_("rural")
        urbano_value = IndividualCare.get_("urbano")

        masculino_rural_size = masculino[
            masculino["co_dim_tipo_localizacao"] == rural_value
        ]

        if masculino_rural_size.shape[0] > 0:
            masculino_rural_size = masculino_rural_size["qtd"].iloc[0]
        else:
            masculino_rural_size = 0

        feminino_rural_size = feminino[
            feminino["co_dim_tipo_localizacao"] == rural_value
        ]

        if feminino_rural_size.shape[0] > 0:
            feminino_rural_size = feminino_rural_size["qtd"].iloc[0]
        else:
            feminino_rural_size = 0

        masculino_urbano_size = masculino[
            masculino["co_dim_tipo_localizacao"] == urbano_value
        ]

        if masculino_urbano_size.shape[0] > 0:
            masculino_urbano_size = masculino_urbano_size["qtd"].iloc[0]
        else:
            masculino_urbano_size = 0

        feminino_urbano_size = feminino[
            feminino["co_dim_tipo_localizacao"] == urbano_value
        ]

        if feminino_urbano_size.shape[0] > 0:
            feminino_urbano_size = feminino_urbano_size["qtd"].iloc[0]
        else:
            feminino_urbano_size = 0

        path = os.getcwd()
        path = Path(path)
        path = os.path.join(path, 'ibge.csv')
        df = pd.read_csv(path, sep=";")

        ibge = int(env.get("CIDADE_IBGE", 0))
        if ibge == '-':
            ibge_population = 0
        else:
            try:
                df_ibge = df[df['IBGE'] == ibge]
                ibge_population = df_ibge['POPULACAO'].iloc[0]
                ibge_population = f'{ibge_population:_.0f}'.replace('_', '.')
            except Exception as exc:
                logging.exception(exc)
                ibge_population = 0
        response = {
            "total": data_frame.shape[0],
            "ibgePopulation": ibge_population,
            "ageGroups": age_groups,
            "locationArea": {
                "rural": int(masculino_rural_size + feminino_rural_size),
                "urbano": int(masculino_urbano_size + feminino_urbano_size),
                "nao_definido": int(
                    data_frame[
                        (data_frame["co_dim_tipo_localizacao"].isnull()) |
                        (data_frame["co_dim_tipo_localizacao"] == 1)
                    ].shape[0]
                ),
            },
            "gender": {
                "feminino": int(data_frame[data_frame["co_dim_sexo"] == 2].shape[0]),
                "masculino": int(data_frame[data_frame["co_dim_sexo"] == 1].shape[0]),
            },
            "indicators": self.indicators,
        }
        return response

    def parse_indicators(
        self, diabetes: DataFrame, hipertensao: DataFrame, gestantes: DataFrame
    ) -> None:
        if not isinstance(diabetes, DataFrame):
            raise InvalidArgument("diabetes must be a DataFrame instance")
        if not isinstance(hipertensao, DataFrame):
            raise InvalidArgument("hipertensao must be a DataFrame instance")
        if not isinstance(gestantes, DataFrame):
            raise InvalidArgument("gestantes must be a DataFrame instance")

        self.indicators = {
            "diabetes": {
                "rural": int(
                    diabetes[
                        diabetes["co_dim_tipo_localizacao"]
                        == IndividualCare.get_("rural")
                    ]["valor"]
                ),
                "urbano": int(
                    diabetes[
                        diabetes["co_dim_tipo_localizacao"]
                        == IndividualCare.get_("urbano")
                    ]["valor"]
                ),
                "nao_informado": int(
                    diabetes[diabetes["co_dim_tipo_localizacao"] == 1]["valor"]
                ),
            },
            "gestantes": {
                "rural": int(
                    len(
                        gestantes[
                            gestantes["co_dim_tipo_localizacao"]
                            == IndividualCare.get_("rural")
                        ]["co_fat_cidadao_pec"]
                        .unique()
                        .tolist()
                    )
                ),
                "urbano": int(
                    len(
                        gestantes[
                            gestantes["co_dim_tipo_localizacao"]
                            == IndividualCare.get_("urbano")
                        ]["co_fat_cidadao_pec"]
                        .unique()
                        .tolist()
                    )
                ),
            },
            "hipertensao": {
                "rural": int(
                    hipertensao[
                        hipertensao["co_dim_tipo_localizacao"]
                        == IndividualCare.get_("rural")
                    ]["valor"]
                ),
                "urbano": int(
                    hipertensao[
                        hipertensao["co_dim_tipo_localizacao"]
                        == IndividualCare.get_("urbano")
                    ]["valor"]
                ),
                "nao_informado": int(
                    hipertensao[hipertensao["co_dim_tipo_localizacao"]
                                == 1]["valor"]
                ),
            },
        }

    def get_demographics_info(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()

            # cidadao_pec = pd.read_sql_query(CIDADAO_PEC_VIVO, con=engine)
            listagem_fci = LISTAGEM_FCI
            if cnes:
                listagem_fci += f"""
    and t3.co_dim_unidade_saude = {cnes};
                """
            else:
                listagem_fci += ";"

            cidadao_pec = pd.read_sql_query(listagem_fci, con=engine)

            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine
            )
            max_date = str(max_date["max"].iloc[0])
            sql = ATENDIMENTO_INDIVIDUAL_CID_CIAPS
            # sql = LISTAGEM_FCI
            if cnes:
                sql += f"""
                     where
                         atd.co_dim_unidade_saude = {cnes}
                 """
            # else:
            #     sql += f"""
            #         where
            #             dt_registro between '{max_date}'::DATE - interval '12 month' and '{max_date}';
            #     """
            atendimento_individual = pd.read_sql_query(sql, con=engine)

            hypertension = Hypertension()
            hypertension_df = hypertension.filter_registers_sql(
                "hipertensao", cnes)

            diabetes = Diabetes()
            diabetes_df = diabetes.filter_registers_sql("diabetes", cnes)

            gestantes = Pregnants()
            gestantes_df = gestantes.filter_registers(atendimento_individual)

            self.parse_indicators(
                diabetes=diabetes_df,
                hipertensao=hypertension_df,
                gestantes=gestantes_df,
            )

            return self.retrieve_demographics_info(cidadao_pec)
