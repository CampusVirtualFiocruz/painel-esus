from unittest import mock

import pytest


@pytest.fixture()
def diabetes_dashboard_repository_mock():
    repository = mock.MagicMock()
    repository.get_total.return_value = {'total': 123}
    return repository
