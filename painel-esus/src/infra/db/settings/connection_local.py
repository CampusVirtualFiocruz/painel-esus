import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self) -> None:
        path = os.getcwd()
        path = path.split('/painel-esus')[0]
        path = path + '/painel-esus'
        self.__connection_string = f"sqlite:///{path}/painel_esus.db"
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
