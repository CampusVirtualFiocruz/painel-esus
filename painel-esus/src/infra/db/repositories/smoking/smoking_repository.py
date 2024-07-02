import pandas as pd
from src.data.interfaces.smoking_repository import (
    SmokingRepository as SmokingRepositoryInterface,
)
from src.infra.db.repositories.sqls.max_dt_atendimento_atendimento_individual import (
    MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL,
)
from src.infra.db.repositories.sqls.smoking.smoking_base import SMOKING_BASE
from src.infra.db.repositories.update_bases import UpdateBasesRepository
from src.infra.db.settings.connection import DBConnectionHandler


class SmokingRepository(SmokingRepositoryInterface):

    def _load_data(self):
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine
            )
            max_date = str(max_date["max"].iloc[0])
            sql = SMOKING_BASE
            sql += f""" and  tfai.co_dim_tempo::text::date between '{max_date}'::DATE - interval '12 month' and now()::date"""

            res = pd.read_sql_query(SMOKING_BASE, con=engine)
            return res
        return pd.DataFrame(data=[])

    def create_database(self):
        smoking = self._load_data()
        update_bases = UpdateBasesRepository()
        update_bases.update_bases(smoking, "atendimento_tabagismo")

    def followed_smoked_people_proportion(self, cnes: int = None):
        return pd.DataFrame(
            data=[
                {
                    "tag": "acompanhadas-ubs-nao-tabagistas",
                    "value": 4451,
                },
                {
                    "tag": "acompanhadas-ubs-tabagistas",
                    "value": 4451,
                },
            ],
        )

    def risk_factors_proportion_by_dant(self, cnes: int = None):
        return pd.DataFrame(
            data=[
                {
                    "tag": "doenca-cardiovascular",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "cancer",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "diabetes-melitus",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "doenca-respiratoria-cronica",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
            ],
        )

    def smokers_by_age(self, cnes: int = None):
        return pd.DataFrame(
            data=[
                {
                    "tag": "ate-30",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "ate-40",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "ate-50",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
            ],
        )

    def proportion_of_dental_consultations_among_smokers(self, cnes: int = None):
        return pd.DataFrame(
            data=[
                {
                    "tag": "sim",
                    "value": 71,
                },
                {
                    "tag": "nao",
                    "value": 39,
                },
            ],
        )

    def smokers_by_sex(self, cnes: int = None):
        return pd.DataFrame(
            data=[
                {
                    "tag": "ate-30",
                    "value": {
                        "masc": 10,
                        "fem": 12,
                    },
                },
                {
                    "tag": "ate-40",
                    "value": {
                        "masc": 10,
                        "fem": 12,
                    },
                },
                {
                    "tag": "ate-50",
                    "value": {
                        "masc": 10,
                        "fem": 12,
                    },
                },
            ],
        )

    def smokers_by_education(self, cnes: int = None):
        return pd.DataFrame(
            data=[
                {
                    "tag": "analfabeto",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "primeiro-grau-completo",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
                {
                    "tag": "primeiro-grau-incompleto",
                    "value": {
                        "urbana": 10,
                        "rural": 12,
                    },
                },
            ],
        )
