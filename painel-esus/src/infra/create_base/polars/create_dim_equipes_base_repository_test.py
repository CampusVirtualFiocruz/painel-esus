from src.infra.create_base.polars.create_dim_equipes_base_repository import CreateDimEquipesBaseRepository

def test_generate_base():
    repo = CreateDimEquipesBaseRepository()
    repo.create_base()
    