from src.domain.use_cases.children.children_use_case import ChildrenUseCase
from src.main.adapters.children_adapter import ChildrenAdapter
from src.presentations.http_types import HttpRequest, HttpResponse
from src.utils.request_params_helper import extract_cnes_equipe


class ChildrenController:
    def __init__(self, use_case: ChildrenUseCase):
        self.__use_case = use_case
        self.__adapter = ChildrenAdapter()

    def get_total(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_total(cnes, equipe)
        adapted = self.__adapter.total_count_children(result)

        return HttpResponse(status_code=200, body={"total-cadastros": adapted})

    def get_by_age(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_by_age(cnes, equipe)
        adapted = self.__adapter.by_age_children(result)

        return HttpResponse(status_code=200, body={"criancas-por-sexo": adapted})

    def get_by_race(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_by_race(cnes, equipe)
        adapted = self.__adapter.by_race_children(result)

        return HttpResponse(
            status_code=200, body={"distribuicao-criancas-raca-cor": adapted}
        )

    def get_first_consult_8d(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_first_consult_8d(cnes, equipe)
        adapted = self.__adapter.first_consult_8d(result)

        return HttpResponse(
            status_code=200, body={"primeira-consulta-ate-8-dia": adapted}
        )

    def get_appointments_until_2_years(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_appointments_until_2_years(cnes, equipe)
        adapted = self.__adapter.appointments_until_2_years(result)

        return HttpResponse(
            status_code=200, body={"nove-consultas-puericultura-2-anos": adapted}
        )

    def get_high_weight_records(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_high_weight_records(cnes, equipe)
        adapted = self.__adapter.high_weight_records(result)

        return HttpResponse(
            status_code=200,
            body={"registro-peso-altura-puericultura-9-consultas": adapted},
        )

    def get_milestone(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_milestone(cnes, equipe)
        adapted = self.__adapter.milestone(result)

        return HttpResponse(
            status_code=200,
            body={"marco-desenvolvimento-avaliados": adapted},
        )

    def get_evaluated_feeding(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.children_evaluated_feeding(cnes, equipe)
        adapted = self.__adapter.evaluated_feeding(result)

        return HttpResponse(
            status_code=200,
            body={"consumo-alimentar-avaliado": adapted},
        )
