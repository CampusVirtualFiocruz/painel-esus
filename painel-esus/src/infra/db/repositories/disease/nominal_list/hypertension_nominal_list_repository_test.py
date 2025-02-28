# pylint: disable=R0913,C0103
from pprint import pprint

from src.infra.db.repositories.disease.nominal_list.diabetes_nominal_list_repository import (
    DiabetesNominalListRepository,
)
from src.infra.db.repositories.disease.nominal_list.hypertension_nominal_list_repository import (
    HypertensionNominalListRepository,
)
from src.main.adapters.nominal_list_adapter import HypertensionNominalListAdapter


def test_list_all():
    repo = HypertensionNominalListRepository()
    users = repo.find_all()
    pprint(users)
    assert len(users) > 0


def test_find_nome():
    repo = HypertensionNominalListRepository()
    users = repo.find_by_nome('LEONEL')
    pprint(users)
    assert len(users) > 0


def test_adapter():
    repo = HypertensionNominalListRepository()
    users = repo.find_by_nome('LEONEL')
    adapter = HypertensionNominalListAdapter(users[0])
    pprint(adapter.to_dict())


def test_filter():
    repo = HypertensionNominalListRepository()
    users = repo.find_filter(25, 0, 10)
    assert len(users['items']) > 0

    users = repo.find_filter(25, 0, 10)
    assert len(users['items']) == 10

def test_join():
    # repo = HypertensionNominalListRepository()
    repo = DiabetesNominalListRepository()
    # user = repo.find_by_nome("IRENILDA")
    users = repo.find_filter(cnes=26)
    print(users)

def test_equipe():
    repo = HypertensionNominalListRepository()
    # repo = DiabetesNominalListRepository()
    # user = repo.find_by_nome("IRENILDA")
    users = repo.find_filter(cnes=26, pagesize=10, page=2)
    for i in users['items']:
        
        print(i.co_fat_cidadao_pec, i.nome )

def test_list_nominal():
    repo = HypertensionNominalListRepository()
    lista = repo.find_filter(25, page=4, pagesize=10)
    [pprint(HypertensionNominalListAdapter(val).to_dict()) for val in lista["items"] ]
    # print(adapter.to_dict())
