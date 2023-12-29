
from src.data.use_cases.diseases_dashboard.disease_dashboard import \
    DiseaseUseCase
from src.domain.entities.diabetes import Diabetes
from src.domain.entities.diabetes_exams import (DiabetesExams,
                                                IndividualDiabetesExams)
from src.infra.db.repositories.disease.diseases_dashboard_local import \
    DiseasesDashboardLocalRepository as DiseasesDashboardRepository
from src.presentations.controllers.diabetes import (
    DiabetesDashboardGetAgeGroupGender, DiabetesDashboardGetAgeGroupsLocation,
    DiabetesDashboardGetComplications, DiabetesDashboardGetExamsCount,
    DiabetesDashboardGetIMC, DiabetesDashboardGetIndividualExamsCount,
    DiabetesDashboardGetProfessionalsCount, DiabetesDashboardGetTotal)


def diabetes_dashboard_get_total():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetTotal(use_case)

    return controller.handle


def diabetes_dashboard_get_age_groups_location():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetAgeGroupsLocation(use_case)

    return controller.handle


def diabetes_dashboard_get_age_group_gender():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetAgeGroupGender(use_case)

    return controller.handle


def diabetes_dashboard_get_complications():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetComplications(use_case)

    return controller.handle


def diabetes_dashboard_get_professionals_count():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetProfessionalsCount(use_case)

    return controller.handle


def diabetes_dashboard_get_exams_count():
    diabetes = Diabetes()
    diabetes_exams = DiabetesExams()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetExamsCount(
        use_case=use_case, diabete_exams=diabetes_exams)

    return controller.handle


def diabetes_dashboard_get_imc():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetIMC(use_case)

    return controller.handle


def diabetes_dashboard_get_individual_exams_count():
    diabetes = Diabetes()
    repository = DiseasesDashboardRepository(diabetes)
    diabetes_exams = IndividualDiabetesExams()
    use_case = DiseaseUseCase(repository)
    controller = DiabetesDashboardGetIndividualExamsCount(
        use_case, diabetes_exams)

    return controller.handle
