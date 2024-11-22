# pylint: disable=W0611
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.env import env
from src.errors.logging import logging


class DBConnectionHandler:

    def __init__(self) -> None:
        if env["ENV"] == "instalador":
            path = self.get_db_path()
        else:
            path = os.getcwd()
            path = Path(path.split("/painel-esus")[0])
            path = os.path.join(path, "painel_esus.db")
            path = os.path.relpath(path)
        self.__connection_string = f"sqlite:///{path}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def get_db_path(self):
        path = os.getcwd()
        path = os.path.join(path, "painel_esus.db")
        return path

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
