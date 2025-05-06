from src.domain.use_cases.oral_health_dashboard_use_case import OralHealthDashboardUseCaseInterface
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.main.adapters.oral_healthy_adapter import OralHealthAdapter

class OralHealthGetCaresByGenderController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardUseCaseInterface):
        self.__use_case = use_case
        self.__adapter = OralHealthAdapter()

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        cnes = int(request.path_params['cnes']) if request.path_params and 'cnes' in request.path_params else None
        equipe_param = request.query_params.get("equipe")
        equipe = int(equipe_param) if equipe_param and equipe_param.isdigit() else None
        category = request.query_params.get('category', 'atendidas')

        response = self.__use_case.get_oral_health_cares_by_gender(cnes, equipe, category)
        adapted_response = self.__adapter.by_gender(response)
        
        return HttpResponse(
            status_code=200,
            body=adapted_response
        )
