# pylint: disable=unused-import
from unittest.mock import patch

import pytest

from src.domain.entities.user_payload import UserPayload
from src.infra.bridge_provider.login_bridge import LoginBridgeRepository

from .tests.mocks.login_fail import login_fail_response

login_data = {
    "username": "10288507860",
    "password": "10288507860esus"
}


@pytest.mark.skip(reason='Avoid request to bridge')
def test_login():

    login_repository = LoginBridgeRepository()
    user = login_repository.check_credentials(
        login_data['username'], login_data['password'])
    assert isinstance(user, UserPayload)


@pytest.mark.skip(reason='Avoid request to bridge')
def test_login_fail():
    login_repository = LoginBridgeRepository()
    user = login_repository.check_credentials(
        login_data['username'], '12'+login_data['password'])
    assert user is None


@pytest.mark.usefixtures('login_fail_response')
def test_login_fail_mock(login_fail_response):
    with patch('src.infra.bridge_provider.login_bridge.requests.Session.request') as req:
        req.return_value.text = login_fail_response
        req.return_value.json.return_value = login_fail_response
        login_repository = LoginBridgeRepository()
        user = login_repository.check_credentials(
            login_data['username'],
            '12'+login_data['password']
        )
        assert user is None
