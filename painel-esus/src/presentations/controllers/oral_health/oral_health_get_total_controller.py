from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class OralHealthGetTotalController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_total(cnes)
        return HttpResponse(
            status_code=200,
            body={'total': response}
        )
