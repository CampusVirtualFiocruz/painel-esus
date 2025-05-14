from src.domain.use_cases.demographic.demographic_use_case import (
    IBGEPopulationUseCaseInterface,
)
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class GetIBGEPopulationController(ControllerInterface):
    def __init__(self, use_case: IBGEPopulationUseCaseInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        response = self.__use_case.get_ibge_population()
        return HttpResponse(status_code=200, body={"data": response})
