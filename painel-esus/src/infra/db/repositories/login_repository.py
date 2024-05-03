import os

from sqlalchemy.sql import text
from src.data.interfaces.login_repository import (
    LoginRepository as LoginRepositoryInterface
)
from src.domain.entities.user_payload import UserPayload
from src.infra.db.settings.connection import DBConnectionHandler

from .sqls.login import LOGIN


class LoginRepository(LoginRepositoryInterface):

    def check_credentials(self, username: str, password: str) -> UserPayload:
        database = DBConnectionHandler()
        with database.get_engine().connect() as con:
            statement = text(LOGIN)
            result = con.execute(statement, {
                "username": username,
                "password_salt": os.getenv('PASSWORD_SALT', 'painel'),
                "password": password
            })
            try:
                db_response = next(result)
                user_raw_data = UserPayload(
                    username=db_response[8],
                    cns=db_response[4],
                    uf=db_response[3],
                    municipio=db_response[2],
                    profiles=['user']
                )
                return user_raw_data
            except StopIteration:
                return None
