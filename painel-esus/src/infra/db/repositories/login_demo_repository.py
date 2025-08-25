import os

from sqlalchemy.sql import text
from src.data.interfaces.login_repository import (
    LoginRepository as LoginRepositoryInterface,
)
from src.domain.entities.user_payload import UserPayload
from src.infra.db.settings.connection import DBConnectionHandler
from src.utils.users_list import users






class LoginDemoRepository(LoginRepositoryInterface):

    def check_credentials(self, username: str, password: str) -> UserPayload:
        for user in users:
            if user["login"] == username and user["password"] == password:
                user_raw_data = UserPayload(
                    username=user["data"]["username"],
                    cns=user["data"]["cns"],
                    uf=user["data"]["uf"],
                    municipio=user["data"]["municipio"],
                    profiles=user["data"]["profiles"],
                )
                return user_raw_data
        return None
