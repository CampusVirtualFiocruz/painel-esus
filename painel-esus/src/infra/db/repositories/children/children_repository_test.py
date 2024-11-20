from pprint import pprint

from src.main.adapters.children_adapter import ChildrenAdapter

from .children_repository import ChildrenRepository
from .sqls import children_by_age_and_gender


def test_children_age_query():
    sql = children_by_age_and_gender(1 , 2)
    assert " equipes.codigo_unidade_saude  = 1  and equipes.codigo_equipe  = 2" in str(sql)

def test_children_age_by_gender():
    repo = ChildrenRepository()
    data = repo.find_grouping_by_ages_gender(25)
    adapter = ChildrenAdapter()
    result = adapter.age_by_gender(data)["data"]
    pprint(result[0],indent= 4, depth=3)
    assert  "tag" in result[0]
    assert "masculino" in result[0]["value"]
    assert "feminino" in result[0]["value"]

    data = repo.find_grouping_by_ages_gender()
    result = adapter.age_by_gender(data)["data"]
    assert "tag" in result[0]
    assert "masculino" in result[0]["value"]
    assert "feminino" in result[0]["value"]


def test_children_age_by_location():
    repo = ChildrenRepository()
    data = repo.find_grouping_by_ages_location(25)
    adapter = ChildrenAdapter()
    result = adapter.age_by_location(data)["data"]

    assert "tag" in result[0]
    assert "urbana" in result[0]["value"]
    assert "rural" in result[0]["value"]
    
    data = repo.find_grouping_by_ages_location()
    result = adapter.age_by_location(data)["data"]

    assert "tag" in result[0]
    assert "urbana" in result[0]["value"]
    assert "rural" in result[0]["value"]


def test_children_total_cares():
    repo = ChildrenRepository()
    data = repo.find_total_children_cares(25)
    adapter = ChildrenAdapter()
    result = adapter.total_cares(data)
    assert "total-criancas-atendidas-2-anos" in result 
    assert "data" in result["total-criancas-atendidas-2-anos"]
    assert "total-criancas-cadastradas-2-anos" in result
    assert "data" in result["total-criancas-cadastradas-2-anos"]
    
    data = repo.find_total_children_cares(25,17)
    result = adapter.total_cares(data)
    pprint(result)
    assert "total-criancas-atendidas-2-anos" in result
    assert "data" in result["total-criancas-atendidas-2-anos"]
    assert "total-criancas-cadastradas-2-anos" in result
    assert "data" in result["total-criancas-cadastradas-2-anos"]

def test_children_location_rate():
    repo = ChildrenRepository()
    data = repo.find_children_location_rate(25)
    adapter = ChildrenAdapter()
    result = adapter.children_location_rate(data)
    pprint(result)

    data = repo.find_children_location_rate()
    result = adapter.children_location_rate(data)
    pprint(result)
    
    data = repo.find_children_location_rate(25,17)
    result = adapter.children_location_rate(data)
    pprint(result)


def test_children_cares_by_professional():
    # repo = ChildrenRepository()
    data = []
    # data = repo.find_children_location_rate(25)

    adapter = ChildrenAdapter()
    result = adapter.children_cares_by_professionals(data)
    pprint(result)


def test_children_by_race():
    repo = ChildrenRepository()
    data = []
    data = repo.find_grouping_by_race(25)

    adapter = ChildrenAdapter()
    result = adapter.children_group_by_race(data)
    pprint(result)
