from src.domain.use_cases.oral_health_dashboard_use_case import (
    OralHealthDashboardUseCaseInterface,
)
from src.main.adapters.oral_healthy_adapter import OralHealthAdapter
from src.presentations.helpers.request_params_helper import extract_cnes_equipe_category
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class OralHealthNominalListController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardUseCaseInterface):
        self.__use_case = use_case
        self.__adapter = OralHealthAdapter()

    def _extract_nominal_params(self, request):
        cnes, equipe, nome, cpf, page, page_size, q, sort, category = (
            None,
            None,
            None,
            None,
            0,
            10,
            None,
            [],
            'atendidas'
        )

        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])

        if request.query_params and "nome" in request.query_params:
            nome = request.query_params["nome"]

        if request.query_params and "cpf" in request.query_params:
            cpf = request.query_params["cpf"]

        if request.query_params and "page" in request.query_params:
            page = int(request.query_params["page"])

        if request.query_params and "itemsPerPage" in request.query_params:
            page_size = request.query_params["itemsPerPage"]

        if request.query_params and "equipe" in request.query_params:
            equipe = request.query_params["equipe"]
        if request.query_params and "q" in request.query_params:
            q = request.query_params["q"]

        if request.query_params and "sort[]" in request.query_params:
            sort = request.query_params.getlist('sort[]')

        if request.query_params and "recorte" in request.query_params:
            category = request.query_params['recorte']

        return cnes, equipe, nome, cpf, page, page_size, q, sort, category

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe, nome, cpf, page, page_size, q, sort, category = self._extract_nominal_params(request)

        response = self.__use_case.find_filter_nominal(
            cnes,
            page,
            page_size,
            nome,
            cpf,
            equipe,
            q,
            sort,
            category
        )
        response["items"] = [
            self.__adapter.nominal_list(r, category).to_dict() for r in response["items"]
        ]

        return HttpResponse(status_code=200, body=response)
