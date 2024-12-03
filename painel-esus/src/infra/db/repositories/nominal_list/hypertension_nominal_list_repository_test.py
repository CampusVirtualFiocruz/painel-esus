from .diabetes_nominal_list_repositorio import DiabeteNominalListRepository
from .hypertension_nominal_list_repository import HypertensionNominalListRepository


def test_total():
    repo = HypertensionNominalListRepository()
    print( repo.create_base())


def test_total_diabetes():
    repo = DiabeteNominalListRepository()
    print(repo.create_base())
    # print(repo.get_hemoglobina_glicada())
    
    
