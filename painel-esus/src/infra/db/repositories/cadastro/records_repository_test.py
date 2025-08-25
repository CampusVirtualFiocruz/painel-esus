from .records_repository import RecordsRepository

repo = RecordsRepository()

def test_nominal_list():
    result = repo.find_filter_nominal()
    total = result["itemsCount"]

    result = repo.find_filter_nominal(cnes=25, equipe=18)
    equipe = result["itemsCount"]

    print(result["items"][0])
    assert total > equipe

def test_get_total():
    total = repo.get_total_group()
    print(total)

def test_get_cpf_cns_rate():
    cns = repo.get_cpf_cns_rate(26,19)
    print(cns)

def test_group_localidade():
    localidade = repo.group_localidade(26,19)
    print(localidade)


def test_group_raca_cor():
    raca_cor = repo.group_raca_cor(26, 19)
    print(raca_cor)


def test_group_records_by_origin():
    group_records_by_origin = repo.group_records_by_origin(26, 19)
    print(group_records_by_origin)


def test_group_records_status():
    group_records_status = repo.group_records_status(26, 19)
    print(group_records_status)


def test_people_who_get_care():
    group_records_status = repo.people_who_get_care(26, 19)
    print(group_records_status)


def test_nominal_list():
    # group_records_status = repo.find_filter_nominal(cnes=26, equipe=19)
    # print(group_records_status)
    group_records_status = repo.find_filter_nominal(cnes=26, equipe=19,query="JOSEFA")
    print(group_records_status)


def test_nominal_list_downlaod():
    # group_records_status = repo.find_filter_nominal(cnes=26, equipe=19)
    # print(group_records_status)
    group_records_status = repo.find_all_download(cnes=26, equipe=19)
    print(group_records_status)
