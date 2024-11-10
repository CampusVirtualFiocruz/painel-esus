from src.domain.use_cases.diseases_dashboard.diabetes_use_case import (
    DiabetesDasboardUseCaseInterface,
)
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class DiabetesDashboardGetProfessionalsCount(ControllerInterface):
    def __init__(self, use_case: DiabetesDasboardUseCaseInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = None, None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])

        response = self.__use_case.get_professionals_count(cnes, equipe)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
