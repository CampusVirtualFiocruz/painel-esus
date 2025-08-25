from src.domain.use_cases.oral_health_dashboard_use_case import (
    OralHealthDashboardUseCaseInterface,
)
from src.main.adapters.oral_healthy_adapter import OralHealthAdapter
from src.presentations.helpers.request_params_helper import extract_cnes_equipe_category
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class OralHealthTotalController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardUseCaseInterface):
        self.__use_case = use_case
        self.__adapter = OralHealthAdapter()

    def _extract_params(self, request):
        cnes, equipe = (
            None,
            None,            
        )

        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])
        if request.query_params and "equipe" in request.query_params:
            equipe = request.query_params["equipe"]

        return cnes, equipe

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = (
            self._extract_params(request)
        )

        response = self.__use_case.get_oral_health_total(cnes, equipe)

        return HttpResponse(status_code=200, body=response)
