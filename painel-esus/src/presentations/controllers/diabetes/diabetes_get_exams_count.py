from src.domain.use_cases.diseases_dashboard.diabetes_use_case import \
    DiabetesDasboardUseCaseInterface
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface

from src.domain.entities.disease_exams import DiseaseExams


class DiabetesDashboardGetExamsCount(ControllerInterface):
    def __init__(self, use_case: DiabetesDasboardUseCaseInterface, diabete_exams: DiseaseExams):
        self.__use_case = use_case
        self.__diabete_exams = diabete_exams

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_exams_count(
            cnes=cnes, exam_disease=self.__diabete_exams)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
