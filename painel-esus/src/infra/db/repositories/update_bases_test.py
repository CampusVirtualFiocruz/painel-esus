from .update_bases import UpdateBasesRepository
from ....domain.entities.diabetes import Diabetes
from ....domain.entities.hypertension import Hypertension
from .disease.diseases_dashboard import DiseasesDashboardRepository


def test_updatebase_diabetes():
    diabetes = Diabetes()
    diabetes_repository = DiseasesDashboardRepository(diabetes)
    cares = diabetes_repository.update_bases()
    update_base_repository = UpdateBasesRepository()
    update_base_repository.update_bases(cares, 'diabetes')

    diabetes = update_base_repository.check_bases('diabetes')
    assert diabetes.shape[0] > 0


def test_updatebase_hypertension():
    hipertensao = Hypertension()
    hipertensao_repository = DiseasesDashboardRepository(hipertensao)
    cares = hipertensao_repository.update_bases()
    update_base_repository = UpdateBasesRepository()
    update_base_repository.update_bases(cares, 'hipertensao')

    hipertensao = update_base_repository.check_bases('hipertensao')
    assert hipertensao.shape[0] > 0
