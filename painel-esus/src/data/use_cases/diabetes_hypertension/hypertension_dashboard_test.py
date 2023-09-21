#pylint: disable=unused-import
from unittest import mock

import pytest
from src.data.use_cases.diabetes_hypertension.tests.mocks.hypertension_repository import \
    hypertension_dashboard_repository_mock
from src.domain.dict_types import DiseaseDashboardTotal
from src.errors import InvalidArgument

from .hypertension_dashboard import HypertensionUseCase


def test_hypertension_dashboard_result():
    with mock.patch(
        'src.data.interfaces.hypertension_dashboard.HypertensionDashboardRepositoryInterface'
        ) as repository:
        repository.get_total.return_value = { 'total': 123}
        use_case = HypertensionUseCase(repository)
        response = use_case.get_total()
        assert response['total'] == 123

@mock.patch('src.data.interfaces.hypertension_dashboard.HypertensionDashboardRepositoryInterface')
def test_hypertension_dashboard_result_patch(repository):
    repository.get_total.return_value = { 'total': 123}
    use_case = HypertensionUseCase(repository)
    response = use_case.get_total()
    assert response['total'] == 123

    response = use_case.get_total(2)
    assert response['total'] == 123

def test_hypertension_dashboard_result2():
    repository = mock.MagicMock()
    repository.get_total.return_value = { 'total': 123}
    use_case = HypertensionUseCase(repository)
    response = use_case.get_total()
    assert response['total'] == 123

    response = use_case.get_total(2)
    assert response['total'] == 123


@pytest.mark.usefixtures('hypertension_dashboard_repository_mock')
def test_hypertension_dashboard_result3(hypertension_dashboard_repository_mock):
    use_case = HypertensionUseCase(hypertension_dashboard_repository_mock)
    response = use_case.get_total()
    assert response['total'] == 123

    response = use_case.get_total(2)
    assert response['total'] == 123

@pytest.mark.usefixtures('hypertension_dashboard_repository_mock')
def test_hypertension_dashboard_input_check(hypertension_dashboard_repository_mock):
    use_case = HypertensionUseCase(hypertension_dashboard_repository_mock)
    with pytest.raises(InvalidArgument):
        use_case.get_total('123')
