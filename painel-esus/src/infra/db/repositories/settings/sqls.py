import os

from sqlalchemy import text

working_directory  = os.getcwd()
input_path = os.path.join(working_directory, "dados", "settings")
FILE_PATH = input_path + os.sep + "acceptance_term.parquet"

def find_all():
    return f'select * from read_parquet("{FILE_PATH}");'


def find_by_username_ibge():
    return f'select * from read_parquet("{FILE_PATH}") where username = $username and cod_ibge = $ibge ;'


def find_by_username_ibge_version():
    return f'select * from read_parquet("{FILE_PATH}") where username = $username and cod_ibge = $ibge and version= $version;'
