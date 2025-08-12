from .create_indicadores_diabetes_repository import CreateIndicadoresDiabetesRepository

repo = CreateIndicadoresDiabetesRepository()

def test_create_base():
    repo.create_base()