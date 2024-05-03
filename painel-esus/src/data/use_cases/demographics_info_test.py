#pylint: disable=unused-import
#pylint: disable=redefined-outer-name
from typing import Dict

import pytest

from .demographics_info import DemographicsInfo
from .tests.mocks.demographics_info_repository_mock import \
    demographics_info_mock


@pytest.mark.usefixtures('demographics_info_mock')
def test_get_demographics_info(demographics_info_mock):

    demographics = DemographicsInfo(demographics_info_mock)
    response = demographics.get_demographics_info()
    assert isinstance(response, Dict)
