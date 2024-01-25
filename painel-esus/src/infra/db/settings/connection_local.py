import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self) -> None:
        path = os.getcwd()
        path = path.split(f'{os.sep}painel-esus')[0]
        path = path + f'{os.sep}painel-esus'
        self.__connection_string = f"sqlite:///{path}{os.sep}painel_esus.db"
        print("CONNECTION STRING", self.__connection_string)
        self.__engine = self.__create_database_engine()
        self.session = None
        print("CONNECTION STRING", self.__connection_string)

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
