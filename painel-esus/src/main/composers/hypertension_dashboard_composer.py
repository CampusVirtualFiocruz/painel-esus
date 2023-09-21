from src.data.use_cases.diabetes_hypertension.hypertension_dashboard import \
    HypertensionUseCase
from src.infra.db.repositories.hypertension.hypertension_dashboard import \
    HypertensionDashboardRepository
from src.presentations.controllers.hypertension import (
    HypertensionDashboardGetAgeGroupGender,
    HypertensionDashboardGetAgeGroupsLocation,
    HypertensionDashboardGetComplications, HypertensionDashboardGetExamsCount,
    HypertensionDashboardGetIMC, HypertensionDashboardGetProfessionalsCount,
    HypertensionDashboardGetTotal)


def hypertension_dashboard_get_total():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetTotal(use_case)

    return controller.handle


def hypertension_dashboard_get_age_groups_location():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetAgeGroupsLocation(use_case)

    return controller.handle


def hypertension_dashboard_get_age_group_gender():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetAgeGroupGender(use_case)

    return controller.handle


def hypertension_dashboard_get_complications():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetComplications(use_case)

    return controller.handle


def hypertension_dashboard_get_professionals_count():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetProfessionalsCount(use_case)

    return controller.handle


def hypertension_dashboard_get_exams_count():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetExamsCount(use_case)

    return controller.handle


def hypertension_dashboard_get_imc():
    repository = HypertensionDashboardRepository()
    use_case = HypertensionUseCase(repository)
    controller = HypertensionDashboardGetIMC(use_case)

    return controller.handle
