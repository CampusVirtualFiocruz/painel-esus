import os
import time

import pytest
from apscheduler.schedulers.background import BackgroundScheduler
from src.presentations.controllers.create_bases.generate_base_thread import (
    GenerateBase,
    generate_base_scheduled,
)

from .conf import HttpUnprocessableEntityError, is_installed_ok, update_env


def test_conf():
    status, response = is_installed_ok()
    print(response)
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


def test_generate_base():
    scheduler = BackgroundScheduler()
    status, _ = is_installed_ok()
    scheduler.start()
    if status:
        generate_base_scheduled(scheduler)
        time.sleep(5)
        GenerateBase().stop()
