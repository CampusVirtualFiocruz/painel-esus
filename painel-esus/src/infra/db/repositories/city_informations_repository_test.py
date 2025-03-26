from .city_informations_repository import CityInformationsRepository
from src.env.conf import getenv
def test_city():
    repo = CityInformationsRepository()
    units = repo.get_city_info()
    print(units)

def test_get_units():
    repo = CityInformationsRepository()
    units = repo.get_units()
    print(units['no_unidade_saude'])


def test_get_units_atd():
    repo = CityInformationsRepository()
    units = repo.get_units_with_patients()
    print(units['no_unidade_saude'])
    print(units)

def test_get_teams():
    repo = CityInformationsRepository()
    units = repo.get_teams(19)
    print(units)
    
def test_mock_name():
    name = 'Tales mota Machado'
    name_exploded = name.split()
    import re
    def mock_word(phrase, gap=2, skip_first=False):
        mock = getenv("MOCK", False, False) == 'True'
        if not mock or phrase=="" or phrase is None:
            return phrase
        words = phrase.split()
        if skip_first:
            return " ".join([words[0],*[word[:gap]+"".join(["*" for n in word[gap:]]) for word in words[1:]]])
        else:
            return " ".join([word[:gap]+"".join(["*" for n in word[gap:]]) for word in words])
    
    print(mock_word("Tales Mota Machado",1,True))
    
