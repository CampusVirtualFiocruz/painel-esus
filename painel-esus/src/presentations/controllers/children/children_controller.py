# pylint: disable=W0613
from src.infra.db.repositories.children.children_repository import ChildrenRepository
from src.main.adapters.children_adapter import ChildrenAdapter
from src.main.adapters.request_adapter import HttpRequest, HttpResponse


class ChildrenController:

    def __init__(self, use_case: ChildrenRepository):
        self.__use_case = use_case
        self._adapter = ChildrenAdapter()

    def parse_request(self, request: HttpRequest):
        cnes, equipe = None, None
        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])
        return cnes, equipe

    def total(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_total_children_cares(cnes, equipe)

        result = self._adapter.total_cares(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_ages_location(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_grouping_by_ages_location(cnes, equipe)

        result = self._adapter.age_by_location(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_race(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_grouping_by_race(cnes, equipe)

        result = self._adapter.children_group_by_race(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_gender(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_grouping_by_ages_gender(cnes, equipe)

        result = self._adapter.age_by_gender(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_location_rate(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_children_location_rate(cnes, equipe)

        result = self._adapter.children_location_rate(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_cares_by_professionals(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_group_professionals_care(cnes, equipe)

        result = self._adapter.children_cares_by_professionals(response)
        return HttpResponse(status_code=200, body=result)

    def get_nominal_list(self, request: HttpRequest) -> HttpResponse:
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
            equipe = request.query_params["equipe"]
        if request.query_params and "q" in request.query_params:
            q = request.query_params["q"]
        
        response = self.__use_case.find_filter_nominal(cnes=cnes, equipe=equipe, pagesize=page_size, page=page, cpf=cpf, nome=nome, query=q)

        result = self._adapter.nominal_list(response)
        return HttpResponse(status_code=200, body=result)

    def get_nominal_list_download(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        return self.__use_case.find_all_download(cnes=cnes, equipe=equipe)
