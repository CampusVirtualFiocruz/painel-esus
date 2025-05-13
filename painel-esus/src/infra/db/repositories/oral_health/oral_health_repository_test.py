from .oral_health_repository import OralHealthRepository

repo = OralHealthRepository()

def test_nominal():
    result = repo.find_filter_nominal(27)
    print(result)

def test_total():
    result = repo.total_ubs()
    print(result)
