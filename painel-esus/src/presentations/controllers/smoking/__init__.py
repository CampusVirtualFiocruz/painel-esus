from abc import abstractmethod
from typing import Any

from src.data.interfaces.smoking_repository import SmokingRepository
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class SmokersController(ControllerInterface):
    def __init__(self, use_case: SmokingRepository):
        self._use_case = use_case

    @abstractmethod
    def action(self, cnes: int = None): pass

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.action(cnes)
        response = response.to_dict(orient='records')
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )


class SmokersBySexController(SmokersController):
    def action(self, cnes: int = None):
        return self._use_case.smokers_by_sex(cnes)


class SmokersByEducationController(SmokersController):
    def action(self, cnes: int = None):
        return self._use_case.smokers_by_education(cnes)


class FollowedSmokedPeopleProportionController(SmokersController):

    def action(self, cnes: int = None):
        return self._use_case.followed_smoked_people_proportion(cnes)


class RiskFactorsProportionByDantController(SmokersController):
    def action(self, cnes: int = None):
        return self._use_case.risk_factors_proportion_by_dant(cnes)


class SmokersByAgeController(SmokersController):
    def action(self, cnes: int = None):
        return self._use_case.smokers_by_age(cnes)


class ProportionOfDentalConsultationsAmongSmokersController(SmokersController):
    def action(self, cnes: int = None):
        return self._use_case.proportion_of_dental_consultations_among_smokers(cnes)
