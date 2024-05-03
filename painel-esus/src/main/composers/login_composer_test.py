import os

import pytest

from src.presentations.http_types import HttpRequest, HttpResponse

from .login_composer import login_composer


@pytest.mark.skip(reason='Avoid hit o bridge')
def test_login_bridge():
    request = HttpRequest(
        None,
        body={
            "username": "10288507860",
            "password": "10288507860esus"
        }
    )
    login = login_composer(request)
    assert isinstance(login, HttpResponse)
    assert login.body is not None
    assert isinstance(login.body['data'], str)
    assert login.status_code == 200


def test_login_admin():
    request = HttpRequest(
        None,
        body={
            "username": os.getenv('ADMIN_USERNAME', 'admin'),
            "password": os.getenv('ADMIN_PASSWORD', 'FCadmin')
        }
    )
    login = login_composer(request)
    assert isinstance(login, HttpResponse)
    assert login.body is not None
    assert isinstance(login.body['data'], str)
    assert login.status_code == 200
    print(login.body)


def test_login_user():
    request = HttpRequest(
        None,
        body={
            "username": '95009337568',
            "password": '700009534775406painel'
        }
    )
    login = login_composer(request)
    assert isinstance(login, HttpResponse)
    assert login.body is not None
    assert isinstance(login.body['data'], str)
    assert login.status_code == 200
    print(login.body)


def test_login_invalid():
    request = HttpRequest(
        None,
        body={
            "username": 'paintball',
            "password": 'paintball'
        }
    )
    login = login_composer(request)
    assert isinstance(login, HttpResponse)
    assert login.body['data'] == 'Username or Password invalid.'
    assert login.status_code == 401
