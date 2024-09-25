# pylint: disable=C0201
import os

from src.data.interfaces.login_repository import \
    LoginRepository as LoginRepositoryInterface
from src.domain.entities.user_payload import UserPayload

admin_map = {
    "admin1": {
        "username": "Admin",
        "cns": "0000000000",
        "uf": "",
        "municipio": "",
        "profiles": ["admin"],
    },
    "admin2": {
        "username": "Admin",
        "cns": "0000000000",
        "uf": "",
        "municipio": "",
        "profiles": ["admin"],
        "ubs": 25,
    },
    "user1": {
        "username": "Admin",
        "cns": "0000000000",
        "uf": "",
        "municipio": "",
        "profiles": ["user"],
        "ubs": 25,
    },
}


class LoginAdmRepository(LoginRepositoryInterface):
    def check_credentials(self, username: str, password: str) -> UserPayload:
        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_password = os.getenv("ADMIN_PASSWORD", "FCadmin")
        if username in admin_map.keys():
            user_raw_data = UserPayload(**admin_map[username])
            return user_raw_data

        if username == admin_username and password == admin_password:
            user_raw_data = UserPayload(
                username="Admin",
                cns="0000000000",
                uf="",
                municipio="",
                profiles=["user"],
            )
            return user_raw_data
        return None
