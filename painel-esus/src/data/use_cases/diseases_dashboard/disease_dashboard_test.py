# pylint: disable=unused-import
# pylint: disable=E0401
from unittest import mock
from unittest.mock import MagicMock, patch

import pytest

from src.data.use_cases.diseases_dashboard.tests.mocks.hypertension_repository import \
    hypertension_dashboard_repository_mock
from src.errors import InvalidArgument

from src.data.use_cases.diseases_dashboard.disease_dashboard import DiseaseUseCase


def test_hypertension_dashboard_result():
    with patch(
        'src.data.interfaces.diseases_dashboard.DiseasesDashboardRepositoryInterface'
    ) as repository:
        repository.get_total.return_value = {'total': 123}
        use_case = DiseaseUseCase(repository)
        response = use_case.get_total()
        assert response['total'] == 123


@mock.patch('src.data.interfaces.diseases_dashboard.DiseasesDashboardRepositoryInterface')
def test_hypertension_dashboard_result_patch(repository):
    repository.get_total.return_value = {'total': 123}
    use_case = DiseaseUseCase(repository)
    response = use_case.get_total()
    assert response['total'] == 123

    response = use_case.get_total(2)
    assert response['total'] == 123


def test_hypertension_dashboard_result2():
    repository = mock.MagicMock()
    repository.get_total.return_value = {'total': 123}
    use_case = DiseaseUseCase(repository)
    response = use_case.get_total()
    assert response['total'] == 123

    response = use_case.get_total(2)
    assert response['total'] == 123


@pytest.mark.usefixtures('hypertension_dashboard_repository_mock')
def test_hypertension_dashboard_result3(hypertension_dashboard_repository_mock: MagicMock):
    use_case = DiseaseUseCase(hypertension_dashboard_repository_mock)
    response = use_case.get_total()
    assert response['total'] == 123

    response = use_case.get_total(2)
    assert response['total'] == 123


@pytest.mark.usefixtures('hypertension_dashboard_repository_mock')
def test_hypertension_dashboard_input_check(hypertension_dashboard_repository_mock: MagicMock):
    use_case = DiseaseUseCase(hypertension_dashboard_repository_mock)
    with pytest.raises(InvalidArgument):
        use_case.get_total('123')
