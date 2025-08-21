import pytest
from src.infra.db.repositories.demographic.location_area_repository import (
    LocationAreaRepository,
)
from src.main.adapters.adapters import DemographicAdapter

from .get_location_area import GetLocationAreaUseCase


@pytest.fixture
def user_case_fatory():
    return GetLocationAreaUseCase(LocationAreaRepository(), DemographicAdapter())

def test_location_adapter(user_case_fatory):
    response = user_case_fatory.get_location_area()
    print(response)
