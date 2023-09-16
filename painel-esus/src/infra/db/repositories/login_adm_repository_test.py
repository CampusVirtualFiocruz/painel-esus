from src.domain.entities.user_payload import UserPayload

from .login_adm_repository import LoginAdmRepository


def test_login():
    username = 'admin'
    password = 'FCadmin'
    login_repository = LoginAdmRepository()
    user = login_repository.check_credentials(username, password)
    assert isinstance(user, UserPayload)

def test_login_fail():
    username = 'admin'
    password = '700009534775406'
    login_repository = LoginAdmRepository()
    user = login_repository.check_credentials(username, password)
    assert user is None
