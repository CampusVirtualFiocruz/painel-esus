# pylint: disable=W0613
from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository
from src.main.adapters.elderly_adapter import ElderlyAdapter
from src.main.adapters.request_adapter import HttpRequest, HttpResponse


class ElderlyController:

    def __init__(self, repository: ElderlyRepository):
        self.__repository = repository
        self._adapter = ElderlyAdapter()

    def parse_request(self, request: HttpRequest):
        cnes, equipe = None, None
        if request.path_params and "cnes" in request.path_params:
            cnes = int(request.path_params["cnes"])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])
        
        return cnes, equipe

    def total_ubs(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.total_ubs(cnes, equipe)
        result = self._adapter.total_ubs(response)
        return HttpResponse(status_code=200, body=result)

    def total_card(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.total_card(cnes, equipe)
        result = self._adapter.total_card(response)
        return HttpResponse(status_code=200, body=result)

    
    def total_medical_cares(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.total_medical_cares(cnes, equipe)
        result = self._adapter.total_medical_cares(response)
        return HttpResponse(status_code=200, body=result)
    
    def by_gender(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.by_gender(cnes, equipe)
        result = self._adapter.by_gender(response)
        return HttpResponse(status_code=200, body=result)
    
    def by_race(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.by_race(cnes, equipe)
        result = self._adapter.by_race(response)
        return HttpResponse(status_code=200, body=result)
    
    def medical_appointment(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.medical_appointment(cnes, equipe)
        result = self._adapter.two_medical_appointment(response)
        return HttpResponse(status_code=200, body=result)
    
    def height_records(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.height_records(cnes, equipe)
        result = self._adapter.two_height_records(response)
        return HttpResponse(status_code=200, body=result)
    
    def acs_visits(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.acs_visits(cnes, equipe)
        result = self._adapter.two_acs_visits(response)
        return HttpResponse(status_code=200, body=result)
    
    def creatinine(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.creatinine(cnes, equipe)
        result = self._adapter.creatinine(response)
        return HttpResponse(status_code=200, body=result)
    
    def dentist_appointment(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.dentist_appointment(cnes, equipe)
        result = self._adapter.dentist_appointment(response)
        return HttpResponse(status_code=200, body=result)
    
    def ivcf_20(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.ivcf_20(cnes, equipe)
        result = self._adapter.ivcf_20(response)
        return HttpResponse(status_code=200, body=result)
    
    def influenza_vaccines(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = self.parse_request(request)
        response = self.__repository.influenza_vaccines(cnes, equipe)
        result = self._adapter.influenza_vaccines(response)
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
            []
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
        response = self.__repository.find_filter_nominal(
            cnes=cnes,
            equipe=equipe,
            page=page,
            pagesize=page_size,
            nome=nome,
            cpf=cpf,
            query=q,
            sort=sort
        )

        response["items"] = [
            self._adapter.nominal_list(r).to_dict() for r in response["items"]
        ]
        
        return HttpResponse(status_code=200, body=response)

    def get_nominal_list_download(self, request: HttpRequest):
        cnes, equipe = self.parse_request(request)
        return self.__repository.find_all_download(cnes=cnes, equipe=equipe)
