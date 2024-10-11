from src.data.use_cases.demographics_info import (
    DemographicsInfo as DemographicsInfoUseCase,
)
from src.infra.db.repositories.demographics_info_v2 import DemographicsInfoV2Repository
from src.presentations.controllers.demographics_info_controller import (
    DemographicsInfoController,
)


def demographics_info_composer():
    repository = DemographicsInfoV2Repository()
    use_case = DemographicsInfoUseCase(repository)
    controller = DemographicsInfoController(use_case)

    return controller.handle
