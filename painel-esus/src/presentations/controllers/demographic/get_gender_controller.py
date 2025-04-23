from src.domain.use_cases.demographic.demographic_use_case import GenderUseCaseInterface
from src.presentations.controllers.utils import parse_request
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class GetGenderController(ControllerInterface):
    def __init__(self, use_case: GenderUseCaseInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)

        response = self.__use_case.get_gender(cnes, equipe)
        return HttpResponse(status_code=200, body={"data": response})
