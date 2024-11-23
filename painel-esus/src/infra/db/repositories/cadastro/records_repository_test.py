from .records_repository import RecordsRepository


def test_nominal_list():
    repo = RecordsRepository()
    result = repo.find_filter_nominal()
    total = result["itemsCount"]

    result = repo.find_filter_nominal(cnes=25, equipe=18)
    equipe = result["itemsCount"]

    print(result["items"][0])
    assert total > equipe
