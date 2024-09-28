from pprint import pprint

from src.infra.db.repositories.disease.nominal_list.hypertension_nominal_list_repository import HypertensionNominalListRepository
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
    users = repo.find_filter('LEONEL', '00886961890')
    assert len(users) > 0

    users = repo.find_filter('LEONEL', '00886961891')
    assert len(users) == 0
