# pylint: disable=E0401
from datetime import date
from typing import Dict

import pandas as pd
from pandas import DataFrame, Series

from src.data.interfaces.demographics_info import \
    DemographicsInfoRepository as DemographicsInfoRepositoryInterface
from src.domain.entities.diabetes import Diabetes
from src.domain.entities.hypertension import Hypertension
from src.domain.entities.pregnancy import Pregnants
from src.errors import InvalidArgument
from src.infra.db.repositories.enuns.individual_cares import IndividualCare
from src.infra.db.settings.connection import DBConnectionHandler

from .sqls import (ATENDIMENTO_INDIVIDUAL_CID_CIAPS, CIDADAO_PEC_VIVO,
                   MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL)

from src.env.conf import env

class DemographicsInfoRepository(DemographicsInfoRepositoryInterface):

    def __init__(self):
        self.indicators = None
        self.faixas_dict = {
            '1': '0 a 5 anos',
            '2': '6 a 12 anos',
            '3': '13 a 17 anos',
            '4': '18 a 29 anos',
            '5': '30 a 44 anos',
            '6': '45 a 59 anos',
            '7': '60 + anos'
        }

    def parse_date(self, data_frame: DataFrame) -> DataFrame:
        data_frame['idade'] = data_frame['co_dim_tempo_nascimento'].apply(
            lambda x: self.__calculate_age(
                date(int(str(x)[:4]),
                     int(str(x)[4:6]),
                     int(str(x)[6:8])
                     )
            )
        )
        return data_frame

    def __calculate_age(self, birth_date: str) -> int:
        today = date.today()
        age = (
            today.year - birth_date.year -
            ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age

    def __create_age_groups_items(self) -> Dict:
        return {
            '0 a 5 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '6 a 12 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '13 a 17 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '18 a 29 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '30 a 44 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '45 a 59 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '60 + anos': {
                'Rural': 0,
                'Urbano': 0
            },
        }

    def __create_age_groups(self) -> Dict:
        return {
            'Feminino': self.__create_age_groups_items(),
            'Masculino': self.__create_age_groups_items(),
        }

    def __hidrate_age_groups(self, row: Series, age_group: Dict) -> None:
        if row['faixas']:
            key = self.faixas_dict[str(row['faixas'])]
            gender = row['co_dim_sexo']
            location = row['co_dim_tipo_localizacao']
            value = int(row['qtd'])
            age_group[gender][key][location] = value

    def __parse_age_group(self, data_frame: DataFrame) -> tuple([DataFrame, DataFrame]):
        data_frame['faixas'] = ''
        mask_faixa1 = (data_frame['idade'] >= 0) & (data_frame['idade'] <= 5)
        data_frame.loc[mask_faixa1, 'faixas'] = '1'

        mask_faixa2 = (data_frame['idade'] >= 6) & (data_frame['idade'] <= 12)
        data_frame.loc[mask_faixa2, 'faixas'] = '2'

        mask_faixa3 = (data_frame['idade'] >= 13) & (data_frame['idade'] <= 17)
        data_frame.loc[mask_faixa3, 'faixas'] = '3'

        mask_faixa4 = (data_frame['idade'] >= 18) & (data_frame['idade'] <= 29)
        data_frame.loc[mask_faixa4, 'faixas'] = '4'

        mask_faixa5 = (data_frame['idade'] >= 30) & (data_frame['idade'] <= 44)
        data_frame.loc[mask_faixa5, 'faixas'] = '5'

        mask_faixa6 = (data_frame['idade'] >= 45) & (data_frame['idade'] <= 59)
        data_frame.loc[mask_faixa6, 'faixas'] = '6'

        mask_faixa7 = data_frame['idade'] >= 60
        data_frame.loc[mask_faixa7, 'faixas'] = '7'

        faixas = data_frame.groupby(
            by=['co_dim_sexo', 'co_dim_tipo_localizacao', 'faixas']
        ).size().reset_index(name='qtd')

        urbano_value = IndividualCare.get_('urbano')
        rural_value = IndividualCare.get_('rural')
        masculino = IndividualCare.get_('Masculino')
        feminino = IndividualCare.get_('Feminino')
        faixas.loc[faixas['co_dim_sexo'] ==
                   masculino, 'co_dim_sexo'] = 'Masculino'
        faixas.loc[faixas['co_dim_sexo'] ==
                   feminino, 'co_dim_sexo'] = 'Feminino'
        faixas.loc[
            faixas['co_dim_tipo_localizacao'] == urbano_value,
            'co_dim_tipo_localizacao'] = 'Urbano'
        faixas.loc[
            faixas['co_dim_tipo_localizacao'] == rural_value,
            'co_dim_tipo_localizacao'] = 'Rural'
        return tuple([data_frame, faixas])

    def retrieve_demographics_info(self, data_frame: DataFrame) -> Dict:
        if not isinstance(data_frame, DataFrame):
            raise InvalidArgument('df must be a DataFrame instance')
        data_frame = self.parse_date(data_frame)
        data_frame, faixas = self.__parse_age_group(data_frame)
        age_groups = self.__create_age_groups()
        faixas.apply(lambda x: self.__hidrate_age_groups(
            x, age_groups), axis=1)

        masculino = data_frame[data_frame['co_dim_sexo'] == 1].groupby(
            by=['co_dim_tipo_localizacao']
        ).size().reset_index(name='qtd')

        feminino = data_frame[data_frame['co_dim_sexo'] == 2].groupby(
            by=['co_dim_tipo_localizacao']
        ).size().reset_index(name='qtd')

        rural_value = IndividualCare.get_('rural')
        urbano_value = IndividualCare.get_('urbano')

        masculino_rural_size = masculino[masculino['co_dim_tipo_localizacao'] == rural_value]
        if masculino_rural_size.shape[0] > 0:
            masculino_rural_size = masculino_rural_size['qtd'].iloc[0]
        else:
            masculino_rural_size = 0

        feminino_rural_size = feminino[feminino['co_dim_tipo_localizacao'] == rural_value]
        if feminino_rural_size.shape[0] > 0:
            feminino_rural_size = feminino_rural_size['qtd'].iloc[0]
        else:
            feminino_rural_size = 0

        masculino_urbano_size = masculino[masculino['co_dim_tipo_localizacao'] == urbano_value]
        if masculino_urbano_size.shape[0] > 0:
            masculino_urbano_size = masculino_urbano_size['qtd'].iloc[0]
        else:
            masculino_urbano_size = 0

        feminino_urbano_size = feminino[feminino['co_dim_tipo_localizacao']
                                        == urbano_value]
        if feminino_urbano_size.shape[0] > 0:
            feminino_urbano_size = feminino_urbano_size['qtd'].iloc[0]
        else:
            feminino_urbano_size = 0

        response = {
            'total': int(data_frame.shape[0]),
            'ibgePopulation': env.get('POPULATION', '-'),
            'ageGroups': age_groups,
            'locationArea': {
                'rural': int(
                    masculino_rural_size +
                    feminino_rural_size
                ),
                'urbano': int(
                    masculino_urbano_size +
                    feminino_urbano_size
                ),
            },
            'gender': {
                'feminino': int(feminino['qtd'].sum()),
                'masculino': int(masculino['qtd'].sum())
            },
            'indicators': self.indicators
        }
        return response

    def parse_indicators(
        self,
        diabetes: DataFrame,
        hipertensao: DataFrame,
        gestantes: DataFrame
    ) -> None:
        if not isinstance(diabetes, DataFrame):
            raise InvalidArgument('diabetes must be a DataFrame instance')
        if not isinstance(hipertensao, DataFrame):
            raise InvalidArgument('hipertensao must be a DataFrame instance')
        if not isinstance(gestantes, DataFrame):
            raise InvalidArgument('gestantes must be a DataFrame instance')
        self.indicators = {
            'diabetes': {
                'rural': int(len(
                    diabetes[diabetes['co_dim_tipo_localizacao'] ==
                             IndividualCare.get_('rural')
                             ]['co_fat_cidadao_pec'].unique().tolist()
                )),
                'urbano': int(len(diabetes[diabetes['co_dim_tipo_localizacao'] ==
                                           IndividualCare.get_('urbano')
                                           ]['co_fat_cidadao_pec'].unique().tolist()
                                  ))
            },
            'gestantes': {
                'rural': int(len(
                    gestantes[gestantes['co_dim_tipo_localizacao'] ==
                              IndividualCare.get_('rural')
                              ]['co_fat_cidadao_pec'].unique().tolist()
                )),
                'urbano': int(len(
                    gestantes[gestantes['co_dim_tipo_localizacao'] ==
                              IndividualCare.get_('urbano')
                              ]['co_fat_cidadao_pec'].unique().tolist()
                ))
            },
            'hipertensao': {
                'rural': int(len(
                    hipertensao[hipertensao['co_dim_tipo_localizacao'] ==
                                IndividualCare.get_('rural')
                                ]['co_fat_cidadao_pec'].unique().tolist()
                )),
                'urbano': int(len(
                    hipertensao[hipertensao['co_dim_tipo_localizacao'] ==
                                IndividualCare.get_('urbano')
                                ]['co_fat_cidadao_pec'].unique().tolist()
                ))
            }
        }

    def get_demographics_info(self, cnes: int = None) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()

            cidadao_pec = pd.read_sql_query(CIDADAO_PEC_VIVO, con=engine)

            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine)
            max_date = str(max_date['max'].iloc[0])
            sql = ATENDIMENTO_INDIVIDUAL_CID_CIAPS
            if cnes:
                sql += f"""
                    where
                        atd.co_dim_unidade_saude = {cnes} AND dt_registro between '{max_date}'::DATE - interval '12 month' and '{max_date}';
                """
            else:
                sql += f"""
                    where
                        dt_registro between '{max_date}'::DATE - interval '12 month' and '{max_date}';
                """
            atendimento_individual = pd.read_sql_query(sql, con=engine)

            hypertension = Hypertension()
            hypertension_df = hypertension.filter_registers(
                atendimento_individual)

            diabetes = Diabetes()
            diabetes_df = diabetes.filter_registers(atendimento_individual)

            gestantes = Pregnants()
            gestantes_df = gestantes.filter_registers(atendimento_individual)

            self.parse_indicators(
                diabetes=diabetes_df,
                hipertensao=hypertension_df,
                gestantes=gestantes_df
            )

            return self.retrieve_demographics_info(cidadao_pec)
