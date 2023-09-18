from unittest.mock import Mock, patch

import pytest
from jwt.exceptions import InvalidSignatureError
from src.errors import HttpBadTokenError

from .token_required import check_token, generate_token, validate_token


def test_generate_token():
    token = generate_token('nome', 'cns', 'MG', 'Belo Horizonte')
    print(token)
    assert isinstance(token, str)

def test_validate_token():
    print()
    token = generate_token('nome', 'cns', 'MG', 'Belo Horizonte')
    validated_token = validate_token(token)
    assert validated_token['username'] == 'nome'
    with patch('src.main.server.decorators.token_required.SECRET_PASS', 'a12SECRET_PASS3123'):
        with pytest.raises(InvalidSignatureError):
            validated_token = validate_token(token)

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
