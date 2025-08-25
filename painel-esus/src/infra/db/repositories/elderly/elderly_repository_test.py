from pprint import pprint
from sqlite3 import adapters

from src.main.adapters.elderly_adapter import ElderlyAdapter

from .elderly_repository import ElderlyRepository

repo = ElderlyRepository()
adapters = ElderlyAdapter()

def test_nominal():
    response = repo.find_filter_nominal(9)
    response["items"] = [
        adapters.nominal_list(r).to_dict() for r in response["items"]
    ]
    print(response["items"])
