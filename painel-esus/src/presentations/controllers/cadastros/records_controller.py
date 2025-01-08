# pylint: disable=W0613
from src.infra.db.repositories.cadastro.records_repository import RecordsRepository
from src.main.adapters.records_adapter import RecordsAdapter
from src.main.adapters.request_adapter import HttpRequest, HttpResponse
from src.presentations.controllers.utils import parse_request


class RecordsController:

    def __init__(self, use_case: RecordsRepository):
        self.__use_case = use_case
        self._adapter = RecordsAdapter()

    def get_total_group(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.get_total_group(cnes, equipe)

        result = self._adapter.get_total_group(response)
        return HttpResponse(status_code=200, body=result)

    def get_cpf_cns_rate(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.get_cpf_cns_rate(cnes, equipe)

        result = self._adapter.get_cpf_cns_rate(response)
        return HttpResponse(status_code=200, body=result)

    def group_localidade(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.group_localidade(cnes, equipe)

        result = self._adapter.group_localidade(response)
        return HttpResponse(status_code=200, body=result)

    def group_raca_cor(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.group_raca_cor(cnes, equipe)

        result = self._adapter.group_raca_cor(response)
        return HttpResponse(status_code=200, body=result)

    def group_records_by_origin(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.group_records_by_origin(cnes, equipe)

        result = self._adapter.group_records_by_origin(response)
        return HttpResponse(status_code=200, body=result)

    def group_records_status(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.group_records_status(cnes, equipe)

        result = self._adapter.records_status(response)
        return HttpResponse(status_code=200, body=result)

    def nominal_list(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe, nome, cpf, page, page_size, q = None, None, None, None, 0, 10, None

        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])

        if request.query_params and "nome" in request.query_params:
            nome = request.query_params["nome"]

        if request.query_params and "cpf" in request.query_params:
            cpf = request.query_params["cpf"]
        if request.query_params and "q" in request.query_params:
            q = request.query_params["q"]
        if request.query_params and "page" in request.query_params:
            page = int(request.query_params["page"])

        if request.query_params and "itemsPerPage" in request.query_params:
            page_size = request.query_params["itemsPerPage"]

        if request.query_params and "equipe" in request.query_params:
            equipe = request.query_params["equipe"]
        response = self.__use_case.find_filter_nominal(
            cnes=cnes, equipe=equipe, pagesize=page_size, page=page, cpf=cpf, nome=nome, query=q
        )

        result = self._adapter.nominal_list(response)
        return HttpResponse(status_code=200, body=result)

    def nominal_list_download(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        return self.__use_case.find_all_download(cnes=cnes, equipe=equipe)

    def people_who_get_care(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        response = self.__use_case.people_who_get_care(cnes=cnes, equipe=equipe)
        result = self._adapter.people_who_get_care(response)
        return HttpResponse(status_code=200, body=result)
