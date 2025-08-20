from .ibge import get_ibge_total


def test_ibge_total():
    result = get_ibge_total()
    print(result)
    assert isinstance(result, int)
    assert result >= 0
