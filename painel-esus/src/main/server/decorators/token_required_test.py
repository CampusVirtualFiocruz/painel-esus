from unittest.mock import Mock

import pytest
from src.errors import HttpBadTokenError

from .token_required import check_token, generate_token


def test_generate_token():
    token = generate_token('nome', 'cns', 'MG', 'Belo Horizonte')
    print(token)
    assert isinstance(token, str)


def test_token():
    token = generate_token('nome', 'cns', 'MG', 'Belo Horizonte')
    mock = Mock()
    mock.headers = {
        'Authorization': 'Bearer '+token
    }
    assert mock.headers.get('Authorization') is not None
    assert isinstance(mock.headers.get('Authorization'), str)

    mock.headers = {
        'Authorization': token
    }
    with pytest.raises(IndexError):
        check_token(mock)

    mock.headers = {}
    with pytest.raises(HttpBadTokenError):
        check_token(mock)

    mock.headers = {
        'Authorization': 'test '
    }
    with pytest.raises(HttpBadTokenError) as exc:
        check_token(mock)
        assert exc.status_code == 498
