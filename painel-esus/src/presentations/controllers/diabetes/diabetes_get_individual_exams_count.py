from src.domain.entities.disease_exams import DiseaseExams
from src.domain.use_cases.diseases_dashboard.diabetes_use_case import (
    DiabetesDasboardUseCaseInterface,
)
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class DiabetesDashboardGetIndividualExamsCount(ControllerInterface):
    def __init__(self, use_case: DiabetesDasboardUseCaseInterface, exams: DiseaseExams):
        self.__use_case = use_case
        self.__exams = exams

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = None, None
        page = 1
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])
        if request.query_params and 'page' in request.query_params:
            page = int(request.query_params['page'])
        if request.query_params and "equipe" in request.query_params:
            equipe = int(request.query_params["equipe"])

        response = self.__use_case.get_individual_exams_count(
            cnes,equipe, self.__exams, page)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
