from .connection_local import DBConnectionHandler


def test_local_path():

    repo = DBConnectionHandler()
    path = repo.get_db_path()
    assert "painel-saude-esus/painel-esus/painel_esus.db" in path
