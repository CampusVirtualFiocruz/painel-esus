from unittest import mock

import pytest
from src.data.use_cases.demographics_info import DemographicsInfo


@pytest.fixture
@mock.patch('src.data.use_cases.demographics_info.DemographicsInfo')
def demographics_info_use_case_mock(mock):
    mock.get_demographics_info.return_value = {}
    return mock


@pytest.fixture
@mock.patch('src.infra.db.repositories.demographics_info.DemographicsInfoRepository')
def demographics_info_use_case_repository_mock(mock):
    use_case = DemographicsInfo(mock)
    mock.get_demographics_info.return_value = {}
    return use_case
