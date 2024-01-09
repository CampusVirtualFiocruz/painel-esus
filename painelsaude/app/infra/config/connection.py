import os
from ...models.conexao import Conexao
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('HOST', 'paineisirece.ckebriuhritw.sa-east-1.rds.amazonaws.com')
dataBase = os.getenv('DATABASE')
user = os.getenv('USER')
passwd = os.getenv('PASSWORD')
port = os.getenv('PORT')

con = Conexao( host, dataBase,  user, passwd, port)