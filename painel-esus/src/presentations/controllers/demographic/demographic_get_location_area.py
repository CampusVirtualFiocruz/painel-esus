from src.domain.use_cases.demographic.demographic_use_case import (
    DemographicLocationAreaUseCaseInterface,
)
from src.presentations.controllers.utils import parse_request
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class DemographicGetLocationArea(ControllerInterface):
    def __init__(self, use_case: DemographicLocationAreaUseCaseInterface):
        self.__use_case = use_case

    def get_location_area(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_location_area(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})

    def get_diabetes_location_area(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_diabetes_location_area(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})

    def get_hypertension_location_area(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_hypertension_location_area(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})

    def get_child_location_area(self) -> HttpResponse:
        response = self.__use_case.get_child_location_area()
        return HttpResponse(status_code=200, body={"data": response})

    def get_elderly_location_area(self) -> HttpResponse:
        response = self.__use_case.get_elderly_location_area()
        return HttpResponse(status_code=200, body={"data": response})
