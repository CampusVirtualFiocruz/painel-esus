import pytest
from unittest.mock import patch, MagicMock
from src.main.adapters.oral_healthy_adapter import OralHealthAdapter

@pytest.fixture
def adapter():
    return OralHealthAdapter()

def test_by_gender(adapter):
    response = [("masculino", "1a4", 10), ("feminino", "1a4", 5)]
    result = adapter.by_gender(response)

    assert "data" in result
    assert len(result["data"]) == 1

    tag_data = result["data"][0]
    assert tag_data["tag"] == "1-4-anos"
    assert tag_data["value"]["masculino"] == 10
    assert tag_data["value"]["feminino"] == 5

def test_by_race(adapter):
    response = [("branca", 10), ("preta", 5), (None, 3)]
    result = adapter.by_race(response)

    assert "data" in result
    branca = next(filter(lambda x: x["tag"] == "branca", result["data"]))
    preta = next(filter(lambda x: x["tag"] == "preta", result["data"]))
    nao_informado = next(filter(lambda x: x["tag"] == "nao-informado", result["data"]))

    assert branca["value"] == 10
    assert preta["value"] == 5
    assert nao_informado["value"] == 3

def test_first_appointment(adapter):
    response = [(0, 10), (1, 5)]
    result = adapter.first_appointment(response)

    assert "data" in result
    nao_realizado = next(filter(lambda x: x["tag"] == "nao-realizado", result["data"]))
    realizado = next(filter(lambda x: x["tag"] == "realizado", result["data"]))

    assert nao_realizado["value"] == 10
    assert realizado["value"] == 5

def test_conclued_treatment(adapter):
    response = [(0, 15), (2, 5)]
    result = adapter.conclued_treatment(response)

    assert "data" in result
    nao_realizado = next(filter(lambda x: x["tag"] == "nao-realizado", result["data"]))
    realizado = next(filter(lambda x: x["tag"] == "realizado", result["data"]))

    assert nao_realizado["value"] == 15
    assert realizado["value"] == 5

def test_extraction(adapter):
    response = [(0, 8), (1, 2)]
    result = adapter.extraction(response)

    assert "data" in result
    nao_realizado = next(filter(lambda x: x["tag"] == "nao-realizado", result["data"]))
    realizado = next(filter(lambda x: x["tag"] == "realizado", result["data"]))

    assert nao_realizado["value"] == 8
    assert realizado["value"] == 2

def test_prevention_procedures(adapter):
    response = [(0, 3), (1, 7)]
    result = adapter.prevention_procedures(response)

    assert "data" in result
    nao_realizado = next(filter(lambda x: x["tag"] == "nao-realizado", result["data"]))
    realizado = next(filter(lambda x: x["tag"] == "realizado", result["data"]))

    assert nao_realizado["value"] == 3
    assert realizado["value"] == 7

def test_atraumatic_treatment(adapter):
    response = [(0, 4), (1, 6)]
    result = adapter.atraumatic_treatment(response)

    assert "data" in result
    nao_realizado = next(filter(lambda x: x["tag"] == "nao-realizado", result["data"]))
    realizado = next(filter(lambda x: x["tag"] == "realizado", result["data"]))

    assert nao_realizado["value"] == 4
    assert realizado["value"] == 6

def test_supervised_brushing(adapter):
    response = [(0, 1), (1, 9)]
    result = adapter.supervised_brushing(response)

    assert "data" in result
    nao_realizado = next(filter(lambda x: x["tag"] == "nao-realizado", result["data"]))
    realizado = next(filter(lambda x: x["tag"] == "realizado", result["data"]))

    assert nao_realizado["value"] == 1
    assert realizado["value"] == 9

@patch("src.main.adapters.oral_healthy_adapter.OralHealtNominalListAdapter")
def test_nominal_list(MockNominalListAdapter, adapter):
    # Test just verifying it passes arguments correctly to the mocked class
    response = [{"mock": "data"}]
    category = "test_category"

    mock_instance = MagicMock()
    MockNominalListAdapter.return_value = mock_instance

    result = adapter.nominal_list(response, category)

    MockNominalListAdapter.assert_called_once_with(response, category)
    assert result == mock_instance
