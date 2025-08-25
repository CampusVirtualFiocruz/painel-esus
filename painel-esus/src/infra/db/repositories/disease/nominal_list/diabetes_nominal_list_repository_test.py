from src.main.adapters.nominal_list_adapter import DiabetesNominalListAdapter

from .diabetes_nominal_list_repository import DiabetesNominalListRepository

repo = DiabetesNominalListRepository()

def test_list_nominal():
    result = repo.find_filter(26)
    adapter = DiabetesNominalListAdapter(result["items"][0])
    print(adapter.to_dict())
