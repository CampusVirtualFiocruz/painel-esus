# pylint: disable=R0913
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.env.conf import env


class DBConnectionHandler:

    def __init__(
        self,
        db_user=None,
        db_password=None,
        db_host=None,
        db_port=None,
        db_database=None,
    ) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "postgresql",
            env.get("DB_USER", "-") if db_user is None else db_user.strip(),
            (
                quote_plus(env.get("DB_PASSWORD", "-"))
                if db_password is None
                else quote_plus(db_password.strip())
            ),
            env.get("DB_HOST", "-") if db_host is None else db_host.strip(),
            env.get("DB_PORT", "-") if db_port is None else db_port.strip(),
            env.get("DB_DATABASE", "-") if db_database is None else db_database.strip(),
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def get_connection_str(self):
        return self.__connection_string
