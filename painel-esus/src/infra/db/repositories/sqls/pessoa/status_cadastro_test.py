from .pessoas import pessoas
from .status_cadastro import status_cadastro


def test_status_cadastro():
    sql = status_cadastro()

    print(sql)


def test_status_pessoa():

    print(pessoas)
