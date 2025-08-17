from src.data.use_cases.demographic.get_age_groups import GetAgeGroupsUseCase
from src.data.use_cases.demographic.get_gender import GetGenderUseCase
from src.data.use_cases.demographic.get_ibge_population import GetIBGEPopulationUseCase
from src.data.use_cases.demographic.get_location_area import GetLocationAreaUseCase
from src.data.use_cases.demographic.get_total_people import GetTotalPeopleUseCase
from src.infra.db.repositories.demographic.age_groups_repository import (
    AgeGroupsRepository,
)
from src.infra.db.repositories.demographic.gender_repository import GenderRepository
from src.infra.db.repositories.demographic.ibge_population_repository import (
    IBGEPopulationRepository,
)
from src.infra.db.repositories.demographic.location_area_repository import (
    LocationAreaRepository,
)
from src.infra.db.repositories.demographic.total_people_repository import (
    TotalPeopleRepository,
)
from src.main.adapters.adapters import DemographicAdapter
from src.presentations.controllers.demographic.get_age_groups_controller import (
    GetAgeGroupsController,
)
from src.presentations.controllers.demographic.get_gender_controller import (
    GetGenderController,
)
from src.presentations.controllers.demographic.get_ibge_population_controller import (
    GetIBGEPopulationController,
)
from src.presentations.controllers.demographic.get_location_area_controller import (
    GetLocationAreaController,
)
from src.presentations.controllers.demographic.get_total_people_controller import (
    GetTotalPeopleController,
)


def _location_area_use_case_factory():
    repository = LocationAreaRepository()
    return GetLocationAreaUseCase(repository, DemographicAdapter())


def get_age_groups_composer():
    repository = AgeGroupsRepository()
    use_case = GetAgeGroupsUseCase(repository)
    controller = GetAgeGroupsController(use_case)
    return controller.handle


def get_gender_composer():
    repository = GenderRepository()
    use_case = GetGenderUseCase(repository)
    controller = GetGenderController(use_case)

    return controller.handle


def get_ibge_population_composer():
    repository = IBGEPopulationRepository()
    use_case = GetIBGEPopulationUseCase(repository)
    controller = GetIBGEPopulationController(use_case)

    return controller.handle


def get_location_area_composer():
    use_case = _location_area_use_case_factory()
    controller = GetLocationAreaController(use_case)

    return controller.get_location_area


def get_diabetes_by_location_area_composer():
    use_case = _location_area_use_case_factory()
    controller = GetLocationAreaController(use_case)
    return controller.get_diabetes_by_location_area


def get_hypertension_by_location_area_composer():
    use_case = _location_area_use_case_factory()
    controller = GetLocationAreaController(use_case)
    return controller.get_hypertension_by_location_area


def get_child_by_location_area_composer():
    use_case = _location_area_use_case_factory()
    controller = GetLocationAreaController(use_case)
    return controller.get_child_by_location_area


def get_elderly_by_location_area_composer():
    use_case = _location_area_use_case_factory()
    controller = GetLocationAreaController(use_case)
    return controller.get_elderly_by_location_area


def get_total_people_composer():
    repository = TotalPeopleRepository()
    use_case = GetTotalPeopleUseCase(repository)
    controller = GetTotalPeopleController(use_case)

    return controller.handle
