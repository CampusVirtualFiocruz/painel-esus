# pylint: disable=unused-import
from unittest.mock import patch

from src.data.use_cases.diabetes_hypertension.hypertension_dashboard import \
    HypertensionUseCase
from src.data.use_cases.diabetes_hypertension.tests.mocks.hypertension_repository import \
    hypertension_dashboard_repository_mock
from src.presentations.http_types import HttpRequest

from .hypertension_dashboard_get_total import HypertensionDashboardGetTotal


def test_hypertension_controller():
    with patch(
        'src.data.interfaces.hypertension_dashboard.HypertensionDashboardRepositoryInterface'
    ) as repository:
        repository.get_total.return_value = {'total': 123}
        use_case = HypertensionUseCase(repository)
        http_request = HttpRequest()
        controller = HypertensionDashboardGetTotal(use_case)
        response = controller.handle(http_request)
        assert response.body['data'] == 123
