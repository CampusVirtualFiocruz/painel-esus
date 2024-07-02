# pylint:disable=invalid-name
from src.data.interfaces.smoking_repository import SmokingRepository
from src.domain.use_cases.smoking.smoking_use_case import \
    SmokingUseCase as SmokingUseCaseInterface


class SmokingUseCase(SmokingUseCaseInterface):
    def __init__(self, repository: SmokingRepository):
        self._repository = repository

    def followed_smoked_people_proportion(self, cnes: int = None):
        return self._repository.followed_smoked_people_proportion(cnes)

    def risk_factors_proportion_by_dant(self, cnes: int = None):
        return self._repository.risk_factors_proportion_by_dant(cnes)

    def smokers_by_age(self, cnes: int = None):
        return self._repository.smokers_by_age(cnes)

    def proportion_of_dental_consultations_among_smokers(
            self, cnes: int = None):
        return self._repository.proportion_of_dental_consultations_among_smokers(cnes)

    def smokers_by_sex(self, cnes: int = None):
        return self._repository.smokers_by_sex(cnes)

    def smokers_by_education(self, cnes: int = None):
        return self._repository.smokers_by_education(cnes)
