from src.infra.create_base.polars.create_fat_atend_indiv_odonto_repository import CreateAtendOdontoBaseRepository

def test_gen_base():
    repo = CreateAtendOdontoBaseRepository()
    repo.create_base()
    