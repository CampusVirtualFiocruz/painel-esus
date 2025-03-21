from .city_informations_repository import CityInformationsRepository


def test_get_units():
    repo = CityInformationsRepository()
    units = repo.get_units()
    print(units)

def test_get_units_atd():
    repo = CityInformationsRepository()
    units = repo.get_units_with_patients()
    print(units)

def test_get_teams():
    repo = CityInformationsRepository()
    units = repo.get_teams(19)
    print(units)
