from src.domain.use_cases.diseases_dashboard.diabetes_use_case import \
    DiabetesDasboardUseCaseInterface
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class DiabetesDashboardGetProfessionalsCount(ControllerInterface):
    def __init__(self, use_case: DiabetesDasboardUseCaseInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_professionals_count(cnes)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
