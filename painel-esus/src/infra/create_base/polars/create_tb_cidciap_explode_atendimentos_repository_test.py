from src.infra.create_base.polars.create_tb_cidciap_explode_atendimentos_repository import CreateCidCiapExplodeAtendimentosRepository


def test_gen_base():
    repo = CreateCidCiapExplodeAtendimentosRepository()
    repo.create_base()
    