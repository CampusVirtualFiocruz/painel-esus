import os
from ...models.conexao import Conexao

host = os.getenv('HOST', 'paineisirece.ckebriuhritw.sa-east-1.rds.amazonaws.com')
dataBase = os.getenv('DATABASE')
user = os.getenv('USER')
passwd = os.getenv('PASSWORD')
port = os.getenv('PORT')

con = Conexao( host, dataBase,  user, passwd, port)