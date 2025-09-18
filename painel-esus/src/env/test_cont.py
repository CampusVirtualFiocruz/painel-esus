import os

import pytest

from .conf import HttpUnprocessableEntityError, is_installed_ok, update_env


def test_conf():
    status, response = is_installed_ok()
    assert status == True

def test_update_env():
    db_user = 'GOKU'
    input = {"DB_USER":db_user}

    update_env(input)
    assert os.getenv('DB_USER') == db_user

    input = {"DRAGAO": db_user}
    with pytest.raises(HttpUnprocessableEntityError) as exc:
        update_env(input)
    assert str(exc.value) == "The key DRAGAO is forbidden for this context."
