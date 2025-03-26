from src.infra.create_base.polars.create_fat_vacinacao_repository import CreateVacinacaoBaseRepository


def test_gen():
    repo = CreateVacinacaoBaseRepository()
    repo.create_base()