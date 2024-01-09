import os
from app import app
from app.models.BaseConfig import BaseConfig
import logging
import urllib.parse
from dotenv import load_dotenv
load_dotenv()

def server_run(pagesPath, dataPath, dir_pages, config, addMsg=None):
    print('RODANDO SERVIDOR')
    bse = BaseConfig.getInstance()
    bse._host = config['host']
    bse._database = config['dataBase']
    bse._user = config['user']
    bse._passwd = config['pwd']
    bse._port = config['port']

    app.run(host='0.0.0.0', port=5001)


if __name__ == '__main__':
    print('INICIANDO')
    print(urllib.parse.quote(os.getenv('PASSWORD', '')))
    config = {
        "host": os.environ['HOST'],
        "dataBase": os.environ['DATABASE'],
        "user": os.environ['USER'],
        "pwd": urllib.parse.quote(os.getenv('PASSWORD', '')),
        "port": os.environ['PORT']
    }
    server_run(
        None, None, None, config, None
    )
