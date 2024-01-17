
from src.data.use_cases.diseases_dashboard.disease_dashboard import \
    DiseaseUseCase
from src.domain.entities.hypertension import Hypertension
from src.domain.entities.hypertension_exams import (
    HypertensionExams, IndividualHypertensionExams)
from src.infra.db.repositories.disease.diseases_dashboard_local import \
    DiseasesDashboardLocalRepository as DiseasesDashboardRepository
from src.presentations.controllers.hypertension import (
    HypertensionDashboardGetAgeGroupGender,
    HypertensionDashboardGetAgeGroupsLocation,
    HypertensionDashboardGetComplications, HypertensionDashboardGetExamsCount,
    HypertensionDashboardGetIMC, HypertensionDashboardGetIndividualExamsCount,
    HypertensionDashboardGetProfessionalsCount, HypertensionDashboardGetTotal)


def hypertension_dashboard_get_total():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetTotal(use_case)

    return controller.handle


def hypertension_dashboard_get_age_groups_location():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetAgeGroupsLocation(use_case)

    return controller.handle


def hypertension_dashboard_get_age_group_gender():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetAgeGroupGender(use_case)

    return controller.handle


def hypertension_dashboard_get_complications():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetComplications(use_case)

    return controller.handle


def hypertension_dashboard_get_professionals_count():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetProfessionalsCount(use_case)

    return controller.handle


def hypertension_dashboard_get_exams_count():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    hypertension_exams = HypertensionExams()
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetExamsCount(
        use_case, hypertension_exams)

    return controller.handle


def hypertension_dashboard_get_imc():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetIMC(use_case)

    return controller.handle


def hypertension_dashboard_get_individual_exams_count():
    hypertension = Hypertension()
    repository = DiseasesDashboardRepository(hypertension)
    hypertension_exam = IndividualHypertensionExams()
    use_case = DiseaseUseCase(repository)
    controller = HypertensionDashboardGetIndividualExamsCount(
        use_case, hypertension_exam)

    return controller.handle
