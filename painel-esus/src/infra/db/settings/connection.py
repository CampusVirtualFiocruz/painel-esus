from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.env.conf import env


class DBConnectionHandler:

    def __init__(self, dbUser = None, dbPassword = None, dbHost = None, dbPort = None, dbDatabase = None) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'postgresql',
            env.get('DB_USER', '-') if dbUser is None else dbUser.strip(),
            env.get('DB_PASSWORD', '-') if dbPassword is None else dbPassword.strip(),
            env.get('DB_HOST', '-') if dbHost is None else dbHost.strip(),
            env.get('DB_PORT', '-') if dbPort is None else dbPort.strip(),
            env.get('DB_DATABASE', '-') if dbDatabase is None else dbDatabase.strip()
        )
        self.__engine = self.__create_database_engine()
        print('+++++++++++++++++++++++++++++++',self.__engine)
        self.session = None
    

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        print("TESTE DE CONEXÃO")
        print( self.__connection_string)
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def get_connection_str(self):
        return self.__connection_string
