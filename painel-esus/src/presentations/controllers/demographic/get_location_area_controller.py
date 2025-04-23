from src.domain.use_cases.demographic.demographic_use_case import (
    LocationAreaUseCaseInterface,
)
from src.presentations.controllers.utils import parse_request
from src.presentations.http_types import HttpRequest, HttpResponse


class GetLocationAreaController:
    def __init__(self, use_case: LocationAreaUseCaseInterface):
        self.__use_case = use_case

    def get_location_area(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_location_area(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})

    def get_diabetes_by_location_area(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_diabetes_by_location_area(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})

    def get_hypertension_by_location_area(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_hypertension_by_location_area(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})

    def get_child_by_location_area(self) -> HttpResponse:
        response = self.__use_case.get_child_by_location_area()
        return HttpResponse(status_code=200, body={"data": response})

    def get_elderly_by_location_area(self) -> HttpResponse:
        response = self.__use_case.get_elderly_by_location_area()
        return HttpResponse(status_code=200, body={"data": response})
