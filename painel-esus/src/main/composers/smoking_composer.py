from src.data.use_cases.smoking.smoking_use_case import SmokingUseCase
from src.infra.db.repositories.smoking.smoking_repository import SmokingRepository
from src.presentations.controllers.smoking import (
    FollowedSmokedPeopleProportionController,
)
from src.presentations.controllers.smoking import (
    ProportionOfDentalConsultationsAmongSmokersController,
)
from src.presentations.controllers.smoking import RiskFactorsProportionByDantController
from src.presentations.controllers.smoking import SmokersByAgeController
from src.presentations.controllers.smoking import SmokersByEducationController
from src.presentations.controllers.smoking import SmokersBySexController

repository = SmokingRepository()
use_case = SmokingUseCase(repository)


def followed_smoked_people_proportion():
    controller = FollowedSmokedPeopleProportionController(use_case)
    return controller.handle


def risk_factors_proportion_by_dant():
    controller = RiskFactorsProportionByDantController(use_case)
    return controller.handle


def smokers_by_age():
    controller = SmokersByAgeController(use_case)
    return controller.handle


def proportion_of_dental_consultations_among_smokers():
    controller = ProportionOfDentalConsultationsAmongSmokersController(
        use_case)
    return controller.handle


def smokers_by_sex():
    controller = SmokersBySexController(use_case)
    return controller.handle


def smokers_by_education():
    controller = SmokersByEducationController(use_case)
    return controller.handle
