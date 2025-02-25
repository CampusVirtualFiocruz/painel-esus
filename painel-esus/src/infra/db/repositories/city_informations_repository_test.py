from .city_informations_repository import CityInformationsRepository


def test_get_units():
    repo = CityInformationsRepository()
    units = repo.get_units()
    print(units)