from src.domain.use_cases.oral_health_dashboard_use_case import OralHealthDashboardUseCaseInterface
from src.presentations.helpers.request_params_helper import extract_cnes_equipe_category
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.main.adapters.oral_healthy_adapter import OralHealthAdapter

class OralHealthGetConcluedTreatmentController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardUseCaseInterface):
        self.__use_case = use_case
        self.__adapter = OralHealthAdapter()

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe, category = extract_cnes_equipe_category(request)

        response = self.__use_case.get_oral_health_conclued_treatment(cnes, equipe, category)
        adapted_response = self.__adapter.conclued_treatment(response)
        
        return HttpResponse(
            status_code=200,
            body=adapted_response
        )
