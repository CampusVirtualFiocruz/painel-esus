from src.domain.use_cases.demographic.demographic_use_case import (
    AgeGroupsUseCaseInterface,
)
from src.presentations.controllers.utils import parse_request
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class GetAgeGroupsController(ControllerInterface):
    def __init__(self, use_case: AgeGroupsUseCaseInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_age_groups(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})
