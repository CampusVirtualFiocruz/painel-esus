from pprint import pprint

import pytest
from src.infra.db.repositories.demographic.gender_repository import GenderRepository
from src.main.adapters.adapters import DemographicAdapter

from .get_gender import GetGenderUseCase


@pytest.fixture
def test_gender_use_case():
    use_case = GetGenderUseCase(GenderRepository())
    return use_case

def test_get_gender(test_gender_use_case):
    result = test_gender_use_case.get_gender()
    result = DemographicAdapter().gender_apadter(result)
    pprint(result)
