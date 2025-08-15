from pprint import pprint

from .adapters import DemographicAdapter


def test_total():
    expected = {
        "data": 0
    }
    adapter = DemographicAdapter()
    result = adapter.total_adapter([0])
    assert result == expected

    result = adapter.total_adapter(0)
    assert result == expected

    result = adapter.total_adapter(None)
    assert result == expected

    result = adapter.total_adapter([None])
    assert result == expected

def test_pyramid():
    adapter = DemographicAdapter()
    result = adapter.age_group_pyramid([])
    pprint(result)
