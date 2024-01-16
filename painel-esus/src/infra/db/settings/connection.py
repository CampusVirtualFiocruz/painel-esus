import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'postgresql',
            os.getenv('DB_USER', 'susopolis_user'),
            os.getenv('DB_PASSWORD', 'R6Hi1J4HMkInYmvQ6iMdId8J2Lz7PP'),
            os.getenv('DB_HOST', 'paineisirece.ckebriuhritw).sa-east-1.rds.amazonaws.com'),
            os.getenv('DB_PORT', '5432'),
            os.getenv('DB_DATABASE', 'postgres')
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
