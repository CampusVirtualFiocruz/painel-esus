# pylint: disable=invalid-name
# pylint: disable=unused-import
# pylint: disable=redefined-outer-name
# pylint: disable=E0401
from typing import Dict
from pandas import DataFrame
import pytest

from src.domain.entities.hypertension import Hypertension
from src.domain.entities.diabetes import Diabetes
from src.domain.entities.pregnancy import Pregnants
from src.errors import InvalidArgument
from src.data.use_cases.tests.data_frame_mocks.calc_age_data_frame import calc_age_df
from src.data.use_cases.tests.data_frame_mocks.demographics_info_df import (
    demographics_info_df,
    demographics_info_df_empty
)
from src.data.use_cases.tests.data_frame_mocks.atendimento_individual_df import (
    atendimento_individual_df,
    atendimento_individual_df_no_rurals,
    atendimento_individual_df_only_rurals,
    atendimento_individual_df_empty
)
from .demographics_info import DemographicsInfoRepository


@pytest.mark.usefixtures("calc_age_df")
def test_calculate_age(calc_age_df):
    df = calc_age_df
    demographics_info = DemographicsInfoRepository()
    response = demographics_info.parse_date(df)
    assert response['idade'].iloc[0] == 1
    assert response['idade'].iloc[1] == 35


@pytest.mark.usefixtures("demographics_info_df")
def test_retrieve_demographics_info(demographics_info_df):

    demographics_info = DemographicsInfoRepository()
    response = demographics_info.retrieve_demographics_info(
        demographics_info_df)

    assert response['total'] == 10
    assert response['locationArea']['rural'] == 4
    assert response['locationArea']['urbano'] == 6
    assert response['gender']['feminino'] == 5
    assert response['gender']['masculino'] == 5

    assert response['ageGroups']['Masculino']['0 a 5 anos']['Rural'] == 1
    assert response['ageGroups']['Masculino']['13 a 17 anos']['Rural'] == 1

    assert response['ageGroups']['Masculino']['30 a 44 anos']['Urbano'] == 1
    assert response['ageGroups']['Masculino']['45 a 59 anos']['Urbano'] == 1
    assert response['ageGroups']['Masculino']['60 + anos']['Urbano'] == 1

    assert response['ageGroups']['Feminino']['0 a 5 anos']['Rural'] == 1
    assert response['ageGroups']['Feminino']['6 a 12 anos']['Rural'] == 1

    assert response['ageGroups']['Feminino']['30 a 44 anos']['Urbano'] == 1
    assert response['ageGroups']['Feminino']['45 a 59 anos']['Urbano'] == 1
    assert response['ageGroups']['Feminino']['60 + anos']['Urbano'] == 1


@pytest.mark.usefixtures("demographics_info_df_empty")
def test_retrieve_demographics_info_when_empty_data(demographics_info_df_empty):
    demographics_info = DemographicsInfoRepository()
    response = demographics_info.retrieve_demographics_info(
        demographics_info_df_empty)
    assert response['total'] == 0
    assert response['locationArea']['rural'] == 0
    assert response['locationArea']['urbano'] == 0
    assert response['gender']['feminino'] == 0
    assert response['gender']['masculino'] == 0

    assert response['ageGroups']['Masculino']['0 a 5 anos']['Rural'] == 0
    assert response['ageGroups']['Masculino']['13 a 17 anos']['Rural'] == 0

    assert response['ageGroups']['Masculino']['30 a 44 anos']['Urbano'] == 0
    assert response['ageGroups']['Masculino']['45 a 59 anos']['Urbano'] == 0
    assert response['ageGroups']['Masculino']['60 + anos']['Urbano'] == 0

    assert response['ageGroups']['Feminino']['0 a 5 anos']['Rural'] == 0
    assert response['ageGroups']['Feminino']['6 a 12 anos']['Rural'] == 0

    assert response['ageGroups']['Feminino']['30 a 44 anos']['Urbano'] == 0
    assert response['ageGroups']['Feminino']['45 a 59 anos']['Urbano'] == 0
    assert response['ageGroups']['Feminino']['60 + anos']['Urbano'] == 0


def test_retrieve_demographics_info_when_invalid_argument():
    demographics_info = DemographicsInfoRepository()
    with pytest.raises(InvalidArgument) as exc:
        demographics_info.retrieve_demographics_info([])
        assert exc.message == 'df must be a DataFrame instance'


@pytest.mark.usefixtures('atendimento_individual_df')
def test_parse_indicators(atendimento_individual_df):
    hypertension = Hypertension()
    hypertension_df = hypertension.filter_registers(atendimento_individual_df)

    diabetes = Diabetes()
    diabetes_df = diabetes.filter_registers(atendimento_individual_df)

    gestantes = Pregnants()
    gestantes_df = gestantes.filter_registers(atendimento_individual_df)

    demographics = DemographicsInfoRepository()
    demographics.parse_indicators(
        diabetes=diabetes_df,
        hipertensao=hypertension_df,
        gestantes=gestantes_df
    )
    response = demographics.indicators
    assert response['diabetes']['rural'] == 1
    assert response['diabetes']['urbano'] == 1

    assert response['gestantes']['rural'] == 1
    assert response['gestantes']['urbano'] == 1

    assert response['hipertensao']['rural'] == 1
    assert response['hipertensao']['urbano'] == 1


