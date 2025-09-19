import os

from .acceptance_term_repository import AcceptanceTermRepository
from .sqls import FILE_PATH


def test_open_file():
    # os.remove(FILE_PATH)
    repo = AcceptanceTermRepository()
    repo.save({'cod_ibge': '123', 'username': 'tales', 'version':'1.0'})
    repo.save({"cod_ibge": "123", "username": "tales", "version": "1.0"})
    repo.save({"cod_ibge": "123", "username": "tales", "version": "1.0"})
    repo.save({"cod_ibge": "1233", "username": "tales", "version": "1.0"})
    all = repo.find_all()
    assert len(all) == 2

def test_find_all():
    repo = AcceptanceTermRepository()
    all = repo.find_all()
    assert len(all) > 0


def test_find_username_ibge():
    repo = AcceptanceTermRepository()
    rec = repo.find_username_ibge_version('tales', '123','1.0')
    print(rec)
    assert len(rec) == 1
