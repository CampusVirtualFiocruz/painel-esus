from src.domain.entities.user_payload import UserPayload

from .login_repository import LoginRepository


def test_login():
    username = '95009337568'
    password = '700009534775406painel'

    login_repository = LoginRepository()
    user = login_repository.check_credentials(username, password)
    assert isinstance(user, UserPayload)

def test_login_fail():
    username = '95009337568'
    password = '700009534775406'

    login_repository = LoginRepository()
    user = login_repository.check_credentials(username, password)
    assert user is None
