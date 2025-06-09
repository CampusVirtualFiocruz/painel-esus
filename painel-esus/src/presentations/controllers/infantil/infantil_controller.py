from src.domain.use_cases.infantil.infantil_use_case import InfantilUseCase
from src.main.adapters.infantil_adapter import InfantilAdapter
from src.presentations.http_types import HttpRequest, HttpResponse
from src.utils.request_params_helper import extract_cnes_equipe


class InfantilController:
    def __init__(self, use_case: InfantilUseCase):
        self.__use_case = use_case
        self.__adapter = InfantilAdapter()

    def get_total(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.infantil_total(cnes, equipe)
        adapted = self.__adapter.total_count_infantil(result)

        return HttpResponse(status_code=200, body={"total-cadastros": adapted})

    def get_by_age(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.infantil_by_age(cnes, equipe)
        adapted = self.__adapter.by_age_infantil(result)

        return HttpResponse(status_code=200, body={"criancas-por-sexo": adapted})

    def get_by_race(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.infantil_by_race(cnes, equipe)
        adapted = self.__adapter.by_race_infantil(result)

        return HttpResponse(
            status_code=200, body={"distribuicao-criancas-raca-cor": adapted}
        )

    def get_first_consult_8d(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.infantil_first_consult_8d(cnes, equipe)
        adapted = self.__adapter.first_consult_8d(result)

        return HttpResponse(
            status_code=200, body={"primeira-consulta-ate-8-dia": adapted}
        )

    def get_appointments_until_2_years(self, request: HttpRequest) -> HttpResponse:
        cnes, equipe = extract_cnes_equipe(request)
        result = self.__use_case.infantil_appointments_until_2_years(cnes, equipe)
        adapted = self.__adapter.appointments_until_2_years(result)

        return HttpResponse(
            status_code=200, body={"nove-consultas-puericultura-2-anos": adapted}
        )
