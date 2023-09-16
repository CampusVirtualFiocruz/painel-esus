from src.infra.bridge_provider.login_bridge import LoginBridgeRepository
from src.domain.entities.user_payload import UserPayload
import pytest
login_data =   {
    "username":"10288507860",
    "password":"10288507860esus"
}
@pytest.mark.skip(reason='Avoid request to bridge')
def test_login():

    login_repository = LoginBridgeRepository()
    user = login_repository.check_credentials(login_data['username'], login_data['password'])
    assert isinstance(user, UserPayload)

@pytest.mark.skip(reason='Avoid request to bridge')
def test_login_fail():
    login_repository = LoginBridgeRepository()
    user = login_repository.check_credentials(login_data['username'], '12'+login_data['password'])
    assert user is None
