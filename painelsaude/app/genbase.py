import os
from .models.conexao import Conexao
import logging
from .models import IreceBase
from tqdm import tqdm
from .models.generateBases import  generateAll
from .controllers.criarBaseFinal import criarBaseFinal
from .controllers.criarCadastroMeste import criarCadastroMeste
from .controllers.indicadoresGestantes import criarIndicadoresGestantes
from .controllers.criarBaseFinalGestante import criarBaseFinalGestante
from .controllers.criarBasesHipertensao import criarBasesHipertensao
from .controllers.criarBasesDiabetes import criarBasesDiabetes
import gc
    
def generateBases():
    host = os.getenv('HOST', 'paineisirece.ckebriuhritw.sa-east-1.rds.amazonaws.com')
    dataBase = os.getenv('DATABASE')
    user = os.getenv('USER')
    passwd = os.getenv('PASSWORD')
    port = os.getenv('PORT')

    con = Conexao( host, dataBase,  user, passwd, port)
    # print(con)
    executions = {
        'generateAll':generateAll,
        'criarCadastroMeste':criarCadastroMeste,
        'criarBaseFinal':criarBaseFinal,
        'criarIndicadoresGestantes':criarIndicadoresGestantes,
        'criarBaseFinalGestante':criarBaseFinalGestante,
        'criarBasesHipertensao':criarBasesHipertensao,
        'criarBasesDiabetes':criarBasesDiabetes
    }

    for i in tqdm( executions, desc="processando bases"):
        if i == 'generateAll':
            executions[i](con)
        else:
            executions[i]('files')
        gc.collect()



