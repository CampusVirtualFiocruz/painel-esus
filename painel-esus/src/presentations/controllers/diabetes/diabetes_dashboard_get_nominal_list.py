from src.data.use_cases.diseases_dashboard.diabetes_nominal_list import (
    DiabetesNominalListUseCase,
)
from src.presentations.controllers.utils.requests_utils import parse_request
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class DiabetesDashboardGetNominalList(ControllerInterface):
    def __init__(self, use_case: DiabetesNominalListUseCase):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe, nome, cpf, page, page_size, q = None, None, None, None, 0, 10, None

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
            equipe = int(request.query_params["equipe"])
        
        if request.query_params and "q" in request.query_params:
            q = request.query_params["q"]
        if request.query_params and "sort[]" in request.query_params:
            sort = request.query_params.getlist('sort[]')
         
        response = self.__use_case.get_nominal_list(
            cnes,
            page,
            page_size,
            nome,
            cpf,
            equipe,
            q,
            sort
        )
        response["items"] = [
            DiabetesNominalListAdapter(r).to_dict() for r in response["items"]
        ]
        return response

        return HttpResponse(status_code=200, body=response)


class DiabetesDashboardGetNominalListDownload:
    def __init__(self, use_case: DiabetesNominalListUseCase):
        self.__use_case = use_case

    def handle(self, request):
        cnes, equipe = parse_request(request)
        response = self.__use_case.get_nominal_list_download(cnes, equipe)

        return response
