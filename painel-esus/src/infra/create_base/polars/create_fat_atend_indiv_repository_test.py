from src.infra.create_base.polars.create_fat_atend_indiv_repository import CreateAtendIndivBaseRepository


def test_gen():
    repo = CreateAtendIndivBaseRepository()
    repo.create_base()
    