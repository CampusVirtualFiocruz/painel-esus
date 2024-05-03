# pylint: disable=unused-import
from unittest.mock import patch

from src.data.use_cases.diseases_dashboard.disease_dashboard import DiseaseUseCase
from src.data.use_cases.diseases_dashboard.tests.mocks.diabetes_repository import (
    diabetes_dashboard_repository_mock
)
from src.presentations.http_types import HttpRequest

from .diabetes_dashboard_get_total import DiabetesDashboardGetTotal


def test_diabetes_controller():
    with patch(
        'src.data.interfaces.diseases_dashboard.DiseasesDashboardRepositoryInterface'
    ) as repository:
        repository.get_total.return_value = {'total': 123}
        use_case = DiseaseUseCase(repository)
        http_request = HttpRequest()
        controller = DiabetesDashboardGetTotal(use_case)
        response = controller.handle(http_request)
        assert response.body['data'] == 123
