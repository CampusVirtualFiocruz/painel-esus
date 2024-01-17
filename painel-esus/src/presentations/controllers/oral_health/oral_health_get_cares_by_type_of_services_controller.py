from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest, HttpResponse


class OralHealthGetCaresByTypeOfServicesController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_cares_by_type_of_services(cnes)
        response = response.rename(
            columns={'ds_tipo_consulta_odonto': 'label', 'total': 'value'})
        response.to_dict(orient='records')
        return HttpResponse(
            status_code=200,
            body=response.to_dict(orient='records')
        )
