from src.main.adapters.hypertension_adapter import HypertensionAdapter
from src.main.adapters.nominal_list_adapter import (
    DiabetesNominalListAdapter,
    HypertensionNominalListAdapter,
)
from src.main.adapters.request_adapter import HttpRequest, HttpResponse

from .hypertension_repository_interface import HypertensionDiabetesRepositoryInterface


class HypertensionDiabetesController:
    _nominal_adapter = None
    _adapter = None
    def __init__(self, repository: HypertensionDiabetesRepositoryInterface, adapter, nominal_adapter):
        self.__repository = repository
        self._adapter =adapter
        self._nominal_adapter = nominal_adapter

    def parse_request(self, request: HttpRequest):
        cnes, equipe = None, None
        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])

        return cnes, equipe

    def get_total(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_total(cnes, equipe)
        return HttpResponse(status_code=200, body=response)

    def get_by_gender(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_by_gender(cnes, equipe)
        result = self._adapter.get_by_gender(response)
        return HttpResponse(status_code=200, body=result)

    def get_by_race(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_by_race(cnes, equipe)
        result = self._adapter.get_by_race(response)
        return HttpResponse(status_code=200, body=result)

    def get_exams_table(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_exams_count(cnes, equipe)
        result = self._adapter.get_exams_count(response)
        return HttpResponse(status_code=200, body=result)

    def get_imc(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_imc(cnes, equipe)
        result = self._adapter.get_imc(response)
        return HttpResponse(status_code=200, body=result)

    def get_complications(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_complications(cnes, equipe)
        result = self._adapter.get_complications(response)
        return HttpResponse(status_code=200, body=result)

    def get_nominal_list(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe, nome, cpf, page, page_size, q, sort = (
            None,
            None,
            None,
            None,
            0,
            10,
            None,
            [],
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
            sort = request.query_params.getlist("sort[]")

        response = self.__repository.get_nominal_list(
            cnes, page, page_size, nome, cpf, equipe, q, sort
        )
        response["items"] = [
            self._nominal_adapter(r).to_dict() for r in response["items"]
        ]
        return HttpResponse(status_code=200, body=response)

    def get_nominal_list_download(self, request):
        cnes, equipe = self.parse_request(request)
        response = self.__repository.get_nominal_list_download(cnes, equipe)
        return response


class HypertensionController(HypertensionDiabetesController):

    def __init__(
        self, repository: HypertensionDiabetesRepositoryInterface):
        super().__init__(
            repository, HypertensionAdapter(), HypertensionNominalListAdapter
        )


class DiabetesController(HypertensionDiabetesController):

    def __init__(self, repository: HypertensionDiabetesRepositoryInterface):
        super().__init__(repository, HypertensionAdapter(), DiabetesNominalListAdapter)
