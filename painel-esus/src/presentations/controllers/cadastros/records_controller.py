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
        cnes, equipe = parse_request(request)
        response = self.__use_case.find_filter_nominal(cnes, equipe)

        result = self._adapter.nominal_list(response)
        return HttpResponse(status_code=200, body=result)
    
    def nominal_list_download(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = parse_request(request)
        return self.__use_case.find_all_download(cnes=cnes, equipe=equipe)
