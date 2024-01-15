import os

from src.data.interfaces.login_repository import (
    LoginRepository as LoginRepositoryInterface
)
from src.domain.entities.user_payload import UserPayload


class LoginAdmRepository(LoginRepositoryInterface):
    def check_credentials(self, username: str, password: str) -> UserPayload:
        admin_username = os.getenv('ADMIN_USERNAME', 'admin')
        admin_password = os.getenv('ADMIN_PASSWORD', 'FCadmin')
        if username == admin_username and password == admin_password:
            user_raw_data = UserPayload(
                username='Admin',
                cns='0000000000',
                uf='',
                municipio='',
                profiles=['user']
            )
            return user_raw_data
        return None
