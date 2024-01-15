from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.data.interfaces.city_information_repository import CityInformationRepository
from src.presentations.http_types import HttpRequest, HttpResponse


class CityInformationsController(ControllerInterface):

    def __init__(self, use_case: CityInformationRepository):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_city_info(cnes)
        response = response.to_dict(orient='records')
        return HttpResponse(
            status_code=200,
            body=response[0]
        )
