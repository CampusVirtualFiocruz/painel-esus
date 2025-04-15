from src.domain.use_cases.demographic.demographic_use_case import (
    DemographicIBGEPopulationUseCaseInterface,
)
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import ControllerInterface


class DemographicGetIBGEPopulation(ControllerInterface):
    def __init__(self, use_case: DemographicIBGEPopulationUseCaseInterface):
        self.__use_case = use_case

    def handle(self) -> HttpResponse:
        response = self.__use_case.get_ibge_population()
        return HttpResponse(status_code=200, body={"data": response})
