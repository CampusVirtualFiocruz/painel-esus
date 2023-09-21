from src.data.use_cases.demographics_info import \
    DemographicsInfo as DemographicsInfoUseCase
from src.infra.db.repositories.demographics_info import \
    DemographicsInfoRepository
from src.presentations.controllers.demographics_info_controller import \
    DemographicsInfoController


def demographics_info_composer():
    repository = DemographicsInfoRepository()
    use_case = DemographicsInfoUseCase(repository)
    controller = DemographicsInfoController(use_case)

    return controller.handle
