from src.data.use_cases.diseases_dashboard.hypertension_nominal_list import HypertensionNominalListUseCase
from src.infra.db.repositories.disease.nominal_list.hypertension_nominal_list_repository import HypertensionNominalListRepository


def test_list():

    use_case = HypertensionNominalListUseCase(
        HypertensionNominalListRepository())
    print(use_case.get_nominal_list_download().head())
