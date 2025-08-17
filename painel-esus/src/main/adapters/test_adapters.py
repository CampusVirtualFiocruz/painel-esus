import unittest
from pprint import pprint

import pytest

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


def test_location():
    adapter = DemographicAdapter()
    result = adapter.location_type_adapter([])
    assert next(filter(lambda x: x['tag'] == 'urbano', result))['value'] == 0
    assert next(filter(lambda x: x["tag"] == "rural", result))["value"] == 0
    assert next(filter(lambda x: x["tag"] == "nao_informado", result))["value"] == 0


def test_gender():
    adapter = DemographicAdapter()
    result = adapter.gender_apadter(
        {
            "feminino": {"tag": "feminino", "value": 3469},
            "indeterminado": {"tag": "indeterminado", "value": 0},
            "masculino": {"tag": "masculino", "value": 3298},
        }
    )
    print(result)

# Python


class TestDemographicAdapter(unittest.TestCase):

    def setUp(self):
        self.adapter = DemographicAdapter()

    def test_total_adapter_list(self):
        result = self.adapter.total_adapter([5])
        assert result == {"data": 5}

    def test_total_adapter_int(self):
        result = self.adapter.total_adapter(7)
        assert result == {"data": 7}

    def test_total_adapter_none(self):
        result = self.adapter.total_adapter(None)
        assert result == {"data": 0}

    def test_total_adapter_list_none(self):
        result = self.adapter.total_adapter([None])
        assert result == {"data": 0}

    def test_location_type_adapter_empty(self):
        result = self.adapter.location_type_adapter([])
        assert next(filter(lambda x: x['tag'] == 'urbano', result))['value'] == 0
        assert next(filter(lambda x: x["tag"] == "rural", result))["value"] == 0
        assert next(filter(lambda x: x["tag"] == "nao_informado", result))["value"] == 0
    def test_location_type_adapter_dict(self):
        response = {"urbano": 10, "rural": 5, "other": 3}
        result = self.adapter.location_type_adapter(response)
        urbano = next(filter(lambda x: x['tag'] == 'urbano', result))
        rural = next(filter(lambda x: x['tag'] == 'rural', result))
        nao_informado = next(filter(lambda x: x['tag'] == 'nao_informado', result))
        assert urbano['value'] == 10
        assert rural['value'] == 5
        assert nao_informado['value'] == 3

    def test_age_group_pyramid_empty(self):
        result = self.adapter.age_group_pyramid([])
        assert "left" in result and "right" in result
        assert all(isinstance(item, dict) for item in result["left"])
        assert all(isinstance(item, dict) for item in result["right"])

    def test_age_group_pyramid_populated(self):
        # resp: [gender, age_group, location, value]
        response = [
            ["Masculino", "0 a 4 anos", "urbano", 12],
            ["Feminino", "0 a 4 anos", "rural", 7],
            ["Masculino", "5 a 9 anos", "nao informado", 3]
        ]
        result = self.adapter.age_group_pyramid(response)
        left_0_4 = next(filter(lambda x: x['tag'] == "0 a 4 anos", result["left"]))
        right_0_4 = next(filter(lambda x: x['tag'] == "0 a 4 anos", result["right"]))
        left_5_9 = next(filter(lambda x: x['tag'] == "5 a 9 anos", result["left"]))
        assert left_0_4["value"]["urbano"] == 12
        assert right_0_4["value"]["rural"] == 7
        assert left_5_9["value"]["nao-informado"] == 3

    def test_gender_apadter_known_keys(self):
        response = {"feminino": 2, "masculino": 3}
        result = self.adapter.gender_apadter(response)
        assert result["feminino"] == 2
        assert result["masculino"] == 3
        assert result["indeterminado"] == 0

    def test_gender_apadter_unknown_key(self):
        response = {"feminino": 1, "outro": 4}
        result = self.adapter.gender_apadter(response)
        assert result["feminino"] == 1
        assert result["indeterminado"] == 4
        assert result["masculino"] == 0

# pytest style for completeness
@pytest.fixture
def adapter():
    return DemographicAdapter()

def test_total_adapter_pytest(adapter):
    assert adapter.total_adapter([10]) == {"data": 10}
    assert adapter.total_adapter(0) == {"data": 0}
    assert adapter.total_adapter(None) == {"data": 0}

def test_location_type_adapter_pytest(adapter):
    response = {"urbano": 1, "rural": 2, "other": 3}
    result = adapter.location_type_adapter(response)
    assert next(filter(lambda x: x['tag'] == 'urbano', result))['value'] == 1
    assert next(filter(lambda x: x['tag'] == 'rural', result))['value'] == 2
    assert next(filter(lambda x: x['tag'] == 'nao_informado', result))['value'] == 3
