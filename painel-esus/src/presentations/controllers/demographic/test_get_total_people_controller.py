from src.data.use_cases.demographic.get_total_people import GetTotalPeopleUseCase
from src.infra.db.repositories.demographic.total_people_repository import (
    TotalPeopleRepository,
)

from .get_total_people_controller import GetTotalPeopleController


def test_total():
    repository = TotalPeopleRepository()
    use_case = GetTotalPeopleUseCase(repository)

    result = use_case.get_total_people()
    print(result)
