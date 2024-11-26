# pylint: disable=W0613
from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository
from src.main.adapters.elderly_adapter import ElderlyAdapter
from src.main.adapters.request_adapter import HttpRequest, HttpResponse


class ElderlyController:

    def __init__(self, use_case: ElderlyRepository):
        self.__use_case = use_case
        self._adapter = ElderlyAdapter()

    def parse_request(self, request: HttpRequest):
        cnes, equipe = None, None
        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])
        return cnes, equipe

    def total(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__use_case.find_total(cnes, equipe)
        result = self._adapter.total(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_ages_location(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__use_case.find_group_by_age_location(cnes, equipe)
        result = self._adapter.age_location(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_race(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_group_by_race(cnes, equipe)
        result = self._adapter.group_by_race(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_by_gender(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__use_case.find_group_by_age_gender(cnes, equipe)
        result = self._adapter.group_by_gender(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_imc_rate(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__use_case.find_group_by_imc(cnes, equipe)
        result = self._adapter.group_by_imc(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_influenza_rate(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_group_by_influenza_rate(cnes, equipe)
        result = self._adapter.influenza_rate(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_odonto_rate(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_group_by_odonto_rate(cnes, equipe)
        result = self._adapter.odonto_rate(response)
        return HttpResponse(status_code=200, body=result)

    def grouping_total_disease_related(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)

        response = self.__use_case.find_total_hipertension_diabetes(cnes, equipe)
        result = self._adapter.total_hipertension_diabetes(response)
        return HttpResponse(status_code=200, body=result)

    def get_nominal_list(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe, nome, cpf, page, page_size, q = (
            None,
            None,
            None,
            None,
            0,
            10,
            None,
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
        response = self.__use_case.find_filter_nominal(
            cnes=cnes,
            equipe=equipe,
            page=page,
            pagesize=page_size,
            nome=nome,
            cpf=cpf,
            query=q,
        )

        result = self._adapter.nominal_list(response)
        return HttpResponse(status_code=200, body=result)

    def get_nominal_list_download(self, request: HttpRequest):
        cnes, equipe = self.parse_request(request)
        return self.__use_case.find_all_download(cnes=cnes, equipe=equipe)
