import pandas as pd
from src.data.interfaces.smoking_repository import SmokingRepository as SmokingRepositoryInterface


class SmokingRepository(SmokingRepositoryInterface):
    def followed_smoked_people_proportion(self, cnes: int = None):
        return pd.DataFrame(data=[
            {
                "tag": "acompanhadas-ubs-nao-tabagistas",
                "value": 4451,
            },
            {
                "tag": "acompanhadas-ubs-tabagistas",
                "value": 4451,
            },
        ],)

    def risk_factors_proportion_by_dant(self, cnes: int = None):
        return pd.DataFrame(data=[
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
        ],)

    def smokers_by_age(self, cnes: int = None):
        return pd.DataFrame(data=[
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
        ],)

    def proportion_of_dental_consultations_among_smokers(
            self, cnes: int = None):
        return pd.DataFrame(data=[
            {
                "tag": "sim",
                "value": 71,
            },
            {
                "tag": "nao",
                "value": 39,
            },
        ],)

    def smokers_by_sex(self, cnes: int = None):
        return pd.DataFrame(data=[
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
        ],)

    def smokers_by_education(self, cnes: int = None):
        return pd.DataFrame(data=[
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
        ],)
