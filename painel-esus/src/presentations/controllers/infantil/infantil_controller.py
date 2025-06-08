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
