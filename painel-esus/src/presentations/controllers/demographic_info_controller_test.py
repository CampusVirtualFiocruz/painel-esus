# pylint: disable=unused-import
import pytest

from src.errors import InvalidArgument
from src.presentations.controllers.tests.mocks.demographics_info_use_case_stub import (
    demographics_info_use_case_mock,
    demographics_info_use_case_repository_mock)
from src.presentations.http_types import HttpRequest, HttpResponse

from .demographics_info_controller import DemographicsInfoController


@pytest.mark.usefixtures('demographics_info_use_case_mock')
def test_demographics_info_controller(demographics_info_use_case_mock):
    request = HttpRequest(
        headers=None,
        body=None,
        query_params=None,
        path_params={'cnes': 1}
    )
    controller = DemographicsInfoController(demographics_info_use_case_mock)
    response = controller.handle(request)
    assert isinstance(response, HttpResponse)
    demographics_info_use_case_mock.get_demographics_info.assert_called_once_with(
        1)


@pytest.mark.usefixtures('demographics_info_use_case_mock')
def test_demographics_info_controller_with_none_argument(demographics_info_use_case_mock):
    request = HttpRequest(
        headers=None,
        body=None,
        query_params=None,
        path_params={'cnes': None}
    )
    controller = DemographicsInfoController(demographics_info_use_case_mock)
    response = controller.handle(request)
    assert isinstance(response, HttpResponse)
    demographics_info_use_case_mock.get_demographics_info.assert_called_once_with(
        None)


@pytest.mark.usefixtures('demographics_info_use_case_repository_mock')
def test_demographics_info_controller_invalid_argument(demographics_info_use_case_repository_mock):
    request = HttpRequest(
        headers=None,
        body=None,
        query_params=None,
        path_params={'cnes': '1'}
    )
    controller = DemographicsInfoController(
        demographics_info_use_case_repository_mock)
    with pytest.raises(InvalidArgument):
        response = controller.handle(request)
        assert isinstance(response, HttpResponse)
        mock = demographics_info_use_case_repository_mock.get_demographics_info
        mock.assert_called_once_with('1')
