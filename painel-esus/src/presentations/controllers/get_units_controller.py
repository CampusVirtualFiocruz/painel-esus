from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.data.interfaces.city_information_repository import CityInformationRepository
from src.presentations.http_types import HttpRequest, HttpResponse


class GetUnitsController(ControllerInterface):

    def __init__(self, use_case: CityInformationRepository):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        response = self.__use_case.get_units()
        response = response.to_dict(orient='records')
        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
