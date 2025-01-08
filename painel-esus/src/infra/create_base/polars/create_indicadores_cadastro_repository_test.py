from .create_fat_atend_indiv_odonto_repository import CreateAtendOdontoBaseRepository
from .create_fat_cad_individual_repository import CreateCadIndividualBaseRepository
from .create_fat_proced_atend_repository import CreateProcedAtendBaseRepository
from .create_indicadores_cadastro_repository import CreateIndicadoresCadastroRepository
from .create_tb_acomp_cidadaos_vinculados_repository import (
    CreateAcompCidadaosVinculadosBaseRepository,
)

# def test_preced_atend():
#     repos = [
#         CreateCadIndividualBaseRepository(),
#         # CreateProcedAtendBaseRepository(),
#         # CreateAtendOdontoBaseRepository(),
#     ]
#     [repo.create_base() for repo in repos]

# def test_create_cidadaos_acompanhados():
#     repo = CreateAcompCidadaosVinculadosBaseRepository()
#     repo.create_base()
def test_indicador():
    repo = CreateIndicadoresCadastroRepository()
    repo.create_base()
