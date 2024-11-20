from pprint import pprint
from sqlite3 import adapters

from src.main.adapters.elderly_adapter import ElderlyAdapter

from .elderly_repository import ElderlyRepository

repo = ElderlyRepository()
adapters = ElderlyAdapter()

def test_total():
    result = repo.find_total()
    result = adapters.total(result)
    assert "total-ubs" in result

    result = repo.find_total(25)
    result = adapters.total(result)
    assert "total-ubs" in result
    assert "total-atendidas" in result
    assert  "data" in result["total-atendidas"]

    result = repo.find_total(25, 18)
    result = adapters.total(result)
    assert "total-ubs" in result
    assert "total-atendidas" in result
    assert "data" in result["total-atendidas"]


def test_age_location():
    result = repo.find_group_by_age_location()
    result = adapters.age_location(result)

    assert "tag" in result[0]
    assert "value" in result[0]
    assert "nao-informado" in result[0]["value"]
    assert "rural" in result[0]["value"]
    assert "urbana" in result[0]["value"]

    result = repo.find_group_by_age_location(25)
    result = adapters.age_location(result)

    assert "tag" in result[0]
    assert "value" in result[0]
    assert "nao-informado" in result[0]["value"]
    assert "rural" in result[0]["value"]
    assert "urbana" in result[0]["value"]

def test_by_race():
    result = repo.find_group_by_race(25)
    result = adapters.group_by_race(result)
    pprint(result)


def test_by_gender():
    result = repo.find_group_by_age_gender(25)
    result = adapters.group_by_gender(result)
    pprint(result)


def test_by_influenza():
    result = repo.find_group_by_influenza_rate(25)
    result = adapters.influenza_rate(result)
    assert "vacinadas" in result[0]["tag"]
    assert "nao-vacinadas" in result[1]["tag"]


def test_by_odonto():
    result = repo.find_group_by_odonto_rate(25)
    result = adapters.odonto_rate(result)
    assert 'atendidas' in result[0]['tag']
    assert "nao-atendidas" in result[1]["tag"]

def test_by_hipertensao():
    result = repo.find_total_hipertension_diabetes(25)
    result = adapters.total_hipertension_diabetes(result)
    pprint(result)
    assert 'hipertensao' in result[0]['tag']
    assert "diabetes" in result[1]["tag"]
    assert "hipertensao-diabetes-associadas" in result[2]["tag"]
