from src.presentatios.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.demographics_info import DemographicsInfo
from src.presentatios.http_types import HttpRequest, HttpResponse

class DemographicsInfoController(ControllerInterface):

    def __init__(self, use_case: DemographicsInfo):
        self.__use_case = use_case

    def handle(self, request:HttpRequest) -> HttpResponse:
        cnes = None
        if 'cnes' in request.path_params:
            cnes = request.path_params['cnes']

        response = self.__use_case.get_demographics_info(cnes)

        return HttpResponse(
            status_code=200,
            body={ 'data': response}
        )
