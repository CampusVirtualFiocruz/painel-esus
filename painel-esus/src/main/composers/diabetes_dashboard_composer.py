from src.infra.db.repositories.hypertension_diabetes.hypertension_diabetes_repository import (
    HypertensionDiabetesRepository,
)
from src.presentations.controllers.hypertension.hypertension_controller import (
    DiabetesController,
)

repository = HypertensionDiabetesRepository("diabetes")


def diabetes_dashboard_get_total():

    controller = DiabetesController(repository)

    return controller.get_total


def diabetes_dashboard_get_age_group_gender():
    controller = DiabetesController(repository)

    return controller.get_by_gender


def diabetes_dashboard_get_complications():
    controller = DiabetesController(repository)

    return controller.get_complications


def diabetes_dashboard_get_exams_count():
    controller = DiabetesController(repository)

    return controller.get_exams_table


def diabetes_dashboard_get_imc():
    controller = DiabetesController(repository)

    return controller.get_imc


def diabetes_dashboard_get_by_race():
    controller = DiabetesController(repository)

    return controller.get_by_race


def diabetes_dashboard_get_nominal_list():
    controller = DiabetesController(repository)
    return controller.get_nominal_list


def diabetes_dashboard_get_nominal_list_download():
    controller = DiabetesController(repository)
    return controller.get_nominal_list_download
