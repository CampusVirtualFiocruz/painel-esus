from .conf import is_installed_ok


def test_conf():
    status, response = is_installed_ok()
    assert status == True
