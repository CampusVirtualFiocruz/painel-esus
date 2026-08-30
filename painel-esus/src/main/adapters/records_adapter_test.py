import pytest
from src.main.adapters.records_adapter import RecordsAdapter

def test_get_total_group_happy_path():
    """Test get_total_group with normal integer and float values."""
    adapter = RecordsAdapter()
    response = [[150, 0.75]]
    result = adapter.get_total_group(response)

    assert result["total-cadastros-ubs"]["data"] == 150
    assert result["porcentagem-cadastros-atualizados"]["data"] == 75.0

def test_get_total_group_with_none_values():
    """Test get_total_group when the response contains None values."""
    adapter = RecordsAdapter()
    response = [[None, None]]
    result = adapter.get_total_group(response)

    assert result["total-cadastros-ubs"]["data"] == 0
    assert result["porcentagem-cadastros-atualizados"]["data"] == 0

def test_get_total_group_with_partial_none_values():
    """Test get_total_group when the response contains partial None values."""
    adapter = RecordsAdapter()

    # Only total is provided
    response1 = [[100, None]]
    result1 = adapter.get_total_group(response1)

    assert result1["total-cadastros-ubs"]["data"] == 100
    assert result1["porcentagem-cadastros-atualizados"]["data"] == 0

    # Only percentage is provided
    response2 = [[None, 0.5]]
    result2 = adapter.get_total_group(response2)

    assert result2["total-cadastros-ubs"]["data"] == 0
    assert result2["porcentagem-cadastros-atualizados"]["data"] == 50.0
