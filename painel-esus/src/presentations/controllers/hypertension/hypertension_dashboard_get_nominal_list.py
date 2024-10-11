from src.data.use_cases.diseases_dashboard.hypertension_nominal_list import HypertensionNominalListUseCase
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class HypertensionDashboardGetNominalList(ControllerInterface):
    def __init__(self, use_case: HypertensionNominalListUseCase):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, nome, cpf, page, page_size = None, None, None, 0, 10

        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        if request.query_params and 'nome' in request.query_params:
            nome = request.query_params['nome']

        if request.query_params and 'cpf' in request.query_params:
            cpf = request.query_params['cpf']

        if request.query_params and 'page' in request.query_params:
            page = int(request.query_params['page'])

        if request.query_params and 'itemsPerPage' in request.query_params:
            page_size = request.query_params['itemsPerPage']

        response = self.__use_case.get_nominal_list(
            cnes, page, page_size, nome, cpf)

        return HttpResponse(
            status_code=200,
            body=response
        )


class HypertensionDashboardGetNominalListDownload():
    def __init__(self, use_case: HypertensionNominalListUseCase):
        self.__use_case = use_case

    def handle(self, cnes=None):
        if cnes is not None:
            cnes = int(cnes)

        response = self.__use_case.get_nominal_list_download(cnes)

        return response