@pytest.mark.usefixtures('atendimento_individual_df_no_rurals')
def test_parse_indicators_no_rurals(atendimento_individual_df_no_rurals):
    hypertension = Hypertension()
    hypertension_df = hypertension.filter_registers(
        atendimento_individual_df_no_rurals)

    diabetes = Diabetes()
    diabetes_df = diabetes.filter_registers(
        atendimento_individual_df_no_rurals)

    gestantes = Pregnants()
    gestantes_df = gestantes.filter_registers(
        atendimento_individual_df_no_rurals)

    demographics = DemographicsInfoRepository()
    demographics.parse_indicators(
        diabetes=diabetes_df,
        hipertensao=hypertension_df,
        gestantes=gestantes_df
    )
    response = demographics.indicators
    assert response['diabetes']['rural'] == 0
    assert response['diabetes']['urbano'] == 2

    assert response['gestantes']['rural'] == 0
    assert response['gestantes']['urbano'] == 2

    assert response['hipertensao']['rural'] == 0
    assert response['hipertensao']['urbano'] == 2


@pytest.mark.usefixtures('atendimento_individual_df_only_rurals')
def test_parse_indicators_only_rurals(atendimento_individual_df_only_rurals):
    hypertension = Hypertension()
    hypertension_df = hypertension.filter_registers(
        atendimento_individual_df_only_rurals)

    diabetes = Diabetes()
    diabetes_df = diabetes.filter_registers(
        atendimento_individual_df_only_rurals)

    gestantes = Pregnants()
    gestantes_df = gestantes.filter_registers(
        atendimento_individual_df_only_rurals)

    demographics = DemographicsInfoRepository()
    demographics.parse_indicators(
        diabetes=diabetes_df,
        hipertensao=hypertension_df,
        gestantes=gestantes_df
    )
    response = demographics.indicators
    assert response['diabetes']['rural'] == 2
    assert response['diabetes']['urbano'] == 0

    assert response['gestantes']['rural'] == 2
    assert response['gestantes']['urbano'] == 0

    assert response['hipertensao']['rural'] == 2
    assert response['hipertensao']['urbano'] == 0


@pytest.mark.usefixtures('atendimento_individual_df_only_rurals')
def test_parse_indicators_empty(atendimento_individual_df_empty):
    hypertension = Hypertension()
    hypertension_df = hypertension.filter_registers(
        atendimento_individual_df_empty)

    diabetes = Diabetes()
    diabetes_df = diabetes.filter_registers(atendimento_individual_df_empty)

    gestantes = Pregnants()
    gestantes_df = gestantes.filter_registers(atendimento_individual_df_empty)

    demographics = DemographicsInfoRepository()
    demographics.parse_indicators(
        diabetes=diabetes_df,
        hipertensao=hypertension_df,
        gestantes=gestantes_df
    )
    response = demographics.indicators
    assert response['diabetes']['rural'] == 0
    assert response['diabetes']['urbano'] == 0

    assert response['gestantes']['rural'] == 0
    assert response['gestantes']['urbano'] == 0

    assert response['hipertensao']['rural'] == 0
    assert response['hipertensao']['urbano'] == 0


@pytest.mark.usefixtures('atendimento_individual_df_only_rurals')
def test_parse_indicators_with_invalid_arguments(atendimento_individual_df_only_rurals):
    demographics = DemographicsInfoRepository()
    with pytest.raises(InvalidArgument) as exc:
        demographics.parse_indicators(
            diabetes=[],
            hipertensao=[],
            gestantes=[]
        )
        assert exc.message == 'diabetes must be a DataFrame instance'

    diabetes = Diabetes()
    diabetes_df = diabetes.filter_registers(
        atendimento_individual_df_only_rurals)
    with pytest.raises(InvalidArgument) as exc:
        demographics.parse_indicators(
            diabetes=diabetes_df,
            hipertensao=[],
            gestantes=[]
        )
        assert exc.message == 'hipertensao must be a DataFrame instance'

        hypertension = Hypertension()
        hypertension_df = hypertension.filter_registers(
            atendimento_individual_df_only_rurals)
        with pytest.raises(InvalidArgument) as exc:
            demographics.parse_indicators(
                diabetes=diabetes_df,
                hipertensao=hypertension_df,
                gestantes=[]
            )
            assert exc.message == 'gestantes must be a DataFrame instance'


@pytest.mark.skip(reason="Avoid hit on BD")
def test_get_demographics_info():
    demographics = DemographicsInfoRepository()
    response = demographics.get_demographics_info()
    assert isinstance(response, Dict)

    response = demographics.get_demographics_info(1)
    assert isinstance(response, Dict)


@pytest.mark.skip(reason="Avoid hit on BD")
def test_get_demographics_info_invalid_argument():
    demographics = DemographicsInfoRepository()
    with pytest.raises(InvalidArgument) as exc:
        demographics.get_demographics_info('1')
        assert exc.message == 'CNES must be int'
