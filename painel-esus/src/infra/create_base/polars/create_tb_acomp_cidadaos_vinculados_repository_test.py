from src.infra.create_base.polars.create_tb_acomp_cidadaos_vinculados_repository import CreateAcompCidadaosVinculadosBaseRepository

def test_gen():
    repo = CreateAcompCidadaosVinculadosBaseRepository()
    repo.create_base()
    