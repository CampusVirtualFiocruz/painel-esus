from unittest.mock import Mock

import pytest
from src.domain.entities.user_payload import UserPayload
from src.errors import HttpBadRequestError, InvalidArgument

from .login import LoginUseCase


@pytest.fixture
def user_payload_mock():
    user = UserPayload(
        'nome',
        'cns',
        'uf',
        'Belo Horizonte',
        profiles=[]
    )
    return user

@pytest.fixture
@pytest.mark.usefixtures('user_payload_mock')
def login_repository_mock(user_payload_mock):
    mock = Mock()
    mock.check_credentials.return_value = user_payload_mock
    return mock

@pytest.mark.usefixtures('login_repository_mock')
def test_login_use_case(login_repository_mock):
    use_case = LoginUseCase(login_repository_mock)
    user_payload = use_case.login('nome', 'cnss')
    assert isinstance(user_payload, UserPayload)
    user_mock = login_repository_mock.check_credentials()
    assert user_payload.username == user_mock.username

    with pytest.raises(HttpBadRequestError) as exc:
        user_payload = use_case.login('nom', 'cnss')
        assert exc.message == 'Username too short'

    with pytest.raises(InvalidArgument) as exc:
        user_payload = use_case.login( 12333, 'cnss')
        assert exc.message == 'Username is required and must be string.'

    with pytest.raises(HttpBadRequestError) as exc:
        user_payload = use_case.login( '#$$', 'cnss')
        assert exc.message == 'Invalid username'

    with pytest.raises(HttpBadRequestError) as exc:
        user_payload = use_case.login( 'asasddd', '$$')
        assert exc.message == 'Password too short'

    with pytest.raises(InvalidArgument) as exc:
        user_payload = use_case.login( 'asasdf', 12223)
        assert exc.message == 'Password is required and must be string.'

    with pytest.raises(InvalidArgument) as exc:
        user_payload = use_case.login( None, '12344')
        assert exc.message == 'Username is required and must be string.'
