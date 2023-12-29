from src.data.use_cases.city_informations import CityInformationsUseCase
from src.infra.db.repositories.city_informations_repository import CityInformationsRepository
from src.presentations.controllers.get_units_controller import GetUnitsController

from src.presentations.controllers.city_information_controller import CityInformationsController


def city_informations_composer():
    repository = CityInformationsRepository()
    use_case = CityInformationsUseCase(repository)
    controller = CityInformationsController(use_case)

    return controller.handle


def get_units_composer():
    repository = CityInformationsRepository()
    use_case = CityInformationsUseCase(repository)
    controller = GetUnitsController(use_case)

    return controller.handle
