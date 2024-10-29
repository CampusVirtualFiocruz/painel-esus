# pylint: disable=unused-import
from pprint import pprint
from unittest.mock import patch

import mock
import pytest
from src.domain.entities.user_payload import UserPayload
from src.infra.bridge_provider.login_bridge import LoginBridgeRepository

from .tests.mocks.login_fail import login_fail_response
from .tests.mocks.response import login
from .tests.mocks.response import login_profile_list
from .tests.mocks.response import login_response
from .tests.mocks.response import login_response_user
from .tests.mocks.response import login_response_user_0

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


@pytest.mark.usefixtures('login_response')
def test_login_response_mock(login_response):
    with patch('src.infra.bridge_provider.login_bridge.requests.Session.request') as req:
        req.return_value.text = login_response
        req.return_value.json.return_value = login_response
        login_repository = LoginBridgeRepository()
        user = login_repository.check_role(login_response)
        assert user[0] == 'admin'


@pytest.mark.usefixtures('login_response_user')
def test_login_response_mock_user(login_response_user):
    with patch('src.infra.bridge_provider.login_bridge.requests.Session.request') as req:
        req.return_value.text = login_response_user
        req.return_value.json.return_value = login_response_user
        login_repository = LoginBridgeRepository()
        user = login_repository.check_role(login_response_user)
        assert user[0] == 'user'
        assert user[1] == '5'


@pytest.mark.usefixtures('login')
@pytest.mark.usefixtures('login_response_user')
def test_login_response_mock_user_body(login, login_response_user, mocker):
    class MockGet:
        text = login

        def json(self):
            return login

    class MockPost:
        text = login_response_user

        def json(self):
            return login_response_user

    mocker.patch(
        'src.infra.bridge_provider.login_bridge.LoginBridgeRepository.who', return_value='bot')
    mocker.patch(
        'src.infra.bridge_provider.login_bridge.LoginBridgeRepository.get_reponse_body', return_value=MockGet())
    mocker.patch(
        'src.infra.bridge_provider.login_bridge.LoginBridgeRepository.post_bridge', return_value=MockPost())

    login_repository = LoginBridgeRepository()

    user = login_repository.check_credentials(
        login_data['username'],
        '12'+login_data['password']
    )
    assert user.ubs == '5'
    assert user.profiles == ['user']
