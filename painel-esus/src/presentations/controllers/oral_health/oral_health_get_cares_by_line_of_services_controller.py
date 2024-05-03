from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class OralHealthGetCaresByLineOfServicesController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_cares_by_line_of_services(cnes)
        return HttpResponse(
            status_code=200,
            body=[

                {
                    "label": "Gestantes",
                    "value":  int(response['gestantes'].iloc[0]),
                    "total": int(response['total'].iloc[0])
                },
                {
                    "label": "Pessoas com deficiência",
                    "value": int(response['especiais'].iloc[0]),
                    "total": int(response['total'].iloc[0])
                },
            ]
        )
