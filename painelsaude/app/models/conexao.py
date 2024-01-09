import psycopg2
import pandas as pd
import numpy as np
import urllib.parse
from sqlalchemy.engine import URL
from sqlalchemy import create_engine


class Conexao(object):
    _db = None

    def __init__(self, mhost, db, usr, pwd, port):
        print('pwd teste: {}'.format(pwd))
        self.mhost = mhost
        self.db = db
        self.usr = usr
        self.pwd = pwd
        self.port = port
        self.connect()

    def connect(self):
        print('pwd: {}'.format(self.pwd))
        connection_url = f'postgresql+psycopg2://{self.usr}:{self.pwd}@{self.mhost}:{self.port}/{self.db}'
        # print(connection_url)
        engine = create_engine(connection_url)
        self._db = engine.connect()

    def testConection(self):
        return self.consultar("""SELECT table_name FROM information_schema.tables
                                 WHERE table_schema = 'public'""")

    def manipular(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except Exception as e:
            print(f'Error {e}')
            return False
        # finally:
        #     if self._db:
        #         self._db.close()
        return True

    def consultar(self, sql, Dataframe=False):
        rs = None
        cur = None
        try:
            self.connect()
            if Dataframe:
                rs = pd.read_sql(sql, self._db)
            else:
                cur = self._db.cursor()
                cur.execute(sql)
                rs = cur.fetchall()
                cur.close()
        except Exception as e:
            print(f'Error {e}')
        finally:
            if self._db:
                self._db.close()
            if cur is not None:
                cur.close()
        return rs

    def consultar_pd(self, sql, Dataframe=False):
        connection_url = f'postgresql+psycopg2://{self.usr}:{self.pwd}@{self.mhost}:{self.port}/{self.db}'
        # print(connection_url)
        engine = create_engine(connection_url)
        rs = None
        cur = None
        with engine.connect() as conn:
            # print(conn)
            # print(pd.read_sql( sql, con = conn ))
            return pd.read_sql(sql, con=conn)

    def close(self):
        self._db.close()


class Connection():
    _db = None
    _config = None

    def __init__(self, conf):
        self._config = conf

    def testConect(self):
        try:
            _db = Conexao(self._config['host'], self._config['dataBase'],
                          self._config['user'], self._config['pwd'], self._config['port'])
            if _db.testConection():
                _db.close()
                return True
            else:
                _db.close()
                return False
        except Exception as e:
            print(e)
            return False

    def conectar(self):
        try:
            _db = Conexao(self._config['host'], self._config['dataBase'],
                          self._config['user'], self._config['pwd'], self._config['port'])
            if _db.testConection():
                return _db
            else:
                return False
        except Exception as e:
            return False
