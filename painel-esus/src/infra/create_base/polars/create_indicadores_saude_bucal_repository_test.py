from .create_indicadores_saude_bucal_repository import CreateIndicadoresSaudeBucalRepository
from .create_fat_atend_indiv_odonto_repository import  CreateAtendOdontoBaseRepository
def test_init():
    # r1 = CreateAtendOdontoBaseRepository()
    # r1.create_base()
    repo = CreateIndicadoresSaudeBucalRepository()
    repo.create_base()
    