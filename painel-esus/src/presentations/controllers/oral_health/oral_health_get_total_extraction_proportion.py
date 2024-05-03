from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest, HttpResponse


class OralHealthGetExtractionProceduresProportionController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_extraction_procedures_proportion(cnes)
        return HttpResponse(
            status_code=200,
            body=[
                {
                    "label": "Exodontia de dente decíduo",
                    "value": int(response['total_dente_deciduo'].iloc[0])
                },
                {
                    "label": "Exodontia de dente permanent",
                    "value": int(response['total_dente_permanente'].iloc[0])
                },
                {
                    "label": "Demais procedimentos",
                    "value": int(response['total_outros'].iloc[0])
                },
            ]
        )
