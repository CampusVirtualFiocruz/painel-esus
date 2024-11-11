from src.domain.use_cases.demographics_info import DemographicsInfo
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class DemographicsInfoController(ControllerInterface):

    def __init__(self, use_case: DemographicsInfo):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = None, None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])

        response = self.__use_case.get_demographics_info(cnes, equipe)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
