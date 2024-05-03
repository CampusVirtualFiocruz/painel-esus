from src.domain.use_cases.diseases_dashboard.hypertension_use_case import \
    HypertensionDasboardUseCaseInterface
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface

from src.domain.entities.disease_exams import DiseaseExams


class HypertensionDashboardGetIndividualExamsCount(ControllerInterface):
    def __init__(self, use_case: HypertensionDasboardUseCaseInterface, exams: DiseaseExams):
        self.__use_case = use_case
        self.__exams = exams

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        page = 1
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])
        if request.query_params and 'page' in request.query_params:
            page = int(request.query_params['page'])

        response = self.__use_case.get_individual_exams_count(
            cnes, self.__exams, page)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
