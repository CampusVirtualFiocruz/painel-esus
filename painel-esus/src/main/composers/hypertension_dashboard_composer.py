from src.data.use_cases.diseases_dashboard.disease_dashboard import \
    DiseaseUseCase
from src.data.use_cases.diseases_dashboard.hypertension_nominal_list import HypertensionNominalListUseCase
from src.domain.entities.hypertension import Hypertension
from src.domain.entities.hypertension_exams import HypertensionExams
from src.domain.entities.hypertension_exams import IndividualHypertensionExams
from src.infra.db.repositories.disease.diseases_dashboard_local import \
    DiseasesDashboardLocalRepository as DiseasesDashboardRepository
from src.infra.db.repositories.disease.nominal_list.hypertension_nominal_list_repository import HypertensionNominalListRepository
from src.presentations.controllers.hypertension import HypertensionDashboardGetAgeGroupGender
from src.presentations.controllers.hypertension import HypertensionDashboardGetAgeGroupsLocation
from src.presentations.controllers.hypertension import HypertensionDashboardGetComplications
from src.presentations.controllers.hypertension import HypertensionDashboardGetExamsCount
from src.presentations.controllers.hypertension import HypertensionDashboardGetIMC
from src.presentations.controllers.hypertension import HypertensionDashboardGetIndividualExamsCount
from src.presentations.controllers.hypertension import HypertensionDashboardGetProfessionalsCount
from src.presentations.controllers.hypertension import HypertensionDashboardGetTotal
from src.presentations.controllers.hypertension.hypertension_dashboard_get_nominal_list import HypertensionDashboardGetNominalList
from src.presentations.controllers.hypertension.hypertension_dashboard_get_nominal_list import HypertensionDashboardGetNominalListDownload


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


def hypertension_dashboard_get_nominal_list():
    repository = HypertensionNominalListRepository()
    use_case = HypertensionNominalListUseCase(repository)
    controller = HypertensionDashboardGetNominalList(
        use_case)

    return controller.handle


def hypertension_dashboard_get_nominal_list_download(cnes):
    repository = HypertensionNominalListRepository()
    use_case = HypertensionNominalListUseCase(repository)
    controller = HypertensionDashboardGetNominalListDownload(
        use_case)

    return controller.handle(cnes)
