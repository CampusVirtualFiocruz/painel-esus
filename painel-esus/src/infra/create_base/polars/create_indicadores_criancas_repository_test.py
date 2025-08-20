from .create_indicadores_criancas_repository import CreateIndicadoresCriancasRepository


def test_create_base():
    repo = CreateIndicadoresCriancasRepository()
    repo.create_base()
    