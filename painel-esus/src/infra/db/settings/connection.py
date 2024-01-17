import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.env.conf import env

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'postgresql',
            env.get('DB_USER', '-'),
            env.get('DB_PASSWORD', '-'),
            env.get('DB_HOST', '-'),
            env.get('DB_PORT', '-'),
            env.get('DB_DATABASE', '-')
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
